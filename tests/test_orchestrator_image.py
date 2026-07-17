from agents.orchestrator import Orchestrator
import json
from pathlib import Path

pipeline = Orchestrator()

image_path = "data/test_images/test3.png"   # Use an image you already tested

result = pipeline.process_image(image_path)

output_dir = Path("data/outputs")
output_dir.mkdir(parents=True, exist_ok=True)

with open(output_dir / "orchestrator_image.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

print("✅ Image pipeline completed.")