from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'HOME'

@app.route('/excel/info', methods=['GET', 'POST'])
def excel_info():
    sheet = request.files['file']
    
    return 'DONE'

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
