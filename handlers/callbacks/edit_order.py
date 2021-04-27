from callbacks_data import edit_order_callback
from loader import dp, bot
import database.db_working as db
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from states import EditOrder


@dp.callback_query_handler(edit_order_callback.filter())
async def edit_order(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)

    data = call.data.split(':')
    order = db.order_status(int(data[1]))
    user_id = int(call.from_user.id)
    st_data = {'order': order.order_id}

    await EditOrder.Edit.set()
    await state.update_data(st_data)

    if order:
        await bot.send_message(user_id, 'Отлично, отправь мне новый текст заказа:')
    else:
        await bot.send_message(user_id, 'Этого заказа больше не существует')