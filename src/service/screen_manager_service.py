"""Service para gerenciar navegação entre telas"""
from typing import Optional, Dict, Any
from pathlib import Path

from src.models.page import Page
from src.repository.page_repository import PageRepository


class ScreenManagerService:
    """Service para lógica de navegação entre telas"""
    
    def __init__(self, repository: PageRepository, qml_base_path: Path):
        self._repository = repository
        self._qml_base_path = qml_base_path
    
    def navigate_to(self, page_name: str, title: str = "", data: Optional[Dict[str, Any]] = None) -> Page:
        """Navega para uma nova página"""
        qml_path = self._get_qml_path(page_name)
        page = Page(
            name=page_name,
            qml_path=str(qml_path),
            title=title,
            data=data or {}
        )
        return self._repository.push(page)
    
    def go_back(self) -> Optional[Page]:
        """Volta para a página anterior"""
        if self._repository.can_go_back():
            # Remove a página atual
            self._repository.pop()
            # Retorna a página anterior (agora no topo)
            return self._repository.peek()
        return None
    
    def get_current_page(self) -> Optional[Page]:
        """Obtém a página atual (topo da pilha)"""
        return self._repository.peek()
    
    def replace_current(self, page_name: str, title: str = "", data: Optional[Dict[str, Any]] = None) -> Page:
        """Substitui a página atual por uma nova"""
        # Remove a página atual
        self._repository.pop()
        # Adiciona a nova página
        return self.navigate_to(page_name, title, data)
    
    def clear_stack(self) -> None:
        """Limpa toda a pilha de navegação"""
        self._repository.clear()
    
    def can_go_back(self) -> bool:
        """Verifica se é possível voltar"""
        return self._repository.can_go_back()
    
    def get_stack_size(self) -> int:
        """Retorna o tamanho da pilha"""
        return self._repository.size()
    
    def _get_qml_path(self, page_name: str) -> Path:
        """Obtém o caminho QML para uma página"""
        # Remove extensão se presente
        if page_name.endswith('.qml'):
            page_name = page_name[:-4]
        
        # Tenta encontrar o arquivo QML
        possible_paths = [
            self._qml_base_path / "pages" / f"{page_name}.qml",
            self._qml_base_path / "pages" / f"{page_name.lower()}.qml",
            self._qml_base_path / f"{page_name}.qml",
        ]
        
        for path in possible_paths:
            if path.exists():
                return path
        
        # Se não encontrar, retorna o caminho padrão
        return self._qml_base_path / "pages" / f"{page_name}.qml"

