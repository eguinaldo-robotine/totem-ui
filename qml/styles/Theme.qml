import QtQuick

QtObject {
    id: theme
    
    // Cores principais
    readonly property color primary: "#3498db"
    readonly property color secondary: "#2ecc71"
    readonly property color accent: "#e74c3c"
    
    // Cores de texto
    readonly property color textPrimary: "#2c3e50"
    readonly property color textSecondary: "#7f8c8d"
    readonly property color textLight: "#ecf0f1"
    
    // Cores de fundo
    readonly property color background: "#ffffff"
    readonly property color backgroundSecondary: "#ecf0f1"
    readonly property color backgroundDark: "#34495e"
    
    // Cores de borda
    readonly property color border: "#bdc3c7"
    readonly property color borderLight: "#ecf0f1"
    
    // Tamanhos de fonte
    readonly property int fontSizeSmall: 12
    readonly property int fontSizeMedium: 14
    readonly property int fontSizeLarge: 18
    readonly property int fontSizeXLarge: 24
    readonly property int fontSizeXXLarge: 32
    
    // Espaçamentos
    readonly property int spacingSmall: 8
    readonly property int spacingMedium: 16
    readonly property int spacingLarge: 24
    
    // Raio de borda
    readonly property int radiusSmall: 4
    readonly property int radiusMedium: 8
    readonly property int radiusLarge: 12
}

