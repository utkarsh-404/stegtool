import shutil
import subprocess
from utils.logger import Logger

REQUIRED_TOOLS = {
    "steghide": "https://github.com/StefanoDeVuono/steghide",
    "zsteg": "https://github.com/zed-0xff/zsteg",
    "openstego": "https://www.openstego.com/",
    "exiftool": "https://exiftool.org/",
    "ffmpeg": "https://ffmpeg.org/",
    "binwalk": "https://github.com/ReFirmLabs/binwalk",
}

def is_tool_installed(tool_name):
    return shutil.which(tool_name) is not None

def check_all_tools():
    Logger.info("Checking for required stego tools...\n")
    missing = []

    for tool, url in REQUIRED_TOOLS.items():
        if is_tool_installed(tool):
            Logger.success(f"{tool} is installed.")
        else:
            Logger.warning(f"{tool} is NOT installed.")
            missing.append((tool, url))

    if missing:
        Logger.warning("\nSome tools are missing.")
        for tool, url in missing:
            Logger.warning(f"- {tool}: {url}")

        Logger.info("Run ./install.sh to install missing tools.")
    else:
        Logger.success("\nAll required tools are installed.")

    return missing
