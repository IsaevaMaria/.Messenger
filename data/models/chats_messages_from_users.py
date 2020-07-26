import sqlalchemy as sa
from data.db_session import SqlAlchemyBase

chats_messages_from_users = sa.Table('chats_messages_from_users',
                                     SqlAlchemyBase.metadata,
                                     sa.Column('id_user', sa.Integer, sa.ForeignKey("users.id"), nullable=True),
                                     sa.Column('id_message', sa.Integer, sa.ForeignKey("chats_messages.id"), nullable=True)
                                    )