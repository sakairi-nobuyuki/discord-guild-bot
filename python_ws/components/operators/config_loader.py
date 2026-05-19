# cofing: utf-8

from pathlib import Path
from typing import Dict
import yaml

def load_users(file_name: str = "default.yaml") -> Dict[str, str|int]:

    conf_file_path = Path(Path(__file__).resolve().parent.parent, "config", file_name)
    if not conf_file_path.exists():
        raise FileNotFoundError(f"{conf_file_path} is not found")
    
    with open(file_name, "r") as f:
        return yaml.safe_load(f)




