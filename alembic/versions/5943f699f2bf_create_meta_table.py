"""Create meta table.

Revision ID: 5943f699f2bf
Revises: 
Create Date: 2022-10-23 13:20:09.948796

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import OID, UUID, BIT
import uuid

# revision identifiers, used by Alembic.
revision = '5943f699f2bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
  op.create_table(
      "meta",
      sa.Column(
          'id',
          UUID(as_uuid=True),
          sa.Identity(),
          primary_key=True,
          default=uuid.uuid4),
      sa.Column('meta', sa.JSON),
      sa.Column('origin_url', sa.String),
  )


def downgrade() -> None:
  op.drop_table("meta")
