from pyrogram import Client, filters
from gtts import gTTS
import config
from io import BytesIO
from pyrogram.types import InputMediaAudio

bot = Client(
    'my_bot', 
    api_id= config.API_ID, 
    api_hash= config.API_HASH, 
    bot_token= config.BOT_TOKEN
    )

@bot.on_message(filters.command('start'))
def start(client, message):
    message.reply_text('Hello, I am a bot')


@bot.on_message(filters.audio)
def download_audio(client, message):
    try:
        # Download the audio file
        print(message.audio.file_id)
        file_path = client.download_media(message.audio.file_id , file_name='audio.ogg')
        
        # Print the path of the downloaded file
        print("Downloaded audio file: ", file_path)
        
        # TODO: Process the audio file
        
    except Exception as e:
        print("Error downloading audio file: ", e)

bot.run()
