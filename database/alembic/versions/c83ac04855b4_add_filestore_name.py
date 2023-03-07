"""Add filestore name

Revision ID: c83ac04855b4
Revises: 77022369cea4
Create Date: 2020-08-11 16:31:36.089779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c83ac04855b4'
down_revision = '77022369cea4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('experiment', sa.Column(
        'experiment_filestore', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('experiment', 'experiment_filestore')
    # ### end Alembic commands ###
