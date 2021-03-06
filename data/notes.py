import sqlalchemy
from .db_session import SqlAlchemyBase


class Note(SqlAlchemyBase):
    __tablename__ = 'Notes'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    text = sqlalchemy.Column(sqlalchemy.TEXT, nullable=True)
