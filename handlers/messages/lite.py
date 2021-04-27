from aiogram import types
from loader import dp, bot
import database.db_working.users as db


@dp.message_handler(commands=['lite'])
async def change_settings(msg: types.Message):
    user_id = int(msg.from_user.id)
    settings = db.user_settings(user_id)
    if settings.lite == 0:
        db.change_settings(user_id, 1)
        await bot.send_message(user_id, 'Отлично! Теперь ты используешь расширенную версию! При завершении '
                                        'покупки, я буду спрашивать стоимость.')
    else:
        db.change_settings(user_id, 0)
        await bot.send_message(user_id, 'Хорошо! Теперь ты используешь упрощённую версию! Я больше не буду спрашивать '
                                        'стоимость, при завершении покупки.')
