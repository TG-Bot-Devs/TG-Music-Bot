from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        text=f"""**Hey, I'm {bn} ðµ

I can play music in your group's voice call. Developed by [Jason](https://t.me/ImJanindu).

Add me And @MusicPlugin to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("â Add To Your Group â", url="https://t.me/JEGroupMusicPlayerBot?startgroup=true")
            ],[
            InlineKeyboardButton("ð¬ Group", url="https://t.me/"),
            InlineKeyboardButton("Channel ð£", url="https://t.me/GROUPMUSICNEWS")
            ],[
            InlineKeyboardButton("ð Commands", url="https://t.me/InfinityBOTs_Support"),
            InlineKeyboardButton("Aboutð¨ð»âð", url="https://t.me/Infinity_BOTs")
            ],[
            InlineKeyboardButton("ð Website ð", url="https://t.ME/")
            ]]
        ),
        disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online â**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Group", url="https://t.me/"),
                    InlineKeyboardButton("Channel", url="httPS://T.ME/")
                ]                
            ]
        )

@Client.on_message(filters.new_chat_members & filters.outgoing & filters.group)
async def new_chat(client, message)
    await client.reply_text(
         text=f"""**â¤ï¸ Thanks for adding me to the group!**

**Promote me as administrator of the group,** otherwise I will not be able to work properly.
            """,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ðCommands", url="https://t.me/"),
                    InlineKeyboardButton("Channelð£", url="httPS://T.ME/")
                ]                
            ]
        )
