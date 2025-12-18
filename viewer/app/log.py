import logging
import sys

LOG_FORMATTER: logging.Formatter = logging.Formatter(
    "[%(asctime)s] %(name)-30s %(levelname)-8s: %(message)s",
    "%Y-%m-%d %H:%M:%S",
)


def configure_logger():
    console_handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(LOG_FORMATTER)

    logger = logging.getLogger("viewer")
    logger.propagate = False
    logger.setLevel(logging.DEBUG)

    logger.addHandler(console_handler)
