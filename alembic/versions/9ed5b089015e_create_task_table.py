"""Create task table.

Revision ID: 9ed5b089015e
Revises: 5943f699f2bf
Create Date: 2022-10-23 13:20:18.034548

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import OID, UUID, BIT, ENUM

# revision identifiers, used by Alembic.
revision = '9ed5b089015e'
down_revision = '5943f699f2bf'
branch_labels = None
depends_on = None


def upgrade() -> None:
  op.create_table(
      "task",
      sa.Column(
          'id',
          sa.Integer,
          sa.Identity(cycle=True, always=True),
          primary_key=True),
      sa.Column('meta_id', UUID),
      sa.Column('processer', sa.String),
      sa.Column('params', sa.String),
      sa.Column(
          'status',
          ENUM('created', 'processing', 'done', 'failed', name="task_status")),
      sa.Column('CreatedAt', sa.DATETIME),
      sa.Column('UpdatedAt', sa.DATETIME),
  )


def downgrade() -> None:
  op.drop_table("task")
