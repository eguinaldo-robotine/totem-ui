"""Controller para gerenciar splash screen"""
from pathlib import Path
from typing import List

from PyQt6.QtCore import QObject, pyqtSignal, pyqtProperty, pyqtSlot

from src.models.splash_image import SplashImage
from src.service.splash_service import SplashService
from src.repository.splash_image_repository import SplashImageRepository


class SplashController(QObject):
    """Controller que gerencia o splash screen"""
    
    # Signals
    current_index_changed = pyqtSignal(int)
    images_loaded = pyqtSignal()
    
    def __init__(self, images_dir: Path, parent=None):
        super().__init__(parent)
        # Inicializa repository e service
        self._repository = SplashImageRepository(images_dir)
        self._service = SplashService(self._repository)
        
        # Estado atual
        self._current_index = 0
        self._images: List[SplashImage] = []
        self._auto_play_enabled = True
        self._auto_play_interval = 3000  # 3 segundos
        
        # Carrega imagens
        self._load_images()
    
    def _load_images(self):
        """Carrega as imagens do service"""
        self._images = self._service.get_images()
        if self._images:
            self.images_loaded.emit()
    
    @pyqtProperty(int, notify=current_index_changed)
    def currentIndex(self) -> int:
        """Propriedade QML para o índice atual"""
        return self._current_index
    
    @pyqtProperty(int)
    def imageCount(self) -> int:
        """Propriedade QML para o número de imagens"""
        return len(self._images)
    
    @pyqtProperty(bool)
    def hasImages(self) -> bool:
        """Propriedade QML para verificar se há imagens"""
        return len(self._images) > 0
    
    @pyqtProperty(int)
    def autoPlayInterval(self) -> int:
        """Propriedade QML para o intervalo de auto-play (ms)"""
        return self._auto_play_interval
    
    @pyqtSlot(int)
    def setAutoPlayInterval(self, interval: int):
        """Slot para definir o intervalo de auto-play"""
        self._auto_play_interval = interval
    
    @pyqtSlot()
    def nextImage(self):
        """Slot para ir para a próxima imagem"""
        self._next_image()
    
    @pyqtSlot()
    def previousImage(self):
        """Slot para ir para a imagem anterior"""
        if len(self._images) > 0:
            self._current_index = (self._current_index - 1) % len(self._images)
            self.current_index_changed.emit(self._current_index)
    
    @pyqtSlot(int)
    def goToImage(self, index: int):
        """Slot para ir para uma imagem específica"""
        if 0 <= index < len(self._images):
            self._current_index = index
            self.current_index_changed.emit(self._current_index)
    
    @pyqtSlot()
    def startAutoPlay(self):
        """Slot para iniciar auto-play (controlado pelo QML)"""
        self._auto_play_enabled = True
    
    @pyqtSlot()
    def stopAutoPlay(self):
        """Slot para parar auto-play (controlado pelo QML)"""
        self._auto_play_enabled = False
    
    @pyqtSlot(result=str)
    def getCurrentImagePath(self) -> str:
        """Slot para obter o caminho da imagem atual"""
        if self._images and 0 <= self._current_index < len(self._images):
            return self._images[self._current_index].path
        return ""
    
    @pyqtSlot(result="QStringList")
    def getAllImagePaths(self) -> List[str]:
        """Slot para obter todos os caminhos de imagens"""
        return [img.path for img in self._images]
    
    def _next_image(self):
        """Método interno para ir para a próxima imagem"""
        if len(self._images) > 0:
            self._current_index = (self._current_index + 1) % len(self._images)
            self.current_index_changed.emit(self._current_index)

