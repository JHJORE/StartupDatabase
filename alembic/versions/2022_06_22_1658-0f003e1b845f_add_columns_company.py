"""add columns company

Revision ID: 0f003e1b845f
Revises: a5f9992d6ee9
Create Date: 2022-06-22 16:58:59.634140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f003e1b845f'
down_revision = 'a5f9992d6ee9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("Company", sa.Column("Description", sa.String))
    op.add_column("Company", sa.Column("Employees", sa.Integer))
    op.add_column("Company", sa.Column("Municipality", sa.String))


def downgrade() -> None:
    op.drop_column("Company", "Description")
    op.drop_column("Company", "Employees")
    op.drop_column("Company", "Municipality")
