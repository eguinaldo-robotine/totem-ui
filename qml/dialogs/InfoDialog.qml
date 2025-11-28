import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "../styles"

Dialog {
    id: infoDialog
    
    property string dialogTitle: "Informação"
    property string dialogMessage: ""
    
    title: dialogTitle
    width: 400
    height: 200
    modal: true
    
    ColumnLayout {
        anchors.fill: parent
        spacing: Theme.spacingMedium
        
        Text {
            Layout.fillWidth: true
            text: dialogMessage
            font.pixelSize: Theme.fontSizeMedium
            color: Theme.textPrimary
            wrapMode: Text.WordWrap
        }
        
        Button {
            Layout.alignment: Qt.AlignRight
            text: "OK"
            onClicked: infoDialog.close()
        }
    }
}

