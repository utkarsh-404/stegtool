# 🔍 stegtool - Python Steganography Toolkit

A comprehensive command-line interface for image steganography operations. Hide and extract secret messages using various steganographic techniques with modular tool support.

![CLI Demo](https://via.placeholder.com/800x400.png?text=CLI+Demo+Screenshot) *Example CLI interface*

## ✨ Features

- **Multiple Steganography Methods**
  - 🖼️ Image-based steganography
  - 🔐 Password-protected secrets
  - 🕵️♂️ Hidden data detection
- **Supported Tools**
  - `steghide` - Robust encryption-based hiding
  - `zsteg` - Advanced LSB analysis
  - `exiftool` - Metadata manipulation
- **Core Operations**
  - 📥 Encode messages/files into images
  - 📤 Decode hidden content from images
  - 🔍 Detect potential steganographic content
- **Cross-Platform**
  - 🐧 Linux / 🍎 macOS / 🪟 Windows (WSL)

## 🛠 Installation

### Prerequisites
- Python 3.7+
- Base system packages:
  ```bash
  # Debian/Ubuntu
  sudo apt install build-essential ruby-dev
