import database.db_working as db


def create_stats_text(user_id):
    complete = db.get_complete(user_id)
    if complete:

        by_days = {}
        total_by_days = {}
        for order in complete:
            if order.date not in by_days:
                by_days[order.date] = [order, ]
            else:
                by_days[order.date].append(order)
            if order.price:
                if order.date not in total_by_days:
                    total_by_days[order.date] = order.price
                else:
                    total_by_days[order.date] += order.price

        text = ''
        total = 0
        for date, orders in by_days.items():
            text += f'🗓 {date}:\n'
            for order in orders:
                if order.user_id == user_id:
                    if order.price:
                        text += f'•{order.text} {round(order.price / 100, 2)}₽\n'
                    else:
                        text += f'•{order.text}\n'
                else:
                    if order.price:
                        text += f'•{order.text} (@{order.user_name}) {round(order.price / 100, 2)}₽\n'
                    else:
                        text += f'•{order.text} (@{order.user_name})\n'

            if date in total_by_days:
                text += f'\n🧾Всего за день: {round(total_by_days[date] / 100, 2)}₽\n\n'
                total += total_by_days[date]

        if total != 0:
            text += f'📈Всего потрачено: {round(total / 100, 2)}₽'

        return text

    else:
        return 'Пока пусто'