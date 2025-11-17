from PIL import Image
from typing import Dict
import easyocr
import numpy as np

_READER = None

def _get_reader(lang_list=['en']):
    global _READER
    if _READER is None:
        _READER = easyocr.Reader(lang_list, gpu=False)
    return _READER

def ocr_image(image: Image.Image, lang_list=['en']) -> Dict:
    reader = _get_reader(lang_list)
    img_arr = np.array(image.convert("RGB"))
    results = reader.readtext(img_arr)
    text = " ".join([r[1] for r in results]).strip()
    details = [{"bbox": r[0], "text": r[1], "conf": float(r[2])} for r in results]
    return {
        "engine": "easyocr",
        "text": text,
        "details": details
    }
