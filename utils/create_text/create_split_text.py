def create_split_text(orders, user_id):
    output = []
    total = 0

    for i, (_, (order, chose)) in enumerate(orders.items()):

        if order.user_id == user_id:
            if chose:
                t = '✔'
            else:
                t = ''
            t += order.text
            if order.price:
                t += f' {round(order.price / 100, 2)}₽'
                if '✔' in t:
                    total += order.price
            output.append(f'{i + 1})' + t)

        elif order.user_id != user_id:
            if chose:
                t = '✔'
            else:
                t = ''
            t += order.text
            if order.price:
                t += f' {round(order.price / 100, 2)}₽'
                if '✔' in t:
                    total += order.price
            output.append(f'{i + 1})' + t + f' (@{order.user_name})')

    text = '\n'.join(output)

    text += f'\n\nОбщая сумма: {round(total / 100, 2)}₽'

    text += '\n\nВыбери заказы, которые хочешь разделить:'

    return text




def create_between_text(data):

    users = data.get('users', None)
    total = data['orders']['total']
    text = ''

    if users:
        for i, user in enumerate(users.values()):
            t = f'{i + 1}) @' + user.user_name + '\n'
            text += t
        text += f'\nНа персону получается: {round(total / (len(users) * 100), 2)}₽\n'

    text += '\nОтлично! Выбери, между кем разделить покупки или отправь мне сообщение с юзернеймами формата "@username1 ' \
            '@username2 ...": '

    return text
