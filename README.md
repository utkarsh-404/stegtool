# 🔍 Steganography Toolkit

A powerful command-line tool for encoding, decoding, brute-forcing, and detecting steganographic content in images, audio, and video files.

> Built for cybersecurity researchers, CTF players, and stego enthusiasts.

---

## ✨ Features

* Encode secret messages into images (PNG, JPG), audio (WAV), and video (MP4)
* Decode and extract hidden messages
* Brute-force password-protected stego files using wordlists
* Detect whether a file contains steganographic data
* Uses `steghide`, `zsteg`, `OpenStego`, custom LSB logic, and more
* Linux support (Debian/Ubuntu based)
* Fully open-source

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/steganography-tool.git
cd steganography-tool
```

### 2. Run the installer

```bash
chmod +x install.sh
./install.sh
```

This will:

* Install required Python packages from `requirements.txt`
* Check and install tools like `steghide`, `zsteg`, etc.

---

## 🚀 Usage

Start the tool with:

```bash
python3 main.py
```

You'll see a menu:

```
1. Encode a message into a file
2. Decode a message from a file
3. Brute-force a password-protected stego file
4. Detect if a file contains hidden data
5. Exit
```

Just pick what you want to do and follow the prompts.

---

## 🔧 Tools Used

* [steghide](https://github.com/StefanoDeVuono/steghide)
* [zsteg](https://github.com/zed-0xff/zsteg)
* [OpenStego](https://www.openstego.com/)
* Python (`Pillow`, `numpy`, `opencv-python`)
* Bash

---

## 📁 Project Structure

```
steganography-tool/
├── core/
│   ├── encode.py
│   ├── decode.py
│   ├── brute_force.py
│   ├── detect.py
│   ├── tools/
│   │   ├── custom_lsb.py
│   │   ├── steg_steg_hide.py
│   │   ├── steg_zsteg.py
│   │   ├── steg_opensteg.py
│   │   ├── steg_audio.py
│   │   ├── steg_video.py
│   │   └── __init__.py
│   └── __init__.py
│
├── utils/
│   ├── installer.py
│   ├── check_tools.py
│   ├── logger.py
│   └── __init__.py
│
├── install.sh
├── requirements.txt
├── main.py
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🔪 Tested On

* Ubuntu 22.04 LTS
* Kali Linux

---

## 📄 License

MIT License — use freely, just give credit.

---

## 👨‍💻 Contribute

Pull requests and ideas are welcome. If you want to extend functionality (e.g., better audio/video support), feel free to open an issue or PR.

---

## ☕ Disclaimer

For educational and legal testing purposes only. Misuse of this tool is strictly prohibited.
