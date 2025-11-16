# OCR-Handwriting-Comparison (Improved)

This repo compares handwriting OCR performance between Pytesseract and EasyOCR. This PR adds a modular structure, a CLI compare tool, evaluation metrics (CER/WER), and improved documentation to make the project contest-ready for Pond bounties.



## Quick Highlights (what I added)
- `src/` layout with OCR engine wrappers and a compare CLI
- `src/ocr/compare.py` — run a single command to compare engines and get JSON output
- Simple but robust CER and WER implementations and unit tests
- Improved README, instructions, and sample usage
- Pond profile link included below

---

## Pond Profile

Developer / Submitter: [Agbe George Terlumun](https://cryptopond.xyz/developer/082ee7de-6b60-11f0-a1f3-024775222cc3)

---

## Install (recommended, Termux-compatible notes included)

### On desktop (Linux / macOS / Windows WSL)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# if using pytesseract, install Tesseract engine:
# Ubuntu/Debian: sudo apt install tesseract-ocr
