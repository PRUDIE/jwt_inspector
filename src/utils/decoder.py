import json
import base64
from typing import Dict, Optional, Any

def decode_jwt(token: str) -> Optional[Dict[str, Any]]:
    #Decode JWT token and return header and payload.
    parts = token.split('.')
    if len(parts) != 3:
        return None  # Invalid JWT
    
    try:
        # Add padding if needed
        header_b64 = parts[0] + '=' * (4 - len(parts[0]) % 4)
        payload_b64 = parts[1] + '=' * (4 - len(parts[1]) % 4)
        
        header = json.loads(base64.b64decode(header_b64))
        payload = json.loads(base64.b64decode(payload_b64))
        
        return {"header": header, "payload": payload}
    except Exception:
        return None