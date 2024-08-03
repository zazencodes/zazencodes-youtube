import sys

sys.path.append("../")
from generate_yaml import generate_yaml_from_pydantic_obj

from config import app_config
from config.domain import AppEngineConfig

generate_yaml_from_pydantic_obj(app_config, "app.yaml", AppEngineConfig)
