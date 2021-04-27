
from database.db_working.users import is_user_exist
from database.db_working.goods import order_status


def create_lite_debs_text(debs, user_id):

    total_dolzhen = 0
    total_nedolzhen = 0
    nedolzhen = {}
    dolzhen = {}
    nedolzhenlist = []

    if debs:

        for deb in debs:

            if deb.user_id == user_id:
                user = is_user_exist(deb.foreign_id)
                if user.user_name not in dolzhen:
                    dolzhen[user.user_name] = deb.amount
                else:
                    dolzhen[user.user_name] += deb.amount
                total_dolzhen += deb.amount

            else:
                user = is_user_exist(deb.user_id)
                if user.user_name not in nedolzhen:
                    nedolzhen[user.user_name] = deb.amount
                else:
                    nedolzhen[user.user_name] += deb.amount

                if user.user_id not in nedolzhenlist:
                    nedolzhenlist.append(user.user_id)
                total_nedolzhen += deb.amount

        out = []

        if nedolzhen:
            for username, amount in nedolzhen.items():
                t = f'Тебе должна(ен) @{username} {round(amount / 100, 2)}₽'
                out.append(t)
        if dolzhen:
            for username, amount in dolzhen.items():
                t = f'Ты должна(ен) @{username} {round(amount / 100, 2)}₽'
                out.append(t)

        text = ''

        for i in range(len(out)):
            t = f'{i + 1})' + out[i] + '\n'
            text += t

        if total_nedolzhen != 0:
            text += f'\nВсего должны: {round(total_nedolzhen / 100, 2)}₽'
            if total_dolzhen != 0:
                text += f'\n\nВсего должна(ен): {round(total_dolzhen / 100, 2)}₽'
        else:
            if total_dolzhen != 0:
                text += f'Всего должна(ен): {round(total_dolzhen / 100, 2)}₽'

        if nedolzhenlist:
            text += f'\n\nНажми на кнопку с номером долга, если тебе его уже вернули:'


        return text, nedolzhenlist

    else:
        return 'Долгов пока нет...', None


def create_extend_debs_text(debs, user_id):

    total_dolzhen = 0
    total_nedolzhen = 0
    nedolzhen = []
    dolzhen = []

    if debs:

        for deb in debs:
            if deb.user_id == user_id:
                dolzhen.append(deb)
                total_dolzhen += deb.amount
            else:
                nedolzhen.append(deb)
                total_nedolzhen += deb.amount

        out = []
        if nedolzhen:
            for deb in nedolzhen:
                user = is_user_exist(deb.user_id)
                order = order_status(deb.order_id)
                t = f'Тебе должна(ен) @{user.user_name} {round(deb.amount / 100, 2)}₽ за заказ "{order.text}"'
                out.append(t)
        if dolzhen:
            for deb in dolzhen:
                user = is_user_exist(deb.foreign_id)
                order = order_status(deb.order_id)
                t = f'Ты должна(ен) @{user.user_name} {round(deb.amount / 100, 2)}₽ за заказ "{order.text}"'
                out.append(t)

        text = ''

        for i in range(len(out)):
            t = f'{i + 1})' + out[i] + '\n'
            text += t

        if total_nedolzhen != 0:
            text += f'\nВсего должны: {round(total_nedolzhen / 100, 2)}₽'
            if total_dolzhen != 0:
                text += f'\n\nВсего должна(ен): {round(total_dolzhen / 100, 2)}₽'
        else:
            if total_dolzhen != 0:
                text += f'Всего должна(ен): {round(total_dolzhen / 100, 2)}₽'

        if nedolzhen:
            text += f'\n\nНажми на кнопку с номером долга, если тебе его уже вернули:'

        return text

    else:
        return 'Долгов пока нет...'