import QtQuick
import QtQuick.Controls
import "../../styles"
import "../../components"

Item {
    id: mainScreen
    
    property string currentPageName: screenStackController ? screenStackController.currentPage : ""
    
    Loader {
        id: pageLoader
        anchors.fill: parent
        source: getPageSource(currentPageName)
        
        function getPageSource(pageName) {
            if (pageName === "main" || pageName === "mainScreen") {
                return "" 
            }
            
            switch(pageName) {
                case "slider":
                    return "../slider/SliderScreen.qml"
                case "product":
                    return "../productScreen/ProductScreen.qml"
                case "payment":
                    return "../paymentScreen/PaymentScreen.qml"
                case "vending":
                    return "../vendingScreen/VendingScreen.qml"
                default:
                    return "../slider/SliderScreen.qml"
            }
        }
    }
    
    // Conecta os sinais do controller
    Connections {
        target: screenStackController
        
        function onPushRequested(pageName) {
            if (screenStackController) {
                screenStackController.currentPage = pageName
                currentPageName = pageName
            }
        }
        
        function onPopRequested(pageName) {
            // Lógica de pop pode ser implementada aqui se necessário
            // Por enquanto, apenas atualiza a página se um nome for fornecido
            if (pageName && screenStackController) {
                screenStackController.currentPage = pageName
                currentPageName = pageName
            }
        }
        
        function onClearStackRequested(pageName) {
            if (screenStackController) {
                screenStackController.currentPage = pageName
                currentPageName = pageName
            }
        }
    }
    
    // Atualiza quando a propriedade currentPage do controller mudar
    Connections {
        target: screenStackController
        
        function onCurrentPageChanged() {
            if (screenStackController) {
                currentPageName = screenStackController.currentPage
            }
        }
    }
}