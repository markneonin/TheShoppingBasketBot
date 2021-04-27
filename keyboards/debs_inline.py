from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callbacks_data import hide_callback, debs_ex_callback, debs_lite_callback


def debs_lite_inline(users_ids):
    if (len(users_ids) % 5) != 0:
        n = (len(users_ids) // 5) + 1
    else:
        n = len(users_ids) // 5

    buttons = []
    for i in range(len(users_ids)):
        buttons.append(InlineKeyboardButton(text=str(i + 1),
                                            callback_data=debs_lite_callback.new(user_id=users_ids[i])))

    lis = []
    for i in range(n):
        lis.append([])
        for j in range(5 * i, 5 * i + 5):
            try:
                lis[i].append(buttons[j])
            except IndexError:
                pass

    lis.append([InlineKeyboardButton(text='Скрыть', callback_data=hide_callback.new(any='1')),
                InlineKeyboardButton(text='Подробнее', callback_data=debs_lite_callback.new(user_id='extend'))])
    debs_lite_ikb = InlineKeyboardMarkup(inline_keyboard=lis)

    return debs_lite_ikb


def debs_ex_inline(debs):
    if (len(debs) % 5) != 0:
        n = (len(debs) // 5) + 1
    else:
        n = len(debs) // 5

    buttons = []
    for i in range(len(debs)):
        buttons.append(InlineKeyboardButton(text=str(i + 1),
                                            callback_data=debs_ex_callback.new(deb_id=debs[i].deb_id)))

    lis = []
    for i in range(n):
        lis.append([])
        for j in range(5 * i, 5 * i + 5):
            try:
                lis[i].append(buttons[j])
            except IndexError:
                pass

    lis.append([InlineKeyboardButton(text='Скрыть', callback_data=hide_callback.new(any='1'))])
    debs_extend_ikb = InlineKeyboardMarkup(inline_keyboard=lis)

    return debs_extend_ikb