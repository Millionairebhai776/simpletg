import pyrogram
from pyrogram import Client

api_id = 16393106
api_hash = "061fbf1aff7eecf2edb8434ddbab7a7d"
bot_token = "5900132667:AAHfAQfu6bGilLr8y2MvwwcH_sEBVPuq8jo"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message()
def handle_messages(client, message):
    if message.text == "/start":
        message.reply("Hello! I am a bot. Use the command /help to see a list of available commands.")
    elif message.text == "/help":
        message.reply("Here is a list of available commands:\n/start - start the bot\n/help - display this message")

app.run()
