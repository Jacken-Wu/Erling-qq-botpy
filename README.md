<p align="center">
    <img src="./cover.png" alt="icon" width="200" height="200">
</p>

<div align="center">

# 二澪(Erling)

</div>
<p align="center">
    <a href="https://raw.githubusercontent.com/Jacken-Wu/Erling-qq-botpy/master/LICENSE">
        <img src="https://img.shields.io/github/license/Jacken-Wu/Erling-qq-botpy" alt="license">
    </a>
    <a href="https://github.com/Jacken-Wu/Erling-qq-botpy/releases">
        <img src="https://img.shields.io/github/v/release/Jacken-Wu/Erling-qq-botpy?color=blueviolet&include_prereleases" alt="release">
    </a>
    <a href="https://www.python.org">
        <img src="https://img.shields.io/badge/language-python3-blue.svg" alt="python3">
    </a>
</p>

## 目录

[项目介绍](#项目介绍)  
[部署](#部署)  
[二澪人设](#二澪人设)

## 项目介绍

本项目为某 VOCALOID 群的群聊机器人 python 代码。  
使用QQ官方机器人接口，前身是 [Erling](https://github.com/Jacken-Wu/Erling)。

## 部署

1. 克隆本仓库或从 [releases](https://github.com/Jacken-Wu/Erling-qq-botpy/releases) 下载压缩包并解压
2. 安装 Python3
3. 安装依赖：`pip install -r requirements.txt`
4. 申请 [QQ 机器人](https://q.qq.com/#/app/bot)，并获得 `token`
5. 将 `config.example.yaml` 复制为 `config.yaml`，并修改其中相应的配置项，其中 `data_path` 为数据文件存放路径
6. 在项目的根目录下运行 `python main.py` 或 `python3 main.py`
7. 其他
    - 你的 `data_path` 下的 `chat/trainning/text/` 中可添加文本，用于生成词向量，具体示例见其中的参考文件
    - 你的 `data_path` 下的 `chat/trainning/conversation/` 中可添加对话语料，用于生成对话数据集，具体示例见其中的参考文件
    - 可以运行 `generate_conversation.py` 生成词向量或对话数据集（需解除该文件中对应的注释）
    - 生成的词向量模型文件位于 `data_path/chat/model_word2vec`，对话数据集文件位于 `data_path/chat/database_conversation.yml`
    - 重新生成对话数据集后无需重启机器人，对机器人使用 `/update` 命令即可更新对话数据集

## 二澪人设

名字：二澪（Erling）  
身高：160cm  
体重：不详  
年龄：17  
印象色：浅蓝

![erling1](https://i0.hdslb.com/bfs/album/9bd124359cc2f015135322b4516ca219c44d8ed8.png@1036w.webp)
![erling2](https://i0.hdslb.com/bfs/new_dyn/7af4a311826cecfb2646458d317e9560229017508.png@1036w.webp)
![erling3](https://i0.hdslb.com/bfs/new_dyn/55e0374fba234f38edcbd7cc087f48cd229017508.png@1036w.webp)
![erling](https://i0.hdslb.com/bfs/new_dyn/dfc9ce61afe92d39198168745a69b7a5229017508.png@1036w.webp)
