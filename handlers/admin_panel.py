import sqlite3
from loader import bot, dp
from aiogram import types
from aiogram.types import ReplyKeyboardRemove, ParseMode, ReplyKeyboardMarkup, KeyboardButton
from handlers.dir.DBCommands import DBCommands
from handlers.dir.states import GET_ROLE, FREELANCER_REG, CUSTOMER, ADMINPANEL

from config import ADMINS
import handlers.dir.keyboards as kb

db=DBCommands()



for admin in ADMINS:
    @dp.message_handler(commands=['admin'], user_id=admin, state='*')
    async def adminpanel_in(message: types.Message):
        await message.answer(text='Админ панель', reply_markup=kb.admin_panel_main_keyboard)
        await ADMINPANEL.admin_panel.set()


    @dp.message_handler(lambda m:m.text=="Статистика", user_id=admin, state=ADMINPANEL.admin_panel)
    async def adminpanel_stat(message: types.Message):
        reflinks = db.select_all_reflinks()

        text = 'Ссылки:\n'
        for reflink in reflinks:
            text += f'{reflink[1]} - {reflink[2]}\n'

        if text=='Ссылки:\n':
            text='Ссылок нет'
        await message.answer(text=text)


        freelancers = db.select_all_freelancer()
        c = []
        cities = []
        for freelancer in freelancers:
            c.append(freelancer[4])
        for city in c:
            if [city,0] not in cities:
                cities.append([city,0])

        for freelancer in freelancers:
            for city in cities:
                if city[0] == freelancer[4]:
                    city[1] +=1
        text = 'Города:\n'
        for city in cities:
            text+=f'{city[0]} - {city[1]}\n'
        if text == 'Города:\n':
            text='Городов нет'
        await message.answer(text=text)







    @dp.message_handler(lambda m: m.text == "Создать ссылку", user_id=admin, state=ADMINPANEL.admin_panel)
    async def adminpanel_add(message: types.Message):
        await message.answer("Введите название для ссылки", reply_markup=kb.back)
        await ADMINPANEL.admin_add_reflink.set()


    @dp.message_handler(lambda m: m.text == "Назад", user_id=admin, state=ADMINPANEL.admin_add_reflink)
    async def adminpanel_add(message: types.Message):
        await message.answer(text='Админ панель', reply_markup=kb.admin_panel_main_keyboard)
        await ADMINPANEL.admin_panel.set()

    @dp.message_handler(user_id=admin, state=ADMINPANEL.admin_add_reflink)
    async def adminpanel_add_reflink(message: types.Message):
        reflinks = db.select_all_reflinks()
        try:
            n='r' + str(int(reflinks[-1][0])+1)
        except:
            n='r1'
        name = message.text
        for reflink in reflinks:
            if reflink[1] == name:
                await message.answer("Такая ссылка уже есть. Введите название для ссылки", reply_markup=kb.back)
                return

        db.add_reflink(par=(n,name))

        bot_name = (await bot.get_me()).username
        reflink = f'http://t.me/{bot_name}?start={n}'
        await message.answer(f'{name}: {reflink}', reply_markup=ReplyKeyboardRemove())
        await message.answer(text='Админ панель', reply_markup=kb.admin_panel_main_keyboard)
        await ADMINPANEL.admin_panel.set()


    @dp.message_handler(lambda m: m.text == "Удалить ссылку", user_id=admin, state=ADMINPANEL.admin_panel)
    async def adminpanel_delete(message: types.Message):
        reflinks = db.select_all_reflinks()

        delete_reflink = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text='Назад')
                ]
            ], resize_keyboard=True)

        for reflink in reflinks:
            delete_reflink.add(KeyboardButton(text=f'{reflink[1]}'))
        await message.answer('Выберите ссылку для удаления', reply_markup=delete_reflink)
        await ADMINPANEL.admin_delete_reflink.set()

    @dp.message_handler(lambda m: m.text == "Назад", user_id=admin, state=ADMINPANEL.admin_delete_reflink)
    async def adminpanel_delete_back(message: types.Message):
        await message.answer(text='Админ панель', reply_markup=kb.admin_panel_main_keyboard)
        await ADMINPANEL.admin_panel.set()
    @dp.message_handler(user_id=admin, state=ADMINPANEL.admin_delete_reflink)
    async def adminpanel_delete_reflink(message: types.Message):
        name = message.text
        try:
            db.delete_reflink(name=name)
            reflinks = db.select_all_reflinks()
            delete_reflink = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text='Назад')
                    ]
                ], resize_keyboard=True)

            for reflink in reflinks:
                delete_reflink.add(KeyboardButton(text=f'{reflink[1]}'))
            await message.answer(f'Ссылка {name} удалена', reply_markup=delete_reflink)

        except Exception as error:
            await message.answer(f'{error}')
            await message.answer('Произошла ошибка. Попробуйте еще раз')


    @dp.message_handler(lambda m: m.text == "Выйти из админ панели", user_id=admin, state=ADMINPANEL.admin_panel)
    async def adminpanel_back(message: types.Message):
        await message.answer(f"Здравствуйте, *{message.from_user.first_name}*.",
                             reply_markup=ReplyKeyboardRemove(),
                             parse_mode=ParseMode.MARKDOWN)
        await message.answer(text='Нажмите на одну из кнопок ниже', reply_markup=kb.roles_keyboard)
        await GET_ROLE.get_role.set()
