from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request

account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def handle_incoming_message():
    message = request.form.get('Body', '').lower()
    response = MessagingResponse()
    response.message('Thanks for your message! We will get back to you as soon as possible.')
    return response, 200