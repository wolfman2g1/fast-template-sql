import os

LOGGER_NAME: str = "Breeze"
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
ROOT_LOG_LEVEL = os.getenv("ROOT_LOG_LEVEL", "INFO")
LOGGING_CONFIG = {
    "version": 1,
    "formatters": {"standard": {"format": "[%(asctime)s] {%(name)s:%(lineno)d} %(levelname)s - %(message)s"}},
    "handlers": {
        "all_std_out": {
            "level": LOG_LEVEL,
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout"
        },
        "console": {
            "level": ROOT_LOG_LEVEL,
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "": {"handlers": ["all_std_out"], "level": ROOT_LOG_LEVEL,"propagate": False},
        "uvicorn": {"handlers": ["all_std_out"], "level": ROOT_LOG_LEVEL,"propagate": False}

    }
}