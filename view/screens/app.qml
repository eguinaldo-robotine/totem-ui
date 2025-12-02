import QtQuick
import QtQuick.Controls
import "../styles"
import "../components"

ApplicationWindow {
    id: window

    property bool debugRotate: false
    property int screenWidth: 1080 * scale
    property int screenHeight: 1920 * scale
    property double scale: 0.5

    width: debugRotate ? screenHeight : screenWidth
    height: debugRotate ? screenWidth : screenHeight
    visible: true
    title: screenStackController ? (screenStackController.currentPage || "Totem UI") : "Totem UI"

    color: "#ffffff"

    // Container para rotacionar a tela inteira sem cortar
    Item {
        id: rotatedRoot
        anchors.fill: parent
        anchors.centerIn: parent

        // Rotaciona apenas se o debugRotate estiver ativo
        rotation: window.debugRotate ? 90 : 0
        transformOrigin: Item.Center

        Loader {
            id: mainScreenLoader

            width: window.debugRotate ? rotatedRoot.height : rotatedRoot.width
            height: window.debugRotate ? rotatedRoot.width : rotatedRoot.height

            anchors.centerIn: parent
            source: "mainScreen/mainScreen.qml"
        }
    }
}

