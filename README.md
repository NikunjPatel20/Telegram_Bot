# Telegram Chatbot with OpenAI's GPT-3

This project demonstrates how to create a Telegram chatbot that interacts with OpenAI's GPT-3 language model. The chatbot takes user messages from a Telegram chat and uses GPT-3 to generate responses.

## Setup

1. Clone this repository to your local machine.
2. Install the required packages using `pip install -r requirements.txt`.
3. Obtain API tokens:
   - Create a Telegram bot by talking to the [BotFather](https://core.telegram.org/bots#botfather) on Telegram and get the bot token.
   - Obtain an OpenAI API key for the GPT-3 model.
4. Configure the API tokens in a file named `keys.py`:

```python
# keys.py

bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
gpt_token = "YOUR_OPENAI_GPT3_API_KEY"

Credits
This project was developed by Nikunj Patel.

