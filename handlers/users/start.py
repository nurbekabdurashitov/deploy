from aiogram.filters import CommandStart , Command
from loader import dp,bot 
from aiogram import types, F
from utils.set_botcommands import commands
from keyboards.defaults.buttons import button
import wikipedia
wikipedia.set_lang('uz')
@dp.message(CommandStart())
async def start_bot(message:types.Message):
      await message.answer(f"Ism Familya : {message.from_user.full_name}\n User ID : {message.from_user.id}", reply_markup=button.as_markup(resize_keyboard = True) )

@dp.message(F.contact)
async def get(message:types.Message):
      contact_id = message.contact.user_id
      full_name = message.contact.first_name+ ' '+message.contact.last_name
      try:
            await message.answer(f"Ism Familyasi: {full_name}\nUser id : <code> {contact_id}</code>")
      except:
            await message.answer("Bu foydalanuvchi Telegramdan ro`yxatdan O`tmagan")


@dp.message(F.chat_shared)
async  def chat_id(message:types.Message):
      chat = message.chat_shared
      chat_name = message.new_chat_title
      chat_id = chat.chat_id
      await  message.answer(f"Chat id = <code>{chat_id}</code>")


@dp.message(F.text == 'About US')
async def About_us(message:types.Message):
      await message.answer("Bot Egasi <code>Nurbek Abdurashitov</code> ")

@dp.message(F.text=="Weather")
async def Get_weather(message:types.Message):
      import requests
      appid = '1fb671c7225e9bf67d75f718f5ac3c40'
      lat = '39.647099'
      lon = '66.960289'
      units = 'metric'
      response = requests.get(
            url='https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units={}'.format(lat, lon, appid, units))
      weath = response.json()['weather'][0]['description']
      wea = (response.json()['main']['temp_max'])
      await  message.answer(f"salom bugungi obi havo haqida ma`lumot beraman \n havo {weath} \nGradus: {wea} ")

@dp.message(Command('help'))
async def get_help(message:types.Message):
      await message.answer("Qanaqa yordam kerak")