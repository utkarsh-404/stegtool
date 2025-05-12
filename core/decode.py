# stegtool/core/decode.py
import os
from getpass import getpass
from importlib import import_module
from pathlib import Path

TOOLS = {
    'steghide': 'steg_steghide',
    'exiftool': 'steg_exiftool',
    'zsteg': 'steg_zsteg'
}

def run_decode_flow():
    try:
        print("\n🔍 Decode Mode")
        
        # Select tool
        print("\nAvailable tools:")
        for i, tool in enumerate(TOOLS.keys(), 1):
            print(f"[{i}] {tool}")
        tool_idx = int(input("\nSelect tool: ")) - 1
        tool_name = list(TOOLS.keys())[tool_idx]
        tool_module = import_module(f'core.tools.{TOOLS[tool_name]}')

        # Get inputs
        stego_path = input("\nEnter stego image path: ").strip()
        if not Path(stego_path).exists():
            raise ValueError("Stego image not found")

        password = getpass("\nPassword (if required): ")
        output_path = input("\nOutput file path for extracted message: ").strip()

        # Execute decoding
        print("\n🔓 Extracting message...")
        tool_module.decode(
            stego_image_path=stego_path,
            password=password,
            output_path=output_path
        )

        print(f"\n✅ Success! Message saved to: {output_path}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")