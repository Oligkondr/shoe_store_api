"""test revision 2

Revision ID: 9db5b2bd38ee
Revises: 9161419b01ff
Create Date: 2025-04-29 13:06:42.011536

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9db5b2bd38ee'
down_revision: Union[str, None] = '9161419b01ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('admins', 'surname',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('admins', 'surname',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
