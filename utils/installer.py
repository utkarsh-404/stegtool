import subprocess
import platform
from utils.logger import Logger

def install_package(package_name):
    try:
        Logger.info(f"Installing {package_name}...")
        subprocess.run(["sudo", "apt-get", "install", "-y", package_name], check=True)
        Logger.success(f"{package_name} installed successfully.")
    except subprocess.CalledProcessError:
        Logger.error(f"Failed to install {package_name}.")

def install_python_package(package_name):
    try:
        Logger.info(f"Installing Python package: {package_name}...")
        subprocess.run(["pip3", "install", package_name], check=True)
        Logger.success(f"{package_name} installed successfully.")
    except subprocess.CalledProcessError:
        Logger.error(f"Failed to install Python package: {package_name}.")

def run_full_install():
    if platform.system() != "Linux":
        Logger.warning("This installer currently supports Linux only.")
        return

    cli_tools = ["steghide", "zsteg", "openstego", "exiftool", "ffmpeg", "binwalk"]
    python_packages = ["pillow", "opencv-python", "numpy", "pycryptodome"]

    Logger.info("Starting full installation...\n")

    for tool in cli_tools:
        install_package(tool)

    for pkg in python_packages:
        install_python_package(pkg)

    Logger.success("\nInstallation complete. You're ready to go!")

