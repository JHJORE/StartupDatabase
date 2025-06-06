"""added givendate to aid

Revision ID: 44f1fa7c8d37
Revises: 8df54f99c2ba
Create Date: 2022-06-24 10:36:21.062319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44f1fa7c8d37'
down_revision = '8df54f99c2ba'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Aid', sa.Column('DateGiven', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Aid', 'DateGiven')
    # ### end Alembic commands ###
