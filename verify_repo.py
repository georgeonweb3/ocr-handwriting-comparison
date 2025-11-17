import os

# Define required structure and minimal content check
required_files = {
    "src/ocr/pytesseract_engine.py": 50,  # min 50 chars
    "src/ocr/easyocr_engine.py": 50,
    "src/ocr/compare.py": 100,
    "src/utils/image_loader.py": 30,
    "tests/test_metrics.py": 30,
    "README.md": 100,
    "requirements.txt": 10
}

images_required = ["Author0.png", "Author1.png", "Author2.png", "Author3.png", "Author4.png"]

# Helper to check file content length
def file_nonempty(path, min_len):
    if not os.path.exists(path):
        return False, "File missing"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        if len(content.strip()) < min_len:
            return False, f"File too short ({len(content.strip())} chars)"
    return True, "OK"

print("=== Repo Verification ===\n")

# Check Python / Markdown / requirements files
for f, min_len in required_files.items():
    ok, msg = file_nonempty(f, min_len)
    print(f"{f}: {msg}")

# Check images
images_path = "images"
if os.path.exists(images_path):
    for img in images_required:
        img_path = os.path.join(images_path, img)
        if os.path.exists(img_path):
            print(f"{img_path}: Found")
        else:
            print(f"{img_path}: Missing")
else:
    print(f"{images_path} directory missing")

# Optional: Check if Pond link exists in README
pond_link_found = False
with open("README.md", "r", encoding="utf-8") as f:
    for line in f:
        if "pond" in line.lower():
            pond_link_found = True
            break
print(f"\nPond bounty link in README: {'Found' if pond_link_found else 'Missing'}")
