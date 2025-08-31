import jwt
from typing import Dict, Any

def has_none_algorithm(decoded_jwt: Dict[str, Any]) -> bool:
    #Check if JWT uses 'none' algorithm.
    return decoded_jwt.get("header", {}).get("alg") == "none"

def validate_jwt_structure(token: str) -> bool:
    #Validate basic JWT structure.
    parts = token.split('.')
    return len(parts) == 3