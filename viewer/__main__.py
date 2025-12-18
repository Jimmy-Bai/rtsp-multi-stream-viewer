import logging
from viewer.app.log import configure_logger

def main() -> None:
    configure_logger()

    logger = logging.getLogger("viewer")
    logger.info("TEST")

if __name__ == "__main__":
    main()