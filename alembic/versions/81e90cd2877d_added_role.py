"""Added role

Revision ID: 81e90cd2877d
Revises: ef090ee774e9
Create Date: 2024-09-26 16:43:13.650891

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '81e90cd2877d'
down_revision: Union[str, None] = 'ef090ee774e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
                    sa.Column('sid', sa.Uuid(), nullable=False),
                    sa.Column('name', sa.VARCHAR(length=225), nullable=False, comment='name of role'),
                    sa.Column('created', sa.DateTime(timezone=True), nullable=False),
                    sa.Column('updated', sa.DateTime(timezone=True), nullable=False),
                    sa.PrimaryKeyConstraint('sid'),
                    sa.UniqueConstraint('sid'),
                    schema='security'
                    )
    op.create_index(op.f('ix_security_role_name'), 'role', ['name'], unique=True, schema='security')
    op.add_column('user', sa.Column('role_sid', sa.Uuid(), nullable=False), schema='users')
    op.add_column('user', sa.Column('img', sa.String(), nullable=False), schema='users')
    op.create_foreign_key(None, 'user', 'role', ['role_sid'], ['sid'], source_schema='users',
                          referent_schema='security', ondelete='RESTRICT')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("user_role_sid_fkey", 'user', schema='users', type_='foreignkey')
    op.drop_column('user', 'img', schema='users')
    op.drop_column('user', 'role_sid', schema='users')
    op.drop_index(op.f('ix_security_role_name'), table_name='role', schema='security')
    op.drop_table('role', schema='security')
    # ### end Alembic commands ###