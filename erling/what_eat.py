# -*- coding: utf-8 -*-
import random
import os


def what_eat(content: str, data_path: str):
    """
    返回一个随机的食物名称
    """
    food_list_path = os.path.join(data_path, 'food_list')
    if not os.path.exists(food_list_path):
        return "二澪找不到食物列表文件了！"
    if not os.path.isfile(food_list_path):
        return "二澪找不到食物列表文件了！"

    food_name = content[4:].strip()
    with open(food_list_path, 'r', encoding='utf-8') as f:
        food_list = f.readlines()
    if food_name == "":
        return random.choice(food_list).strip()

    if (food_name + '\n') not in food_list:
        with open(food_list_path, 'a', encoding='utf-8') as f:
            f.write(food_name + '\n')
        return f"邦邦咔邦！已将 {food_name} 添加到食物列表！"
    else:
        return f"{food_name} 已经在食物列表了哦~"
