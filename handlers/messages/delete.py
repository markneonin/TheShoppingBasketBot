from aiogram import types
from loader import dp, bot
import database.db_working as db
from keyboards.delete_inline import *
from utils.create_text.create_delete_text import create_delete_text


@dp.message_handler(commands=['delete'])
async def hide_order(msg: types.Message):

    user_id = msg.from_user.id

    orders = db.get_orders(user_id)
    text = create_delete_text(orders, user_id)

    if orders: keyb = delete_inline(orders)
    else: keyb = None

    await bot.send_message(user_id, text, reply_markup=keyb)
