"""Módulo principal da aplicação Totem UI"""
import sys
from pathlib import Path

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine, qmlRegisterType

from src.controller.app.app_controller import AppController
from src.controller.slider.sliderController import SliderController
from src.controller.screenManager.ScreenManagerController import ScreenManagerController as ScreenStackController
from src.utils.fonts import load_font


def main():
    app = QGuiApplication(sys.argv)
    
    project_root = Path(__file__).parent.parent

    engine = QQmlApplicationEngine()
    
    view_base_path = project_root / "view"
    screens_path = view_base_path / "screens"
    assets_path = project_root / "assets" / "splash-images"
    qml_file = screens_path / "app.qml"
    
    load_font("assets/fonts/TEXAT BOLD PERSONAL USE___.otf", project_root)
    
    qmlRegisterType(AppController, "TotemUI", 1, 0, "AppController")
    qmlRegisterType(SliderController, "TotemUI", 1, 0, "SliderController")
    
    app_controller = AppController()
    slider_controller = SliderController(assets_path)
    screen_stack_controller = ScreenStackController()
    
    engine.rootContext().setContextProperty("appController", app_controller)
    engine.rootContext().setContextProperty("sliderController", slider_controller)
    engine.rootContext().setContextProperty("screenStackController", screen_stack_controller)
    
    
    screen_stack_controller.pushPage("slider")
    
    if not qml_file.exists():
        print(f"Erro: Arquivo QML não encontrado em {qml_file}")
        sys.exit(-1)
    
    engine.load(str(qml_file))
    
    if not engine.rootObjects():
        sys.exit(-1)
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
