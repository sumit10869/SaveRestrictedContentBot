#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 22439323
API_HASH = "e0e203c8be2c2c58b04d0c59fc82f507"
BOT_TOKEN = "7470597083:AAFgqPndTMvlAOvPY8eoOpPqUXGRPWOxM80"
SESSION = "AQFxJpUAso6Gc_jfCm5vNvC0yvIA8Yd8VK6Vk8bZKuZx6zQvnbsxv3jHvO32flwyN-gc_V7irBDKzM2QeB0lJwwDwykR0Vq0x76xOC7yMLSpKw562NB6oyp8JpnMiJHWkboj5GXz74FTbiYMxM26AVDEtFQsY2Q7ZSqlRO7TQXwaKCnxWhKnYmqD_6QSqX3UB_L2HlaJ6-DP6rGPGXqTVBisB7bc0JAR-HSDaZtlnzGY6xehoy60eFCvbEefJkvtOZlqApukf-3_KLjKv0aMSjfg2NdgI3w0N7qZJ55OQh7WNlb1Sy8MYstsDV-hwlJS6GdRnYRyBr9zkFI5VI9AQ4lwqRzNiQAAAAGrY-DQAA"
FORCESUB = "neetumamvol_2"
AUTH = 7170416848
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
