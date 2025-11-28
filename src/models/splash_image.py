"""Model para imagens do splash screen"""
from dataclasses import dataclass
from pathlib import Path

from src.models.base_model import BaseModel


@dataclass
class SplashImage(BaseModel):
    """Model que representa uma imagem do splash screen"""
    path: str
    name: str = ""
    
    def __post_init__(self):
        """Validação após inicialização"""
        if not self.name:
            # Extrai o nome do arquivo sem extensão
            self.name = Path(self.path).stem

