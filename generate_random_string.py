import random
import string

def generate_random_string(length=10):
    chars = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    return ''.join(random.choice(chars) for _ in range(length))
