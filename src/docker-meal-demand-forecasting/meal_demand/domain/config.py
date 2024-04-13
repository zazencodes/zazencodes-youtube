from dataclasses import dataclass
from typing import Dict, List
from pathlib import Path


@dataclass
class Config:
    seed: int | None
    data_path: Path
    center_type: str | None
    models_path: Path
    model_id: str
    model_params: Dict | None
    fulfilment_center_file: str
    meal_info_file: str
    train_file: str
    target: str
    numeric_features: List[str]
    ohe_features: List[str]
    max_week: int
