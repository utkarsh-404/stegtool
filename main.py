#!/usr/bin/env python3

import sys
import os
import argparse

# Core functionalities
from core.encode import run_encode
from core.decode import run_decode
from core.brute_force import run_brute_force
from core.detect import run_detect

# Utils
from utils.logger import banner, print_info, print_error


def main_menu():
    banner()

    while True:
        print_info("Select an option:")
        print("1. Encode a message into a file")
        print("2. Decode a message from a file")
        print("3. Brute-force a password-protected stego file")
        print("4. Detect if a file contains hidden data")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '1':
            run_encode()
        elif choice == '2':
            run_decode()
        elif choice == '3':
            run_brute_force()
        elif choice == '4':
            run_detect()
        elif choice == '5':
            print_info("Exiting. Goodbye!")
            sys.exit(0)
        else:
            print_error("Invalid input. Please choose a number between 1 and 5.")


def handle_cli_args():
    parser = argparse.ArgumentParser(
        description="Steganography Tool - CLI mode",
        usage="python3 main.py <command> [options]"
    )

    subparsers = parser.add_subparsers(dest="command")

    # Encode
    encode_parser = subparsers.add_parser("encode", help="Encode a message into a file")
    encode_parser.add_argument("--file", required=True, help="Path to input file")
    encode_parser.add_argument("--message", required=True, help="Message to hide")
    encode_parser.add_argument("--password", help="Password (if needed)")
    encode_parser.add_argument("--tool", choices=["custom_lsb", "steghide", "zsteg", "opensteg"], default="custom_lsb")

    # Decode
    decode_parser = subparsers.add_parser("decode", help="Decode a message from a file")
    decode_parser.add_argument("--file", required=True, help="Path to input file")
    decode_parser.add_argument("--password", help="Password (if needed)")
    decode_parser.add_argument("--tool", choices=["custom_lsb", "steghide", "zsteg", "opensteg"], default="custom_lsb")

    # Brute-force
    brute_parser = subparsers.add_parser("brute", help="Brute-force password for a stego file")
    brute_parser.add_argument("--file", required=True, help="Path to input file")
    brute_parser.add_argument("--wordlist", required=True, help="Path to wordlist file")
    brute_parser.add_argument("--tool", choices=["steghide"], default="steghide")

    # Detect
    detect_parser = subparsers.add_parser("detect", help="Detect hidden data in a file")
    detect_parser.add_argument("--file", required=True, help="Path to input file")

    args = parser.parse_args()

    if args.command == "encode":
        run_encode(file=args.file, message=args.message, password=args.password, tool=args.tool)
    elif args.command == "decode":
        run_decode(file=args.file, password=args.password, tool=args.tool)
    elif args.command == "brute":
        run_brute_force(file=args.file, wordlist=args.wordlist, tool=args.tool)
    elif args.command == "detect":
        run_detect(file=args.file)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            handle_cli_args()
        else:
            main_menu()
    except KeyboardInterrupt:
        print_error("\nInterrupted by user. Exiting.")
        sys.exit(1)
        
