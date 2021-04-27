from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callbacks_data import delete_callback, hide_callback


def delete_inline(orders):
    if (len(orders) % 5) != 0:
        n = (len(orders) // 5) + 1
    else:
        n = len(orders) // 5

    buttons = []
    flag = False
    for i in range(len(orders)):
        buttons.append(InlineKeyboardButton(text=str(i + 1),
                                            callback_data=delete_callback.new(order_id=orders[i].order_id)))
        if orders[i].status == 1:
            flag = True

    lis = []
    for i in range(n):
        lis.append([])
        for j in range(5 * i, 5 * i + 5):
            try:
                lis[i].append(buttons[j])
            except IndexError:
                pass

    lis.append([InlineKeyboardButton(text='Удалить всё', callback_data=delete_callback.new(order_id='all')),
                InlineKeyboardButton(text='Скрыть', callback_data=hide_callback.new(any='1'))])

    if flag:
        lis[-1].append(
            InlineKeyboardButton(text='Удалить купленое', callback_data=delete_callback.new(order_id='complete')))

    delete_ikb = InlineKeyboardMarkup(inline_keyboard=lis)
    return delete_ikb
