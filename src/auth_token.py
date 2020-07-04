import jwt
import secrets

# Secret key to decode token
SECRET = 'z6Ct_d2Wy0ZcZZVUYD3beI5ZCSsFrR6-f3ZDyn_MW00'

# Accepted emails for authorization
EMAILS = ['lucas@sheetgo.com', 'mauricio@sheetgo.com', 'rafael@sheetgo.com']

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
