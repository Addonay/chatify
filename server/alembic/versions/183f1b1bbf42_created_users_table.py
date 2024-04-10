"""created users table

Revision ID: 183f1b1bbf42
Revises: 
Create Date: 2024-04-10 12:22:45.264946

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '183f1b1bbf42'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('username', sa.String()),
        sa.Column('email', sa.String(), nullable=False, unique=True),
        sa.Column('password', sa.String()),
        sa.Column('profile_image', sa.String(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('users')
