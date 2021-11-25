"""create districts table

Revision ID: 07542475d335
Revises: d855d1c627b4
Create Date: 2021-11-24 19:41:41.703096

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import ForeignKey


# revision identifiers, used by Alembic.
revision = '07542475d335'
down_revision = 'd855d1c627b4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'districts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(150), nullable=False),
        sa.Column('town_id', sa.Integer, ForeignKey('towns.id')),
    )


def downgrade():
    op.drop_table('districts')
