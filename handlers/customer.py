from loader import bot, dp
from aiogram import types
from aiogram.types import ReplyKeyboardRemove, ParseMode, Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from handlers.dir.DBCommands import DBCommands
from handlers.dir.states import CUSTOMER, GET_ROLE
import handlers.dir.keyboards as kb
from config import provider_token
import json
db=DBCommands()



@dp.message_handler(state=CUSTOMER.get_city)
async def customer_get_city(message: Message):
    city = message.text
    chatid = message.from_user.id
    name = message.from_user.full_name
    username = message.from_user.username
    try:
        db.add_customer(par=(chatid, username, name, city))

    except:
        db.update_city_customer(par=(city, chatid))
    await message.answer(f"Ваш город *{city}*", reply_markup=ReplyKeyboardRemove(), parse_mode=ParseMode.MARKDOWN)
    await message.answer(f"Верно?", reply_markup=kb.yes_no)

