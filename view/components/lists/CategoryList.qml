import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "../../styles"

Rectangle {
    id: categoryList
    color: '#00ffffff'
    radius: style.radius
    clip: false  

    LayoutStyle {
        id: style
        root: categoryList
    }

    property var categories: [
        "Destaques",
        "Bebidas",
        "Águas",
        "Cafés",
        "Lanches",
        "Snacks",
        "Doces"
    ]

    property int currentIndex: 0

    signal categorySelected(string categoryName, int index)

    ColumnLayout {
        anchors.fill: parent
        
        ListView {
            id: listView
            Layout.fillWidth: true
            Layout.fillHeight: true

            clip: false  
            model: categoryList.categories
            currentIndex: categoryList.currentIndex
            boundsBehavior: Flickable.StopAtBounds

            delegate: Rectangle {
                id: delegateRoot
                width: listView.width 
                height: style.percentHeight(0.14)
                radius: (listView.currentIndex === index) ? 5 : 0
                anchors.horizontalCenter: parent.horizontalCenter
                scale: (listView.currentIndex === index) ? 1.08 : 1.0
                color: (listView.currentIndex === index) ? '#7c6464' : "#f1e2cf"
                transformOrigin: Item.Center
                z: (listView.currentIndex === index) ? 1 : 0

                    Behavior on scale {
                        NumberAnimation {
                            duration: 200
                            easing.type: Easing.OutCubic
                        }
                    }

                    RowLayout {
                        anchors.fill: parent
                        anchors.leftMargin: style.paddingSmall
                        anchors.rightMargin: style.paddingSmall

                        Label {
                            id: categoryLabel
                            text: modelData
                            color: (listView.currentIndex === index) ? '#f1e2cf' : '#7c6464'
                            font.pixelSize: style.fontSmall
                            font.family: fontFamilyBlack
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                        }
                    }

                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            listView.currentIndex = index
                            categoryList.currentIndex = index
                            categoryList.categorySelected(modelData, index)
                        }
                    }
                
            }
        }
    }
}