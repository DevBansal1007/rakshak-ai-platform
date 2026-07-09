from dataclasses import dataclass


@dataclass
class Settings:
    APP_NAME = "Rakshak AI"
    VERSION = "1.0.0"
    DESCRIPTION = (
        "AI-Powered Fraud Early Warning and Intelligence Platform"
    )


settings = Settings()