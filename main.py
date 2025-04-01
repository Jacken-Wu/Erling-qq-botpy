# -*- coding: utf-8 -*-
import asyncio
import os

import botpy
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import GroupMessage, Message

import erling


config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))

_log = logging.get_logger()

erling.init(config["data_path"])
asking, answer = erling.update_conversation(config["data_path"])


class MyClient(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 on_ready!")

    async def send(self, message: GroupMessage, content: str):
        messageResult = await message._api.post_group_message(
            group_openid=message.group_openid,
            msg_type=0, 
            msg_id=message.id,
            content=content)
        _log.info(messageResult)

    async def on_group_at_message_create(self, message: GroupMessage):
        user_id = message.author.member_openid
        erling.add_love(user_id, config["data_path"])
        print(message)
        content = message.content
        # 去掉首尾的所有空格
        content = content.strip()

        # 空消息
        if content == "":
            result = erling.say_hi()
            await self.send(message, result)
            return None

        # 参数为整个 content 字符串
        # 随机
        if content.startswith("/rand"):
            result = erling.rand(content)
            await self.send(message, result)
            return None

        # 吃啥
        if content.startswith("/eat"):
            result = erling.what_eat(content, config["data_path"])
            await self.send(message, result)
            return None

        # 查看 love
        if content.startswith("/love"):
            result = erling.get_love(user_id, config["data_path"])
            await self.send(message, result)
            return None

        # 推荐音乐
        if content.startswith("/music"):
            result = erling.music(config["data_path"])
            await self.send(message, result)
            return None

        # 聊天
        result = erling.reply_conversation(content, config["data_path"], asking, answer)
        await self.send(message, result)


if __name__ == "__main__":
    intents = botpy.Intents(public_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=config["appid"], secret=config["secret"])
