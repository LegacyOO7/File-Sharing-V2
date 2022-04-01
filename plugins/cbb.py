#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='t.me/MysterySD'>꧁❏รเlєภt ๔є๓๏ภ❏꧂</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Channel : @FuZionX\n○ Support Group : @FuZionXGroup</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("↩ 𝗕𝗮𝗰𝗸", callback_data = "back"),
                        InlineKeyboardButton("🔐 𝗖𝗹𝗼𝘀𝗲 🔐", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "help":
        await query.message.edit_text(
            text = f"<b> Ignore This </b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡ 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 𝙇𝙞𝙣𝙠𝙨 ⚡", url = "https://t.me/Series_omega")
                    ],
                    [
                        InlineKeyboardButton("↩ 𝗕𝗮𝗰𝗸", callback_data = "back"),
                        InlineKeyboardButton("🔐 𝗖𝗹𝗼𝘀𝗲 🔐", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "back":
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚡ 𝗛𝗲𝗹𝗽 ⚡", callback_data = "help")
                ],
                [
                    InlineKeyboardButton("⚡ 𝗔𝗯𝗼𝘂𝘁 𝗠𝗲 ⚡", callback_data = "about"),
                    InlineKeyboardButton("⚡ 𝗖𝗹𝗼𝘀𝗲 ⚡", callback_data = "close")
                ],
                [
                    InlineKeyboardButton("⚡ 𝙁𝙪𝙕𝙞𝙤𝙣𝙓 ⚡", url = "https://t.me/Series_omega"),
                    InlineKeyboardButton("⚡ 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝙂𝙧𝙤𝙪𝙥 ⚡", url = "https://t.me/MallutorentsGroup")
                ]
            ]
        )
        await query.message.edit_text(
            text = START_MSG.format(
                first = query.message.from_user.first_name,
                last = query.message.from_user.last_name,
                username = None if not query.message.from_user.username else '@' + query.message.from_user.username,
                mention = query.message.from_user.mention,
                id = query.message.from_user.id
            ),
            reply_markup = reply_markup,
            disable_web_page_preview = True
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
