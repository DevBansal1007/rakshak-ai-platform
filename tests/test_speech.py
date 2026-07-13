from agents.audio.speech_agent import SpeechAgent
import json
from pathlib import Path

speech = SpeechAgent()

result = speech.transcribe_audio(
    "data/test_audio/treat2.ogg"
)

output_dir = Path("data/outputs")
output_dir.mkdir(parents=True, exist_ok=True)

with open(output_dir / "speech_output.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

print("✅ Speech-to-Text completed.")
print("📄 Output saved to data/outputs/speech_output.json")