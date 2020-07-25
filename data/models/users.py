import sqlalchemy as sa
from data.db_session import SqlAlchemyBase
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin


class Users(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = sa.Column('id', sa.Integer, autoincrement=True, primary_key=True)
    name = sa.Column('name', sa.String, nullable=True)
    email = sa.Column('email', sa.String, nullable=True, unique=True)
    status = sa.Column('status', sa.String, nullable=True)
    about = sa.Column('about', sa.String, nullable=True)
    password = sa.Column('hashed_password', sa.String, nullable=True)

    friends = sa.orm.relation('Friends')
    friends_invitations = sa.orm.relation('FriendsInv')
    users_to_chats = sa.orm.relation('UsersToChats')
    chats_invitations = sa.orm.relation('ChatsInv')
    friends_messages = sa.orm.relation('FriendsMessages')
    chats_messages_from_users = sa.orm.relation('ChatsMessagesFromUsers')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
