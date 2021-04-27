from sqlalchemy import or_, between

from database.database import Session
from database import tables


def create_user(user_id, user_name):
    session = Session()

    user = tables.User(user_id=user_id, user_name=user_name)
    access = tables.Access(user_id=user_id, access=user_id)
    status = tables.UserStatus(user_id=user_id)
    settings = tables.Settings(user_id=user_id)

    try:
        session.add(user)
        session.add(access)
        session.add(status)
        session.add(settings)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def is_user_exist(user_id):
    session = Session()
    user = session.query(tables.User).filter(tables.User.user_id == user_id).first()
    session.close()
    if user:
        return user
    else:
        return False


def update_username(user_id, user_name):
    session = Session()
    try:
        session.query(tables.User).filter(
            tables.User.user_id == user_id).update(
            {'user_name': user_name})
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def is_user_exist_by_username(user_name):
    session = Session()
    user = session.query(tables.User).filter(tables.User.user_name == user_name).first()
    session.close()
    if user:
        return user
    else:
        return False


def user_settings(user_id):
    session = Session()
    settings = session.query(tables.Settings).filter(tables.Settings.user_id == user_id).first()
    session.close()
    return settings


def change_settings(user_id, value):
    session = Session()
    try:
        session.query(tables.Settings).filter(
            tables.Settings.user_id == user_id).update(
            {'lite': value})
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def get_users():
    session = Session()

    users = session.query(tables.User).all()

    session.close()

    return users


def delete_user(user_id):
    session = Session()
    session.query(tables.User).filter(tables.User.user_id == user_id).delete()
    session.commit()
    session.close()
