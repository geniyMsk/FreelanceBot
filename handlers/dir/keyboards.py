from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

roles_keyboard=InlineKeyboardMarkup(
    inline_keyboard=[
     [
        InlineKeyboardButton(text='Я самозанятый', callback_data='freelancer')
     ],
     [
        InlineKeyboardButton(text='Я заказчик', callback_data='customer')
     ]
    ])


reg_name_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Взять из аккаунта Телеграм', callback_data='give_name')
        ]
    ])


reg_number_keyboard = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text='Отправить номер телефона', request_contact=True)
    ],
    [
        KeyboardButton(text='Не хочу оставлять телефон - пишите в Телеграм')
    ]
], resize_keyboard=True, one_time_keyboard=True)


freelancer_main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Изменить статус')
        ],
        [
            KeyboardButton(text='Заполнить данные о себе заново')
        ],
        [
            KeyboardButton(text='Вернуться в главное меню')
        ]
    ], resize_keyboard=True, one_time_keyboard=True)

yes_no = InlineKeyboardMarkup(
    inline_keyboard=[
     [
        InlineKeyboardButton(text='Да', callback_data='yes'),
        InlineKeyboardButton(text='Нет', callback_data='no')
     ]
    ])

yes = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да")
        ]
    ], resize_keyboard=True)


admin_panel_main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Статистика')
        ],
        [
            KeyboardButton(text='Создать ссылку'),
            KeyboardButton(text='Удалить ссылку')
        ],
        [
            KeyboardButton(text='Выйти из админ панели')
        ]
    ], resize_keyboard=True)

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Назад')
        ]
    ],resize_keyboard=True)


customer_lk = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = 'Реферальная программа', callback_data='ref_programm')
        ],
        [
            InlineKeyboardButton(text='Поиск фрилансеров', callback_data='search'),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='back')
        ]
    ])
