"""create towns table

Revision ID: d855d1c627b4
Revises: 0baa2def3f36
Create Date: 2021-11-24 19:36:39.248741

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import ForeignKey


# revision identifiers, used by Alembic.
revision = 'd855d1c627b4'
down_revision = '0baa2def3f36'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'towns',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(150), nullable=False),
        sa.Column('department_id', sa.Integer, ForeignKey('departments.id')),
    )


def downgrade():
    op.drop_table('towns')
