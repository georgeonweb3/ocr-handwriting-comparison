import argparse
import json
from pathlib import Path
from PIL import Image
from src.ocr.pytesseract_engine import ocr_image as pytesseract_ocr
from src.ocr.easyocr_engine import ocr_image as easyocr_ocr
from src.utils.image_loader import load_image, is_image_file

def compare_image(image_path: str, lang: str = 'eng'):
    if not is_image_file(image_path):
        raise ValueError("Provided file doesn't look like an image")
    img = load_image(image_path)
    res_tess = pytesseract_ocr(img, lang=lang)
    res_easy = easyocr_ocr(img, lang_list=[lang[:2]])
    return {
        "image": str(image_path),
        "pytesseract": res_tess,
        "easyocr": res_easy
    }

def main():
    parser = argparse.ArgumentParser(description="Compare OCR engines")
    parser.add_argument("--image", "-i", required=True)
    parser.add_argument("--lang", "-l", default="eng")
    parser.add_argument("--output", "-o", default=None)
    args = parser.parse_args()
    out = compare_image(args.image, args.lang)
    out_json = json.dumps(out, indent=2)
    if args.output:
        Path(args.output).write_text(out_json, encoding="utf-8")
        print(f"Wrote results to {args.output}")
    else:
        print(out_json)

if __name__ == "__main__":
    main()
