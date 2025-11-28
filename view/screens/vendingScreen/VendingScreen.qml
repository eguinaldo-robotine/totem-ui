import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "../../styles"
import "../../components"

Page {
    id: vendingPage
    title: "Vending Screen"

    LayoutStyle {
        id: style
        root: vendingPage
    }

    Rectangle {
        id: contentBackground
        anchors.fill: parent
        color: style.background

        ColumnLayout {
            id: contentLayout
            anchors.fill: parent
            spacing: 0

           Rectangle {
                id: headerSlider
                Layout.fillWidth: true
                Layout.preferredHeight: style.percentHeight(0.12)
                color: style.header
            }

            Rectangle {
                id: userinfo
                Layout.fillWidth: true
                Layout.preferredHeight: style.percentHeight(0.12)
                color: style.userInfo
            }


            RowLayout {
                Layout.fillWidth: true
                Layout.fillHeight: true
                spacing: 0

                Rectangle {
                    id: category
                    Layout.preferredWidth: style.percentWidth(0.30)
                    Layout.fillHeight: true
                    color: style.secondary
                }
                
                ColumnLayout {
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    spacing: 0

                    Rectangle {
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        color: style.primary
                    }

                    GridView {
                        id: products
                        Layout.fillWidth: true
                        Layout.fillHeight: true
                        Layout.leftMargin: style.paddingMedium
                        Layout.rightMargin: style.paddingMedium
                        Layout.topMargin: style.paddingMedium
                        clip: true
                        interactive: true
                        cellWidth: style.percentWidth(0.33)
                        cellHeight: style.percentWidth(0.33)
                        model: 13

                        delegate: Item {
                            width: products.cellWidth
                            height: products.cellHeight

                            Rectangle {
                                anchors.fill: parent
                                anchors.margins: style.cellMargin
                                radius: style.radius
                                color: style.primary
                            }
                        }
                    }
                }
            }

            Rectangle {
                id: cart
                Layout.fillWidth: true
                Layout.preferredHeight: style.percentHeight(0.10)
                Layout.maximumHeight: style.footerHeight
                color: style.accent
            }

        }
    }
}
