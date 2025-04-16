import logging
import sys
from typing import Optional


class Logger:
    def __init__(
        self,
        name: str = "ml-batch-jobs",
        level: int = logging.INFO,
        log_file: Optional[str] = None,
    ):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.propagate = False  # Avoid duplicate logs

        # Avoid adding handlers multiple times
        if not self.logger.handlers:
            formatter = logging.Formatter(
                fmt="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )

            # Console handler
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

            # Optional file handler
            if log_file:
                file_handler = logging.FileHandler(log_file)
                file_handler.setFormatter(formatter)
                self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger
