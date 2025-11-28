import QtQuick
import QtQuick.Controls
import "../styles"

Button {
    id: primaryButton
    
    property alias buttonText: primaryButton.text
    
    font.pixelSize: Theme.fontSizeMedium
    padding: Theme.spacingMedium
    
    background: Rectangle {
        color: primaryButton.pressed ? Qt.darker(Theme.primary, 1.2) : 
               primaryButton.hovered ? Qt.lighter(Theme.primary, 1.1) : Theme.primary
        radius: Theme.radiusSmall
        
        Behavior on color {
            ColorAnimation { duration: 200 }
        }
    }
    
    contentItem: Text {
        text: primaryButton.text
        font: primaryButton.font
        color: Theme.textLight
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }
}

