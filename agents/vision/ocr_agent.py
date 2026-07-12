import easyocr
import warnings
import logging

warnings.filterwarnings("ignore")
logging.getLogger("easyocr").setLevel(logging.ERROR)


class OCRAgent:

    def __init__(self):

        self.reader = easyocr.Reader(
            ['en', 'hi'],
            gpu=False
        )

    def extract_text(self, image_path: str):

        try:

            result = self.reader.readtext(
                image_path,
                paragraph=True
            )

            text = "\n".join(
                [line[1] for line in result]
            )

            return {
                "success": True,
                "text": text,
                "language": ["en", "hi"],
                "line_count": len(result)
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }