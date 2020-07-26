import sqlalchemy as sa
from data.models.users_to_chats import users_to_chats as utc
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Chats(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'chats'
    __table_args__ = {'extend_existing': True}

    id = sa.Column('id', sa.Integer, autoincrement=True, primary_key=True)
    name = sa.Column('name', sa.String, nullable=True)
    status = sa.Column('status', sa.String, nullable=True)
    author = sa.Column('author', sa.Integer, sa.ForeignKey("users.id"), nullable=True)

    authors = sa.orm.relation("Users", foreign_keys=[author])
    users = sa.orm.relation("Users", secondary=utc)
    chats_invitations = sa.orm.relation("ChatsInv")
    chats_messages = sa.orm.relation("ChatsMessages")

