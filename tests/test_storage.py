from atlas.storage.database import init_db


def test_init_db_creates_database_and_tables(monkeypatch, tmp_path):
    db_path = tmp_path / "atlas-test.db"
    monkeypatch.setenv("DATABASE_PATH", str(db_path))
    monkeypatch.setenv("ANGEL_API_KEY", "demo-key")
    monkeypatch.setenv("ANGEL_CLIENT_ID", "demo-client")
    monkeypatch.setenv("LOG_LEVEL", "INFO")

    init_db()

    assert db_path.exists()
    assert db_path.stat().st_size >= 0
