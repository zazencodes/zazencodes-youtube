import logging
from pathlib import Path


def get_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s;%(levelname)s;%(message)s",
    )
    logger = logging.getLogger(Path().resolve().parent.parent.name)
    return logger
