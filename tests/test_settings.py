import os

from atlas.config.settings import Settings, load_settings


def test_load_settings_accepts_required_values(monkeypatch):
    monkeypatch.setenv("ANGEL_API_KEY", "demo-key")
    monkeypatch.setenv("ANGEL_CLIENT_ID", "demo-client")
    monkeypatch.setenv("DATABASE_PATH", "data/atlas.db")
    monkeypatch.setenv("LOG_LEVEL", "INFO")

    settings = load_settings(os.environ)

    assert isinstance(settings, Settings)
    assert settings.angel_api_key == "demo-key"
    assert settings.angel_client_id == "demo-client"
    assert settings.database_path == "data/atlas.db"
    assert settings.log_level == "INFO"


def test_load_settings_requires_all_values(monkeypatch):
    monkeypatch.delenv("ANGEL_API_KEY", raising=False)
    monkeypatch.delenv("ANGEL_CLIENT_ID", raising=False)
    monkeypatch.delenv("DATABASE_PATH", raising=False)
    monkeypatch.delenv("LOG_LEVEL", raising=False)
    monkeypatch.setenv("ANGEL_API_KEY", "demo-key")
    monkeypatch.setenv("ANGEL_CLIENT_ID", "demo-client")
    monkeypatch.setenv("DATABASE_PATH", "data/atlas.db")

    try:
        load_settings(os.environ)
    except ValueError as exc:
        assert "LOG_LEVEL" in str(exc)
    else:
        raise AssertionError("Expected ValueError for missing LOG_LEVEL")
