import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

pr0fess0r_99=Client(
    "𝗕𝗼𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱 [ 𝗥𝗜𝗖𝗞 𝗚𝗥𝗜𝗠𝗘𝗦 ]",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

CHAT_ID=int(os.environ.get("CHAT_ID", None))
TEXT=os.environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour Auto Approved")
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me() 
    button=[[
      InlineKeyboardButton("😶‍🌫️𝗨𝗽𝗱𝗮𝘁𝗲𝘀", url="https://t.me/CPTN5DW"),
      InlineKeyboardButton("🧑‍💻𝗕𝗼𝘁 𝘿𝙚𝙫𝙤𝙡𝙤𝙥𝙚𝙧", url="https://t.me/J1_CHANG_WOOK")
      ],[
      InlineKeyboardButton("𝙆𝙞𝙢 𝙎𝙚𝙟𝙚𝙤𝙣𝙜 𝙈𝙤𝙫𝙞𝙚𝙨 & 𝙎𝙚𝙧𝙞𝙚𝙨 [ 𝘽𝙤𝙩 𝙐𝙥𝙙𝙖𝙩𝙚𝙨 ]", url=f"https://t.me/+m-34h62uJ8I1M2Jl")
      ]]
    await message.reply_text(text="**𝙃𝙀𝙇𝙇𝙊 🫵🏻\n𝗜𝗮𝗺 𝗔 𝗦𝗶𝗺𝗽𝗹𝗲 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗔𝘂𝘁𝗼 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗔𝗰𝗰𝗲𝗽𝘁 𝗕𝗼𝘁 𝗔𝗱𝗱 𝗬𝗼𝘂𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗼𝗿 𝗚𝗿𝗼𝘂𝗽 😉.\n**", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@pr0fess0r_99.on_chat_join_request(filters.chat(CHAT_ID))
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} 𝙹𝙾𝙸𝙽𝙴𝙳 ⚡") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))       

print("𝗕𝗼𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱 [ 𝗥𝗜𝗖𝗞 𝗚𝗥𝗜𝗠𝗘𝗦 ]")
pr0fess0r_99.run()
