from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table

naming_convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

metadata = MetaData(naming_convention=naming_convention)

ACTION_USER = Table(
    'action_user',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('id_user', Integer, nullable=True),
    Column('action', String, nullable=True),
    Column('date', String, nullable=True, default=str(datetime.utcnow())),

)

ACTION = Table(
    'action',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('id_book', Integer, nullable=True),
    Column('id_user', Integer, nullable=True),
    Column('action', String, nullable=True),
    Column('obj_type', String, nullable=True),
    Column('date', String, nullable=True, default=str(datetime.utcnow())),
)

ACTION_BOOK = Table(
    'action_book',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('id_book', Integer, nullable=True),
    Column('action', String, nullable=True),
    Column('date', String, nullable=True, default=str(datetime.utcnow())),
)