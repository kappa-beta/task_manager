"""Update 'time_log' table

Revision ID: 156538929fec
Revises: 
Create Date: 2022-03-02 16:30:48.127566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '156538929fec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('header', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('plan_start', sa.Date(), nullable=True),
    sa.Column('plan_end', sa.Date(), nullable=True),
    sa.Column('executors', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('time_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time_log_id', sa.Integer(), nullable=False),
    sa.Column('start', sa.Date(), nullable=False),
    sa.Column('end', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['time_log_id'], ['task.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('time_log')
    op.drop_table('task')
    op.drop_table('accounts')
    # ### end Alembic commands ###