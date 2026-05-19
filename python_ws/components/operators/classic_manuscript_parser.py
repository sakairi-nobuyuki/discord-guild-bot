# coding: utf-8

from typing import List
import re


def laziest_parser(text: str) -> List[str]:
    # 改行を整理
    text = text.replace("\n", "")
    # 文分割
    sentences = re.split(r"(?<=[。！？.!?])\s*", text)
    # 空文字除去
    sentences = [s.strip() for s in sentences if s.strip()]

    return sentences
