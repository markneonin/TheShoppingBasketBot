from aiogram import types
from loader import dp, bot
import database.db_working as db
from callbacks_data import goods_callback
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from states import EditOrder
from aiogram.dispatcher import FSMContext
from keyboards.edit_order_inline import *


@dp.message_handler(state=EditOrder.Edit)
async def edit_mes(msg: types.Message, state: FSMContext):
    username = msg.from_user.username
    data = await state.get_data()
    order_id = data['order']
    db.order_up(order_id, msg.text + f' [изменено @{username}]')

    keyb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Список покупок',
                                                                       callback_data=goods_callback.new(
                                                                           user_id=int(msg.from_user.id)))]])
    await state.finish()
    await bot.send_message(msg.from_user.id, 'Заказ успешно изменён!', reply_markup=keyb)


@dp.message_handler(commands=['edit'])
async def edit(msg: types.Message):

    user_id = msg.from_user.id
    orders = db.get_orders(user_id)
    user_available = [i for i in orders if i.status == 0 and i.user_id == user_id]
    foreign_available = [i for i in orders if i.status == 0 and i.user_id != user_id]

    if user_available or foreign_available:
        output = []
        for ord in user_available:
            t = ord.text
            output.append(t)
        for ord in foreign_available:
            t = ord.text + f' (@{ord.user_name})'
            output.append(t)

        orders = []
        orders += user_available + foreign_available

        for i in range(1, len(output) + 1):
            output[i - 1] = f'{i})' + output[i - 1]

        keyb = edit_inline(orders)
        text = '\n'.join(output)
        text += '\n\nКакой заказ будем редактировать?'

        await bot.send_message(msg.from_user.id, text, reply_markup=keyb)

    else:
        await bot.send_message(msg.from_user.id, 'Пока нечего редактировать.')
