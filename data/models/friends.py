import sqlalchemy as sa
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Friends(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'friends'
    __table_args__ = {'extend_existing': True}

    id = sa.Column('id', sa.Integer, autoincrement=True, primary_key=True)
    id_first_user = sa.Column('id_first_user', sa.Integer)
    id_second_user = sa.Column('id_second_user', sa.Integer)
