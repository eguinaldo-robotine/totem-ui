import QtQuick
import QtQuick.Controls
import "../../styles"
import "../../components"

Page {
    id: sliderPage
    
    title: "Slider Screen"


    Rectangle {
        id: sliderBackground
        anchors.fill: parent
        color: "#f0f0f0"
        clip: true 

        property var imageList: []
        property int currentIndex: 0
        property int slideInterval: 4000 
        property bool isLoaded: false

        Timer {
            id: carouselTimer
            interval: sliderBackground.slideInterval
            running: sliderBackground.isLoaded && sliderBackground.imageList.length > 1
            repeat: true
            onTriggered: {
                if (sliderBackground.imageList.length > 1) {
                    sliderBackground.currentIndex = (sliderBackground.currentIndex + 1) % sliderBackground.imageList.length
                    console.log("Mudando para imagem:", sliderBackground.currentIndex)
                }
            }
        }

        Component.onCompleted: {
            if (sliderController && sliderController.hasImages) {
                let imgs = sliderController.loadImages();
                console.log("Imagens carregadas:", imgs.length)
                if (imgs && imgs.length > 0) {
                    sliderBackground.imageList = imgs;
                    sliderBackground.isLoaded = true;
                    console.log("Slider iniciado com", imgs.length, "imagens")
                    if (imgs.length > 1) {
                        carouselTimer.start()
                    }
                }
            }
        }

        Row {
            id: imageRow
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            width: sliderBackground.width * sliderBackground.imageList.length
            x: -sliderBackground.currentIndex * sliderBackground.width
            
            Behavior on x {
                NumberAnimation {
                    duration: 500
                    easing.type: Easing.InOutCubic
                }
            }
            
            Repeater {
                model: sliderBackground.imageList.length
                
                Image {
                    width: sliderBackground.width
                    height: sliderBackground.height
                    fillMode: Image.PreserveAspectCrop
                    source: sliderBackground.imageList[index]
                    smooth: true
                    cache: true
                    asynchronous: true
                    
                    onStatusChanged: {
                        if (status === Image.Error) {
                            console.log("Erro ao carregar imagem: " + source);
                        } else if (status === Image.Ready) {
                            console.log("Imagem carregada: " + source);
                        }
                    }
                }
            }
        }

        Loader {
            anchors.centerIn: parent
            sourceComponent: (!sliderBackground.isLoaded || sliderBackground.imageList.length === 0) ? loadingOverlay : null
        }
        
        // Rodapé com fade e botão
        Rectangle {
            id: footer
            anchors.bottom: parent.bottom
            anchors.left: parent.left
            anchors.right: parent.right
            height: 300
            color: "#000000"
            
            // Gradiente fade na parte superior
            gradient: Gradient {
                GradientStop { position: 0.0; color: '#00c7c7c7' }  // Transparente no topo
                GradientStop { position: 0.3; color: '#80dad9d9' }   // Semi-transparente
                GradientStop { position: 1.0; color: '#ffffff' }     // Preto no rodapé
            }
            
            // Botão central
            Button {
                id: startOrderButton
                anchors.centerIn: parent
                anchors.verticalCenterOffset: 10  // Ajuste para centralizar melhor
                width: 300
                height: 60
                text: "Iniciar Pedido"
                
                background: Rectangle {
                    color: startOrderButton.pressed ? "#2d5aa0" : "#3d6bb0"
                    radius: 30
                    border.color: "#ffffff"
                    border.width: 2
                    
                    Behavior on color {
                        ColorAnimation { duration: 150 }
                    }
                }
                
                contentItem: Text {
                    text: startOrderButton.text
                    font.pixelSize: 24
                    font.bold: true
                    color: "#ffffff"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                }
                
                onClicked: {
                    console.log("Botão Iniciar Pedido clicado")
                    // Aqui você pode adicionar a lógica para navegar para a próxima tela
                    if (screenStackController) {
                        screenStackController.pushPage("vending")
                    }
                }
            }
        }

        Component {
            id: loadingOverlay
            Column {
                anchors.centerIn: parent
                spacing: 16

                Text {
                    text: "Totem UI"
                    font.pixelSize: 48
                    font.bold: true
                    color: "#333333"
                    horizontalAlignment: Text.AlignHCenter
                }

                Text {
                    text: sliderController && sliderController.hasImages
                        ? "Carregando imagens..."
                        : "Nenhuma imagem encontrada"
                    font.pixelSize: 24
                    color: "#666666"
                    horizontalAlignment: Text.AlignHCenter
                }
            }
        }
    }
    
    // Inicia o auto-play quando a página carregar
    Component.onCompleted: {
        if (sliderController && sliderController.hasImages) {
            sliderController.startAutoPlay()
        }
    }
    
    Component.onDestruction: {
        if (sliderController) {
            sliderController.stopAutoPlay()
        }
    }
}

