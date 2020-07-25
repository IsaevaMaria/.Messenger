import sqlalchemy as sa
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Messages(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'messages'
    __table_args__ = {'extend_existing': True}

    id = sa.Column('id', sa.Integer, autoincrement=True, primary_key=True)
    text = sa.Column('text', sa.String, nullable=True)
    date = sa.Column('date', sa.DateTime, nullable=True)

    friends_messages = sa.orm.relation("FriendsMessages")