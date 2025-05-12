# stegtool/core/tools/steg_exiftool.py
import subprocess
from shutil import which

def check_install():
    if not which('exiftool'):
        raise EnvironmentError("exiftool not installed. Get it from https://exiftool.org/")

def encode(cover_image_path, message_file, password, output_path):
    check_install()
    cmd = [
        'exiftool',
        f'-Comment<={message_file}',
        '-overwrite_original',
        '-o', output_path,
        cover_image_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"exiftool failed: {result.stderr.strip()}")

def decode(stego_image_path, password, output_path):
    check_install()
    cmd = ['exiftool', '-Comment', '-b', stego_image_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"exiftool failed: {result.stderr.strip()}")
    
    with open(output_path, 'w') as f:
        f.write(result.stdout)

def detect(image_path):
    check_install()
    cmd = ['exiftool', image_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
