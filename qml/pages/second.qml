import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "../styles"
import "../components"

Page {
    id: secondPage
    
    title: "Segunda Página"
    
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: Theme.spacingLarge
        spacing: Theme.spacingLarge
        
        Text {
            Layout.alignment: Qt.AlignHCenter
            text: "Segunda Página"
            font.pixelSize: Theme.fontSizeXXLarge
            font.bold: true
            color: Theme.textPrimary
        }
        
        Text {
            Layout.alignment: Qt.AlignHCenter
            text: "Esta é a segunda página da aplicação"
            font.pixelSize: Theme.fontSizeMedium
            color: Theme.textSecondary
        }
        
        PrimaryButton {
            Layout.alignment: Qt.AlignHCenter
            buttonText: "Voltar"
            onClicked: {
                screenManager.goBack()
            }
        }
        
        PrimaryButton {
            Layout.alignment: Qt.AlignHCenter
            buttonText: "Ir para Splash"
            onClicked: {
                screenManager.navigateTo("splash", "Splash Screen")
            }
        }
        
        Item {
            Layout.fillHeight: true
        }
    }
}

