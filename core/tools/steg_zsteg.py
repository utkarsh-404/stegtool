import subprocess
import sys
from utils.check_tools import is_tool_installed

# Ensure zsteg is installed
if not is_tool_installed('zsteg'):
    print("[!] zsteg is not installed. Please install it to use this feature.")
    sys.exit(1)


def encode_zsteg(image_path, output_path):
    """
    Encode a message into a PNG image using zsteg.
    :param image_path: Path to the PNG image.
    :param output_path: Path to save the encoded PNG.
    :return: None
    """
    try:
        print(f"[+] Encoding image {image_path}...")
        # Example zsteg encode command (we'll just use zsteg's ability to hide data with LSB)
        command = [
            'zsteg', image_path, '--embed', 'LSB', '--output', output_path
        ]
        subprocess.run(command, check=True)
        print(f"[+] Steganographic PNG saved as {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"[!] Error during encoding: {e}")


def decode_zsteg(image_path):
    """
    Decode hidden messages from a PNG image using zsteg.
    :param image_path: Path to the PNG stego image.
    :return: None
    """
    try:
        print(f"[+] Detecting hidden message in {image_path}...")
        command = [
            'zsteg', image_path
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"[+] Detected data:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"[!] Error during decoding: {e}")


def main():
    """
    Main function to test the zsteg encoding/decoding functionality.
    """
    print("\n[+] ZSTEG Steganography Wrapper")
    
    # Set paths
    image_path = "cover_image.png"   # Input PNG image
    output_path = "encoded_image.png" # Output file after embedding data

    # Encode data
    encode_zsteg(image_path, output_path)

    # Decode data
    decode_zsteg(output_path)


if __name__ == "__main__":
    main()
