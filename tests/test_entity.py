from agents.analysis.entity_agent import EntityAgent
import json
from pathlib import Path


entity = EntityAgent()

sample_text = """
आपका बैंक खाता बंद कर दिया जाएगा।

कृपया इस UPI पर ₹500 भेजें:
fraud@ybl

मोबाइल: 9876543210
"""

result = entity.extract_entities(sample_text)

output_dir = Path("data/outputs")
output_dir.mkdir(parents=True, exist_ok=True)

with open(output_dir / "entity_output.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

print("✅ Entity Extraction Completed")