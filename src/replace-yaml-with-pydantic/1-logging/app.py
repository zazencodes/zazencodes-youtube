import logging
import logging.config
import yaml


def setup_logging(config_path: str):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    logging.config.dictConfig(config)


setup_logging("logging_config.yaml")
logger = logging.getLogger("myapp")

if __name__ == "__main__":
    logger.debug("Starting the application")
    logger.info("Application running")
    logger.warning("TODO: provide app code here")
    logger.error("No app code provided!")
