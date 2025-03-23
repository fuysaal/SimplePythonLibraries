import secrets
import string


# Function to generate a secure password
def gen_password(n):
    # Define characters: uppercase, lowercase, digits, and punctuation
    chars = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password meets security requirements
    password = ''.join(secrets.choice(chars) for i in range(n))

    # Optionally, you can check that the password contains at least one of each required character type:
    if not any(c.islower() for c in password):
        password += secrets.choice(string.ascii_lowercase)
    if not any(c.isupper() for c in password):
        password += secrets.choice(string.ascii_uppercase)
    if not any(c.isdigit() for c in password):
        password += secrets.choice(string.digits)
    if not any(c in string.punctuation for c in password):
        password += secrets.choice(string.punctuation)

    # Ensure the password is the correct length after adjustments
    return password[:n]


# Example usage
pwd = gen_password(15)
print(pwd)
