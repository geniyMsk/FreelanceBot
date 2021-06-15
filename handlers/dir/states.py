from aiogram.dispatcher.filters.state import State, StatesGroup

class GET_ROLE(StatesGroup):
    get_role=State()


class FREELANCER_REG(StatesGroup):
    name = State()
    description = State()
    city = State()
    number = State()
    lk = State()

class CUSTOMER(StatesGroup):
    lk = State()
    get_city = State()
    search = State()


class ADMINPANEL(StatesGroup):
    admin_panel = State()
    admin_add_reflink = State()
    admin_delete_reflink = State()