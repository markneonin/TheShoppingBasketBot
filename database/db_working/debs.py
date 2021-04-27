from sqlalchemy import or_, between

from database.database import Session
from database import tables


def create_debs(debs):
    session = Session()
    try:
        session.add_all(debs)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def find_debs(user_id):
    session = Session()

    debs = session.query(tables.Debs).filter(or_(tables.Debs.user_id == user_id, tables.Debs.foreign_id == user_id)).all()
    session.close()
    return debs


def delete_user_debs(user_id, foreign_id):
    session = Session()
    session.query(tables.Debs).filter(tables.Debs.user_id == user_id).filter(tables.Debs.foreign_id == foreign_id).delete()
    session.commit()
    session.close()


def delete_deb(deb_id):
    session = Session()
    session.query(tables.Debs).filter(tables.Debs.deb_id == deb_id).delete()
    session.commit()
    session.close()
