def create_delete_text(orders, user_id):

    if orders:

        output = []
        total = 0

        for i in range(len(orders)):
            if orders[i].created: date = '.'.join(orders[i].created.split('.')[:2])
            else: date = '01.01'

            if orders[i].status == 0 and orders[i].user_id == user_id:
                output.append(f'{i + 1})' + orders[i].text + f' 🗓{date}')

            elif orders[i].status == 0 and orders[i].user_id != user_id:
                output.append(f'{i + 1})' + orders[i].text + f' (@{orders[i].user_name})'+ f' 🗓{date}')

            elif orders[i].status == 1 and orders[i].user_id == user_id:
                t = '\u0336'.join(orders[i].text) + '\u0336'
                if orders[i].price:
                    t += f' {round(orders[i].price / 100, 2)}₽'
                    total += orders[i].price
                output.append(f'{i + 1})' + t + f' 🗓{date}')

            elif orders[i].status == 1 and orders[i].user_id != user_id:
                t = '\u0336'.join(orders[i].text) + '\u0336'
                if orders[i].price:
                    t += f' {round(orders[i].price / 100, 2)}₽'
                    total += orders[i].price
                output.append(f'{i + 1})' + t + f' (@{orders[i].user_name})' + f' 🗓{date}')

        text = '\n'.join(output)
        text += '\n\nКакой заказ удалить?'

        return text

    else:
        return 'Пусто...'
