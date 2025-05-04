import argparse
import os
import sys
import subprocess
from pathlib import Path
import mimetypes

sys.path.append(str(Path(__file__).resolve().parents[1]))

from utils.check_tools import is_tool_installed


def check_metadata(file_path):
    try:
        result = subprocess.run(['exiftool', file_path], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        suspicious_fields = [line for line in result.stdout.splitlines() if "Comment" in line or "Software" in line or "User" in line]
        return suspicious_fields
    except Exception as e:
        return []


def check_entropy(file_path):
    from collections import Counter
    import math

    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        if not data:
            return 0
        counter = Counter(data)
        total = len(data)
        entropy = -sum(count / total * math.log2(count / total) for count in counter.values())
        return entropy
    except Exception as e:
        return 0


def detect_tool_signatures(file_path):
    found = []
    try:
        with open(file_path, 'rb') as f:
            data = f.read(2048)
            if b"steghide" in data:
                found.append("steghide signature found")
            if b"OpenStego" in data:
                found.append("OpenStego signature found")
        return found
    except:
        return []


def detect_steganography(file_path):
    print(f"\n[+] Analyzing file: {file_path}")

    if not os.path.exists(file_path):
        print("[!] File does not exist.")
        return

    mime_type, _ = mimetypes.guess_type(file_path)
    print(f"[+] File type detected: {mime_type}")

    print("\n[*] Checking metadata...")
    metadata = check_metadata(file_path)
    if metadata:
        print("[!] Suspicious metadata found:")
        for line in metadata:
            print("    -", line)
    else:
        print("[+] No suspicious metadata.")

    print("\n[*] Checking file entropy...")
    entropy = check_entropy(file_path)
    print(f"[+] Entropy: {entropy:.2f}")
    if entropy > 7.5:
        print("[!] High entropy. Might contain hidden data.")
    elif entropy < 4.0:
        print("[!] Very low entropy. Might be padded or altered.")
    else:
        print("[+] Normal entropy range.")

    print("\n[*] Looking for tool-specific signatures...")
    sigs = detect_tool_signatures(file_path)
    if sigs:
        for sig in sigs:
            print(f"[!] {sig}")
    else:
        print("[+] No known tool signatures found.")

    print("\n[✓] Detection complete.")


def main():
    parser = argparse.ArgumentParser(description="Detect signs of steganography in a media file.")
    parser.add_argument('--file', required=True, help='Path to the media file to analyze')
    args = parser.parse_args()

    detect_steganography(args.file)


if __name__ == "__main__":
    main()
