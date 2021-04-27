from callbacks_data import split_callback
from loader import dp, bot
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from states import *
from utils.create_text.create_split_text import *
from keyboards.split_inline import *
from handlers.messages.split import create_debs


@dp.callback_query_handler(split_callback.filter(), state=Split.who_paid)
async def who_paid(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)

    user_id = call.from_user.id
    data = call.data.split(':')
    paid_id = int(data[1])
    data = await state.get_data()
    text = create_split_text(data['orders'], user_id)
    keyb = choose_ord_split(data['orders'])
    data['paid'] = paid_id

    await state.update_data(data)
    await Split.choose_orders.set()
    await bot.send_message(user_id, text=text, reply_markup=keyb)


@dp.callback_query_handler(split_callback.filter(), state=Split.choose_orders)
async def choose_orders(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)

    message_id = call['message']['message_id']
    chat_id = call['message']['chat']['id']
    user_id = call.from_user.id
    data = call.data.split(':')
    order_id = data[1]
    data = await state.get_data()
    order_to_price = None

    if order_id == 'all':
        flag = True
        for  _, (k, v) in data['orders'].items():
            if data['orders'][k.order_id][1]: flag = False
        for _, (k, v) in data['orders'].items():
            data['orders'][k.order_id][1] = True if flag else False

    elif order_id == 'go':

        new_orders = {'orders': [], 'total': 0}
        for _, (k, v) in data['orders'].items():
            if v:
                new_orders['orders'].append(k)
                new_orders['total'] += k.price

        data['orders'] = new_orders
        data['users'] = {}

        text = create_between_text(data)
        keyb = between_inline(user_id, False)

        await Split.between.set()
        await state.update_data(data)
        await bot.send_message(user_id, text=text, reply_markup=keyb)
        return None

    else:
        for _, (k, v) in data['orders'].items():
            if k.order_id == int(order_id):
                if k.price:
                    data['orders'][k.order_id][1] = False if data['orders'][k.order_id][1] else True
                else:
                    order_to_price = k

    text = create_split_text(data['orders'], user_id)
    keyb = choose_ord_split(data['orders'])

    if not order_to_price:
        await state.update_data(data)
        await bot.edit_message_text(message_id=message_id, chat_id=chat_id, text=text)
        await bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id,
                                        reply_markup=keyb)

    else:
        await Split.order_price.set()
        await state.update_data({'price': order_to_price.order_id})
        await bot.send_message(user_id,
                               'Стоимость данного заказа неизвестна, отправь мне цену, после чего, покупку '
                               'можно будет разделить:')


@dp.callback_query_handler(split_callback.filter(), state=Split.between)
async def between(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)

    message_id = call['message']['message_id']
    chat_id = call['message']['chat']['id']
    data = call.data.split(':')
    main_user_id = int(call.from_user.id)
    user_id = data[1]
    data = await state.get_data()

    if user_id == 'split':
        await state.finish()
        await create_debs(data, main_user_id)

    else:
        user = data['users'].get(int(user_id), None)
        if user:
            data['users'].pop(int(user_id))
        else:
            data['users'][int(user_id)] = is_user_exist(int(user_id))

        text = create_between_text(data)
        keyb = between_inline(int(user_id), len(data['users']) > 0)
        await state.update_data(data)
        await bot.edit_message_text(message_id=message_id, chat_id=chat_id, text=text)
        await bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id,
                                            reply_markup=keyb)
