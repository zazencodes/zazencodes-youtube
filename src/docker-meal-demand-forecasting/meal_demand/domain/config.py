from dataclasses import dataclass
from typing import Dict, List
from pathlib import Path


@dataclass
class Config:
    data_path: Path
    models_path: Path
    model_id: str
    model_params: Dict
    fulfilment_center_file: str
    meal_info_file: str
    train_file: str
    target: str
    numeric_features: List[str]
    ohe_features: List[str]
