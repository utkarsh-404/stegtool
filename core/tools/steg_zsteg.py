# stegtool/core/tools/steg_zsteg.py
import subprocess
from shutil import which

def check_install():
    if not which('zsteg'):
        raise EnvironmentError("zsteg not installed. Install with 'gem install zsteg'")

def encode(*args, **kwargs):
    raise NotImplementedError("zsteg doesn't support encoding")

def decode(stego_image_path, password, output_path):
    check_install()
    cmd = ['zsteg', '-e', 'b1,bgr,lsb,xy', '-o', output_path, stego_image_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"zsteg failed: {result.stderr.strip()}")

def detect(image_path):
    check_install()
    cmd = ['zsteg', '-a', image_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
