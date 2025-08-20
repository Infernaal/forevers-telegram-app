import secrets
import string

def generate_strong_password(length: int = 18) -> str:
    """
    Generate a strong password with letters, digits, and special characters.
    Default length is 14 characters.
    """
    base_letters = string.ascii_letters
    digits = string.digits
    special = '!@#$%'
    # Количество спецсимволов: 2 или 3
    num_special = secrets.choice([2, 3])
    num_digits = max(2, length // 5)
    num_letters = length - num_special - num_digits
    # Гарантируем хотя бы одну заглавную, одну строчную, одну цифру, один спецсимвол
    password_chars = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(digits),
        secrets.choice(special)
    ]
    # Остальные буквы
    password_chars += [secrets.choice(base_letters) for _ in range(num_letters - 2)]
    # Остальные цифры
    password_chars += [secrets.choice(digits) for _ in range(num_digits - 1)]
    # Остальные спецсимволы
    password_chars += [secrets.choice(special) for _ in range(num_special - 1)]
    # Перемешиваем
    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)
