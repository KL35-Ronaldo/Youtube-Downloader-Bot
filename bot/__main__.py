import config
from pyrogram import Client

DOWNLOAD_LOCATION = "./Downloads"
BOT_TOKEN = config.BOT_TOKEN
API_ID = config.API_ID
API_HASH = config.API_HASH


Bot = Client(
    session_name="YouTube-DL-Bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins={'root': 'plugins'},
    workers=100
)

Bot.run()
