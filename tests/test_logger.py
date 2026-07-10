from atlas.utils.logger import get_logger


def test_get_logger_returns_logger_with_name():
    logger = get_logger(__name__)

    assert logger is not None
