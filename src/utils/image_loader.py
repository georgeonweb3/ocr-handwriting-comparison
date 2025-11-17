from PIL import Image
import os

def load_image(path: str) -> Image.Image:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Image not found: {path}")
    return Image.open(path)

def is_image_file(path: str) -> bool:
    return os.path.splitext(path)[1].lower() in {'.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'}
