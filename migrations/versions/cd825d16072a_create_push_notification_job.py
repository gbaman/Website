"""create_push_notification_job

Revision ID: cd825d16072a
Revises: 1418c5eca608
Create Date: 2024-04-15 20:10:24.975271

"""

# revision identifiers, used by Alembic.
revision = "cd825d16072a"
down_revision = "1418c5eca608"

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "push_notification_job",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("target_id", sa.Integer(), nullable=False),
        sa.Column("created", sa.DateTime(), nullable=False),
        sa.Column("state", sa.String(), nullable=False),
        sa.Column("not_before", sa.DateTime(), nullable=True),
        sa.Column("related_to", sa.String(), nullable=True),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("body", sa.String(), nullable=True),
        sa.Column("error", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_push_notification_job")),
        sa.ForeignKeyConstraint(
            ["target_id"],
            ["web_push_target.id"],
            name=op.f("fk_push_notification_job_target_id_web_push_target_id"),
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("push_notification_job")
    # ### end Alembic commands ###
