from aiogram import types
from loader import dp, bot
from database.db_working import users as user_db
from database.db_working import access as access_db
from database.db_working import goods as goods_db
from callbacks_data import goods_callback
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@dp.message_handler()
async def process(msg: types.Message):

    if '@' in msg.text:

        user_name = msg.text.split('@')
        if len(user_name) != 2:
            await bot.send_message(msg.from_user.id, 'Не понял... Повторите попытку.')
        else:
            is_exist = user_db.is_user_exist_by_username(user_name[1].lower())
            if not is_exist:
                await bot.send_message(msg.from_user.id, f'@{user_name[1]} пока не использует меня')
            else:
                access = access_db.check_access(is_exist.user_id, int(msg.from_user.id))
                if not access:
                    access_db.create_access(is_exist.user_id, msg.from_user.id)
                    await bot.send_message(msg.from_user.id,
                                           f'Отлично! Теперь у @{user_name[1]} есть доступ к твоим '
                                           f'покупкам')
                else:
                    access_db.delete_access(access.access_id)
                    await bot.send_message(msg.from_user.id,
                                           f'Понял. Теперь у @{user_name[1]} нет доступа к твоим '
                                           f'покупкам')


    else:
        goods_db.create_order(msg.from_user.id, msg.text)
        keyb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Список покупок',
                                                                           callback_data=goods_callback.new(
                                                                               user_id=int(msg.from_user.id)))]])
        await bot.send_message(msg.from_user.id, 'Сделано.', reply_markup=keyb)