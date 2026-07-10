import os
import tempfile
from pathlib import Path

from atlas.storage.database import init_db


def test_init_db_creates_database_and_tables():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "atlas-test.db"
        os.environ["DATABASE_PATH"] = str(db_path)
        os.environ["ANGEL_API_KEY"] = "demo-key"
        os.environ["ANGEL_CLIENT_ID"] = "demo-client"
        os.environ["LOG_LEVEL"] = "INFO"

        init_db()

        assert db_path.exists()
        assert db_path.stat().st_size >= 0
