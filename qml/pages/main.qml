import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "../styles"
import "../components"

Page {
    id: mainPage
    
    title: "Totem UI"
    
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: Theme.spacingLarge
        spacing: Theme.spacingLarge
        
        Text {
            Layout.alignment: Qt.AlignHCenter
            text: "Bem-vindo ao Totem UI"
            font.pixelSize: Theme.fontSizeXXLarge
            font.bold: true
            color: Theme.textPrimary
        }
        
        StatusCard {
            id: statusCard
            title: "Qt 6.10 + QML + Python"
            message: appController.statusMessage
            isLoading: appController.isLoading
        }
        
        PrimaryButton {
            Layout.alignment: Qt.AlignHCenter
            buttonText: "Clique aqui"
            onClicked: {
                appController.onButtonClicked()
            }
        }
        
        PrimaryButton {
            Layout.alignment: Qt.AlignHCenter
            buttonText: "Voltar para Splash"
            onClicked: {
                screenManager.navigateTo("splash", "Splash Screen")
            }
        }
        
        PrimaryButton {
            Layout.alignment: Qt.AlignHCenter
            buttonText: "Navegar para Segunda Página"
            onClicked: {
                screenManager.navigateTo("second", "Segunda Página")
            }
        }
        
        PrimaryButton {
            Layout.alignment: Qt.AlignHCenter
            buttonText: "Resetar Status"
            onClicked: {
                appController.resetStatus()
            }
        }
        
        Item {
            Layout.fillHeight: true
        }
    }
}
