from agents.vision.ocr_agent import OCRAgent
from agents.audio.speech_agent import SpeechAgent
from agents.analysis.entity_agent import EntityAgent
from agents.analysis.scam_agent import ScamAgent


class Orchestrator:
    """
    Coordinates all AI agents.
    """

    def __init__(self):

        self.ocr_agent = OCRAgent()

        self.speech_agent = SpeechAgent()

        self.entity_agent = EntityAgent()

        self.scam_agent = ScamAgent()

    # text processing
    def process_text(self, text: str):

        entities = self.entity_agent.extract_entities(text)

        analysis = self.scam_agent.analyze_scam(
            text=text,
            entities=entities
        )

        return {
            "success": True,
            "input_type": "text",
            "text": text,
            "entities": entities,
            "analysis": analysis
        }
    
    # IMAGE PROCESSING
    def process_image(self, image_path: str):

        ocr_result = self.ocr_agent.extract_text(image_path)

        if not ocr_result["success"]:

            return ocr_result

        text = ocr_result["text"]

        entities = self.entity_agent.extract_entities(text)

        analysis = self.scam_agent.analyze_scam(
            text=text,
            entities=entities
        )

        return {
            "success": True,
            "input_type": "image",
            "text": text,
            "entities": entities,
            "analysis": analysis
        }


        # AUDIO PROCESSING
    def process_audio(self, audio_path: str):

        speech_result = self.speech_agent.transcribe_audio(audio_path)

        if not speech_result["success"]:

            return speech_result

        text = speech_result["transcript"]

        entities = self.entity_agent.extract_entities(text)

        analysis = self.scam_agent.analyze_scam(
            text=text,
            entities=entities
        )

        return {
            "success": True,
            "input_type": "audio",
            "text": text,
            "entities": entities,
            "analysis": analysis
        }