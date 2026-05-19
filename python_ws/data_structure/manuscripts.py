# coding: utf-8

from pathlib import Path
from typing import List, Dict
from dataclasses import dataclass, field
import os

from components.operators import classic_manuscript_parser as classic_parser

def list_manuscript_paths() -> List[Path]:
    file_abs_path = Path(__file__).resolve()
    manuscript_dir_path = Path(file_abs_path.parent.parent, "data", "quotes", "manuscripts")
    return list(manuscript_dir_path.glob("*.txt"))

def load_manuscript(file_path: str) -> str:
    return Path(file_path).read_text(encoding="utf-8")


@dataclass
class Manuscript:
    name: str
    title: str
    author: str
    file_path: str
    sentences: list = field(default_factory=list)

    def __post_init__(self) -> None:
        parser = classic_parser.laziest_parser
        self.sentences = parser(load_manuscript(self.file_path))


