import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_id = sa.Column(sa.Integer, primary_key=True)
    user_name = sa.Column(sa.String, nullable=True)


class Access(Base):
    __tablename__ = 'access'

    access_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer)
    access = sa.Column(sa.Integer)


class Orders(Base):
    __tablename__ = 'orders'

    order_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer)
    user_name = sa.Column(sa.String)
    text = sa.Column(sa.Text)
    status = sa.Column(sa.Integer, default=0)
    price = sa.Column(sa.Integer, nullable=True)
    hide = sa.Column(sa.Integer, default=0)
    date = sa.Column(sa.Text, default='04.04.2021')
    created = sa.Column(sa.Text)


class Settings(Base):
    __tablename__ = 'settings'

    user_id = sa.Column(sa.Integer, primary_key=True)
    lite = sa.Column(sa.Integer, default=0)


class Debs(Base):
    __tablename__ = 'debs'

    deb_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer)
    foreign_id = sa.Column(sa.Integer)
    amount = sa.Column(sa.Integer)
    order_id = sa.Column(sa.Integer)




