import random
import string

def generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):

    letters = string.ascii_letters

    numbers = string.digits

    symbols = string.punctuation

    all_characters = letters + numbers + symbols

    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

