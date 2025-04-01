# -*- coding: utf-8 -*-
import os
import shutil


def new_file(content: str, file_path: str):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def init(data_path: str):
    """
    初始化，新建必要的文件和文件夹
    """
    chat_path = os.path.join(data_path, 'chat')
    if not os.path.exists(chat_path):
        os.makedirs(chat_path)

    # 食物、音乐、loves列表
    food_path = os.path.join(data_path, 'food_list')
    music_path = os.path.join(data_path,'music_list')
    loves_path = os.path.join(data_path, 'loves')
    if not os.path.exists(food_path):
        new_file('小笼包\n豆腐脑\n馒头\n', food_path)
    if not os.path.exists(music_path):
        new_file('音乐1\n音乐2\n音乐3\n', music_path)
    if not os.path.exists(loves_path):
        new_file('', loves_path)

    # 聊天语料
    conversation_path = os.path.join(data_path, 'chat/trainning/conversation')
    text_path = os.path.join(data_path, 'chat/trainning/text')
    if not os.path.exists(conversation_path):
        os.makedirs(conversation_path)
    if not os.path.exists(text_path):
        os.makedirs(text_path)

    conversation_example = os.path.join(conversation_path, 'conversation_example.yml')
    text_example = os.path.join(text_path, 'trainning_text_example.txt')
    database_conversation_path = os.path.join(data_path, 'chat/database_conversation.yml')
    model_word2vec_path = os.path.join(data_path,'chat/model_word2vec')
    if not os.path.exists(conversation_example):
        shutil.copyfile('./init_files/conversation_example.yml', conversation_example)
    if not os.path.exists(text_example):
        shutil.copyfile('./init_files/trainning_text_example.txt', text_example)
    if not os.path.exists(database_conversation_path):
        shutil.copyfile('./init_files/database_conversation_example.yml', database_conversation_path)
    if not os.path.exists(model_word2vec_path):
        shutil.copyfile('./init_files/model_word2vec', model_word2vec_path)
