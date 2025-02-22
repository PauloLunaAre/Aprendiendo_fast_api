"""Eliminar columna estado2

Revision ID: 9fe583aac070
Revises: e2dc8ed83058
Create Date: 2024-07-04 09:59:23.816858

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9fe583aac070'
down_revision: Union[str, None] = 'e2dc8ed83058'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'estado2')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('estado2', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
