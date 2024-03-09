from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ➕"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["• ⚠️ ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs ⚠️ •"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["• 🌙 ᴏᴡɴᴇʀ 🌙•"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["• 🌙 sᴜᴘᴘᴏʀᴛ 🌙•"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["• 🌙 ᴜᴘᴅᴀᴛᴇs 🌙 •"], url=config.SUPPORT_CHANNEL),
        ],
    ]
    return buttons
