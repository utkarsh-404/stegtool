import subprocess
import os
import sys
from pathlib import Path

# Ensure Steghide is installed
sys.path.append(str(Path(__file__).resolve().parents[2]))

from utils.check_tools import is_tool_installed

# Check if Steghide is installed
if not is_tool_installed('steghide'):
    print("[!] Steghide is not installed. Please install it to use this feature.")
    sys.exit(1)


def encode_steg_hide(image_path, message_file, password, output_path):
    """
    Encode a message into an image using Steghide.
    :param image_path: Path to the cover image.
    :param message_file: Path to the file containing the message to hide.
    :param password: Password for the steganography.
    :param output_path: Path to save the output file.
    :return: None
    """
    try:
        print(f"[+] Encoding message from {message_file} into {image_path}...")
        command = [
            'steghide', 'embed', '-cf', image_path, '-ef', message_file,
            '-p', password, '-sf', output_path
        ]
        subprocess.run(command, check=True)
        print(f"[+] Steganographic image saved as {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"[!] Error during encoding: {e}")


def decode_steg_hide(stego_image_path, password, output_message_path):
    """
    Decode a hidden message from an image using Steghide.
    :param stego_image_path: Path to the stego image.
    :param password: Password for the steganography.
    :param output_message_path: Path to save the extracted message.
    :return: None
    """
    try:
        print(f"[+] Extracting message from {stego_image_path}...")
        command = [
            'steghide', 'extract', '-sf', stego_image_path, '-p', password,
            '-xf', output_message_path
        ]
        subprocess.run(command, check=True)
        print(f"[+] Message extracted and saved to {output_message_path}")
    except subprocess.CalledProcessError as e:
        print(f"[!] Error during decoding: {e}")


def main():
    """
    Main function to test the Steghide encoding/decoding functionality.
    """
    print("\n[+] Steghide Steganography Wrapper")
    
    # Set paths
    image_path = "cover_image.png"  # Cover image
    message_file = "message.txt"    # Message file
    output_path = "stego_image.png" # Output file
    password = "secret_password"    # Password for encoding/decoding
    output_message_path = "output_message.txt"  # Decoded message

    # Encode message into image
    encode_steg_hide(image_path, message_file, password, output_path)

    # Decode message from image
    decode_steg_hide(output_path, password, output_message_path)


if __name__ == "__main__":
    main()
