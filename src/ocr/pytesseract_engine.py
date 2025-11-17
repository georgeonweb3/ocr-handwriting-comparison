# src/ocr/pytesseract_engine.py
from PIL import Image, ImageOps
import pytesseract
from typing import Dict

def preprocess_image(image: Image.Image) -> Image.Image:
    """Basic grayscale + contrast enhancement"""
    img = image.convert("L")
    img = ImageOps.autocontrast(img)
    return img

def ocr_image(image: Image.Image, lang: str = 'eng') -> Dict:
    """
    Run pytesseract OCR on a PIL image.
    Returns a dict with 'text' and 'raw' (tsv dict).
    """
    img = preprocess_image(image)
    text = pytesseract.image_to_string(img, lang=lang)
    data = pytesseract.image_to_data(img, lang=lang, output_type=pytesseract.Output.DICT)
    return {
        "engine": "pytesseract",
        "text": text.strip(),
        "raw": data
    }

