import argparse
import os
import sys
from pathlib import Path

# Importing custom encoding tools
sys.path.append(str(Path(__file__).resolve().parents[1]))  # add root to path

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


def encode_message(filepath, message, password, tool=None):
    file_type = get_file_type(filepath)

    if tool is None:
        if file_type == 'image':
            tool = 'custom_lsb'
        else:
            print("[!] Please specify a tool for non-image files.")
            return

    print(f"[+] Using tool: {tool}")

    if tool == 'custom_lsb':
        custom_lsb.encode(filepath, message)
    elif tool == 'steghide':
        steg_steg_hide.encode(filepath, message, password)
    elif tool == 'zsteg':
        steg_zsteg.encode(filepath, message)
    elif tool == 'opensteg':
        steg_opensteg.encode(filepath, message, password)
    else:
        print(f"[!] Tool '{tool}' not supported yet.")


def run_encode():
    parser = argparse.ArgumentParser(description="Encode a message into a media file.")
    parser.add_argument('--file', required=True, help='Path to input image/audio/video file')
    parser.add_argument('--message', required=True, help='Message to hide')
    parser.add_argument('--password', help='Password (optional, used for tools like steghide)')
    parser.add_argument('--tool', choices=['custom_lsb', 'steghide', 'zsteg', 'opensteg'], help='Tool to use (default: custom_lsb for images)')

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"[!] File not found: {args.file}")
        sys.exit(1)

    encode_message(args.file, args.message, args.password, args.tool)


if __name__ == "__main__":
    main()
