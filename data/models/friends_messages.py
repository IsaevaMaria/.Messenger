import sqlalchemy as sa
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class ChatsMessages(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'chats_messages'
    __table_args__ = {'extend_existing': True}

    id = sa.Column('id', sa.Integer, autoincrement=True, primary_key=True)
    id_user_from = sa.Column('id_user_from', sa.Integer, sa.ForeignKey("users.id"), nullable=True)
    id_user_to = sa.Column('id_user_to', sa.Integer, sa.ForeignKey("users.id"), nullable=True)
    id_message = sa.Column('id_message', sa.Integer, sa.ForeignKey("messages.id"), nullable=True)

    users = sa.orm.relation("Users", foreign_keys=[id_user_from, id_user_to])
    messages = sa.orm.relation("Messages", foreign_keys=[id_message])