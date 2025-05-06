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

def get_file_type(filepath):
    """
    Determines the file type based on file extension.
    :param filepath: Path to the file.
    :return: String representing file type ('image' or 'other').
    """
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
    _, extension = os.path.splitext(filepath)
    
    if extension.lower() in image_extensions:
        return 'image'
    else:
        return 'other'

def encode(filepath, message, password, tool=None):
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
        # Create a temporary message file
        message_file = "/tmp/message.txt"
        with open(message_file, "w") as msg_file:
            msg_file.write(message)
        
        # Call the encode function from steg_steg_hide
        output_file = filepath  # or you can specify a different output path
        steg_steg_hide.encode_steg_hide(filepath, message_file, password, output_file)
    elif tool == 'zsteg':
        steg_zsteg.encode(filepath, message)
    elif tool == 'opensteg':
        steg_opensteg.encode(filepath, message, password)
    else:
        print(f"[!] Tool '{tool}' not supported yet.")



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
