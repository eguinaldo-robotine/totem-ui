"""Utilitários para carregamento de fontes"""
from pathlib import Path
from typing import Optional

from PyQt6.QtGui import QFontDatabase


def load_font(relative_path: str, project_root: Optional[Path] = None) -> Optional[str]:

    if project_root is None:
        project_root = Path(__file__).parent.parent.parent
    
    font_path = project_root / relative_path
    
    if not font_path.exists():
        print(f"Aviso: Arquivo de fonte não encontrado: {font_path}")
        return None
    
    font_id = QFontDatabase.addApplicationFont(str(font_path))
    
    if font_id == -1:
        print(f"Aviso: Não foi possível carregar a fonte de {font_path}")
        return None
    
    font_families = QFontDatabase.applicationFontFamilies(font_id)
    
    if font_families:
        font_family_name = font_families[0]
        print(f"Fonte carregada: {font_family_name} (de {relative_path})")
        return font_family_name
    
    print(f"Aviso: Nenhuma família de fonte encontrada em {font_path}")
    return None

