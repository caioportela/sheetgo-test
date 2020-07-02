import io
import jwt
from flask import Flask, jsonify, render_template, request, send_file
from openpyxl import load_workbook
from PIL import Image

app = Flask(__name__)

EMAILS = ["lucas@sheetgo.com", "mauricio@sheetgo.com", "rafael@sheetgo.com"]
SECRET = 'z6Ct_d2Wy0ZcZZVUYD3beI5ZCSsFrR6-f3ZDyn_MW00'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/excel/info', methods=['POST'])
def excel_info():
    sheet = request.files['file']
    sheet = load_workbook(sheet, read_only=True)

    sheetnames = sorted(sheet.sheetnames)
    return jsonify(sheetnames)

@app.route('/image/convert', methods=['POST', 'GET'])
def image_convert():
    format = request.form.get('format')
    file = request.files['file']

    file_object = io.BytesIO()

    with Image.open(file) as image:
        image.save(file_object, format)
        file_object.seek(0)

        return send_file(file_object, mimetype='image/{}'.format(format))

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
