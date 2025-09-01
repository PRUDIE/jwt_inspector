import jwt
from typing import Optional, Dict, Any

def verify_jwt_signature(token: str, key: str, algorithm: str = "HS256") -> Optional[Dict[str, Any]]:
    #Verify JWT signature and return decoded payload.
    try:
        decoded = jwt.decode(token, key, algorithms=[algorithm])
        return decoded
    except jwt.InvalidTokenError:
        return None