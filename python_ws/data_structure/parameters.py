# coding: utf-8

from dataclasses import dataclass, field
from typing import Dict, List
import os
import yaml
from time import time

def load_yaml(file_path:str) -> Dict[str, str|int|float]:
    with open(file_path, "r") as f:
            return yaml.safe_load(file_path)

@dataclass
class Member:
    name: str
    id: int

@dataclass
class Members:
    
    data: List[Member] = field(default_factory=list)
    name_list: List[str] = field(default_factory=list)
    id_list: List[int] = field(default_factory=list)

def load_member(data_dict: Dict[str, str|int]) -> Member:
    if not isinstance(data_dict, dict):
        raise TypeError(f"{data_dict} is not a Dict")
    if not (all([[r_k for r_k in ["name", "id"] if r_k == t_k] for t_k in data_dict.keys()])):
        raise KeyError(f"{list(data_dict.keys())} is not compatible for initializing a Member instance")
        
    return Member(**data_dict)

def load_members(data_dict_list: List[Dict[str, str|int]]) -> Members:
    if not isinstance(data_dict_list, list):
        raise TypeError(f"{data_dict_list} is not a List")

    ms = Members()

    for data_dict in data_dict_list:
        m = load_member(data_dict)
        ms.data.append(m)
        ms.id_list.append(m.id)
        ms.name_list.append(m.name)
    return ms

def load_schedule():
    pass

class Parameters:
    def __init__(self, file_path: str) -> None:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} was not found")
        
        params = load_yaml(file_path)

        
