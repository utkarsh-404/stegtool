# stegtool/utils/check_tools.py
import shutil

def is_tool_installed(tool_name):
    return shutil.which(tool_name) is not None

def verify_dependencies():
    required = ['steghide', 'exiftool', 'zsteg']
    missing = [tool for tool in required if not is_tool_installed(tool)]
    if missing:
        print("⚠️ Missing dependencies:")
        for tool in missing:
            print(f"- {tool}")
        print("\nInstall missing tools before proceeding")
        return False
    return True
