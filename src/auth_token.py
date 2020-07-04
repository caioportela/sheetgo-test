import jwt
import secrets

from src.app import EMAILS, SECRET

def generate():
    """Generate the auth token."""
    email = secrets.choice(EMAILS)
    token = jwt.encode({ 'email': email }, SECRET, algorithm='HS256').decode('utf-8')

    token = 'Bearer {}'.format(token)

    print(token)

    # Return the token for test purposes
    return token

if __name__ == '__main__':
    generate()
