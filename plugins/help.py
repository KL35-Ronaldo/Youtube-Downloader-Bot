from pyrogram import Client, Filters

@Client.on_message(Filters.command(["help"]))
async def send_help(client, message):
    helptxt = f"Just Send Me A **YouTube Video URL**"
    await message.reply_text(helptxt)
