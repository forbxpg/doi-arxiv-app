"""Base model."""

from datetime import datetime, timedelta, timezone

from sqlalchemy import DateTime, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


def get_current_tz_info(tz_name: str = "Europe/Moscow"):
    """Get timezone info for specified timezone."""
    return timezone(
        offset=timedelta(hours=3),
        name=tz_name,
    )


def get_moscow_time():
    """Get current time in Moscow timezone."""
    return datetime.now(tz=get_current_tz_info())


class Base(DeclarativeBase):
    """Base model."""

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=get_moscow_time,
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=get_moscow_time,
        onupdate=get_moscow_time,
        nullable=False,
    )
