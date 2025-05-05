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

    # 1. Install Ruby if missing (needed for zsteg)
    if not is_tool_installed("ruby"):
        print("[!] ruby not found. Installing ruby-full...")
        install_system_tool("ruby-full")

    # 2. Install zsteg via gem if missing
    if not is_tool_installed("zsteg"):
        print("[!] zsteg not found. Installing via gem...")
        install_ruby_gem("zsteg")

    # 3. Install other system tools if not already installed
    #    We handle opensteg, steghide, ffmpeg here
    system_tools = ['steghide', 'openstego', 'ffmpeg']
    for tool in system_tools:
        if not is_tool_installed(tool):
            print(f"[!] {tool} not found. Installing {tool}...")
            # openstego may require Java + manual install; we try apt first
            install_system_tool(tool)
    
    # 4. Install Python dependencies
    install_requirements()
    
    # 5. Final check: report any missing tools
    check_all_tools()

def is_tool_installed(tool):
    """Check if a command line tool is installed by probing --version."""
    try:
        subprocess.check_call([tool, "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_system_tool(tool):
    """Install a system tool using apt (Linux) or brew (macOS)."""
    try:
        if sys.platform.startswith('linux'):
            subprocess.check_call(['sudo', 'apt-get', 'update'], stdout=subprocess.DEVNULL)
            subprocess.check_call(['sudo', 'apt-get', 'install', '-y', tool])
        elif sys.platform == 'darwin':
            subprocess.check_call(['brew', 'install', tool])
        else:
            print(f"[!] Unsupported OS ({sys.platform}) for {tool}. Please install manually.")
            sys.exit(1)
        print(f"[+] {tool} installed.")
    except subprocess.CalledProcessError:
        print(f"[!] Failed to install {tool}.")
        # Do not exit here; allow final check to report missing tools
        

def install_ruby_gem(gem_name):
    """Install a Ruby gem."""
    try:
        subprocess.check_call(['sudo', 'gem', 'install', gem_name])
        print(f"[+] {gem_name} gem installed.")
    except subprocess.CalledProcessError:
        print(f"[!] Failed to install {gem_name} gem.")
        # Do not exit here; allow final check to report missing tools

if __name__ == "__main__":
    ensure_dependencies()
