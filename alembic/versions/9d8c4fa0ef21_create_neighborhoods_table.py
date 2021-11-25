"""create neighborhoods table

Revision ID: 9d8c4fa0ef21
Revises: 07542475d335
Create Date: 2021-11-24 19:42:52.426889

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import ForeignKey


# revision identifiers, used by Alembic.
revision = '9d8c4fa0ef21'
down_revision = '07542475d335'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'neighborhoods',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(150), nullable=False),
        sa.Column('district_id', sa.Integer, ForeignKey('districts.id')),
    )


def downgrade():
    op.drop_table('neighborhoods')
