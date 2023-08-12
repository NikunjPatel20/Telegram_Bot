import requests
import os
import signal

from flask import Flask
from flask import request
from flask import Response
from keys import *  # Import API tokens
import openai

# Set up OpenAI API key
openai.api_key = gpt_token

# Telegram Bot token
TOKEN = bot_token

app = Flask(__name__)

# Function to parse incoming Telegram message
def parse_message(message):
    print("message-->", message)
    chat_id = message['message']['chat']['id']  # Extract chat ID from the incoming message
    txt = message['message']['text']  # Extract text content from the incoming message
    print("Text :", txt)
    return chat_id, txt

# Function to send a message using the Telegram API
def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    headers = {'Content-Type': 'application/json'}  # Define headers
    
    # Send POST request to the Telegram API
    response = requests.post(url, json=payload, headers=headers)
    return response

# Route to handle favicon requests
@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return empty response

# Main route to process incoming messages and generate responses
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()  # Get the incoming message data
        
        chat_id, txt = parse_message(msg)  # Parse the message
        
        # Use GPT-3 to generate a response
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": txt}
            ]
        )
        response = completion['choices'][0]['message']['content']
        print("ChatGPT response: ", response)
        
        # Send the generated response back to the Telegram chat
        tel_send_message(chat_id, response)
        return Response('ok', status=200)  # Return success response
    else:
        return "<h1>Welcome!</h1>"  # Display welcome message

# Entry point of the application
if __name__ == '__main__':
    app.run(port=5000)  # Run the Flask app on port 5000
