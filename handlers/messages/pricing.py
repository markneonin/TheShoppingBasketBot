from aiogram import types
from loader import dp, bot
from database.db_working import goods as goods_db
from states import OrderPrice
from aiogram.dispatcher import FSMContext
from utils.create_text.create_goods_text import create_goods_text, create_date
from keyboards.goods_inline import goods_inline


@dp.message_handler(state=OrderPrice.Pricing)
async def pricing(msg: types.Message, state: FSMContext):
    user_id = msg.from_user.id
    try:
        price = msg.text.replace(',', '.')
        price = float(price)
        price = int(price * 100)

        if price >= 10 ** 18:
            await bot.send_message(msg.from_user.id, 'Многовато будет... попробуй ещё раз.')
        elif price < 1:
            await bot.send_message(msg.from_user.id, 'Маловато будет... попробуй ещё раз.')
        else:
            data = await state.get_data()
            goods_db.order_price_up(data['order'], price)
            goods_db.update_order_status(data['order'], 1, create_date())

            orders = goods_db.get_orders(user_id)
            text = create_goods_text(orders, user_id)
            keyb = goods_inline(orders)

            await state.finish()
            await bot.send_message(user_id, text, reply_markup=keyb)

    except Exception:
        await bot.send_message(user_id, 'Что-то не сходится... попробуйте ещё раз.')