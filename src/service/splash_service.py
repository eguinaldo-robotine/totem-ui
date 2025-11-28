"""Service para gerenciar splash screen"""
from pathlib import Path
from typing import List

from src.models.splash_image import SplashImage
from src.repository.splash_image_repository import SplashImageRepository


class SplashService:
    """Service para lógica do splash screen"""
    
    def __init__(self, repository: SplashImageRepository):
        self._repository = repository
    
    def get_images(self) -> List[SplashImage]:
        """Obtém todas as imagens do splash"""
        return self._repository.get_all()
    
    def get_image_count(self) -> int:
        """Retorna o número de imagens"""
        return self._repository.count()
    
    def has_images(self) -> bool:
        """Verifica se há imagens disponíveis"""
        return self._repository.count() > 0

