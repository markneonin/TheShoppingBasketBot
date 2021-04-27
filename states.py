from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderPrice(StatesGroup):
    Pricing = State()


class EditOrder(StatesGroup):
    Edit = State()


class Split(StatesGroup):
    who_paid = State()
    choose_orders = State()
    order_price = State()
    between = State()