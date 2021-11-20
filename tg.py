#!/usr/bin/env python3
from pyrogram import Client
from pyrogram import filters

# ~~~~~~ CONFIG ~~~~~~~~ #
ACCOUNT = "@TestingGuy"
PHONE_NR = '+918987772892'

# https://my.telegram.org/auth?to=apps
API_ID = 10361737 
API_HASH = "0cab51c2877113d5874c7bbaaf3252f6"

# CHAT ID
SOURCE_CHAT = -1001402869192 
TARGET_CHAT = -795979744
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

#@app.on_message()
#def my_handler(client, message):
#    print(message)

#def getAllChatIDs():
#    for x in app.get_dialogs():
#        print (x.chat.type, x.chat.title, x.chat.id)

app.run()
