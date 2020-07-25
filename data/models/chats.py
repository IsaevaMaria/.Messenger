import sqlalchemy as sa
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Chats(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'chats'
    __table_args__ = {'extend_existing': True}

    id = sa.Column('id', sa.Integer, autoincrement=True, primary_key=True)
    name = sa.Column('name', sa.String, nullable=True)
    status = sa.Column('status', sa.String, nullable=True)
    author = sa.Column('author', sa.Integer, sa.ForeignKey("users.id"), nullable=True)

    users = sa.orm.relation("Users", foreign_keys=[author])
    chats_invitations = sa.orm.relation("ChatsInv")
    users_to_chats = sa.orm.relation("UsersToChats")
    chats_messages = sa.orm.relation("ChatsMessages")

