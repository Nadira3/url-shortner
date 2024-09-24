
import random
import string


def generate_short_code():
    """
    generate randomly unique short code
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=7))