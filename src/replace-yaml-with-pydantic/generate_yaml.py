from pydantic import BaseModel
from typing import Type
from pathlib import Path
import yaml


def generate_yaml_from_pydantic_obj(
    obj: BaseModel,
    file_path: str,
    obj_model: Type[BaseModel] = BaseModel,
):
    fp = Path(file_path)
    fp.parent.mkdir(exist_ok=True, parents=True)

    print(f"Writing to file {file_path}")
    fp.write_text(yaml.dump(obj.model_dump(by_alias=True, exclude_none=True)))

    if obj_model:
        try:
            validate_yaml(file_path, obj_model)
        except Exception as err:
            print(f"Failed to validate YAML:\n{err}")


def validate_yaml(
    file_path: str,
    obj_model: Type[BaseModel],
):
    print(f"Validating against model {obj_model}")
    with open(file_path, "r") as f:
        yaml_data = yaml.safe_load(f)
        print(yaml_data)
    obj_model(**yaml_data)
    print("Validation OK 🪷")
