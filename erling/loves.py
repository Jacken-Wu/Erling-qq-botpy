# -*- coding: utf-8 -*-
import os


def add_love(id: str, data_path: str):
    love_path = os.path.join(data_path, 'loves')
    with open(love_path, 'r', encoding='utf-8') as f:
        loves_list = f.readlines()
    is_exist = False
    for i in range(len(loves_list)):
        love_data = loves_list[i].strip().split()
        if love_data[0] == id:
            loves_list[i] = f"{id} {int(love_data[1]) + 1}\n"
            is_exist = True
            break
    if not is_exist:
        loves_list.append(f"{id} 1\n")

    with open(love_path, 'w', encoding='utf-8') as f:
        f.writelines(loves_list)


def get_love(id: str, data_path: str):
    love_path = os.path.join(data_path, 'loves')
    with open(love_path, 'r', encoding='utf-8') as f:
        loves_list = f.readlines()
    for love in loves_list:
        love_data = love.strip().split()
        if love_data[0] == id:
            return love_data[1]
    return '1'
