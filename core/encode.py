# stegtool/core/encode.py
import os
import tempfile
from getpass import getpass
from importlib import import_module
from pathlib import Path

TOOLS = {
    'steghide': 'steg_steghide',
    'exiftool': 'steg_exiftool',
    'zsteg': 'steg_zsteg'
}

def run_encode_flow():
    try:
        print("\n🛠  Encode Mode")
        
        # Select tool
        print("\nAvailable tools:")
        for i, tool in enumerate(TOOLS.keys(), 1):
            print(f"[{i}] {tool}")
        tool_idx = int(input("\nSelect tool: ")) - 1
        tool_name = list(TOOLS.keys())[tool_idx]
        tool_module = import_module(f'core.tools.{TOOLS[tool_name]}')

        # Get inputs
        cover_path = input("\nEnter cover image path: ").strip()
        if not Path(cover_path).exists():
            raise ValueError("Cover image not found")

        msg_type = input("\nInput message as (1) text or (2) file: ").strip()
        if msg_type == '1':
            with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
                f.write(input("\nEnter secret message: "))
                msg_path = f.name
        elif msg_type == '2':
            msg_path = input("\nEnter message file path: ").strip()
            if not Path(msg_path).exists():
                raise ValueError("Message file not found")
        else:
            raise ValueError("Invalid message type")

        password = getpass("\nPassword (optional, press Enter to skip): ")
        output_path = input("\nOutput stego image path: ").strip()

        # Execute encoding
        print("\n🔒 Encoding message...")
        tool_module.encode(
            cover_image_path=cover_path,
            message_file=msg_path,
            password=password,
            output_path=output_path
        )

        print(f"\n✅ Success! Stego image saved to: {output_path}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
    finally:
        if msg_type == '1' and 'msg_path' in locals():
            os.remove(msg_path)