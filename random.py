import random
import string

def generate_random_password(length=12):
    # Define character sets
    letters = string.ascii_letters  # a-z and A-Z
    digits = string.digits  # 0-9
    special_chars = string.punctuation  # Special characters like !, @, #, etc.
    
    # Combine all the character sets
    all_chars = letters + digits + special_chars
    
    # Randomly choose characters from the combined set
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

