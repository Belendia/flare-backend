"""empty message

Revision ID: 8d54b47fb850
Revises: 
Create Date: 2020-04-19 21:59:16.091133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d54b47fb850'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('model_om_child')
    op.drop_table('gender')
    op.drop_table('contact')
    op.drop_table('model_om_parent')
    op.drop_table('contact_group')
    op.create_unique_constraint(None, 'language', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'language', type_='unique')
    op.create_table('contact_group',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('model_om_parent',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('field_string', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('field_string')
    )
    op.create_table('contact',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), nullable=False),
    sa.Column('address', sa.VARCHAR(length=564), nullable=True),
    sa.Column('birthday', sa.DATE(), nullable=True),
    sa.Column('personal_phone', sa.VARCHAR(length=20), nullable=True),
    sa.Column('personal_celphone', sa.VARCHAR(length=20), nullable=True),
    sa.Column('contact_group_id', sa.INTEGER(), nullable=False),
    sa.Column('gender_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['contact_group_id'], ['contact_group.id'], ),
    sa.ForeignKeyConstraint(['gender_id'], ['gender.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('gender',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('model_om_child',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('field_string', sa.VARCHAR(length=50), nullable=False),
    sa.Column('parent_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['model_om_parent.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('field_string')
    )
    # ### end Alembic commands ###