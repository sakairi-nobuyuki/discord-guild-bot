# coding: utf-8

from typing import Dict, Any
import pytest
from data_structure import *


@pytest.fixture()
def mock_params() -> Dict[str, Any]:
    return {
        "members": [{"name": "moc", "id": 123}, {"name": "tb", "id": "234"}],
        "timer": None,
    }


def test_load_member() -> None:
    m = load_member({"id": 123, "name": "poyo"})
    assert isinstance(m, Member)
    assert m.id == 123
    assert m.name == "poyo"


def test_load_member(mock_params: Dict[str, Any]) -> None:
    m = load_member(mock_params["members"][0])
    assert isinstance(m, Member)
    assert m.id == mock_params["members"][0]["id"]
    assert m.name == mock_params["members"][0]["name"]


def test_load_member_key_error() -> None:

    with pytest.raises(KeyError):
        load_member({"id": 123, "neme": "poyo"})


def test_load_members(mock_params: Dict[str, Any]) -> None:
    ms = load_members(mock_params["members"])

    assert isinstance(ms, Members)
    for m in ms.data:
        assert isinstance(m, Member)
        m_j = ms.id_list.index(m.id)
        assert ms.data[m_j].id == m.id
