import QtQuick
import QtQuick.Controls
import "../styles"
import "../components"

ApplicationWindow {
    id: window
    width: 1080 / 2
    height: 1920 / 2
    visible: true
    title: screenStackController ? (screenStackController.currentPage || "Totem UI") : "Totem UI"
    
    color: "#ffffff"
    
    Loader {
        id: mainScreenLoader
        anchors.fill: parent
        source: "mainScreen/mainScreen.qml"
    }
}

