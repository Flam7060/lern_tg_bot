import logging
import sys


def setup_logging(level: int = logging.INFO) -> None:
    """Единая настройка логирования для всего приложения."""
    logging.basicConfig(
        level=level,
        stream=sys.stdout,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    )
