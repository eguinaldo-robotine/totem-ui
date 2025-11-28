import QtQuick
import QtQuick.Controls
import "../styles"
import "../components"

ApplicationWindow {
    id: window
    width: 1080 / 2
    height: 1920 / 2
    visible: true
    title: screenManager ? (screenManager.currentPageTitle || "Totem UI") : "Totem UI"
    
    color: "#ffffff"
    
    ScreenStack {
        id: screenStack
        anchors.fill: parent
    }
    
}

