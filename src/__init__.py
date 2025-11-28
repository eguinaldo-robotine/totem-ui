"""Módulo principal do Totem UI"""
import sys
from pathlib import Path

# Adiciona o diretório raiz do projeto ao sys.path para permitir imports absolutos
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

