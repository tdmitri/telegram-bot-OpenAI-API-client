import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up the OpenAI API client
openai.api_key = secrets["api_key"]

# Set up the Telegram bot
bot = telegram.Bot(token=secrets["bot_token"])
updater = Updater(bot.token)

# Define a function that will be called whenever the bot receives a message
def handle_message(bot, update):
    # Get the message text and send it to the Assistant API
    text = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=1024,
        n = 1,
        temperature=0.5,
    )

    # Get the response text and send it back to the user
    response_text = response["choices"][0]["text"]
    bot.send_message(chat_id=update.message.chat_id, text=response_text)

# Set up the bot to call the `handle_message` function whenever it receives a message
message_handler = MessageHandler(Filters.text, handle_message)
updater.dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
