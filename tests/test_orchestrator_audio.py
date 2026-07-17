from agents.orchestrator import Orchestrator
import json
from pathlib import Path

pipeline = Orchestrator()

audio_path = "data/test_audio/treat2.ogg"   # Use an audio file you already tested

result = pipeline.process_audio(audio_path)

output_dir = Path("data/outputs")
output_dir.mkdir(parents=True, exist_ok=True)

with open(output_dir / "orchestrator_audio.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

print("✅ Audio pipeline completed.")