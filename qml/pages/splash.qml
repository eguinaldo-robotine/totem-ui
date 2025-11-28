import QtQuick
import QtQuick.Controls
import "../styles"
import "../components"

Page {
    id: splashPage
    
    title: "Splash Screen"
    
    // Splash Screen com carrossel
    SplashScreen {
        id: splashScreenComponent
        anchors.fill: parent
    }
    
    // Inicia o auto-play quando a página carregar
    Component.onCompleted: {
        if (splashController && splashController.hasImages) {
            // Inicia auto-play do carrossel
            splashController.startAutoPlay()
        }
    }
    
    // Para o auto-play quando sair da página
    Component.onDestruction: {
        if (splashController) {
            splashController.stopAutoPlay()
        }
    }
}

