"""Módulo principal da aplicação Totem UI"""
import sys
from pathlib import Path

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine, qmlRegisterType

from src.controller.app_controller import AppController
from src.controller.screen_manager_controller import ScreenManagerController
from src.controller.splash_controller import SplashController


def main():
    """Função principal que inicia a aplicação"""
    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    
    # Obtém os diretórios base
    project_root = Path(__file__).parent.parent
    qml_base_path = project_root / "qml"
    assets_path = project_root / "assets" / "splash-images"
    
    # Registra os controllers no QML
    qmlRegisterType(AppController, "TotemUI", 1, 0, "AppController")
    qmlRegisterType(ScreenManagerController, "TotemUI", 1, 0, "ScreenManagerController")
    qmlRegisterType(SplashController, "TotemUI", 1, 0, "SplashController")
    
    # Cria instâncias dos controllers e registra como contexto
    app_controller = AppController()
    screen_manager = ScreenManagerController(qml_base_path)
    splash_controller = SplashController(assets_path)
    
    engine.rootContext().setContextProperty("appController", app_controller)
    engine.rootContext().setContextProperty("screenManager", screen_manager)
    engine.rootContext().setContextProperty("splashController", splash_controller)
    
    # Obtém o diretório do arquivo atual (ApplicationWindow principal)
    qml_file = qml_base_path / "pages" / "app.qml"
    
    # Inicializa o screen manager com a página de splash
    screen_manager.initialize("splash", "Splash Screen")
    
    if not qml_file.exists():
        print(f"Erro: Arquivo QML não encontrado em {qml_file}")
        sys.exit(-1)
    
    engine.load(str(qml_file))
    
    if not engine.rootObjects():
        sys.exit(-1)
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
