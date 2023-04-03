from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from chatbot import askgpt, start_chat_log

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values['Body']
    chat_log = session.get('chat_log')

    if incoming_msg == '/clear':
      chat_log = start_chat_log
      answer = 'Chat log cleared.'
    else:
      answer, chat_log = askgpt(incoming_msg, chat_log)

    session['chat_log'] = chat_log

    r = MessagingResponse()
    r.message(answer)
    return str(r)