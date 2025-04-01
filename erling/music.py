# -*- coding: utf-8 -*-
import random
import os


def music(data_path: str):
    musit_list_path = os.path.join(data_path, "music_list")
    with open(musit_list_path, "r", encoding="utf-8") as f:
        music_list = f.readlines()
    music_selected = random.choice(music_list).strip()
    return f"二澪在音乐库中找到了《{music_selected}》，你有听过吗？"
