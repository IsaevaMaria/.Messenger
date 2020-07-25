import sqlalchemy as sa
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class UsersToChats(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'users_to_chats'
    __table_args__ = {'extend_existing': True}

    id = sa.Column('id', sa.Integer, autoincrement=True, primary_key=True)
    id_user = sa.Column('id_user', sa.Integer, sa.ForeignKey("users.id"), nullable=True)
    id_chat = sa.Column('id_chat', sa.Integer, sa.ForeignKey("chats.id"), nullable=True)

    users = sa.orm.relation("Users", foreign_keys=[id_user])
    chats = sa.orm.relation("Chats", foreign_keys=[id_chat])