import sqlalchemy as sa
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class ChatsMessagesFromUsers(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'chats_messages_from_users'
    __table_args__ = {'extend_existing': True}

    id = sa.Column('id', sa.Integer, autoincrement=True, primary_key=True)
    id_user = sa.Column('id_user', sa.Integer, sa.ForeignKey("users.id"), nullable=True)
    id_message = sa.Column('id_message', sa.Integer, sa.ForeignKey("chats_messages.id"), nullable=True)

    users = sa.orm.relation("Users", foreign_keys=[id_user])
    chats_messages = sa.orm.relation("ChatsMessages", foreign_keys=[id_message])