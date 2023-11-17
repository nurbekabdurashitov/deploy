from aiogram.utils.keyboard import ReplyKeyboardBuilder , KeyboardButton

from aiogram.types.keyboard_button_request_chat import KeyboardButtonRequestChat

button = ReplyKeyboardBuilder()
button.add(KeyboardButton(text="Profile",  request_contact=True))
button.add(KeyboardButton(text="Chat id", request_chat=KeyboardButtonRequestChat(chat_is_channel=False, request_id=7154)))
button.add(KeyboardButton(text="Channel id", request_chat=KeyboardButtonRequestChat(chat_is_channel=True , request_id=2330)))
button.add(KeyboardButton(text="About US"))
button.add(KeyboardButton(text="Weather"))

button.adjust(2,1,2)
