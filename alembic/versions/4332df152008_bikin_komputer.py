"""bikin komputer

Revision ID: 4332df152008
Revises: 
Create Date: 2023-12-23 18:50:44.723736

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4332df152008"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "komputer",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("image_url", sa.String(length=255), nullable=False),
        sa.Column("stock", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.bulk_insert(
        sa.table(
            "komputer",
            sa.column("name", sa.String),
            sa.column("description", sa.String),
            sa.column("price", sa.Integer),
            sa.column("image_url", sa.String),
            sa.column("stock", sa.Integer),
        ),
        [
            {
                "name": "Laptop ASUS ZenBook 14",
                "description": "Laptop tipis dan ringan dengan layar 14 inci, prosesor Intel Core i7, dan RAM 16GB.",
                "price": 12000000,
                "image_url": "https://example.com/images/asus-zenbook-14-laptop.jpg",
                "stock": 15,
            },
            {
                "name": "Desktop PC HP Pavilion",
                "description": "Komputer desktop dengan prosesor AMD Ryzen 7, grafis NVIDIA GeForce GTX, dan RAM 32GB.",
                "price": 15000000,
                "image_url": "https://example.com/images/hp-pavilion-desktop-pc.jpg",
                "stock": 10,
            },
            {
                "name": "Laptop Apple MacBook Pro 16",
                "description": "Laptop dengan layar 16 inci, prosesor M1 Pro, dan penyimpanan 512GB.",
                "price": 25000000,
                "image_url": "https://example.com/images/macbook-pro-16-laptop.jpg",
                "stock": 8,
            },
            {
                "name": "All-in-One PC Dell Inspiron 27",
                "description": "Komputer all-in-one dengan layar sentuh 27 inci, prosesor Intel Core i5, dan RAM 8GB.",
                "price": 18000000,
                "image_url": "https://example.com/images/dell-inspiron-27-all-in-one-pc.jpg",
                "stock": 12,
            },
            {
                "name": "Laptop Lenovo ThinkPad X1 Carbon",
                "description": "Laptop bisnis dengan layar 14 inci, prosesor Intel Core i5, dan penyimpanan 256GB.",
                "price": 16000000,
                "image_url": "https://example.com/images/lenovo-thinkpad-x1-carbon-laptop.jpg",
                "stock": 20,
            },
            {
                "name": "Mini PC Intel NUC",
                "description": "Mini PC dengan prosesor Intel Core i3, RAM 8GB, dan penyimpanan SSD 256GB.",
                "price": 6000000,
                "image_url": "https://example.com/images/intel-nuc-mini-pc.jpg",
                "stock": 25,
            },
            {
                "name": "Laptop MSI GS66 Stealth",
                "description": "Laptop gaming dengan layar 15 inci, prosesor Intel Core i9, grafis NVIDIA RTX 3080, dan RAM 32GB.",
                "price": 30000000,
                "image_url": "https://example.com/images/msi-gs66-stealth-laptop.jpg",
                "stock": 5,
            },
            {
                "name": "Desktop PC Acer Aspire TC",
                "description": "Komputer desktop dengan prosesor Intel Core i7, grafis Intel UHD Graphics, dan RAM 16GB.",
                "price": 13000000,
                "image_url": "https://example.com/images/acer-aspire-tc-desktop-pc.jpg",
                "stock": 18,
            },
            {
                "name": "Laptop Dell XPS 13",
                "description": "Laptop dengan layar 13 inci, prosesor Intel Core i7, dan penyimpanan SSD 512GB.",
                "price": 19000000,
                "image_url": "https://example.com/images/dell-xps-13-laptop.jpg",
                "stock": 14,
            },
            {
                "name": "Gaming PC CyberPowerPC Gamer Xtreme",
                "description": "Komputer gaming dengan prosesor Intel Core i5, grafis NVIDIA GeForce RTX 3060, dan RAM 16GB.",
                "price": 22000000,
                "image_url": "https://example.com/images/cyberpowerpc-gamer-xtreme-gaming-pc.jpg",
                "stock": 7,
            },
        ],
    )


def downgrade() -> None:
    op.execute("DELETE FROM komputer")
    op.drop_table("komputer")
