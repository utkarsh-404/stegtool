import os
import subprocess
import sys
from utils.check_tools import check_all_tools

def install_requirements():
    """Install Python dependencies via pip."""
    try:
        print("[*] Installing Python dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("[+] Python dependencies installed.")
    except subprocess.CalledProcessError:
        print("[!] Failed to install Python dependencies.")
        sys.exit(1)

def ensure_dependencies():
    """Ensure required tools and libraries are installed."""
    print("[*] Checking system dependencies...")
    
    # Install system dependencies if not already installed
    system_tools = ['steghide', 'zsteg', 'opensteg', 'ffmpeg']
    for tool in system_tools:
        if not is_tool_installed(tool):
            print(f"[!] {tool} not found. Installing...")
            install_system_tool(tool)
    
    # Check and install Python dependencies
    install_requirements()
    
    # Check if all necessary tools are available
    check_all_tools()

def is_tool_installed(tool):
    """Check if a command line tool is installed."""
    try:
        subprocess.check_call([tool, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_system_tool(tool):
    """Install the system tool using the appropriate package manager."""
    try:
        if sys.platform == 'linux' or sys.platform == 'linux2':
            subprocess.check_call(['sudo', 'apt-get', 'install', '-y', tool])
        elif sys.platform == 'darwin':
            subprocess.check_call(['brew', 'install', tool])
        else:
            print(f"[!] Unsupported OS for {tool}. Please install manually.")
            sys.exit(1)
    except subprocess.CalledProcessError:
        print(f"[!] Failed to install {tool}.")
        sys.exit(1)

if __name__ == "__main__":
    ensure_dependencies()
