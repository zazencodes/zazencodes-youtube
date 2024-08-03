import logging
import sys

sys.path.append("../")
from generate_yaml import generate_yaml_from_pydantic_obj

from config import logging_config
from config import LoggingConfig

generate_yaml_from_pydantic_obj(logging_config, "logging_config.yaml", LoggingConfig)
