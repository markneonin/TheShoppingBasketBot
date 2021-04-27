from sqlalchemy import or_, between

from database.database import Session
from database import tables


def create_access(user_id, foreign_id):
    session = Session()

    access = tables.Access(user_id=user_id, access=foreign_id)

    try:
        session.add(access)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def check_access(user_id, foreign_id):
    session = Session()
    access = session.query(tables.Access).filter(tables.Access.user_id == user_id).filter(tables.Access.access == foreign_id).first()
    session.close()
    if access:
        return access
    else:
        return False


def delete_access(access_id):
    session = Session()
    session.query(tables.Access).filter(tables.Access.access_id == access_id).delete()
    session.commit()
    session.close()


def get_access(user_id):
    session = Session()

    access1 = session.query(tables.Access).filter(tables.Access.user_id == user_id).all()
    access2 = session.query(tables.Access).filter(tables.Access.access == user_id).all()

    ids = []
    for ac in access1:
        if user_id != ac.access:
            ids.append(ac.access)

    for ac in access2:
        if user_id != ac.user_id:
            ids.append(ac.user_id)

    users = session.query(tables.User).filter(tables.User.user_id.in_(ids)).all()

    session.close()

    return users