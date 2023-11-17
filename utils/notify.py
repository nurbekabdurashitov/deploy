from loader import dp, bot 
from aiogram import types
from data.config import ADMINS
      
async def start_up():
      for i in ADMINS:
            await bot.send_message(chat_id=i, text=f"Assalomu Alaykum\n Bot muammosiz ishga tushdi")

async def shut_up():
      for i in ADMINS:
            await bot.send_message(chat_id=i, text=f"Bot ishlamayapti !!!")

      