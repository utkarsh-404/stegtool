# stegtool/utils/filetype.py
import mimetypes

def is_valid_image(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type and mime_type.startswith('image/')
