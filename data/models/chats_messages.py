import sqlalchemy as sa
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class ChatsMessages(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'chats_messages'
    __table_args__ = {'extend_existing': True}

    id = sa.Column('id', sa.Integer, autoincrement=True, primary_key=True)
    id_chat = sa.Column('id_chat', sa.Integer, sa.ForeignKey("chats.id"), nullable=True)
    text = sa.Column('text', sa.String, nullable=True)
    date = sa.Column('date', sa.DateTime, nullable=True)

    chats = sa.orm.relation("Chats", foreign_keys=[id_chat])
    chats_messages_from_users = sa.orm.relation("ChatsMessagesFromUsers")