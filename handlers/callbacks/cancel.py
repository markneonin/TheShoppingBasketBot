from loader import dp, bot
import database.db_working as db
from utils.create_text.create_goods_text import create_goods_text, create_date
from keyboards.goods_inline import goods_inline
from callbacks_data import cancel_callback
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from states import OrderPrice


@dp.callback_query_handler(cancel_callback.filter(), state=OrderPrice.Pricing)
async def cancel(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    user_id = call.from_user.id

    data = call.data.split(':')
    db.order_price_up(int(data[1]), None)
    db.update_order_status(int(data[1]), 1, create_date())

    orders = db.get_orders(user_id)
    text = create_goods_text(orders, user_id)
    keyb = goods_inline(orders)

    await state.finish()
    await bot.send_message(call.from_user.id, text=text, reply_markup=keyb)