"""Module to hold `User` model definition."""
import ormar

from app.db import MainMeta


class User(ormar.Model):
    """Schema for the `User` model."""

    class Meta(MainMeta):
        """Extend the MainMeta."""

    id = ormar.Integer(primary_key=True)
    full_name = ormar.String(max_length=255)
    email = ormar.String(max_length=255)
    hashed_password = ormar.String(nullable=False, max_length=255)
    is_active = ormar.Boolean(default=True)
    is_superuser = ormar.Boolean(default=False)
