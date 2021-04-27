import sqlite3

with sqlite3.connect('goods_database.db') as db:
    cursor = db.cursor()
    query = f"""
    SELECT * FROM orders
    """
    result = cursor.execute(query)
    result = result.fetchall()
    for i in result:
        print(i)