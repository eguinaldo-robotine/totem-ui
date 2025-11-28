"""Script para configurar o ambiente virtual e instalar dependências"""
import subprocess
import sys
from pathlib import Path


def run_command(cmd, check=True):
    """Executa um comando e exibe a saída"""
    print(f"Executando: {' '.join(cmd)}")
    result = subprocess.run(cmd, check=check, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr and result.returncode != 0:
        print(result.stderr, file=sys.stderr)
    return result


def setup_environment():
    """Configura o ambiente virtual e instala dependências"""
    venv_path = Path(__file__).parent.parent / "venv"
    
    # Verifica se o ambiente virtual já existe
    if venv_path.exists():
        print("⚠️  Ambiente virtual já existe. Deseja recriar? (s/N): ", end="")
        resposta = input().strip().lower()
        if resposta != 's':
            print("Mantendo ambiente virtual existente.")
        else:
            import shutil
            shutil.rmtree(venv_path)
            print("Ambiente virtual removido.")
    
    # Cria ambiente virtual se não existir
    if not venv_path.exists():
        print("\n📦 Criando ambiente virtual...")
        run_command([sys.executable, "-m", "venv", str(venv_path)])
    
    # Determina o executável do pip no ambiente virtual
    if sys.platform == "win32":
        pip_exe = venv_path / "Scripts" / "pip.exe"
        python_exe = venv_path / "Scripts" / "python.exe"
    else:
        pip_exe = venv_path / "bin" / "pip"
        python_exe = venv_path / "bin" / "python"
    
    # Atualiza pip
    print("\n⬆️  Atualizando pip...")
    run_command([str(python_exe), "-m", "pip", "install", "--upgrade", "pip"])
    
    # Instala o projeto
    print("\n📥 Instalando dependências do projeto...")
    project_root = Path(__file__).parent.parent
    run_command([str(pip_exe), "install", "-e", str(project_root)])
    
    print("\n✅ Ambiente configurado com sucesso!")
    print("\nPara ativar o ambiente virtual:")
    if sys.platform == "win32":
        print(f"  {venv_path}\\Scripts\\activate")
    else:
        print(f"  source {venv_path}/bin/activate")
    print("\nPara executar a aplicação:")
    print("  python src/main.py")


def main():
    """Função principal para o entry point"""
    try:
        setup_environment()
    except KeyboardInterrupt:
        print("\n\n❌ Operação cancelada pelo usuário.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"\n\n❌ Erro ao executar comando: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Erro inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

