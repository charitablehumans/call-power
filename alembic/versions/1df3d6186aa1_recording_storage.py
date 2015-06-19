"""recording_storage

Revision ID: 1df3d6186aa1
Revises: 35545845a94c
Create Date: 2015-06-18 15:37:52.781203

"""

# revision identifiers, used by Alembic.
revision = '1df3d6186aa1'
down_revision = '35545845a94c'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

from flask.ext import store


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campaign_recording', schema=None) as batch_op:
        batch_op.add_column(sa.Column('file_storage', store.sqla.FlaskStoreType(length=256), nullable=True))

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('campaign_recording', schema=None) as batch_op:
        batch_op.drop_column('file_storage')

    ### end Alembic commands ###