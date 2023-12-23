"""bikin buku

Revision ID: c22cdf2ac5f8
Revises: 1c0d8efc78e8
Create Date: 2023-12-23 18:28:52.479496

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c22cdf2ac5f8"
down_revision: Union[str, None] = "1c0d8efc78e8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(
        sa.Table(
            "buku",
            sa.MetaData(),
            sa.Column("name", sa.String(length=255), nullable=False),
            sa.Column("description", sa.Text(), nullable=False),
            sa.Column("price", sa.Integer(), nullable=False),
            sa.Column("image_url", sa.String(length=255), nullable=False),
            sa.Column("stock", sa.Integer(), nullable=False),
        ),
        [
            {
                "name": "Sapiens: A Brief History of Humankind",
                "description": "A groundbreaking narrative of humanity's creation and evolution.",
                "price": 200000,
                "image_url": "https://example.com/images/sapiens-book.jpg",
                "stock": 20,
            },
            {
                "name": "The Subtle Art of Not Giving a F*ck",
                "description": "A counterintuitive approach to living a good life.",
                "price": 180000,
                "image_url": "https://example.com/images/subtle-art-book.jpg",
                "stock": 30,
            },
            {
                "name": "Educated",
                "description": "A memoir about the author's journey from survival to the pursuit of knowledge.",
                "price": 220000,
                "image_url": "https://example.com/images/educated-book.jpg",
                "stock": 25,
            },
            {
                "name": "Becoming",
                "description": "Michelle Obama's memoir reflecting on her experiences, hopes, and achievements.",
                "price": 250000,
                "image_url": "https://example.com/images/becoming-book.jpg",
                "stock": 18,
            },
            {
                "name": "Atomic Habits",
                "description": "A guide on how tiny changes can lead to remarkable results.",
                "price": 190000,
                "image_url": "https://example.com/images/atomic-habits-book.jpg",
                "stock": 22,
            },
            {
                "name": "Where the Crawdads Sing",
                "description": "A novel about love, mystery, and the natural world.",
                "price": 210000,
                "image_url": "https://example.com/images/crawdads-book.jpg",
                "stock": 27,
            },
            {
                "name": "The Alchemist",
                "description": "A philosophical novel about finding one's destiny.",
                "price": 150000,
                "image_url": "https://example.com/images/alchemist-book.jpg",
                "stock": 35,
            },
            {
                "name": "The Silent Patient",
                "description": "A psychological thriller about a woman's act of violence and her silence.",
                "price": 240000,
                "image_url": "https://example.com/images/silent-patient-book.jpg",
                "stock": 15,
            },
            {
                "name": "Thinking, Fast and Slow",
                "description": "A book that offers insights into how the mind works and makes decisions.",
                "price": 230000,
                "image_url": "https://example.com/images/thinking-fast-slow-book.jpg",
                "stock": 20,
            },
            {
                "name": "The Power of Habit",
                "description": "Exploring the science behind why habits exist and how they can be changed.",
                "price": 200000,
                "image_url": "https://example.com/images/power-of-habit-book.jpg",
                "stock": 28,
            },
        ],
    )


def downgrade() -> None:
    op.execute("DELETE FROM buku")
