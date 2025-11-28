"""Controller para gerenciar a aplicação"""
from PyQt6.QtCore import QObject, pyqtSignal, pyqtProperty, pyqtSlot

from src.models.app_state import AppState
from src.service.app_state_service import AppStateService
from src.repository.app_state_repository import AppStateRepository


class AppController(QObject):
    """Controller que conecta QML com a lógica de negócio"""
    
    # Signals
    status_message_changed = pyqtSignal(str)
    loading_changed = pyqtSignal(bool)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        # Inicializa repository e service
        self._repository = AppStateRepository()
        self._service = AppStateService(self._repository)
        
        # Estado atual
        self._current_state = self._service.get_current_state()
    
    @pyqtProperty(str, notify=status_message_changed)
    def statusMessage(self) -> str:
        """Propriedade QML para mensagem de status"""
        return self._current_state.status_message
    
    @pyqtProperty(bool, notify=loading_changed)
    def isLoading(self) -> bool:
        """Propriedade QML para estado de carregamento"""
        return self._current_state.is_loading
    
    @pyqtSlot(str)
    def updateStatusMessage(self, message: str):
        """Slot para atualizar mensagem de status"""
        self._current_state = self._service.update_status_message(message)
        self.status_message_changed.emit(self._current_state.status_message)
    
    @pyqtSlot()
    def onButtonClicked(self):
        """Slot chamado quando o botão é clicado"""
        self.updateStatusMessage("Botão clicado!")
    
    @pyqtSlot()
    def resetStatus(self):
        """Slot para resetar o status"""
        self.updateStatusMessage("Aguardando interação...")

