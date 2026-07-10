from config.settings import Settings, load_settings


def test_load_settings_accepts_required_values():
    env = {
        "ANGEL_API_KEY": "demo-key",
        "ANGEL_CLIENT_ID": "demo-client",
        "DATABASE_PATH": "data/atlas.db",
        "LOG_LEVEL": "INFO",
    }

    settings = load_settings(env)

    assert isinstance(settings, Settings)
    assert settings.angel_api_key == "demo-key"
    assert settings.angel_client_id == "demo-client"
    assert settings.database_path == "data/atlas.db"
    assert settings.log_level == "INFO"


def test_load_settings_requires_all_values():
    env = {
        "ANGEL_API_KEY": "demo-key",
        "ANGEL_CLIENT_ID": "demo-client",
        "DATABASE_PATH": "data/atlas.db",
    }

    try:
        load_settings(env)
    except ValueError as exc:
        assert "LOG_LEVEL" in str(exc)
    else:
        raise AssertionError("Expected ValueError for missing LOG_LEVEL")
