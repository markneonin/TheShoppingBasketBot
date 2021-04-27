from loader import dp, bot
from aiogram.types import CallbackQuery
from keyboards.delete_inline import hide_callback
from states import *
from aiogram.dispatcher import FSMContext

states = [Split.who_paid,
          Split.between,
          Split.choose_orders,
          Split.order_price,
          OrderPrice.Pricing,
          EditOrder.Edit]


@dp.callback_query_handler(hide_callback.filter())
async def hide(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    message_id = call['message']['message_id']
    chat_id = call['message']['chat']['id']
    await state.finish()
    await bot.delete_message(message_id=int(message_id), chat_id=int(chat_id))


@dp.callback_query_handler(hide_callback.filter(), state=states)
async def hide_in_state(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    message_id = call['message']['message_id']
    chat_id = call['message']['chat']['id']
    await state.finish()
    await bot.delete_message(message_id=int(message_id), chat_id=int(chat_id))






