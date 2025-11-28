"""Model base para entidades"""
from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class BaseModel:
    """Classe base para todos os models"""
    
    def to_dict(self) -> Dict[str, Any]:
        """Converte o model para dicionário"""
        return {
            key: value
            for key, value in self.__dict__.items()
            if not key.startswith('_')
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BaseModel':
        """Cria uma instância do model a partir de um dicionário"""
        return cls(**data)

