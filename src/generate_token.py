import jwt
import secrets

EMAILS = ['lucas@sheetgo.com', 'mauricio@sheetgo.com', 'rafael@sheetgo.com']
SECRET = 'z6Ct_d2Wy0ZcZZVUYD3beI5ZCSsFrR6-f3ZDyn_MW00'

def generate():
    """Generate the auth token."""
    email = secrets.choice(EMAILS)
    token = jwt.encode({ 'email': email }, SECRET).decode('utf-8')

    print('Bearer {}'.format(token))

if __name__ == '__main__':
    generate()
