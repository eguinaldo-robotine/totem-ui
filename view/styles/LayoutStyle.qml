import QtQuick

QtObject {
    id: style
    
    // Referência ao componente pai (será definida ao instanciar)
    property Item root: null
    
    readonly property color primary: "#298b55"
    readonly property color secondary: "#362cb6"
    readonly property color background: "#2e2e2e"
    readonly property color header: "#ff0000"
    readonly property color accent: "#bcda36"
    readonly property color text: "#ffffff"
    readonly property color userInfo: "#797888"
    
    readonly property int fontSmall: root ? root.height * 0.012 : 12
    readonly property int fontMedium: root ? root.height * 0.018 : 18
    readonly property int fontLarge: root ? root.height * 0.026 : 26
    
    readonly property int paddingSmall: root ? root.width * 0.01 : 10
    readonly property int paddingMedium: root ? root.width * 0.02 : 20
    readonly property int paddingLarge: root ? root.width * 0.04 : 40
    
    function percentWidth(p) { 
        return root ? root.width * p : 0 
    }
    
    function percentHeight(p) { 
        return root ? root.height * p : 0 
    }
    
    function keepRatio(width, ratio) { 
        return width * ratio 
    }
    
    readonly property int radius: 12
    
    // Alturas padrão
    readonly property int headerHeight: 100
    readonly property int footerHeight: 100
    readonly property int categoryWidth: 180
    
    // Tamanhos de célula do grid
    readonly property int cellSize: 170
    readonly property int cellMargin: 5
}

