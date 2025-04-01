# -*- coding: utf-8 -*-
import random


def say_hi():
    """
    返回一个问候语
    """
    words = ["在", "二澪在哦", "怎么了", "在的呢~", "嗯？", "请问有什么事吗？", "什么，在想我的事情？"]
    return random.choice(words)
