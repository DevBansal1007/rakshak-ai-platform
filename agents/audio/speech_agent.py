from faster_whisper import WhisperModel

class SpeechAgent:
    def __init__(self):
        """
        Initialize Whisper model once.
        """
        
        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

    def transcribe_audio(self, audio_path: str):
        """
        Convert speech to text.

        Args:
            audio_path (str): Path to audio file.

        Returns:
            dict
        """
        try:

            segments, info = self.model.transcribe(
                audio_path,
                beam_size=5,
                vad_filter=True
            )

            transcript = " ".join(
                segment.text.strip()
                for segment in segments
            )

            return {
                "success": True,
                "transcript": transcript,
                "language": info.language,
                "duration": info.duration
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }