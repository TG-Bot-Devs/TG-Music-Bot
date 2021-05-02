from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        text=f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [Jason](https://t.me/ImJanindu).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("➕ Add To Your Group ➕", url="https://t.me/JEGroupMusicPlayerBot?startgroup=true")
            ],[
            InlineKeyboardButton("💬 Group", url="https://t.me/"),
            InlineKeyboardButton("Channel 📣", url="https://t.me/GROUPMUSICNEWS")
            ],[
            InlineKeyboardButton("🎛 Commands", url="https://t.me/InfinityBOTs_Support"),
            InlineKeyboardButton("About👨🏻‍🎓", url="https://t.me/Infinity_BOTs")
            ],[
            InlineKeyboardButton("🌐 Website 🌐", url="https://t.ME/")
            ]]
        ),
        disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Group", url="https://t.me/"),
                    InlineKeyboardButton("Channel", url="httPS://T.ME/")
                ]                
            ]
        )


