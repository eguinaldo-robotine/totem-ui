"""Módulo principal da aplicação Totem UI - Versão Debug
Captura todos os erros, exceções e logs durante a execução
"""
import sys
import logging
import traceback
import warnings
from pathlib import Path
from datetime import datetime
from typing import Any

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt6.QtCore import qInstallMessageHandler, QtMsgType, QLoggingCategory

from src.controller.app.app_controller import AppController
from src.controller.slider.sliderController import SliderController
from src.controller.screenManager.ScreenManagerController import ScreenManagerController as ScreenStackController
from src.utils.fonts import load_font


# Configuração do logging
def setup_logging(log_dir: Path) -> logging.Logger:
    """Configura o sistema de logging com arquivo e console"""
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Nome do arquivo de log com timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"totem_ui_debug_{timestamp}.log"
    
    # Configuração do formato
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    
    # Configuração do logger
    logger = logging.getLogger("TotemUI")
    logger.setLevel(logging.DEBUG)
    
    # Remove handlers existentes
    logger.handlers.clear()
    
    # Handler para arquivo (todos os níveis)
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(log_format, date_format))
    logger.addHandler(file_handler)
    
    # Handler para console (INFO e acima)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter(log_format, date_format))
    logger.addHandler(console_handler)
    
    logger.info(f"Logging iniciado. Arquivo de log: {log_file}")
    logger.info("=" * 80)
    logger.info("Iniciando aplicação Totem UI em modo DEBUG")
    logger.info("=" * 80)
    
    return logger


def qt_message_handler(msg_type: QtMsgType, context: Any, message: str) -> None:
    """Handler para mensagens do Qt/QML"""
    logger = logging.getLogger("TotemUI.Qt")
    
    # Mapeia tipos de mensagem do Qt para níveis de log
    msg_type_map = {
        QtMsgType.QtDebugMsg: logging.DEBUG,
        QtMsgType.QtInfoMsg: logging.INFO,
        QtMsgType.QtWarningMsg: logging.WARNING,
        QtMsgType.QtCriticalMsg: logging.ERROR,
        QtMsgType.QtFatalMsg: logging.CRITICAL,
    }
    
    log_level = msg_type_map.get(msg_type, logging.INFO)
    
    # Formata a mensagem com contexto
    formatted_message = f"[{context.category}] {message}"
    if context.file:
        formatted_message += f" (File: {context.file}, Line: {context.line}, Function: {context.function})"
    
    logger.log(log_level, formatted_message)


def exception_handler(exc_type: type, exc_value: Exception, exc_traceback: Any) -> None:
    """Handler global para exceções não tratadas"""
    logger = logging.getLogger("TotemUI.Exception")
    
    if issubclass(exc_type, KeyboardInterrupt):
        # Permite que KeyboardInterrupt seja tratado normalmente
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    
    # Loga a exceção completa
    logger.critical(
        "Exceção não tratada capturada!",
        exc_info=(exc_type, exc_value, exc_traceback)
    )
    
    # Também imprime no console para visibilidade imediata
    print("\n" + "=" * 80, file=sys.stderr)
    print("ERRO CRÍTICO: Exceção não tratada!", file=sys.stderr)
    print("=" * 80, file=sys.stderr)
    traceback.print_exception(exc_type, exc_value, exc_traceback, file=sys.stderr)
    print("=" * 80 + "\n", file=sys.stderr)
    
    # Chama o handler padrão também
    sys.__excepthook__(exc_type, exc_value, exc_traceback)


def warning_handler(message: Warning, category: type, filename: str, lineno: int, file=None, line=None) -> None:
    """Handler para warnings do Python"""
    logger = logging.getLogger("TotemUI.Warning")
    logger.warning(
        f"Warning capturado: {category.__name__}: {message} "
        f"(File: {filename}, Line: {lineno})"
    )


