"""Controller para gerenciar a tela de slider"""
from PyQt6.QtCore import QObject, pyqtProperty, pyqtSlot, QUrl, pyqtSignal
from pathlib import Path
from typing import List


class SliderController(QObject):
    """Controller para gerenciar a tela de slider com carrossel de imagens"""
    
    def __init__(self, assets_path: Path = None):
        super().__init__()
        self.assets_path = assets_path
        self._images: List[str] = []
        self._load_images()
    
    hasImagesChanged = pyqtSignal()
    
    def _load_images(self):
        """Carrega as imagens na inicialização"""
        if self.assets_path and self.assets_path.exists():
            image_files = sorted(self.assets_path.glob("*.png"))
            self._images = [str(img.absolute()) for img in image_files]
            self.hasImagesChanged.emit()
    
    @pyqtProperty(bool, notify=hasImagesChanged)
    def hasImages(self):
        """Verifica se há imagens disponíveis"""
        return len(self._images) > 0
    
    @pyqtProperty(int)
    def imageCount(self):
        """Retorna a quantidade de imagens"""
        return len(self._images)
    
    @pyqtSlot(result=list)
    def loadImages(self):
        """Retorna lista de URLs das imagens para o QML"""
        if not self._images:
            return []
        
        # Converte caminhos absolutos para URLs file://
        urls = []
        for img_path in self._images:
            url = QUrl.fromLocalFile(img_path)
            urls.append(url.toString())
        return urls
    
    @pyqtSlot()
    def startAutoPlay(self):
        """Inicia o auto-play do carrossel"""
        pass
    
    @pyqtSlot()
    def stopAutoPlay(self):
        """Para o auto-play do carrossel"""
        pass
