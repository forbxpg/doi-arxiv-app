"""Test datetime."""

from datetime import datetime, timedelta
from core.database.models.base import get_current_tz_info


def test_get_current_tz_info():
    """Test get current timezone info."""
    tz = get_current_tz_info()
    dt = datetime.now()
    assert tz.tzname(dt) == "Europe/Moscow"
    assert tz.utcoffset(dt) == timedelta(hours=3)
