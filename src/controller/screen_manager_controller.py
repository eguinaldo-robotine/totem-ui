"""Controller para gerenciar navegação entre telas"""
from pathlib import Path
from typing import Optional, Dict, Any

from PyQt6.QtCore import QObject, pyqtSignal, pyqtProperty, pyqtSlot

from src.models.page import Page
from src.service.screen_manager_service import ScreenManagerService
from src.repository.page_repository import PageRepository


class ScreenManagerController(QObject):
    """Controller que gerencia a pilha de páginas e navegação"""
    
    # Signals
    current_page_changed = pyqtSignal(str)  # qml_path
    page_title_changed = pyqtSignal(str)
    can_go_back_changed = pyqtSignal(bool)
    stack_size_changed = pyqtSignal(int)
    
    def __init__(self, qml_base_path: Path, parent=None):
        super().__init__(parent)
        # Inicializa repository e service
        self._repository = PageRepository()
        self._service = ScreenManagerService(self._repository, qml_base_path)
        
        # Estado atual
        self._current_page: Optional[Page] = None
    
    @pyqtProperty(str, notify=current_page_changed)
    def currentPagePath(self) -> str:
        """Propriedade QML para o caminho da página atual"""
        if self._current_page:
            return self._current_page.qml_path
        return ""
    
    @pyqtProperty(str, notify=page_title_changed)
    def currentPageTitle(self) -> str:
        """Propriedade QML para o título da página atual"""
        if self._current_page:
            return self._current_page.title
        return ""
    
    @pyqtProperty(bool, notify=can_go_back_changed)
    def canGoBack(self) -> bool:
        """Propriedade QML para verificar se pode voltar"""
        return self._service.can_go_back()
    
    @pyqtProperty(int, notify=stack_size_changed)
    def stackSize(self) -> int:
        """Propriedade QML para o tamanho da pilha"""
        return self._service.get_stack_size()
    
    @pyqtSlot(str, str, result=bool)
    def navigateTo(self, page_name: str, title: str = "") -> bool:
        """Slot para navegar para uma nova página"""
        try:
            page = self._service.navigate_to(page_name, title)
            self._update_current_page(page)
            return True
        except Exception as e:
            print(f"Erro ao navegar para {page_name}: {e}")
            return False
    
    @pyqtSlot(str, str, "QVariantMap", result=bool)
    def navigateToWithData(self, page_name: str, title: str, data: Dict[str, Any]) -> bool:
        """Slot para navegar para uma nova página com dados"""
        try:
            page = self._service.navigate_to(page_name, title, data)
            self._update_current_page(page)
            return True
        except Exception as e:
            print(f"Erro ao navegar para {page_name}: {e}")
            return False
    
    @pyqtSlot(result=bool)
    def goBack(self) -> bool:
        """Slot para voltar para a página anterior"""
        try:
            page = self._service.go_back()
            if page:
                self._update_current_page(page)
                return True
            return False
        except Exception as e:
            print(f"Erro ao voltar: {e}")
            return False
    
    @pyqtSlot(str, str, result=bool)
    def replaceCurrent(self, page_name: str, title: str = "") -> bool:
        """Slot para substituir a página atual"""
        try:
            page = self._service.replace_current(page_name, title)
            self._update_current_page(page)
            return True
        except Exception as e:
            print(f"Erro ao substituir página: {e}")
            return False
    
    @pyqtSlot()
    def clearStack(self):
        """Slot para limpar toda a pilha"""
        self._service.clear_stack()
        self._current_page = None
        self.current_page_changed.emit("")
        self.page_title_changed.emit("")
        self.can_go_back_changed.emit(False)
        self.stack_size_changed.emit(0)
    
    def _update_current_page(self, page: Page):
        """Atualiza a página atual e emite signals"""
        self._current_page = page
        self.current_page_changed.emit(page.qml_path)
        self.page_title_changed.emit(page.title)
        self.can_go_back_changed.emit(self._service.can_go_back())
        self.stack_size_changed.emit(self._service.get_stack_size())
    
    def initialize(self, initial_page: str, title: str = ""):
        """Inicializa o screen manager com uma página inicial"""
        self.navigateTo(initial_page, title)

