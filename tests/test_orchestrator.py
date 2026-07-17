from agents.orchestrator import Orchestrator
import json
from pathlib import Path

pipeline = Orchestrator()

text = """
प्रिय ग्राहक,

आपका आधार अवैध गतिविधि से जुड़ा पाया गया है।

तुरंत कॉल करें।

मोबाइल:
9876543210

UPI:
fraud@paytm

OTP साझा करें।
"""

result = pipeline.process_text(text)

output_dir = Path("data/outputs")
output_dir.mkdir(parents=True, exist_ok=True)

with open(output_dir / "orchestrator_text.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

print("✅ Orchestrator text pipeline completed.")



