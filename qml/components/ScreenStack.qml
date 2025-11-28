import QtQuick
import QtQuick.Controls

Loader {
    id: pageLoader
    
    anchors.fill: parent
    
    // Inicializa com a primeira página
    Component.onCompleted: {
        if (screenManager && screenManager.currentPagePath) {
            loadPage(screenManager.currentPagePath)
        }
    }
    
    // Conecta ao signal de mudança de página
    Connections {
        target: screenManager
        
        function onCurrentPagePathChanged() {
            if (screenManager && screenManager.currentPagePath) {
                loadPage(screenManager.currentPagePath)
            }
        }
    }
    
    function loadPage(qmlPath) {
        if (qmlPath) {
            pageLoader.source = qmlPath
        }
    }
}

