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
                Layout.preferredHeight: style.headerHeight
                Layout.maximumHeight: style.headerHeight
                color: style.header
            }

            Rectangle {
                id: userinfo
                Layout.fillWidth: true
                Layout.preferredHeight: style.headerHeight
                Layout.maximumHeight: style.headerHeight
                color: style.userInfo
            }


            RowLayout {
                Layout.fillWidth: true
                Layout.fillHeight: true
                spacing: 0

                Rectangle {
                    id: category
                    Layout.preferredWidth: style.categoryWidth
                    Layout.fillHeight: true
                    color: style.secondary
                }

                GridView {
                    id: products
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    Layout.leftMargin: style.paddingMedium
                    Layout.rightMargin: style.paddingMedium
                    clip: true
                    interactive: true
                    cellWidth: style.cellSize
                    cellHeight: style.cellSize

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

            Rectangle {
                id: cart
                Layout.fillWidth: true
                Layout.preferredHeight: style.footerHeight
                Layout.maximumHeight: style.footerHeight
                color: style.accent
            }

        }
    }
}
