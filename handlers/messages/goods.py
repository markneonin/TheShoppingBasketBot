from aiogram import types
from loader import dp, bot
import database.db_working.goods as db
from utils.create_text.create_goods_text import create_goods_text
from keyboards.goods_inline import goods_inline


@dp.message_handler(commands=['goods'])
async def goods_list(msg: types.Message):

    user_id = msg.from_user.id
    orders = db.get_orders(user_id)

    text = create_goods_text(orders, user_id)

    if orders: keyb = goods_inline(orders)
    else: keyb = None

    await bot.send_message(msg.from_user.id, text, reply_markup=keyb)
