from aiogram import types
from loader import dp, bot
from keyboards.debs_inline import *
from aiogram.dispatcher import FSMContext
from utils.create_text.create_debs_text import *
from database.db_working.debs import find_debs


@dp.message_handler(commands=['debs'])
async def debs(msg: types.Message, state: FSMContext):
    user_id = int(msg.from_user.id)

    debs = find_debs(user_id)
    text, ids = create_lite_debs_text(debs, user_id)

    if ids: keyb = debs_lite_inline(ids)
    else: keyb = None

    await bot.send_message(msg.from_user.id, text=text, reply_markup=keyb)
