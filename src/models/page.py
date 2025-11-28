"""Model para representar uma página/tela"""
from dataclasses import dataclass
from typing import Optional, Dict, Any

from src.models.base_model import BaseModel


@dataclass
class Page(BaseModel):
    """Model que representa uma página na pilha de navegação"""
    name: str
    qml_path: str
    title: str = ""
    data: Optional[Dict[str, Any]] = None
    
    def __post_init__(self):
        """Validação após inicialização"""
        if not self.title:
            self.title = self.name.replace("_", " ").title()

