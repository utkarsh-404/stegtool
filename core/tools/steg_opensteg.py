import os
import subprocess
import sys
from utils.check_tools import is_tool_installed

# Path to OpenStego .jar (adjust path if needed)
OPENSTEGO_JAR_PATH = os.path.join(os.path.dirname(__file__), 'bin', 'openstego.jar')

def check_openstego():
    if not os.path.exists(OPENSTEGO_JAR_PATH):
        print(f"[!] OpenStego jar not found at: {OPENSTEGO_JAR_PATH}")
        print("[!] Please download it from https://www.openstego.com/ and place it in the tools/bin directory.")
        sys.exit(1)
    if not is_tool_installed('java'):
        print("[!] Java is not installed. Please install Java to run OpenStego.")
        sys.exit(1)

def encode_openstego(cover_image, secret_file, output_image):
    """
    Use OpenStego to encode a file into an image.
    """
    check_openstego()

    try:
        command = [
            'java', '-jar', OPENSTEGO_JAR_PATH,
            'embed',
            '-mf', secret_file,
            '-cf', cover_image,
            '-sf', output_image
        ]
        subprocess.run(command, check=True)
        print(f"[+] Data embedded into {output_image}")
    except subprocess.CalledProcessError as e:
        print(f"[!] Encoding failed: {e}")


def decode_openstego(stego_image, output_dir):
    """
    Use OpenStego to decode hidden file from an image.
    """
    check_openstego()

    try:
        command = [
            'java', '-jar', OPENSTEGO_JAR_PATH,
            'extract',
            '-sf', stego_image,
            '-xd', output_dir
        ]
        subprocess.run(command, check=True)
        print(f"[+] Data extracted to {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"[!] Decoding failed: {e}")


def main():
    print("[+] Testing OpenStego wrapper")

    # Sample paths (replace with actual paths while testing)
    cover = "sample_cover.jpg"
    secret = "secret.txt"
    output = "encoded_openstego.jpg"
    output_dir = "output/"

    encode_openstego(cover, secret, output)
    decode_openstego(output, output_dir)


if __name__ == "__main__":
    main()
