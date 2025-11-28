import QtQuick
import QtQuick.Controls
import "../../styles"
import "../../components"

Page {
    id: vendingPage

    title: "Vending Screen"

    Rectangle {
        id: contentBackground
        anchors.fill: parent
        color: "#f0f0f0"
    }

    // Exibe o component Overlay
    Overlay {
        id: overlay
        anchors.fill: parent
        overlayTitle: "Totem UI"
        overlayMessage: "Bem-vindo à tela de vending!"
    }
}
