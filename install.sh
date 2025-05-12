#!/bin/bash
# install.sh

# Ensure script stops on errors
set -e

# Check platform
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Debian/Ubuntu
    if [ -x "$(command -v apt)" ]; then
        sudo apt update
        sudo apt install -y steghide exiftool ruby ruby-dev
    # RedHat/Fedora
    elif [ -x "$(command -v dnf)" ]; then
        sudo dnf install -y steghide perl-Image-ExifTool ruby ruby-devel
    fi

elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    brew install steghide exiftool ruby
else
    echo "Unsupported OS. Please install manually:"
    echo "- steghide: http://steghide.sourceforge.net/"
    echo "- exiftool: https://exiftool.org/"
    echo "- zsteg: https://github.com/zed-0xff/zsteg"
    exit 1
fi

# Install zsteg (Ruby gem)
if [ -x "$(command -v gem)" ]; then
    sudo gem install zsteg
else
    echo "Ruby not found! Installing Ruby..."
    # For Debian/Ubuntu
    if [ -x "$(command -v apt)" ]; then
        sudo apt install -y ruby ruby-dev
    # For RedHat/Fedora
    elif [ -x "$(command -v dnf)" ]; then
        sudo dnf install -y ruby ruby-devel
    fi
    sudo gem install zsteg
fi

# Verify installations
echo "Verifying installations:"
command -v steghide >/dev/null 2>&1 || { echo >&2 "steghide not installed!"; exit 1; }
command -v exiftool >/dev/null 2>&1 || { echo >&2 "exiftool not installed!"; exit 1; }
command -v zsteg >/dev/null 2>&1 || { echo >&2 "zsteg not installed!"; exit 1; }

echo -e "\n✅ All dependencies installed successfully!"
