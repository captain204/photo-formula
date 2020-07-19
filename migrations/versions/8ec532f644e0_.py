"""empty message

Revision ID: 8ec532f644e0
Revises: 0599c36df7c0
Create Date: 2020-07-17 18:18:04.360508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ec532f644e0'
down_revision = '0599c36df7c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_contacts_email', table_name='contacts')
    op.create_index(op.f('ix_contacts_email'), 'contacts', ['email'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contacts_email'), table_name='contacts')
    op.create_index('ix_contacts_email', 'contacts', ['email'], unique=1)
    # ### end Alembic commands ###
