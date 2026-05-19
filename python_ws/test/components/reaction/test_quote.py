# coding: utf-8

from components.reaction import *
from data_structure import Manuscript

def test_load_index() -> None:
    quote_file_index = load_index()
    assert isinstance(quote_file_index, list)


def test_create_manuscript() -> None:
    quote_file_index = load_index()
    m1 = create_manuscript(quote_file_index[0])
    assert isinstance(m1, Manuscript)
    assert len(m1.sentences) > 0

class TestQuoteNovelsPoems:
    def test_init_instance(self) -> None:
        qts = QuoteNovelsPoems()
        assert isinstance(qts, QuoteNovelsPoems)
        assert len(qts.manuscripts) > 0
        
    def test_create_quote(self) -> None:
        qts = QuoteNovelsPoems()
        assert len(qts.create_quote(1, 2, 10)) > 10

        m1 = qts.manuscripts[0]
        sentences1 = m1.sentences
        assert qts.create_quote(0, len(sentences1) - 1, 5) ==  sentences1[-1:][0]
