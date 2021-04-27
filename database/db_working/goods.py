from sqlalchemy import or_, between

from database.database import Session
from database import tables
from utils.create_text.create_goods_text import create_date


def create_order(user_id, text):
    session = Session()

    user = session.query(tables.User).filter(
        tables.User.user_id == user_id).first()

    date = create_date()
    order = tables.Orders(user_id=user_id,
                          user_name=user.user_name,
                          text=text,
                          created=date)

    try:
        session.add(order)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def get_orders(user_id):
    session = Session()

    access = session.query(tables.Access).filter(tables.Access.user_id == user_id).all()

    foreign_ids = []
    for ac in access:
        foreign_ids.append(ac.access)

    orders = session.query(tables.Orders).filter(tables.Orders.user_id.in_(foreign_ids)).filter(tables.Orders.hide == 0).all()

    session.close()

    return orders


def order_status(order_id):
    session = Session()
    order = session.query(tables.Orders).filter(tables.Orders.order_id == order_id).first()
    session.close()
    return order


def update_order_status(order_id, status, date):
    session = Session()
    try:
        session.query(tables.Orders).filter(
            tables.Orders.order_id == order_id).update(
            {'status': status,
             'date': date})
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def hide_order(order_id):
    session = Session()
    session.query(tables.Orders).filter(tables.Orders.order_id == order_id).update({'hide': 1})
    session.commit()
    session.close()


def hide_all(user_id):
    session = Session()

    access = session.query(tables.Access).filter(tables.Access.user_id == user_id).all()

    foreign_ids = []
    for ac in access:
        foreign_ids.append(ac.access)

    session.query(tables.Orders).filter(tables.Orders.user_id.in_(foreign_ids)).update({'hide': 1})
    session.commit()
    session.close()


def order_up(order_id, text):
    session = Session()
    try:
        session.query(tables.Orders).filter(
            tables.Orders.order_id == order_id).update(
            {'text': text})
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def order_price_up(order_id, price):
    session = Session()
    try:
        session.query(tables.Orders).filter(
            tables.Orders.order_id == order_id).update(
            {'price': price})
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def get_to_split(user_id):
    session = Session()

    access = session.query(tables.Access).filter(tables.Access.user_id == user_id).all()

    foreign_ids = []
    for ac in access:
        foreign_ids.append(ac.access)

    orders = session.query(tables.Orders).filter(tables.Orders.user_id.in_(foreign_ids)).filter(
        tables.Orders.hide == 0).filter(tables.Orders.status == 1).all()

    debs = session.query(tables.Debs).distinct().filter(or_(tables.Debs.user_id == user_id, tables.Debs.foreign_id == user_id)).all()
    session.close()

    splited = []
    for deb in debs:
        splited.append(deb.order_id)

    out = []
    for order in orders:
        if order.order_id not in splited:
            out.append(order)

    return out


def hide_complete(user_id):
    session = Session()

    access = session.query(tables.Access).filter(tables.Access.user_id == user_id).all()

    foreign_ids = []
    for ac in access:
        foreign_ids.append(ac.access)

    session.query(tables.Orders).filter(tables.Orders.user_id.in_(foreign_ids)).filter(tables.Orders.status == 1).update({'hide': 1})
    session.commit()
    session.close()


def get_complete(user_id):
    session = Session()

    access = session.query(tables.Access).filter(tables.Access.user_id == user_id).all()

    foreign_ids = []
    for ac in access:
        foreign_ids.append(ac.access)

    orders = session.query(tables.Orders).filter(tables.Orders.user_id.in_(foreign_ids)).filter(tables.Orders.status == 1).all()

    session.close()

    return orders
