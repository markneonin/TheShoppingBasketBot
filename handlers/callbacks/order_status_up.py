from loader import dp, bot
import database.db_working.users as user_db
import database.db_working.goods as goods_db
from utils.create_text.create_goods_text import create_goods_text, create_date
from keyboards.goods_inline import goods_inline
from callbacks_data import status_up_callback
from aiogram.types import CallbackQuery
from utils.alarm import alarm
from callbacks_data import cancel_callback
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from states import OrderPrice


@dp.callback_query_handler(status_up_callback.filter())
async def order_status_up(call: CallbackQuery, state: FSMContext):

    await call.answer(cache_time=1)
    data = call.data.split(':')
    order = goods_db.order_status(int(data[1]))
    user_id = int(call.from_user.id)
    settings = user_db.user_settings(user_id)
    message_id = call['message']['message_id']
    chat_id = call['message']['chat']['id']

    if settings.lite == 0:
        if order:
            if order.status == 0:
                goods_db.update_order_status(order.order_id, 1, create_date())
                if order.user_id != user_id:
                    await alarm(order, user_id)

            else:
                goods_db.update_order_status(order.order_id, 0, '01.01.2000')

            orders = goods_db.get_orders(user_id)
            new_text = create_goods_text(orders, user_id)
            keyb = goods_inline(orders)

            await bot.edit_message_text(message_id=message_id, chat_id=chat_id, text=new_text)
            await bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id, reply_markup=keyb)

        else:
            await bot.send_message(user_id, 'Этого заказа больше не существует')

    else:
        if order:
            if order.status == 1:
                goods_db.update_order_status(order.order_id, 0, '01.01.2000')
                goods_db.order_price_up(order.order_id, None)

                orders = goods_db.get_orders(user_id)
                new_text = create_goods_text(orders, user_id)
                keyb = goods_inline(orders)

                await bot.edit_message_text(message_id=message_id, chat_id=chat_id, text=new_text)
                await bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id,
                                                    reply_markup=keyb)

            else:
                if order.user_id != user_id:
                    await alarm(order=order, user_id=user_id)

                keyb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Не указывать цену',
                                                                                   callback_data=cancel_callback.new(
                                                                                           order_id=order.order_id))]])
                data = {'order': order.order_id}
                await state.update_data(data)
                await OrderPrice.Pricing.set()
                await bot.send_message(user_id, 'Почём?', reply_markup=keyb)
        else:
            await bot.send_message(user_id, 'Этого заказа больше не существует')
