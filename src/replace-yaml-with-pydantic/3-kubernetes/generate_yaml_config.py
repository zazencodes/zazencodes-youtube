import sys

sys.path.append("../")
from generate_yaml import generate_yaml_from_pydantic_obj

from config import pod_config
from config.domain import PodConfig

generate_yaml_from_pydantic_obj(pod_config, "redis-pod.yaml", PodConfig)
