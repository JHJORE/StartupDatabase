"""add column HomePage to Company

Revision ID: 8df54f99c2ba
Revises: 
Create Date: 2022-06-23 13:50:34.320878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8df54f99c2ba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("Company", sa.Column("HomePage", sa.String))


def downgrade() -> None:
    op.drop_column("Company", "HomePage")
