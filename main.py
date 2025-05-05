#!/usr/bin/env python3

import sys
import os

# Core functionalities
from core.encode import run_encode
from core.decode import run_decode
from core.brute_force import run_brute_force
from core.detect import run_detect

# Utils
from utils.installer import ensure_dependencies
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

if __name__ == "__main__":
    try:
        ensure_dependencies()
        main_menu()
    except KeyboardInterrupt:
        print_error("\nInterrupted by user. Exiting.")
        sys.exit(1)
