"""Service para gerenciar estado da aplicação"""
from src.models.app_state import AppState
from src.repository.app_state_repository import AppStateRepository


class AppStateService:
    """Service para lógica de negócio do estado da aplicação"""
    
    def __init__(self, repository: AppStateRepository):
        self._repository = repository
    
    def get_status_message(self) -> str:
        """Obtém a mensagem de status atual"""
        state = self._repository.get_default()
        return state.status_message
    
    def update_status_message(self, message: str) -> AppState:
        """Atualiza a mensagem de status"""
        state = self._repository.get_default()
        state.status_message = message
        return self._repository.save(state)
    
    def set_loading(self, is_loading: bool) -> AppState:
        """Define o estado de carregamento"""
        state = self._repository.get_default()
        state.is_loading = is_loading
        return self._repository.save(state)
    
    def get_current_state(self) -> AppState:
        """Obtém o estado atual"""
        return self._repository.get_default()

