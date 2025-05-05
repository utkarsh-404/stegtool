#!/bin/bash

# Ensure script is run with sudo (needed for apt installs)
if [ "$(id -u)" -ne 0 ]; then
  echo "Please run with sudo: sudo ./install.sh"
  exit 1
fi

echo "🔧 Updating system packages..."
apt-get update -y

echo "📦 Installing required CLI tools..."
apt-get install -y steghide zsteg openstego libimage-exiftool-perl ffmpeg binwalk

echo "🐍 Installing Python dependencies from requirements.txt..."
# Make sure pip3 is available
if ! command -v pip3 &> /dev/null; then
  echo "pip3 could not be found. Installing python3-pip..."
  apt-get install -y python3-pip
fi

pip3 install -r requirements.txt

echo "✅ Installation complete! Run 'python3 main.py' to start the tool."
