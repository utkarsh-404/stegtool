# stegtool/core/detect.py
import os
from importlib import import_module
from pathlib import Path

TOOLS = {
    'exiftool': 'steg_exiftool',
    'zsteg': 'steg_zsteg'
}

def run_detect_flow():
    try:
        print("\n🔎 Detection Mode")
        image_path = input("\nEnter image path to analyze: ").strip()
        if not Path(image_path).exists():
            raise ValueError("Image file not found")

        print("\n🕵️ Scanning for hidden content...\n")
        
        for tool_name, module_name in TOOLS.items():
            try:
                tool_module = import_module(f'core.tools.{module_name}')
                if hasattr(tool_module, 'detect'):
                    print(f"=== Results from {tool_name.upper()} ===")
                    print(tool_module.detect(image_path) + "\n")
            except Exception as e:
                print(f"{tool_name} detection failed: {str(e)}\n")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
