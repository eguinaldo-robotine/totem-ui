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
                Layout.preferredHeight: style.percentHeight(0.15)
                color: style.header
            }

            Item {
                id: userinfo
                Layout.fillWidth: true
                Layout.preferredHeight: style.percentHeight(0.12)

                RowLayout {
                    anchors.fill: parent
                    ColumnLayout {
                        Label {
                        // margin left 30
                            Layout.leftMargin: style.marginMedium
                            text: "Oi, Fulano"
                            color: "Black"
                            font.pixelSize: 36
                            font.bold: true
                            font.family: "Roboto"
                            horizontalAlignment: Text.AlignLeft
                        }
                        Label {
                            Layout.leftMargin: 30
                            text: "pontos: 100"
                            color: "Black"
                            font.pixelSize: 12
                            font.bold: true
                            font.family: "Roboto"
                            horizontalAlignment: Text.AlignLeft
                        }
                    }

                    Item {
                        Layout.fillWidth: true
                    }

                    Rectangle {
                        Layout.rightMargin: 30
                        radius: 10
                        Layout.preferredWidth: 200
                        Layout.preferredHeight: 60
                        color: "Red"
                    }

                }   
            }

            RowLayout {
                Layout.fillWidth: true
                Layout.fillHeight: true
                spacing: 0

                CategoryList {
                    id: categoryList
                    Layout.preferredWidth: style.percentWidth(0.23)
                    Layout.preferredHeight: style.percentHeight(0.45)
                    Layout.alignment: Qt.AlignTop
                    Layout.leftMargin: style.marginMedium
                }
                
                ColumnLayout {
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    spacing: 0

                    Label {
                        Layout.leftMargin: style.marginMedium
                        text: "Categoria"
                        color: "Black"
                        font.pixelSize: 32
                        font.bold: true
                        font.family: style.primaryFont
                        horizontalAlignment: Text.AlignLeft
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
                        cellWidth: style.percentWidth(0.35)
                        cellHeight: style.percentWidth(0.35)
                        model: 13

                        delegate: Item {
                            width: products.cellWidth
                            height: products.cellHeight

                            Rectangle {
                                anchors.fill: parent
                                anchors.margins: style.marginMedium
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
