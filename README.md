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
  ```

### Quick Install
```bash
curl -O https://raw.githubusercontent.com/utkarsh-404/stegtool/main/install.sh
chmod +x install.sh
sudo ./install.sh
```

### Manual Dependency Setup
1. **steghide**: [Download](https://steghide.sourceforge.net/)
2. **exiftool**: [Install Guide](https://exiftool.org/install.html)
3. **zsteg**: `gem install zsteg`

## 🖥 Usage

Start the interactive menu:
```bash
python main.py
```

### Menu Structure
```
[1] Encode Message
  |- Select tool (steghide/exiftool/zsteg)
  |- Input image + message
  |- Set password (optional)
  
[2] Decode Message
  |- Choose extraction tool
  |- Input stego image
  |- Provide password if needed
  
[3] Detect Hidden Data
  |- Automatic analysis with multiple tools
  |- Metadata inspection
  |- LSB pattern detection
```

### Example Workflows

**1. Encode with steghide**
```bash
# Using menu:
1. Select "Encode Message"
2. Choose steghide
3. Provide:
   - Cover image: cat.jpg
   - Message: secret.txt
   - Password: hunter2
   - Output: secret_cat.png

# Direct command (if implemented):
python main.py encode -t steghide -i cat.jpg -m secret.txt -o secret_cat.png -p hunter2
```

**2. Detect hidden data**
```bash
[3] Detect Hidden Data > suspicious_image.jpg
=> zsteg analysis shows LSB patterns
=> exiftool reveals suspicious metadata
```

**3. Extract with zsteg**
```bash
python main.py decode -t zsteg -i suspicious.png -o extracted_data
```

## 🛡 Security Notes

- 🔒 Passwords never stored - only used at runtime
- ⚠️ Avoid using real passwords for sensitive operations
- 🔐 steghide provides AES-128 encryption

## 🌐 Supported Formats

| Tool       | Encode Formats | Decode Formats |
|------------|----------------|----------------|
| steghide   | JPEG, BMP      | JPEG, BMP      |
| exiftool   | All image      | Metadata only  |
| zsteg      | N/A            | PNG, BMP       |

## 🚨 Limitations

- zsteg doesn't support encoding
- exiftool messages visible in metadata
- Steghide limited to specific formats

## 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Submit PR with tests
4. Follow PEP8 guidelines

```bash
git clone https://github.com/yourusername/stegtool
cd stegtool
# Setup dev environment
python -m venv venv
source venv/bin/activate
```

## 📜 License

MIT License - See [LICENSE](LICENSE) file

---

**Disclaimer**: Use only for legal, authorized purposes. Developers not responsible for misuse.
```
