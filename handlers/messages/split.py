from aiogram import types
from loader import dp, bot
from database.db_working.users import is_user_exist_by_username
import database.db_working.goods as goods_db
from keyboards.split_inline import *
from aiogram.dispatcher import FSMContext
from states import Split
from utils.create_text.create_split_text import *
from database.tables import Debs
from callbacks_data import debs_lite_callback


@dp.message_handler(commands=['split'])
async def split(msg: types.Message, state: FSMContext):
    user_id = int(msg.from_user.id)
    res = db.get_to_split(int(msg.from_user.id))

    if res:
        keyb = paid_inline(user_id)
        data = {i.order_id: [i, False] for i in res}

        await state.update_data({'orders': data})
        await Split.who_paid.set()
        await bot.send_message(user_id, 'Для начала определимся, кто платил. Просто отправь мне '
                                        '@имя_пользователя:', reply_markup=keyb)
    else:
        await bot.send_message(user_id, 'Делить можно только завершенные покупки, пока таких нет.')


@dp.message_handler(state=Split.who_paid)
async def who_paid(msg: types.Message, state: FSMContext):
    user_id = msg.from_user.id
    if '@' not in msg.text or msg.text.count('@') > 1:
        keyb = paid_inline(user_id)
        await bot.send_message(msg.from_user.id, 'Так не пойдёт, переделывай:', reply_markup=keyb)
    else:
        _, user_name = msg.text.split('@')
        user = is_user_exist_by_username(user_name.lower())
        if not user:
            keyb = paid_inline(user_id)
            await bot.send_message(msg.from_user.id,
                                   f'@{user_name} к сожалению, пока не использует меня, жду валидный юзернейм:', reply_markup=keyb)
        else:
            data = await state.get_data()

            text  = create_split_text(data['orders'], int(msg.from_user.id))
            keyb = choose_ord_split(data['orders'])
            await Split.choose_orders.set()
            await state.update_data({'paid': user.user_id})
            await bot.send_message(msg.from_user.id, text=text, reply_markup=keyb)


@dp.message_handler(state=Split.order_price)
async def order_price(msg: types.Message, state: FSMContext):
    user_id = msg.from_user.id
    try:
        price = msg.text.replace(',', '.')
        price = float(price)
        price = int(price * 100)

        if price >= 10 ** 18:
            await bot.send_message(msg.from_user.id, 'Многовато будет... попробуй ещё раз.')
        elif price < 1:
            await bot.send_message(msg.from_user.id, 'Маловато будет... попробуй ещё раз.')
        else:
            data = await state.get_data()
            order_id = data['price']
            goods_db.order_price_up(order_id, price)
            order = goods_db.order_status(order_id)
            data['orders'][order_id][0] = order
            data['orders'][order_id][1] = True
            data['price'] = None

            text = create_split_text(data['orders'], user_id)
            keyb = choose_ord_split(data['orders'])

            await Split.choose_orders.set()
            await state.update_data(data)
            await bot.send_message(user_id, text, reply_markup=keyb)

    except Exception:
        await bot.send_message(user_id, 'Что-то не сходится... попробуйте ещё раз.')


@dp.message_handler(state=Split.between)
async def order_price(msg: types.Message, state: FSMContext):

    if '@' not in msg.text:
        await bot.send_message(msg.from_user.id, 'Добавь, пожалуйста, "@" к именам пользователей')
    else:
        usernames = [i.strip() for i in msg.text.split('@')]
        usernames = [i.lower() for i in usernames if i != '']
        users = []
        invalid_usernames = []

        flag = True
        for username in usernames:
            user = is_user_exist_by_username(username)
            if not user:
                flag = False
                invalid_usernames.append(username)
            else:
                users.append(user)

        if flag:

            data = await state.get_data()
            for user in users:
                data['users'][user.user_id] = user

            await state.finish()
            await create_debs(data, int(msg.from_user.id))


        else:
            string = ' @'.join(invalid_usernames)
            await bot.send_message(msg.from_user.id,
                                   f'Эти господа{string} пока меня не используют, повтори попытку:')


async def create_debs(data, user_id):


    owner_id = int(data['paid'])
    orders = data['orders']['orders']
    users = data['users']

    n = len(users)
    debs = []
    for user in users.values():
        for order in orders:
            if user.user_id != owner_id:
                deb = Debs(user_id=user.user_id,
                                  foreign_id=owner_id,
                                  amount=round(order.price / n),
                                  order_id=order.order_id)
                debs.append(deb)

    db.create_debs(debs)
    keyb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Подробнее', callback_data=debs_lite_callback.new(user_id='show'))]])

    await bot.send_message(user_id, 'Готово! Проверь долги.', reply_markup=keyb)