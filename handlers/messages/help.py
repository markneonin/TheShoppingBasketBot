from aiogram import types
from loader import dp, bot
from data import *


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, help_msg)