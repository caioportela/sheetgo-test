from flask import Flask, jsonify, request
from openpyxl import load_workbook

app = Flask(__name__)

@app.route('/')
def index():
    return 'HOME'

@app.route('/excel/info', methods=['GET', 'POST'])
def excel_info():
    sheet = request.files['file']
    sheet = load_workbook(sheet, read_only=True)

    sheetnames = sorted(sheet.sheetnames)
    return jsonify(sheetnames)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
