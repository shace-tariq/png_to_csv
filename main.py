import cv2
import pytesseract
import re
import pandas as pd

# Set path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Step 1: Load and preprocess image
image = cv2.imread("input.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Step 2: OCR extraction
text = pytesseract.image_to_string(gray, config='--psm 6')

# Step 3: Process lines
lines = text.strip().split('\n')
lines = [line.strip() for line in lines if line.strip()]
rows = [re.split(r'\s+', line) for line in lines]
rows = [row for row in rows if len(row) >= 3]

# Normalize row lengths
max_cols = max(len(row) for row in rows)
for row in rows:
    while len(row) < max_cols:
        row.append("")

# Step 4: Save to CSV
df = pd.DataFrame(rows)
df.to_csv("output.csv", index=False, header=False)
print("✅ Data saved to output.csv")
