from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from YTMUSIC import app
from config import BOT_USERNAME
from YTMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ˹𝐓𝐄𝐀𝐌-𝐕𝐀𝐌𝐏𝐈𝐑𝐄❤️‍🔥˼ ʙᴏᴛ ✪
 
 ❍ • ʙsᴅᴋ ʀᴇᴘᴏ ʟᴇɢᴀ ◉‿◉ •
 
 ❍ • ᴘᴇʜʟᴇ ᴠᴀᴍᴘɪʀᴇ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟ •
 
 ❍ • ᴄʜᴜᴘ ᴄʜᴜᴘ ʙᴏᴛ ʟᴇᴋᴇ ɴɪᴋᴀʟ •
 
 ❍ • ʀᴇᴘᴏs ᴛᴏ ɴᴀʜɪ ᴍɪʟᴇɢᴀ ʙᴇᴛᴀ ⊂◉‿◉ •
 
 ❍ • ᴀɢʀ ᴄʜᴀʜɪʏᴇ ᴛᴏ ᴠᴀᴍᴘɪʀᴇ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟɴᴀ ᴘᴀᴅᴇɢᴀ •
 
 ❍ • ᴠᴀᴍᴘɪʀᴇ ᴘᴀᴘᴀ • **"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("•ᴀᴅᴅ ᴍᴇ•", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("•sᴜᴘᴘᴏʀᴛ•", url="https://t.me/llDPZ_EDITIXll"),
          InlineKeyboardButton("•ᴏᴡɴᴇʀ•", url="https://t.me/llDPZ_EDITIXll"),
          ],
               [
                InlineKeyboardButton("•ᴜᴘᴅᴀᴛᴇs•", url="https://t.me/llDPZ_EDITIXll"),

],
[
              InlineKeyboardButton("•˹𝐓𝐄𝐀𝐌-𝐕𝐀𝐌𝐏𝐈𝐑𝐄❤️‍🔥˼•", url=f"https://t.me/llDPZ_EDITIXll"),
              InlineKeyboardButton("︎•˹𝐓𝐄𝐀𝐌-𝐕𝐀𝐌𝐏𝐈𝐑𝐄❤️‍🔥˼•", url=f"https://t.me/llDPZ_EDITIXll"),
              ],
              [
              InlineKeyboardButton("•˹𝐓𝐄𝐀𝐌-𝐕𝐀𝐌𝐏𝐈𝐑𝐄❤️‍🔥˼•", url=f"https://t.me/llDPZ_EDITIXll"),
InlineKeyboardButton("•˹𝐓𝐄𝐀𝐌-𝐕𝐀𝐌𝐏𝐈𝐑𝐄❤️‍🔥˼•", url=f"https://t.me/llDPZ_EDITIXll"),
],
[
InlineKeyboardButton("•˹𝐓𝐄𝐀𝐌-𝐕𝐀𝐌𝐏𝐈𝐑𝐄❤️‍🔥˼ᴄ•", url=f"https://t.me/llDPZ_EDITIXll"),
InlineKeyboardButton("•˹𝐓𝐄𝐀𝐌-𝐕𝐀𝐌𝐏𝐈𝐑𝐄❤️‍🔥˼•", url=f"https://t.me/llDPZ_EDITIXll"),
],
[
              InlineKeyboardButton("•˹𝐓𝐄𝐀𝐌-𝐕𝐀𝐌𝐏𝐈𝐑𝐄❤️‍🔥˼•", url=f"https://t.me/llDPZ_EDITIXll"),
              InlineKeyboardButton("•˹𝐓𝐄𝐀𝐌-𝐕𝐀𝐌𝐏𝐈𝐑𝐄❤️‍🔥˼•︎", url=f"https://t.me/llDPZ_EDITIXll"),
              ],
              [
              InlineKeyboardButton("•˹𝐓𝐄𝐀𝐌-𝐕𝐀𝐌𝐏𝐈𝐑𝐄❤️‍🔥˼•", url=f"https://t.me/llDPZ_EDITIXll"),
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/ifgxkd.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/BABY-MUSIC/BABYTUNE/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[•ʙᴏᴛ-ᴏᴡɴᴇʀ•](https://t.me/lllVAMPIRE_KINll) | [•ᴜᴘᴅᴀᴛᴇs•](https://t.me/llDPZ_EDITIXll)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
