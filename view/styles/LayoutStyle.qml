import QtQuick

QtObject {
    id: style
    
    // Referência ao componente pai (será definida ao instanciar)
    property Item root: null
    
    readonly property color primary: '#e4e4e4'
    readonly property color secondary: '#c0c0c0'
    readonly property color background: '#ffffff'
    readonly property color header: '#cfcfcf'
    readonly property color accent: '#414141'
    readonly property color text: "#ffffff"
    readonly property color userInfo: "#797888"
    
    readonly property int fontSmall: root ? root.height * 0.012 : 12
    readonly property int fontMedium: root ? root.height * 0.018 : 18
    readonly property int fontLarge: root ? root.height * 0.026 : 26
    
    readonly property int paddingSmall: root ? root.width * 0.01 : 10
    readonly property int paddingMedium: root ? root.width * 0.02 : 20
    readonly property int paddingLarge: root ? root.width * 0.04 : 40

    readonly property int marginSmall: root ? root.width * 0.01 : 10
    readonly property int marginMedium: root ? root.width * 0.02 : 20
    readonly property int marginLarge: root ? root.width * 0.04 : 40
    
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
    
    readonly property int headerHeight: 100
    readonly property int footerHeight: 100
    readonly property int categoryWidth: 180
    
    readonly property int cellSize: 170
    readonly property int cellMargin: 5

    readonly property string fontFamily: "Roboto"
    readonly property string fontFamilyBold: "Roboto-Bold"
    readonly property string fontFamilyLight: "Roboto-Light"
    readonly property string fontFamilyMedium: "Roboto-Medium"
    readonly property string fontFamilyRegular: "Roboto-Regular"
    readonly property string fontFamilyThin: "Roboto-Thin"
    readonly property string fontFamilyUltraLight: "Roboto-UltraLight"
    readonly property string fontFamilyBlack: "Roboto-Black"

    readonly property string primaryFont: "Texas Tango BOLD PERSONAL USE"

}
