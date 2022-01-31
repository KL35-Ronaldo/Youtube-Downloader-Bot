from config import SESSION, API_ID, API_HASH, BOT_TOKEN, WORKERS, PLUGINS, SLEEP_THRESHOLD
from pyrogram import Client

Bot = Client(
    session_name=SESSION,
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=PLUGINS,
    workers=WORKERS,
    sleep_threshold=SLEEP_THRESHOLD
)

Bot.run()
