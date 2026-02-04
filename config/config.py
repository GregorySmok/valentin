import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

MYSQLHOST = str(os.getenv("HOST"))

MYSQLUSER = str(os.getenv("USER"))

MYSQLPASSWORD = str(os.getenv("PASSWORD"))

MYSQLDB = str(os.getenv("DB"))

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / 'logs'
ITEMS_PER_PAGE = 3

admins = [563385265]

CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
GROUP_ID = int(os.getenv("GROUP_ID"))