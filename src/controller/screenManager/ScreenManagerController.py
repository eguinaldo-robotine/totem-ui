from PyQt6.QtCore import QObject, pyqtSlot, pyqtSignal, pyqtProperty


class ScreenManagerController(QObject):

    pushRequested = pyqtSignal(str) 
    popRequested = pyqtSignal(str)   
    clearStackRequested = pyqtSignal(str) 
    
    _currentPage = ""
    
    def __init__(self):
        super().__init__()
        self._currentPage = ""
    
    currentPageChanged = pyqtSignal()
    
    @pyqtProperty(str, notify=currentPageChanged)
    def currentPage(self):
        """Retorna a página atual"""
        return self._currentPage
    
    @currentPage.setter
    def currentPage(self, value: str):
        """Define a página atual"""
        if self._currentPage != value:
            self._currentPage = value
            self.currentPageChanged.emit()
    
    @pyqtSlot(str)
    def pushPage(self, pageName: str):
        """Empilha uma nova página na pilha de navegação"""
        if pageName:
            self._currentPage = pageName
            self.pushRequested.emit(pageName)
    
    @pyqtSlot(str)
    def popPage(self, pageName: str = ""):
        """Remove a página atual da pilha de navegação"""
        self.popRequested.emit(pageName if pageName else self._currentPage)
    
    @pyqtSlot(str)
    def clearStack(self, pageName: str):
        """Limpa a pilha e define uma nova página inicial"""
        if pageName:
            self._currentPage = pageName
            self.clearStackRequested.emit(pageName)

