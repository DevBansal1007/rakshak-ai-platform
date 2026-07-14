from agents.analysis.entity_agent import EntityAgent
from agents.analysis.scam_agent import ScamAgent

from pathlib import Path
import json

entity = EntityAgent()
scam = ScamAgent()

sample_dir = Path("data/sample_scam_text")
output_dir = Path("data/outputs")
output_dir.mkdir(parents=True, exist_ok=True)

for sample_file in sorted(sample_dir.glob("*.txt")):

    text = sample_file.read_text(encoding="utf-8")

    entities = entity.extract_entities(text)

    result = scam.analyze_scam(
        text=text,
        entities=entities
    )

    output = {
        "sample": sample_file.name,
        "entities": entities,
        "analysis": result
    }

    output_path = output_dir / f"{sample_file.stem}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)

    print(
        f"✓ {sample_file.name:<25} "
        f"{result['category']} "
        f"(Score: {result['risk_score']})"
    )

print("\n✅ All sample files processed successfully.")

