"""Repository base"""
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')


class BaseRepository(ABC, Generic[T]):
    """Classe base para repositories"""
    
    @abstractmethod
    def get_by_id(self, id: str) -> Optional[T]:
        """Busca um item por ID"""
        pass
    
    @abstractmethod
    def get_all(self) -> List[T]:
        """Busca todos os itens"""
        pass
    
    @abstractmethod
    def save(self, item: T) -> T:
        """Salva um item"""
        pass
    
    @abstractmethod
    def delete(self, id: str) -> bool:
        """Deleta um item por ID"""
        pass

