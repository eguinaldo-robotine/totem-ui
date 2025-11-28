"""Model para estado da aplicação"""
from dataclasses import dataclass
from typing import Optional

from src.models.base_model import BaseModel


@dataclass
class AppState(BaseModel):
    """Model que representa o estado da aplicação"""
    status_message: str = "Aguardando interação..."
    is_loading: bool = False
    current_page: Optional[str] = None

