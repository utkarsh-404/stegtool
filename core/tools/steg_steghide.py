# stegtool/core/tools/steg_steghide.py
import subprocess
from shutil import which

def check_install():
    if not which('steghide'):
        raise EnvironmentError("steghide not installed. Get it from https://steghide.sourceforge.net/")

def encode(cover_image_path, message_file, password, output_path):
    check_install()
    cmd = [
        'steghide', 'embed',
        '-cf', cover_image_path,
        '-ef', message_file,
        '-sf', output_path,
        '-p', password,
        '-f'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"steghide failed: {result.stderr.strip()}")

def decode(stego_image_path, password, output_path):
    check_install()
    cmd = [
        'steghide', 'extract',
        '-sf', stego_image_path,
        '-xf', output_path,
        '-p', password,
        '-f'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"steghide failed: {result.stderr.strip()}")

def detect(image_path):
    return "Steghide detection requires extraction attempt with password"