from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import database.db_working as db
from callbacks_data import split_callback, hide_callback
from database.db_working.users import is_user_exist


def paid_inline(user_id):
    users = db.get_access(user_id)
    if (len(users) % 2) != 0:
        n = (len(users) // 2) + 1
    else:
        n = len(users) // 2

    buttons = []
    for user in users:
        buttons.append(InlineKeyboardButton(text='@' + user.user_name,
                                            callback_data=split_callback.new(order_id=user.user_id)))

    lis = []
    for i in range(n):
        lis.append([])
        for j in range(2 * i, 2 * i + 2):
            try:
                lis[i].append(buttons[j])
            except IndexError:
                pass

    if (len(users) % 2) != 0:
        lis[-1].append(InlineKeyboardButton(text='Я платил(а)', callback_data=split_callback.new(order_id=user_id)))
    else:
        lis.append([InlineKeyboardButton(text='Я платил(а)', callback_data=split_callback.new(order_id=user_id))])

    paid_ikb = InlineKeyboardMarkup(inline_keyboard=lis)
    return paid_ikb


def choose_ord_split(orders):

    if (len(orders) % 5) != 0:
        n = (len(orders) // 5) + 1
    else:
        n = len(orders) // 5

    flag = True
    buttons = []
    flagg = False

    for i, (_, (order, chose)) in enumerate(orders.items()):
        buttons.append(InlineKeyboardButton(text=str(i + 1),
                                            callback_data=split_callback.new(order_id=order.order_id)))

        if not order.price:
            flag = False

        if chose:
            flagg = True

    lis = []
    for i in range(n):
        lis.append([])
        for j in range(5 * i, 5 * i + 5):
            try:
                lis[i].append(buttons[j])
            except IndexError:
                pass

    lis.append([InlineKeyboardButton(text='Скрыть', callback_data=hide_callback.new(any='1'))])

    if flag:
        lis[-1].append(InlineKeyboardButton(text='Отметить всё', callback_data=split_callback.new(order_id='all')))
    if flagg:
        lis[-1].append(InlineKeyboardButton(text='Делить!', callback_data=split_callback.new(order_id='go')))

    split_ikb = InlineKeyboardMarkup(inline_keyboard=lis)

    return split_ikb


def between_inline(user_id, flag):
    main = is_user_exist(user_id)

    users = db.get_access(user_id)
    if (len(users) % 2) != 0:
        n = (len(users) // 2) + 1
    else:
        n = len(users) // 2

    buttons = []
    for user in users:
        buttons.append(InlineKeyboardButton(text='@' + user.user_name,
                                            callback_data=split_callback.new(order_id=user.user_id)))

    buttons.append(InlineKeyboardButton(text='@' + main.user_name,
                                            callback_data=split_callback.new(order_id=main.user_id)))


    lis = []
    for i in range(n+1):
        lis.append([])
        for j in range(2 * i, 2 * i + 2):
            try:
                lis[i].append(buttons[j])
            except IndexError:
                pass
    if flag:
        if (len(users) % 2) != 0:
            lis[-1].append(InlineKeyboardButton(text='Делим!', callback_data=split_callback.new(order_id='split')))
        else:
            lis.append([InlineKeyboardButton(text='Делим!', callback_data=split_callback.new(order_id='split'))])

    between_ikb = InlineKeyboardMarkup(inline_keyboard=lis)
    return between_ikb

