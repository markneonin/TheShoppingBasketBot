from loader import dp, bot
import database.db_working.goods as db
from utils.create_text.create_goods_text import create_goods_text
from keyboards.goods_inline import goods_inline
from callbacks_data import goods_callback
from aiogram.types import CallbackQuery


@dp.callback_query_handler(goods_callback.filter())
async def show_goods(call: CallbackQuery):
    await call.answer(cache_time=1)

    user_id = call.from_user.id
    orders = db.get_orders(user_id)

    text = create_goods_text(orders, user_id)
    keyb = goods_inline(orders)

    await bot.send_message(user_id, text, reply_markup=keyb)