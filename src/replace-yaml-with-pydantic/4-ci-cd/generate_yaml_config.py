import sys

sys.path.append("../")
from generate_yaml import generate_yaml_from_pydantic_obj

from config import workflow
from config import Workflow

generate_yaml_from_pydantic_obj(workflow, "test.yml", Workflow)
