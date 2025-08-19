import secrets
import string

def generate_strong_password(length: int = 14) -> str:
    """
    Generate a strong password with letters, digits, and special characters.
    Default length is 14 characters.
    """
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        # Ensure password contains at least one letter, digit, and special char
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)):
            return password
