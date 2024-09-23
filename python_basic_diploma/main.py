import os
from dotenv import load_dotenv
from TelebotApi import startBot

load_dotenv()

token = os.getenv("Telebot_Token")

startBot.start_new_bot(token)
