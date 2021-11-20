#!/usr/bin/env python3
from pyrogram import Client
from pyrogram import filters

# ~~~~~~ CONFIG ~~~~~~~~ #
ACCOUNT = "@{your username}"
PHONE_NR = '+91{your telegram linked number}'

# https://my.telegram.org/auth?to=apps
API_ID = {Telegram app API ID} 
API_HASH = "{TELEGRAM APP API HASH}"

# CHAT ID
SOURCE_CHAT = {CHAT ID FROM WHERE WANNA COPY} 
TARGET_CHAT = {CHAT ID OF THE GROUP WHERE U WANNA PASTE THE MESSAGES}
# ~~~~~~~~~~~~~~~~~~~~~~ #

app = Client(
    ACCOUNT,
    phone_number=PHONE_NR,
    api_id=API_ID,
    api_hash=API_HASH
)

filters.chat(SOURCE_CHAT)
@app.on_message(filters.chat(SOURCE_CHAT))
def my_handler(client, message):
    message.copy(  # copy() so there's no "forwarded from" header
        chat_id=TARGET_CHAT,  # the channel you want to post to
        caption="Copied from XYZ"  # Caption
    )
# UNCOMMENT THIS CODE TO FIND OUT CHAT ID OF THE PRIVATE GROUPS 
#@app.on_message()
#def my_handler(client, message):
#    print(message)

app.run()
