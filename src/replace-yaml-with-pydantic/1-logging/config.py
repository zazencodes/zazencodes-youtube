from pydantic import BaseModel


class FormatterConfig(BaseModel):
    format: str


class LoggerConfig(BaseModel):
    level: str
    handlers: list[str]
    propagate: bool


class LoggingConfig(BaseModel):
    version: int
    disable_existing_loggers: bool
    formatters: dict[str, FormatterConfig]
    handlers: dict[str, dict]
    loggers: dict[str, LoggerConfig]


logging_config = LoggingConfig(
    version=1,
    disable_existing_loggers=False,
    formatters={
        "simple": FormatterConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
    },
    handlers={
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
        }
    },
    loggers={
        "myapp": LoggerConfig(level="DEBUG", handlers=["console"], propagate=False)
    },
)
