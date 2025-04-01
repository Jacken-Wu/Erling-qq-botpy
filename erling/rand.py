# -*- coding: utf-8 -*-
import random


def rand(content: str):
    """
    将 content 按空格分为列表，然后随机返回其中一个元素。
    """
    content = content[5:].strip()
    if content == "":
        return "这是一枚聪明人才能看得见的赛博骰子"

    words = content.split()
    return random.choice(words)
