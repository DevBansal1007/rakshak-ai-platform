
#  version 1 
# from agents.vision.ocr_agent import OCRAgent


# ocr = OCRAgent()

# result = ocr.extract_text(
#     "data/test_images/ocr.png"
# )

# print(result)

#  for just seeing in file format 
from agents.vision.ocr_agent import OCRAgent
import json
from pathlib import Path

ocr = OCRAgent()

result = ocr.extract_text("data/test_images/ocr.png")

output_dir = Path("data/outputs")
output_dir.mkdir(parents=True, exist_ok=True)

with open(output_dir / "ocr_output.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

print("✅ OCR completed.")
print("📄 Output saved to data/outputs/ocr_output.json")