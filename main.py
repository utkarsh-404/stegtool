# stegtool/main.py
import os
from core.encode import run_encode_flow
from core.decode import run_decode_flow
from core.detect import run_detect_flow

def main_menu():
    while True:
        print("\n🔍 stegtool - Steganography Toolkit")
        print("[1] Encode Message")
        print("[2] Decode Message")
        print("[3] Detect Hidden Data")
        print("[4] Exit")
        choice = input("\nSelect an option: ").strip()

        if choice == '1':
            run_encode_flow()
        elif choice == '2':
            run_decode_flow()
        elif choice == '3':
            run_detect_flow()
        elif choice == '4':
            print("\n🖖 Goodbye!")
            break
        else:
            print("\n❌ Invalid option, try again.")

if __name__ == "__main__":
    main_menu()
