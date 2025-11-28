"""Repository para gerenciar pilha de páginas"""
from typing import List, Optional

from src.models.page import Page
from src.repository.base_repository import BaseRepository


class PageRepository(BaseRepository[Page]):
    """Repository para gerenciar pilha de páginas"""
    
    def __init__(self):
        self._stack: List[Page] = []
    
    def get_by_id(self, id: str) -> Optional[Page]:
        """Busca página por nome"""
        for page in self._stack:
            if page.name == id:
                return page
        return None
    
    def get_all(self) -> List[Page]:
        """Retorna todas as páginas na pilha"""
        return self._stack.copy()
    
    def save(self, item: Page) -> Page:
        """Adiciona página à pilha"""
        self._stack.append(item)
        return item
    
    def delete(self, id: str) -> bool:
        """Remove página da pilha por nome"""
        for i, page in enumerate(self._stack):
            if page.name == id:
                self._stack.pop(i)
                return True
        return False
    
    def push(self, page: Page) -> Page:
        """Adiciona página ao topo da pilha"""
        return self.save(page)
    
    def pop(self) -> Optional[Page]:
        """Remove e retorna a página do topo da pilha"""
        if self._stack:
            return self._stack.pop()
        return None
    
    def peek(self) -> Optional[Page]:
        """Retorna a página do topo sem remover"""
        if self._stack:
            return self._stack[-1]
        return None
    
    def clear(self) -> None:
        """Limpa toda a pilha"""
        self._stack.clear()
    
    def size(self) -> int:
        """Retorna o tamanho da pilha"""
        return len(self._stack)
    
    def can_go_back(self) -> bool:
        """Verifica se é possível voltar (mais de uma página na pilha)"""
        return len(self._stack) > 1

