import io
import logging
from contextlib import redirect_stdout

from kernel.utils.logger import Logger


def test_logger_creation_defaults():
    logger_instance = Logger()
    logger = logger_instance.get_logger()

    assert isinstance(logger, logging.Logger)
    assert logger.name == "ml-batch-jobs"
    assert logger.level == logging.INFO
    assert not logger.propagate
    assert any(isinstance(h, logging.StreamHandler) for h in logger.handlers)


def test_logger_output_to_stdout():
    logger_instance = Logger(name="test-logger")
    logger = logger_instance.get_logger()

    f = io.StringIO()
    with redirect_stdout(f):
        logger.info("hello world")


def test_logger_with_log_file(tmp_path):
    log_file_path = tmp_path / "test_log.log"
    logger_instance = Logger(name="file-logger", log_file=str(log_file_path))
    logger = logger_instance.get_logger()

    logger.warning("written to file")

    # Read back the file to ensure the log was written
    with open(log_file_path, "r") as f:
        content = f.read()
        assert "written to file" in content
        assert "file-logger" in content
        assert "WARNING" in content
