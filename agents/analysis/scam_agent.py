class ScamAgent:

    def __init__(self):
        """
        Initialize Scam Agent.
        """
        pass

    def analyze_scam(self, text: str, entities: dict):
        """
        Analyze scam probability from text and extracted entities.

        Args:
            text (str): Input text.
            entities (dict): Output from EntityAgent.

        Returns:
            dict
        """

        score = 0  # later here will change with prediction = distilbert.predict(text) for better accuracy
        reasons = []
        category = "Unknown"

        text_lower = text.lower()

        # ---------- Rule 1 ----------
        urgent_keywords = [
            "urgent",
            "immediately",
            "within 24 hours",
            "last warning",
            "act now",
            "expire",
            "expired",
            "final notice",
            "final warning",
            "limited time",
            "verify immediately",
            "respond now",
            "suspended",
            "blocked",
            "freeze",
            "deactivated"
        ]

        if any(word in text_lower for word in urgent_keywords):
            score += 20
            reasons.append("Urgency detected")

        # ---------- Rule 2 ----------
        government_keywords = [
            "cbi",
            "police",
            "cyber crime",
            "cybercrime",
            "cyber cell",
            "crime branch",
            "supreme court",
            "high court",
            "income tax",
            "aadhaar",
            "aadhar",
            "pan",
            "passport",
            "rbi",
            "bank manager",
            "customs",
            "digital arrest",
            "legal notice",
            "fir",
            "warrant"
        ]

        if any(word in text_lower for word in government_keywords):
            score += 25
            reasons.append("Government impersonation")

        # ---------- Rule 3 : OTP / Verification ----------
        otp_keywords = [
            "otp",
            "verification code",
            "share otp",
            "verify otp",
            "authentication",
            "verification",
            "kyc",
            "re-kyc",
            "account verification",
            "confirm identity"
        ]

        if any(word in text_lower for word in otp_keywords):
            score += 25
            reasons.append("OTP request")

        # ---------- Rule 4 ----------
        payment_keywords = [
            "upi",
            "pay now",
            "payment",
            "send money",
            "transfer",
            "bank transfer",
            "refund",
            "cashback",
            "reward",
            "gift",
            "prize",
            "lottery",
            "claim reward",
            "processing fee",
            "security deposit",
            "qr code",
            "collect request"
        ]

        if any(word in text_lower for word in payment_keywords):
            score += 20
            reasons.append("Money transfer request")

        # ---------- Rule 5 ----------
        if entities["upi_ids"]:
            score += 5

        if entities["phones"]:
            score += 5
        if entities["urls"]:
            score += 10
            reasons.append("URL detected")

            
        # ---------- Rule 6 : Remote Access ----------

        remote_keywords = [
            "anydesk",
            "teamviewer",
            "quicksupport",
            "remote access",
            "screen share",
            "install app",
            "download apk",
            "apk file"
        ]

        if any(word in text_lower for word in remote_keywords):
            score += 25
            reasons.append("Remote access request")


        # ---------- Rule 7 : Fear / Threat ----------

        threat_keywords = [
            "arrest",
            "illegal",
            "criminal",
            "case registered",
            "court",
            "jail",
            "fine",
            "penalty",
            "account blocked",
            "account suspended",
            "account frozen"
        ]

        if any(word in text_lower for word in threat_keywords):
            score += 20
            reasons.append("Fear or threat tactics")
        

        if score >= 70:
            category = "High Risk Scam"

        elif score >= 40:
            category = "Suspicious"

        else:
            category = "Low Risk"

        return {
            "is_scam": score >= 40,
            "risk_score": min(score, 100),
            "category": category,
            "reasons": reasons
        }