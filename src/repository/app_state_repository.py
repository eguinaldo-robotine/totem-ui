"""Repository para estado da aplicação"""
from typing import List, Optional

from src.models.app_state import AppState
from src.repository.base_repository import BaseRepository


class AppStateRepository(BaseRepository[AppState]):
    """Repository para gerenciar estado da aplicação"""
    
    def __init__(self):
        self._storage: dict[str, AppState] = {}
        # Estado padrão
        self._default_state = AppState()
        self._storage["default"] = self._default_state
    
    def get_by_id(self, id: str) -> Optional[AppState]:
        """Busca estado por ID"""
        return self._storage.get(id)
    
    def get_all(self) -> List[AppState]:
        """Retorna todos os estados"""
        return list(self._storage.values())
    
    def save(self, item: AppState) -> AppState:
        """Salva o estado"""
        state_id = item.current_page or "default"
        self._storage[state_id] = item
        return item
    
    def delete(self, id: str) -> bool:
        """Deleta um estado"""
        if id in self._storage:
            del self._storage[id]
            return True
        return False
    
    def get_default(self) -> AppState:
        """Retorna o estado padrão"""
        return self._default_state

