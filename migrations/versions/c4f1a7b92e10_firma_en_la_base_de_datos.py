"""la firma de entrega se guarda en la base de datos (columna packages.signature)

Revision ID: c4f1a7b92e10
Revises: 9d15f59ec52b
Create Date: 2026-11-15 20:30:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


# revision identifiers, used by Alembic.
revision = 'c4f1a7b92e10'
down_revision = '9d15f59ec52b'
branch_labels = None
depends_on = None


def upgrade():
    # MEDIUMBLOB en MySQL (un BLOB normal solo aguanta 64 KB); en SQLite es un BLOB común
    with op.batch_alter_table('packages', schema=None) as batch_op:
        batch_op.add_column(sa.Column(
            'signature', sa.LargeBinary().with_variant(mysql.MEDIUMBLOB(), 'mysql'), nullable=True
        ))


def downgrade():
    with op.batch_alter_table('packages', schema=None) as batch_op:
        batch_op.drop_column('signature')
