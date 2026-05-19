# coding: utf-8

from copy import deepcopy
from typing import List, Dict, Any
from pathlib import Path
import yaml

from data_structure import Manuscript, load_manuscript, list_manuscript_paths

def load_index() -> List[Dict[str, Any]]:
    index_path = Path(Path(__file__).resolve().parent.parent.parent, "data", "quotes", "index.yaml")
    if not index_path.exists():
        raise FileNotFoundError(f"{str(index_path)} is not found")
    print("loading index: ", index_path, str(index_path))
    with open(index_path, "r") as f:
        return yaml.safe_load(f)

def obtain_manuscript_path(index_dict: Dict[str, str]) -> Path:
    return Path(Path(__file__).resolve().parent.parent.parent, "data", "quotes", index_dict["body_file"])

def create_manuscript(index_dict: Dict[str, str]):
    #file_path = obtain_manuscript_path(index_dict)
    index_dict_tmp = deepcopy(index_dict)
    index_dict_tmp["file_path"] = obtain_manuscript_path(index_dict_tmp)
    index_dict_tmp.pop("body_file")
    return Manuscript(**index_dict_tmp)

def create_manuscript_path_list(manuscript_index_list: List[Dict[str, Any]]) -> List[Manuscript]:
    quotes_dir_path =  Path(Path(__file__).resolve().parent.parent.parent, "data", "quotes")
    for manuscript in manuscript_index_list:
        file_path = Path(quotes_dir_path, manuscript["body_file"])
        print(file_path, file_path.exists())

class QuoteNovelsPoems:
    def __init__(self) -> None:
        self.manuscripts = list(map(create_manuscript, load_index()))
        self.n_manuscripts = len(self.manuscripts)
        self.max_sentences = max([len(m.sentences) for m in self.manuscripts])
    
    def create_quote(self, i_manuscript: int, i_sentences: int, l_quote: int) -> str:
        i_manuscript = i_manuscript % self.n_manuscripts
        sentences = self.manuscripts[i_manuscript].sentences
        n_sentence = len(sentences)

        if i_sentences > n_sentence:
            i_sentences = i_sentences % n_sentence

        m = self.manuscripts[i_manuscript]
        template = f"{m.author}著、{m.title}より、\n"
        if i_sentences + l_quote > n_sentence:
            return template + ("").join(sentences[i_sentences:])
        else:
            return template + ("").join(sentences[i_sentences: i_sentences+l_quote])
