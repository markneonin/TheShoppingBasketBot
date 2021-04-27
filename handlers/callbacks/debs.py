from loader import dp, bot
import database.db_working as db
from utils.create_text.create_debs_text import create_lite_debs_text, create_extend_debs_text
from aiogram.types import CallbackQuery
from keyboards.debs_inline import *
from callbacks_data import debs_lite_callback, debs_ex_callback


@dp.callback_query_handler(debs_lite_callback.filter())
async def debs_query(call: CallbackQuery):

    await call.answer(cache_time=1)
    message_id = call['message']['message_id']
    chat_id = call['message']['chat']['id']
    data = call.data.split(':')
    main_user_id = int(call.from_user.id)
    debs = db.find_debs(main_user_id)

    if data[1] == 'extend':
        text = create_extend_debs_text(debs, main_user_id)
        keyb = debs_ex_inline(debs)
        await bot.send_message(main_user_id, text, reply_markup=keyb)

    elif data[1] == 'show':
        debs = db.find_debs(main_user_id)
        text, ids = create_lite_debs_text(debs, main_user_id)

        if ids:
            keyb = debs_lite_inline(ids)
        else:
            keyb = None

        await bot.send_message(main_user_id, text=text, reply_markup=keyb)

    else:
        user_id = int(data[1])
        db.delete_user_debs(user_id, main_user_id)
        debs = db.find_debs(main_user_id)
        if debs:
            text, users = create_lite_debs_text(debs, main_user_id)
            keyb = debs_lite_inline(users)
            if text == 'Долгов пока нет...':
                await bot.delete_message(message_id=message_id, chat_id=chat_id)
            else:
                await bot.edit_message_text(message_id=message_id, chat_id=chat_id, text=text)
                await bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id,
                                                reply_markup=keyb)
        else:
            await bot.delete_message(message_id=message_id, chat_id=chat_id)



@dp.callback_query_handler(debs_ex_callback.filter())
async def debsex_query(call: CallbackQuery):
    await call.answer(cache_time=1)
    message_id = call['message']['message_id']
    chat_id = call['message']['chat']['id']
    data = call.data.split(':')
    deb_id = int(data[1])
    main_user_id = int(call.from_user.id)
    db.delete_deb(deb_id)
    debs = db.find_debs(main_user_id)

    text = create_extend_debs_text(debs, main_user_id)
    keyb = debs_ex_inline(debs)

    if text == 'Долгов пока нет...':
        await bot.delete_message(message_id=message_id, chat_id=chat_id)
    else:
        await bot.edit_message_text(message_id=message_id, chat_id=chat_id, text=text)
        await bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id,
                                            reply_markup=keyb)


