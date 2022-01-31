from pyrogram import Client, Filters

@Client.on_message(Filters.command(["start"]))
async def send_start(client, message):
    helptxt = f"Just Send Me A **YouTube Video URL**"
    await message.reply_text(helptxt)
