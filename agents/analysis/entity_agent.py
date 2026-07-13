import re

from utils.upi_handles import VALID_UPI_HANDLES


class EntityAgent:

    def __init__(self):
        pass

    def extract_entities(self, text: str):
        """
        Extract phone numbers, emails, URLs and UPI IDs from text.
        """

        phone_pattern = r"\b(?:\+91[-\s]?)?[6-9]\d{9}\b"

        email_pattern = (
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
        )

        url_pattern = (
            r"https?://[^\s]+|www\.[^\s]+"
        )

        # Extract potential UPI IDs
        upi_pattern = (
            r"\b[a-zA-Z0-9._-]{2,}@[a-zA-Z0-9._-]{2,}\b"
        )

        phones = sorted(set(re.findall(phone_pattern, text)))

        emails = sorted(
            set(email.lower() for email in re.findall(email_pattern, text))
        )

        urls = sorted(
            set(url.rstrip(".,!?") for url in re.findall(url_pattern, text))
        )

        upi_candidates = set(re.findall(upi_pattern, text))

        upi_ids = sorted(
            upi.lower()
            for upi in upi_candidates
            if upi.split("@", 1)[1].lower() in VALID_UPI_HANDLES
        )

        return {
            "phones": phones,
            "emails": emails,
            "urls": urls,
            "upi_ids": upi_ids,
        }