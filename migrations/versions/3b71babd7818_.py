"""empty message

Revision ID: 3b71babd7818
Revises: c2241c54779a
Create Date: 2023-11-29 11:17:50.220539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b71babd7818'
down_revision = 'c2241c54779a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('release_date', sa.String(length=20), nullable=True),
    sa.Column('popularity', sa.Float(), nullable=True),
    sa.Column('vote_count', sa.Integer(), nullable=True),
    sa.Column('vote_average', sa.Float(), nullable=True),
    sa.Column('overview', sa.Text(), nullable=True),
    sa.Column('poster_path', sa.String(length=255), nullable=True),
    sa.Column('genre_ids', sa.String(length=255), nullable=True),
    sa.Column('adult', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('movie_ko')
    op.drop_table('movie_en')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie_en',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), nullable=False),
    sa.Column('release_date', sa.VARCHAR(length=20), nullable=True),
    sa.Column('popularity', sa.FLOAT(), nullable=True),
    sa.Column('vote_count', sa.INTEGER(), nullable=True),
    sa.Column('vote_average', sa.FLOAT(), nullable=True),
    sa.Column('overview', sa.TEXT(), nullable=True),
    sa.Column('poster_path', sa.VARCHAR(length=255), nullable=True),
    sa.Column('genre_ids', sa.VARCHAR(length=255), nullable=True),
    sa.Column('adult', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie_ko',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), nullable=False),
    sa.Column('release_date', sa.VARCHAR(length=20), nullable=True),
    sa.Column('popularity', sa.FLOAT(), nullable=True),
    sa.Column('vote_count', sa.INTEGER(), nullable=True),
    sa.Column('vote_average', sa.FLOAT(), nullable=True),
    sa.Column('overview', sa.TEXT(), nullable=True),
    sa.Column('poster_path', sa.VARCHAR(length=255), nullable=True),
    sa.Column('genre_ids', sa.VARCHAR(length=255), nullable=True),
    sa.Column('adult', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('movie')
    # ### end Alembic commands ###
