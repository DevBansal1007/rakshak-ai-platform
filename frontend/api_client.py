import requests
import logging
from typing import Dict, Any, Optional

# Set up logging to help trace network errors during live hackathon demonstrations
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RakshakAPIClient:
    """
    Client wrapper for the Rakshak AI FastAPI Backend.
    This class handles all outgoing HTTP requests, JSON serialization, and error handling
    so the Streamlit UI never crashes if the backend server drops connection.
    """
    
    def __init__(self, base_url: str = "http://127.0.0.1:8000"):
        """
        Initializes the connection. 
        When deploying to AWS, update this base_url to your live App Runner endpoint.
        """
        self.base_url = base_url
        self.headers = {
            "Accept": "application/json"
        }

    def analyze_text_log(self, text_content: str) -> Dict[str, Any]:
        """
        CITIZEN PORTAL: Sends raw text (WhatsApp messages, SMS) to the LLM agent pipeline.
        
        Endpoint Expected: POST /api/v1/analyze/text
        Payload: {"text": "suspicious message string"}
        """
        endpoint = f"{self.base_url}/api/v1/analyze/text"
        
        try:
            # We use a 10-second timeout. If the LLM takes too long, it aborts rather than freezing the UI.
            response = requests.post(
                endpoint, 
                json={"text": text_content}, 
                headers=self.headers,
                timeout=10
            )
            # Raise an HTTPError if the HTTP request returned an unsuccessful status code (e.g., 500 or 404)
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.Timeout:
            logger.error("Text analysis request timed out.")
            return {"error": "Connection timed out. The threat intelligence engine is currently under heavy load."}
        except requests.exceptions.RequestException as e:
            logger.error(f"Text analysis failed: {e}")
            return {"error": f"Failed to connect to Rakshak servers. Detail: {str(e)}"}

    def analyze_document(self, file_bytes: bytes, file_name: str) -> Dict[str, Any]:
        """
        CITIZEN PORTAL: Uploads images or PDFs (Fake warrants, UPI screenshots) to the OCR agent.
        
        Endpoint Expected: POST /api/v1/analyze/file
        Payload: multipart/form-data containing the file buffer
        """
        endpoint = f"{self.base_url}/api/v1/analyze/file"
        
        # Format the binary data for a standard multipart/form-data upload
        # Tuple format: (filename, file_object, content_type)
        files = {
            "file": (file_name, file_bytes, "application/octet-stream")
        }
        
        try:
            # Vision models and OCR take longer, so the timeout is extended to 20 seconds
            response = requests.post(
                endpoint, 
                files=files, 
                timeout=20
            )
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Document analysis failed: {e}")
            return {"error": f"Vision pipeline interrupted. Detail: {str(e)}"}

    def generate_ncrp_report(self, case_id: str) -> Optional[bytes]:
        """
        CITIZEN PORTAL: Requests the generated PDF document for official reporting.
        
        Endpoint Expected: GET /api/v1/report/{case_id}/download
        Returns: Raw PDF byte stream (which Streamlit can directly serve as a download button)
        """
        endpoint = f"{self.base_url}/api/v1/report/{case_id}/download"
        
        try:
            response = requests.get(endpoint, timeout=10)
            response.raise_for_status()
            return response.content # Return raw bytes instead of JSON
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch NCRP PDF: {e}")
            return None

    def fetch_command_intelligence(self, state: str, district: str, time_window: str) -> Dict[str, Any]:
        """
        ENFORCEMENT PORTAL: Fetches macro-level geospatial and network intelligence for the LE dashboard.
        
        Endpoint Expected: GET /api/v1/intelligence/dashboard
        Query Params: ?state=X&district=Y&window=Z
        """
        endpoint = f"{self.base_url}/api/v1/intelligence/dashboard"
        
        params = {
            "state": state,
            "district": district,
            "window": time_window
        }
        
        try:
            response = requests.get(
                endpoint, 
                params=params, 
                headers=self.headers,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Command center sync failed: {e}")
            return {"error": "Unable to synchronize live intelligence feeds."}