import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "../styles"

Rectangle {
    id: splashScreen
    
    color: Theme ? Theme.backgroundDark : "#34495e"
    anchors.fill: parent
    
    // Carrossel de imagens usando SwipeView
    SwipeView {
        id: swipeView
        anchors.fill: parent
        currentIndex: splashController ? splashController.currentIndex : 0
        interactive: true
        
        // Conecta mudanças do controller
        Connections {
            target: splashController
            
            function onCurrentIndexChanged() {
                if (splashController && swipeView.currentIndex !== splashController.currentIndex) {
                    swipeView.currentIndex = splashController.currentIndex
                }
            }
        }
        
        // Atualiza o controller quando o usuário desliza
        onCurrentIndexChanged: {
            if (splashController && swipeView.currentIndex !== splashController.currentIndex) {
                splashController.goToImage(swipeView.currentIndex)
            }
        }
        
        // Cria as páginas dinamicamente
        Repeater {
            model: splashController ? splashController.imageCount : 0
            
            Item {
                width: swipeView.width
                height: swipeView.height
                
                Image {
                    id: splashImage
                    anchors.fill: parent
                    source: {
                        if (splashController) {
                            var paths = splashController.getAllImagePaths()
                            if (index >= 0 && index < paths.length) {
                                return "file://" + paths[index]
                            }
                        }
                        return ""
                    }
                    fillMode: Image.PreserveAspectCrop
                    asynchronous: true
                    cache: true
                    smooth: true
                }
            }
        }
    }
    
    // Indicadores de página (dots)
    Row {
        id: pageIndicators
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottomMargin: 30
        spacing: 10
        
        Repeater {
            model: splashController ? splashController.imageCount : 0
            
            Rectangle {
                width: 12
                height: 12
                radius: 6
                color: {
                    var currentIdx = splashController ? splashController.currentIndex : 0
                    var primaryColor = Theme ? Theme.primary : "#3498db"
                    var borderColor = Theme ? Theme.border : "#bdc3c7"
                    return index === currentIdx ? primaryColor : borderColor
                }
                
                Behavior on color {
                    ColorAnimation { duration: 200 }
                }
            }
        }
    }
    
    // Timer para auto-play
    Timer {
        id: autoPlayTimer
        interval: splashController ? splashController.autoPlayInterval : 3000
        running: splashController && splashController.hasImages && splashController.imageCount > 1
        repeat: true
        onTriggered: {
            if (splashController) {
                splashController.nextImage()
            }
        }
        
        // Reinicia quando o intervalo mudar
        onIntervalChanged: {
            if (running) {
                restart()
            }
        }
    }
    
    // Conecta ao controller para controlar o timer
    Connections {
        target: splashController
        
        function onImagesLoaded() {
            if (splashController && splashController.hasImages && splashController.imageCount > 1) {
                autoPlayTimer.start()
            }
        }
    }
}
