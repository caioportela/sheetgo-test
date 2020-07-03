import io
import jwt
from flask import Flask, jsonify, render_template, request, send_file
from flask_httpauth import HTTPTokenAuth
from openpyxl import load_workbook
from PIL import Image

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

# Secret key to decode token
SECRET = 'z6Ct_d2Wy0ZcZZVUYD3beI5ZCSsFrR6-f3ZDyn_MW00'

# Accepted emails for authorization
EMAILS = ['lucas@sheetgo.com', 'mauricio@sheetgo.com', 'rafael@sheetgo.com']

@auth.verify_token
def verify_token(token):
    """Decode and verify the auth token."""
    if not token: return False

    token_decoded = jwt.decode(token, SECRET)
    email = token_decoded['email']

    return email in EMAILS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/excel/info', methods=['POST'])
@auth.login_required
def excel_info():
    """Return the tabs from the excel file, ordered alphabetically."""
    sheet = request.files['file']
    sheet = load_workbook(sheet, read_only=True)

    sheetnames = sorted(sheet.sheetnames)
    return jsonify(sheetnames)

@app.route('/image/convert', methods=['POST'])
@auth.login_required
def image_convert():
    """Convert the format of an image."""
    format = request.form.get('format')
    file = request.files['file']

    file_object = io.BytesIO()

    with Image.open(file) as image:
        image.save(file_object, format)
        file_object.seek(0)

        return send_file(file_object, mimetype='image/{}'.format(format))

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
