#!/bin/bash

echo "=============================="
echo " Steganography Tool Installer "
echo "=============================="

# Check for Python3
if ! command -v python3 &> /dev/null; then
    echo "[!] Python3 is not installed. Please install Python 3.7+ first."
    exit 1
fi

# Create virtual environment
echo "[*] Creating virtual environment..."
python3 -m venv venv || { echo "[!] Failed to create virtual environment"; exit 1; }

# Activate the virtual environment
source venv/bin/activate || { echo "[!] Failed to activate virtual environment"; exit 1; }

# Upgrade pip
echo "[*] Upgrading pip..."
pip install --upgrade pip

# Install Python dependencies
echo "[*] Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt || { echo "[!] Failed to install Python packages"; exit 1; }

# Install required system tools
echo "[*] Installing system tools..."

# Update package lists once
sudo apt-get update -y

# Steghide
if ! command -v steghide &> /dev/null; then
    echo "[*] Installing steghide..."
    sudo apt-get install -y steghide
else
    echo "[+] steghide already installed."
fi

# exiftool
if ! command -v exiftool &> /dev/null; then
    echo "[*] Installing exiftool..."
    sudo apt-get install -y libimage-exiftool-perl
else
    echo "[+] exiftool already installed."
fi

# ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "[*] Installing ffmpeg..."
    sudo apt-get install -y ffmpeg
else
    echo "[+] ffmpeg already installed."
fi

# binwalk
if ! command -v binwalk &> /dev/null; then
    echo "[*] Installing binwalk..."
    sudo apt-get install -y binwalk
else
    echo "[+] binwalk already installed."
fi

# Ruby (for zsteg)
if ! command -v ruby &> /dev/null; then
    echo "[*] Installing Ruby..."
    sudo apt-get install -y ruby-full
else
    echo "[+] Ruby already installed."
fi

# zsteg via gem
if ! command -v zsteg &> /dev/null; then
    echo "[*] Installing zsteg (Ruby gem)..."
    sudo gem install zsteg
    if command -v zsteg &> /dev/null; then
        echo "[+] zsteg installed successfully."
    else
        echo "[!] Failed to install zsteg via gem."
    fi
else
    echo "[+] zsteg already installed."
fi

echo "======================================"
echo "[+] Setup complete! You're good to go."
echo "To start using the tool, activate the virtual environment:"
echo "    source venv/bin/activate"
echo "Then run:"
echo "    python main.py"
echo "======================================"
