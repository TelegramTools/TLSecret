#!/usr/bin/python3
import getpass, logging, sys, time, io
try:
    import cryptg
    from cryptg import *
except:
    pass
import os
from getpass import getpass
from sys import exit
from telethon.sync import TelegramClient, events
from telethon.events import StopPropagation
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import *
from telethon.tl.types import *
from telethon.utils import *
from telethon.sessions import StringSession
import pyAesCrypt
import logging

password = "PASSWORD_FOR_SECRET_MODE_HERE"
bufferSize = 64 * 4096
api_id = YOUR_API_ID_HERE
api_hash = 'YOUR_API_HASH_HERE'
TLdevice_model = 'Desktop device'
TLsystem_version = 'Console'
TLapp_version = '- TLSecret 1.0.4'
TLlang_code = 'en'
TLsystem_lang_code = 'en'
dialogs = None
ChosenChat = None
file = None

client1 = TelegramClient("User2", api_id, api_hash, device_model=TLdevice_model, system_version=TLsystem_version, app_version=TLapp_version, lang_code=TLlang_code, system_lang_code=TLsystem_lang_code)
logging.basicConfig(filename="TLSecretHelper-log.log", level=logging.DEBUG, format='%(asctime)s %(message)s')

def StartClient1():
    global client1
    try:
        client1.connect()
        if not client1.is_user_authorized():
            client1.start(force_sms=False)
        SelfUser1 = client1.get_me()
    except:
        if not client1.is_connected():
            getpass("You are not connected to the internet or the phone was given in the incorrect format. Check your connection and press ENTER to try again: ")
        StartClient1()
    return

@client1.on(events.NewMessage(chats=ChosenChat, incoming=True))
async def EventHandler(event):
    if "WooHoo!" in event.raw_text:
        print("\nResponse received!")
        await client1.delete_messages(ChosenChat, [file.id, event.message.id], revoke=True)
        await client1.disconnect()
    return

def sprint(string, *args, **kwargs):
    #Safe Print (handle UnicodeEncodeErrors on some terminals)
    try:
        print(string, *args, **kwargs)
    except UnicodeEncodeError:
        string = string.encode('utf-8', errors='ignore')\
                       .decode('ascii', errors='ignore')
        print(string, *args, **kwargs)

def PrintChatList():
    global dialogs
    while True:
        dialogs = client1.get_dialogs(limit=None)
        i = None
        while i is None:
            print("This is the chat list. Choose your partner:\n\n")
            for i, dialog in enumerate(dialogs, start=1):
                if get_display_name(dialog.entity) == "":
                    name = "Deleted Account"
                elif isinstance(dialog.entity, InputPeerSelf):
                    name = "Chat with yourself (Saved Messages)"
                else:
                    name = get_display_name(dialog.entity)
                sprint('{}. {}'.format(i, name))

            print()
            print('> Who is your partner?')
            print('> Available commands:')
            print('  !q: Quits the dialogs window and exits.')
            print('  !l: Logs out, terminating this session.')
            print()
            i = input('Enter dialog ID or a command to continue: ')
            if i is None:
                continue
            if i == '!q':
                exit(1)
            if i == '!l':
                client1.log_out()
                exit(0)
        try:
            i = int(i if i else 0) - 1
            # Ensure it is inside the bounds, otherwise retry
            dialog_count = dialogs.total
            if not 0 <= i < dialog_count:
                i = None
        except:
            i = None
            print("That's not a valid Chat. Please, try again.")
            continue

            # Retrieve the selected user (or chat, or channel)
        return dialogs[i].entity

##ENTRY POINT OF THE CODE
client1.connect()
print("\nWelcome! This app will create an encrypted session file and will send it through Telegram to your partner for using it with other Telegram's Tools apps\n\nWARNING: Although this makes decrypting the session file or accessing your account difficult for your partner, there are some ways to get the password and decrypt it using reverse-engineering means. Use it with a trustful person and with this consideration in mine.\nYou will always have the option to revoke the session file for your partner if you see that something isn't going as expected.")
getpass("\n\n\nPress ENTER to continue")

if not client1.is_user_authorized():
    print("\nNow, it's time to login in Telegram\n")
    StartClient1()
    print("Done! Connected to Telegram!")
    client1.disconnect()
    sess = io.BytesIO(StringSession.save(client1.session).encode())
    with open("DB.aes", "wb") as fOut:
        pyAesCrypt.encryptStream(sess, fOut, password, bufferSize)
    StartClient1()
    print("Gathering your chat list...")
    ChosenChat = PrintChatList()
    dialogs.clear()
    print("\n\nSending your session file to your partner...")
    file = client1.send_file(ChosenChat, "DB.aes")
    print("\n\nWaiting for a response...")
    client1.run_until_disconnected()
    print("Your partner has been authorised in Telegram successfully!\nYou can keep this window open for revoking the session in case you think it's necessary.\nYou can close this app if you don't want to revoke it.\n\n")
    getpass("\n\nPress ENTER to revoke the session: ")
    print("\nLogging out...")
    while not client1.is_connected():
        client1.connect()
        if client1.is_connected():
            break
        else:
            print("There was a connection problem... Retrying in 2s")
            time.sleep(2)
    client1.log_out()
    print("\n\nLogged out!")
else:
    getpass("There is already a session logged in. Press ENTER to revoke it: ")
    while not client1.is_connected():
        client1.connect()
        if client1.is_connected():
            break
        else:
            print("There was a connection problem... Retrying in 2s")
            time.sleep(2)
    client1.log_out()
    try:
        os.remove("DB.aes")
    except:
        pass
    print("Done!")
getpass("Press ENTER to close TLSecret...")
