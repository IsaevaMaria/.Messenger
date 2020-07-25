import sqlalchemy as sa
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class FriendsMessages(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'friends_messages'
    __table_args__ = {'extend_existing': True}

    id = sa.Column('id', sa.Integer, autoincrement=True, primary_key=True)
    id_user_from = sa.Column('id_user_from', sa.Integer)
    id_user_to = sa.Column('id_user_to', sa.Integer)
    id_message = sa.Column('id_message', sa.Integer, sa.ForeignKey("messages.id"), nullable=True)
    messages = sa.orm.relation("Messages", foreign_keys=[id_message])