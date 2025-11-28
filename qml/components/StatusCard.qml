import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "../styles"

Rectangle {
    id: statusCard
    
    property string title: "Status"
    property string message: ""
    property bool isLoading: false
    
    Layout.fillWidth: true
    Layout.preferredHeight: 200
    
    color: Theme.backgroundSecondary
    radius: Theme.radiusMedium
    border.color: Theme.border
    border.width: 2
    
    ColumnLayout {
        anchors.centerIn: parent
        spacing: Theme.spacingMedium
        
        Text {
            Layout.alignment: Qt.AlignHCenter
            text: statusCard.title
            font.pixelSize: Theme.fontSizeLarge
            color: Theme.textPrimary
        }
        
        Text {
            Layout.alignment: Qt.AlignHCenter
            text: statusCard.message
            font.pixelSize: Theme.fontSizeMedium
            color: Theme.textSecondary
        }
        
        BusyIndicator {
            Layout.alignment: Qt.AlignHCenter
            visible: statusCard.isLoading
            running: statusCard.isLoading
        }
    }
}

