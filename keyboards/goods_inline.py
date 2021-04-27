from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callbacks_data import status_up_callback


def goods_inline(orders):
    if (len(orders) % 5) != 0:
        n = (len(orders) // 5) + 1
    else:
        n = len(orders) // 5

    buttons = []
    for i in range(len(orders)):
        buttons.append(InlineKeyboardButton(text=str(i + 1),
                                            callback_data=status_up_callback.new(order_id=orders[i].order_id)))

    lis = []
    for i in range(n):
        lis.append([])
        for j in range(5 * i, 5 * i + 5):
            try:
                lis[i].append(buttons[j])
            except IndexError:
                pass

    goods_ikb = InlineKeyboardMarkup(inline_keyboard=lis)
    return goods_ikb
