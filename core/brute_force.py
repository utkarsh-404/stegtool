import argparse
import subprocess
import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))  # Add root to path

from utils.check_tools import is_tool_installed

def brute_force_steghide(file_path, wordlist, output_file="bruteforce_output.txt", quiet=False):
    if not is_tool_installed("steghide"):
        print("[!] Steghide is not installed.")
        return None

    if not os.path.exists(wordlist):
        print("[!] Wordlist file not found.")
        return None

    with open(wordlist, 'r', errors='ignore') as wl:
        for password in wl:
            password = password.strip()
            if not quiet:
                print(f"[*] Trying password: {password}")
            try:
                result = subprocess.run(
                    ['steghide', 'extract', '-sf', file_path, '-xf', output_file, '-p', password, '-f'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.DEVNULL,
                    text=True
                )
                if "wrote extracted data" in result.stdout.lower():
                    print(f"[+] Success! Password: {password}")
                    with open(output_file, 'r', errors='ignore') as msg_file:
                        print(f"[+] Extracted Message:\n{msg_file.read()}")
                    return password
            except Exception as e:
                continue

    print("[-] Brute-force failed. No password matched.")
    return None


def main():
    parser = argparse.ArgumentParser(description="Brute-force steghide password using a wordlist.")
    parser.add_argument('--file', required=True, help='Stego file to attack')
    parser.add_argument('--wordlist', required=True, help='Path to password wordlist')
    parser.add_argument('--output', default='bruteforce_output.txt', help='File to save extracted message')
    parser.add_argument('--quiet', action='store_true', help='Suppress password attempts from output')

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"[!] File not found: {args.file}")
        sys.exit(1)

    brute_force_steghide(args.file, args.wordlist, args.output, args.quiet)


if __name__ == "__main__":
    main()
