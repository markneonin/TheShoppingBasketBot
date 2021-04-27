from aiogram import types
from loader import dp, bot
import utils.create_text.create_stats_text as ct


@dp.message_handler(commands=['stats'])
async def stats(msg: types.Message):
    text = ct.create_stats_text(msg.from_user.id)
    await bot.send_message(msg.from_user.id, text=text)