# -*- coding: utf-8 -*-
from gensim.models import Word2Vec
import jieba
import re
import os
import numpy as np
import random


def update_conversation(data_path: str) -> tuple:
    """
    更新对话库。
    """
    database_path = os.path.join(data_path, 'chat/database_conversation.yml')
    with open(database_path, 'r', encoding='utf-8') as f:
        origin = f.readlines()
    asking = []
    answer = []
    for line in origin:
        if line[:4] == '- - ':
            asking.append(eval(line[4:]))
        elif line[:4] == '  - ':
            answer.append(line[4:])

    return asking, answer


def split_sentence(sentence: str) -> list:
    """
    将句子分割为词语。
    """
    sentence = re.sub("[\s+\.\!\/_.$%^*(++\"\'“”《》]+|[+——！，。？、~·@#￥%……&* ( ) ◆☥♥【】（）《》‘’'-'；：‘]+", "", sentence)
    words = jieba.lcut(sentence)
    return words


def generate_vec(data_path: str) -> bool:
    """
    生成并保存词向量模型。生成的模型保存在用户自定的data_path下。
    """
    text_path = os.path.join(data_path, 'chat/trainning/text/')
    files = os.listdir(text_path)
    lines = []
    for file in files:
        with open(os.path.join(text_path, file), 'r', encoding='utf-8') as f:
            text = f.readlines()
        for sentence in text:
            lines.append(split_sentence(sentence))
    model = Word2Vec(lines, vector_size = 20, window=3, min_count=3, epochs=7,negative=10)
    model.save(os.path.join(data_path,'chat/model_word2vec'))
    return True


def generate_conversation(data_path: str) -> bool:
    """
    使用词向量生成对话数据库。
    """
    database_path = os.path.join(data_path, 'chat/database_conversation.yml')
    model_path = os.path.join(data_path,'chat/model_word2vec')
    conversation_path = os.path.join(data_path, 'chat/trainning/conversation/')
    with open(database_path, 'w', encoding='utf-8') as f:  # 清空
        pass
    model = Word2Vec.load(model_path)
    files = os.listdir(conversation_path)
    chat_q = []
    chat_a = []
    for file in files:
        with open(os.path.join(conversation_path, file), 'r', encoding='utf-8') as f:
            origin = f.readlines()
        origin = origin[3:]
        for conver in origin:
            if len(conver) > 4:
                if conver[:4] == '- - ':
                    chat_q.append(conver[4:])
                elif conver[:4] == '  - ':
                    chat_a.append(conver[4:])

    chat_vec_temp = []
    chat_answer_tamp = []
    with open(database_path, 'a', encoding='utf-8') as f:
        for i in range(len(chat_q)):
            # 计算句向量
            words = split_sentence(chat_q[i])
            length = len(words)
            vec = np.zeros(20)
            for word in words:
                try:
                    vec += model.wv.get_vector(word)
                except KeyError:
                    pass

            if length != 0:
                vec /= length

            vec_string = str(list(vec))
            if (np.linalg.norm(vec) != 0) and (vec_string not in chat_vec_temp) and (chat_a[i] not in chat_answer_tamp):  # 模不为0且Q和A都未重复
                chat_vec_temp.append(vec_string)
                chat_answer_tamp.append(chat_a[i])
                f.write('- - ' + vec_string + '\n')
                f.write('  - ' + chat_a[i])

    return True


def compare(vec1: list, vec2: list) -> float:
    """
    使用夹角余弦值比较两个向量的相似程度，输入两个向量，输出相似度（0~1之间）。
    """
    num = np.dot(vec1, vec2)
    conum = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    if conum == 0:
        return 0
    else:
        cos_value = num / conum
        return 0.5 * cos_value + 0.5


def reply_conversation(input_str: str, data_path: str, asking: list, answer: list) -> str:
    """
    对输入语句进行答复。
    """
    model_path = os.path.join(data_path, 'chat/model_word2vec')
    model = Word2Vec.load(model_path)
    words = split_sentence(input_str)
    length = len(words)
    input_vec = np.zeros(20)
    for word in words:
        try:
            input_vec += model.wv.get_vector(word)
        except KeyError:
            pass
    if length != 0:
        input_vec /= length

    if np.linalg.norm(input_vec) == 0:
        reply = '这个话题二澪还听不懂呢'
    else:
        similarities = []
        for vec in asking:
            similarities.append(compare(input_vec, vec))

        # 在权重相同的所有回答中随机选择一个
        max_sim = max(similarities)
        reply_indexs = []
        while max(similarities) == max_sim:
            reply_indexs.append(similarities.index(max(similarities)))
            similarities[reply_indexs[-1]] = 0
        reply_index = reply_indexs[random.randint(0, len(reply_indexs) - 1)]

        # 7%的概率丢弃当前回答，选择下一个最高相似度的回答，重复4次得到最终回答
        for times in range(4):
            i = random.randint(0, 99)
            if i < 7:
                reply_index = similarities.index(max(similarities))
                similarities[reply_index] = 0

        reply = answer[reply_index][:-1]
        save_chat(input_str, reply, data_path)

    return reply


def save_chat(word_in: str, word_out: str, data_path: str):
    """
    保存对话日志。
    """
    chat_log_path = os.path.join(data_path, 'chat/chat.log')
    if not os.path.exists(chat_log_path):
        with open(chat_log_path, 'w', encoding='utf-8') as f:
            f.write('%s | %s\n' % (word_in, word_out))
    with open(chat_log_path, 'a', encoding='utf-8') as f:
        f.write('%s | %s\n' % (word_in, word_out))


if __name__ == '__main__':
    # generate_vec()
    # generate_conversation('../data/')
    asking, answer = update_conversation('../data/')
    # model = Word2Vec.load(data_path + 'model_word2vec')
    # print('和“超超”相关度最高的词：')
    # print(model.wv.most_similar('超超',topn=5))
    while True:
        in_str = input()
        if in_str == 'exit':
            break
        else:
            print(reply_conversation(in_str, '../data/', asking, answer))
