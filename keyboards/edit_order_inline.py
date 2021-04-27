from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callbacks_data import edit_order_callback as edit_callback, hide_callback


def edit_inline(orders):
    if (len(orders) % 5) != 0:
        n = (len(orders) // 5) + 1
    else:
        n = len(orders) // 5

    buttons = []
    for i in range(len(orders)):
        buttons.append(InlineKeyboardButton(text=str(i + 1),
                                            callback_data=edit_callback.new(order_id=orders[i].order_id)))

    lis = []
    for i in range(n):
        lis.append([])
        for j in range(5 * i, 5 * i + 5):
            try:
                lis[i].append(buttons[j])
            except IndexError:
                pass
    lis.append([InlineKeyboardButton(text='Скрыть', callback_data=hide_callback.new(any='1'))])
    edit_ikb = InlineKeyboardMarkup(inline_keyboard=lis)

    return edit_ikb