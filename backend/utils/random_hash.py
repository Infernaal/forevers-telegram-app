import secrets
import string


def random_hash(length: int = 12) -> str:
    """
    Generate a random hash string of specified length.
    Similar to PHP randomHash function.
    
    Args:
        length: Length of the hash to generate
        
    Returns:
        Random hash string containing alphanumeric characters
    """
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))
