import argparse
import os
import sys
from pathlib import Path

# Importing decoding tools
sys.path.append(str(Path(__file__).resolve().parents[1]))  # Add root to path

from core.tools import custom_lsb, steg_steg_hide, steg_zsteg, steg_opensteg


def get_file_type(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext in ['.png', '.jpg', '.jpeg', '.bmp']:
        return 'image'
    elif ext in ['.wav', '.mp3']:
        return 'audio'
    elif ext in ['.mp4', '.avi', '.mov', '.mkv']:
        return 'video'
    else:
        return 'unknown'


def decode_message(filepath, password=None, tool=None):
    file_type = get_file_type(filepath)

    if tool is None:
        if file_type == 'image':
            tool = 'custom_lsb'
        else:
            print("[!] Please specify a tool for non-image files.")
            return

    print(f"[+] Using tool: {tool}")

    if tool == 'custom_lsb':
        message = custom_lsb.decode(filepath)
    elif tool == 'steghide':
        message = steg_steg_hide.decode(filepath, password)
    elif tool == 'zsteg':
        message = steg_zsteg.decode(filepath)
    elif tool == 'opensteg':
        message = steg_opensteg.decode(filepath, password)
    else:
        print(f"[!] Tool '{tool}' not supported yet.")
        return

    if message:
        print(f"[+] Hidden message:\n{message}")
    else:
        print("[!] No message found or decoding failed.")


def main():
    parser = argparse.ArgumentParser(description="Decode a hidden message from a media file.")
    parser.add_argument('--file', required=True, help='Path to the stego file')
    parser.add_argument('--password', help='Password if required (e.g., for steghide)')
    parser.add_argument('--tool', choices=['custom_lsb', 'steghide', 'zsteg', 'opensteg'], help='Tool to use (default: custom_lsb for images)')

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"[!] File not found: {args.file}")
        sys.exit(1)

    decode_message(args.file, args.password, args.tool)


if __name__ == "__main__":
    main()
