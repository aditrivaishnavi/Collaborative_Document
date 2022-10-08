from flask import Flask, render_template, request, jsonify
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant

app = Flask(__name__)
fake = Faker()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/token')
def generate_token():
    TWILIO_ACCOUNT_SID = 'ACa7ed088d745d453bdc2fa2c111e76b4a'
    TWILIO_SYNC_SERVICE_SID = 'IS24c5a345ef6ce0168c912773ff35d976'
    TWILIO_API_KEY = 'SKe36ef6f8b1da876f5506d49efd032916'
    TWILIO_API_SECRET = 'DrPHvGvOd7MeRb2HadFXaUdTS1406U14'

    username = request.args.get('username', fake.user_name())

    token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity = username)

    sync_grant_access - SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity = username, token = token.to_jwt().decode())

@app.route('/', methods = ['POST'])
def download_text():
    text_from_notepad = request.form['text']

    with open('workfile.txt', 'w') as f:
        f.write(text_from_notepad)
    
    path_to_store_txt = "workfile.txt"

    return send_file(path_to_store_txt, as_attachment = True)

if __name__ == "__main__":
    app.run()