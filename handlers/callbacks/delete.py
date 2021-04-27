from loader import dp, bot
import database.db_working as db
from utils.create_text.create_delete_text import create_delete_text
from callbacks_data import delete_callback
from aiogram.types import CallbackQuery
from keyboards.delete_inline import delete_inline


@dp.callback_query_handler(delete_callback.filter())
async def delete(call: CallbackQuery):
    await call.answer(cache_time=1)
    user_id = int(call.from_user.id)
    data = call.data.split(':')
    message_id = int(call['message']['message_id'])
    chat_id = int(call['message']['chat']['id'])

    if data[1] == 'all':
        db.hide_all(user_id)
        await bot.delete_message(message_id=message_id, chat_id=chat_id)

    elif data[1] == 'complete':
        db.hide_complete(user_id)

        orders = db.get_orders(user_id)

        if orders:
            text = create_delete_text(orders, user_id)
            keyb = delete_inline(orders)
            await bot.send_message(user_id, text=text, reply_markup=keyb)

        else:
            await bot.delete_message(message_id=message_id, chat_id=chat_id)

    else:
        order_id = int(data[1])
        db.hide_order(order_id)

        orders = db.get_orders(user_id)
        if orders:
            text = create_delete_text(orders, user_id)
            keyb = delete_inline(orders)

            await bot.edit_message_text(message_id=message_id, chat_id=chat_id, text=text)
            await bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id,
                                                reply_markup=keyb)
        else:
            await bot.delete_message(message_id=message_id, chat_id=chat_id)
