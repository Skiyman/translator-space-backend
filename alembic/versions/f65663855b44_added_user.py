"""Added user

Revision ID: f65663855b44
Revises: 
Create Date: 2024-09-26 12:53:05.706879

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f65663855b44'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('sid', sa.Uuid(), nullable=False),
    sa.Column('name', sa.String(), nullable=False, comment='name of user'),
    sa.Column('middle_name', sa.String(), nullable=False, comment='middle name of user'),
    sa.Column('last_name', sa.String(), nullable=False, comment='last name of user'),
    sa.Column('email', sa.String(), nullable=False, comment='email'),
    sa.Column('phone', sa.String(), nullable=True, comment='phone'),
    sa.Column('hashed_password', sa.String(), nullable=False, comment='password'),
    sa.Column('last_activity', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('sid'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('sid'),
    schema='users'
    )
    op.create_index(op.f('ix_users_user_email'), 'user', ['email'], unique=True, schema='users')
    op.create_index(op.f('ix_users_user_name'), 'user', ['name'], unique=False, schema='users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_user_name'), table_name='user', schema='users')
    op.drop_index(op.f('ix_users_user_email'), table_name='user', schema='users')
    op.drop_table('user', schema='users')
    # ### end Alembic commands ###
