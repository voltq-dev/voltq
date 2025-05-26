import logging

import pytest
from src.voltq.logger import logger, set_level


@pytest.fixture(scope="module")
def caplog_fixture(caplog) -> logging.Logger:
    """Fixture to capture log messages during tests."""
    logger.addHandler(caplog.handler)
    logger.setLevel(logging.DEBUG)
    yield caplog
    logger.removeHandler(caplog.handler)


def test_logger_name():
    """Test that the logger has the correct name."""
    # Arrange
    expected_name = "voltq"

    # Act

    # Assert
    assert expected_name == logger.name, "Logger name should be 'voltq'."


def test_default_level_and_handler():
    """Test that the logger has the default level and a handler."""
    # Arrange
    expected_level = logging.INFO
    expected_handler_type = logging.StreamHandler
    expected_handlers_count = 1
    # Act

    # Assert
    assert expected_level == logger.level, "Logger level should be set to INFO."
    assert expected_handlers_count == len(
        logger.handlers
    ), "Logger should have one handler."
    assert isinstance(
        logger.handlers[0], expected_handler_type
    ), "Logger handler should be a StreamHandler."


def test_set_level():
    """Test setting the logging level."""
    # Arrange
    log_level = logging.DEBUG
    expected_level = log_level

    # Act
    set_level(log_level)

    # Assert
    assert expected_level == logger.level, "Logger level should be set to DEBUG."


def test_log_output_info(caplog):
    """Test that INFO messages are logged."""
    # Arrange
    message = "This is an info message."
    expected_level = logging.INFO

    # Act
    logger.info(message)

    # Assert
    assert message in caplog.text
    assert expected_level == caplog.records[0].levelno, "Log level should be INFO."


def test_log_output_debug_not_shown_at_info_level(caplog):
    """Test that DEBUG messages are not logged at INFO level."""
    # Arrange
    message = "This is a debug message."
    set_level(logging.INFO)
    # Act
    logger.debug(message)

    # Assert
    assert (
        message not in caplog.text
    ), "DEBUG messages should not be shown at INFO level."
