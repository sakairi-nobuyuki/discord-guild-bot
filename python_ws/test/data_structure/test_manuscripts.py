# coding:utf-8

from data_structure.manuscripts import *

def test_load_manuscript():
    ml = list_manuscript_paths()
    assert isinstance(ml, list)
    assert len(ml) > 0
        
class TestManuscript:
    text_file = list_manuscript_paths()[0]

    m = Manuscript("hoge", "piyo", "tb", text_file)
    
    assert isinstance(m, Manuscript)
    assert m.name == "hoge"
    assert m.title == "piyo"
    assert m.author == "tb"
    assert len(m.sentences) > 0
    for text in m.sentences:
        assert isinstance(text, str)