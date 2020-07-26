import sqlalchemy as sa
from data.db_session import SqlAlchemyBase

users_to_chats = sa.Table('users_to_chats',
                          SqlAlchemyBase.metadata,
                          sa.Column('id_user', sa.Integer, sa.ForeignKey("users.id"), nullable=True),
                          sa.Column('id_chat', sa.Integer, sa.ForeignKey("chats.id"), nullable=True)
                        )