def main():
    """Função principal que inicia a aplicação em modo debug"""
    # Obtém o diretório raiz do projeto
    project_root = Path(__file__).parent.parent
    log_dir = project_root / "logs"
    
    # Configura logging
    logger = setup_logging(log_dir)
    
    try:
        logger.info("Configurando handlers de exceção e warnings...")
        
        # Configura handler global de exceções
        sys.excepthook = exception_handler
        
        # Configura handler de warnings
        warnings.showwarning = warning_handler
        warnings.filterwarnings("always")  # Mostra todos os warnings
        
        # Configura handler de mensagens do Qt
        qInstallMessageHandler(qt_message_handler)
        
        logger.info("Inicializando QGuiApplication...")
        print("[DEBUG] Criando QGuiApplication...", file=sys.stderr)
        
        # Configura orientação retrato para framebuffer
        import os
        os.environ.setdefault('QT_QPA_FB_ROTATION', '90')  # 90 = retrato, 270 = retrato invertido
        
        try:
            app = QGuiApplication(sys.argv)
            
            # Configura a orientação da tela
            from PyQt6.QtCore import Qt
            # Pode também usar app.setAttribute se necessário
            
            logger.info(f"QGuiApplication criado. Argumentos: {sys.argv}")
            print(f"[DEBUG] QGuiApplication criado", file=sys.stderr)
        except Exception as e:
            logger.error(f"Erro ao criar QGuiApplication: {e}", exc_info=True)
            raise
        
        # Carrega a fonte Texas Tango
        font_family = load_font("assets/fonts/TEXAT BOLD PERSONAL USE___.otf", project_root)
        if font_family:
            logger.info(f"Fonte Texas Tango carregada: {font_family}")
            print(f"[DEBUG] Fonte Texas Tango carregada: {font_family}", file=sys.stderr)
        
        logger.info("Criando QQmlApplicationEngine...")
        engine = QQmlApplicationEngine()
        
        # Obtém os diretórios base
        view_base_path = project_root / "view"
        screens_path = view_base_path / "screens"
        assets_path = project_root / "assets" / "splash-images"
        
        logger.info(f"Diretórios configurados:")
        logger.info(f"  - Project root: {project_root}")
        logger.info(f"  - View base: {view_base_path}")
        logger.info(f"  - Screens: {screens_path}")
        logger.info(f"  - Assets: {assets_path}")
        
        # Verifica se os diretórios existem
        if not view_base_path.exists():
            logger.error(f"Diretório view não encontrado: {view_base_path}")
            raise FileNotFoundError(f"Diretório view não encontrado: {view_base_path}")
        
        if not screens_path.exists():
            logger.error(f"Diretório screens não encontrado: {screens_path}")
            raise FileNotFoundError(f"Diretório screens não encontrado: {screens_path}")
        
        logger.info("Registrando controllers no QML...")
        try:
            qmlRegisterType(AppController, "TotemUI", 1, 0, "AppController")
            logger.debug("AppController registrado")
            
            qmlRegisterType(SliderController, "TotemUI", 1, 0, "SliderController")
            logger.debug("SliderController registrado")
        except Exception as e:
            logger.error(f"Erro ao registrar controllers: {e}", exc_info=True)
            raise
        
        logger.info("Criando instâncias dos controllers...")
        try:
            app_controller = AppController()
            logger.debug("AppController criado")
            
            slider_controller = SliderController(assets_path)
            logger.debug(f"SliderController criado com assets_path: {assets_path}")
            
            screen_stack_controller = ScreenStackController()
            logger.debug("ScreenStackController criado")
        except Exception as e:
            logger.error(f"Erro ao criar controllers: {e}", exc_info=True)
            raise
        
        logger.info("Registrando controllers no contexto QML...")
        try:
            engine.rootContext().setContextProperty("appController", app_controller)
            engine.rootContext().setContextProperty("sliderController", slider_controller)
            engine.rootContext().setContextProperty("screenStackController", screen_stack_controller)
            logger.debug("Controllers registrados no contexto QML")
        except Exception as e:
            logger.error(f"Erro ao registrar controllers no contexto: {e}", exc_info=True)
            raise
        
        qml_file = screens_path / "app.qml"
        logger.info(f"Verificando arquivo QML: {qml_file}")
        
        if not qml_file.exists():
            error_msg = f"Erro: Arquivo QML não encontrado em {qml_file}"
            logger.error(error_msg)
            print(error_msg, file=sys.stderr)
            sys.exit(-1)
        
        logger.info(f"Carregando arquivo QML: {qml_file}")
        try:
            screen_stack_controller.pushPage("slider")
            logger.debug("Página 'slider' adicionada à pilha")
            
            engine.load(str(qml_file))
            logger.info("Arquivo QML carregado com sucesso")
        except Exception as e:
            logger.error(f"Erro ao carregar QML: {e}", exc_info=True)
            raise
        
        if not engine.rootObjects():
            error_msg = "Erro: Nenhum objeto raiz foi criado após carregar o QML"
            logger.error(error_msg)
            print(error_msg, file=sys.stderr)
            sys.exit(-1)
        
        logger.info("Aplicação iniciada com sucesso. Entrando no loop de eventos...")
        logger.info("=" * 80)
        
        exit_code = app.exec()
        
        logger.info("=" * 80)
        logger.info(f"Aplicação finalizada com código de saída: {exit_code}")
        
        sys.exit(exit_code)
        
    except KeyboardInterrupt:
        logger.info("Aplicação interrompida pelo usuário (Ctrl+C)")
        sys.exit(0)
    except Exception as e:
        logger.critical(f"Erro fatal durante inicialização: {e}", exc_info=True)
        print(f"\nErro fatal: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(-1)


if __name__ == "__main__":
    main()

