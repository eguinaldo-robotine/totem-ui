"""Repository para gerenciar imagens do splash screen"""
from pathlib import Path
from typing import List, Optional

from src.models.splash_image import SplashImage
from src.repository.base_repository import BaseRepository


class SplashImageRepository(BaseRepository[SplashImage]):
    """Repository para gerenciar imagens do splash screen"""
    
    def __init__(self, images_dir: Path):
        self._images_dir = images_dir
        self._images: List[SplashImage] = []
        self._load_images()
    
    def _load_images(self):
        """Carrega todas as imagens do diretório"""
        if not self._images_dir.exists():
            return
        
        # Extensões de imagem suportadas
        image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'}
        
        # Carrega todas as imagens
        for image_file in sorted(self._images_dir.iterdir()):
            if image_file.suffix.lower() in image_extensions:
                image = SplashImage(
                    path=str(image_file),
                    name=image_file.stem
                )
                self._images.append(image)
    
    def get_by_id(self, id: str) -> Optional[SplashImage]:
        """Busca imagem por nome"""
        for image in self._images:
            if image.name == id:
                return image
        return None
    
    def get_all(self) -> List[SplashImage]:
        """Retorna todas as imagens"""
        return self._images.copy()
    
    def save(self, item: SplashImage) -> SplashImage:
        """Adiciona uma imagem (não usado normalmente)"""
        self._images.append(item)
        return item
    
    def delete(self, id: str) -> bool:
        """Remove uma imagem (não usado normalmente)"""
        for i, image in enumerate(self._images):
            if image.name == id:
                self._images.pop(i)
                return True
        return False
    
    def count(self) -> int:
        """Retorna o número de imagens"""
        return len(self._images)

