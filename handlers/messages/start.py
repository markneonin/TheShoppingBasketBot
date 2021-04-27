from aiogram import types
from loader import dp, bot
import database.db_working.users as db

from data import *


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    if not user_name:
        user_name = 'unknown'

    is_exit = db.is_user_exist(user_id)

    if not is_exit:
        db.create_user(user_id, user_name.lower())
    else:
        db.update_username(user_id, user_name.lower())

    if user_name == 'unknown':
        await bot.send_message(message.from_user.id, bad_greet)
    else:
        await bot.send_message(message.from_user.id, good_greet)
