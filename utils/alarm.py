from loader import bot
from database.db_working.users import is_user_exist


async def alarm(order, user_id):
    user = is_user_exist(user_id)
    await bot.send_message(order.user_id, f'@{user.user_name} купил ваш заказ "{order.text}"')

