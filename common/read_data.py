#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project    ：Python2026 
@File       ：read_data.py
@IDE        ：PyCharm 
@Date       ：2025/12/23 22:32:41 
@Author     ：JinJiacheng
@description：读取文件工具类
'''
import os.path
from configparser import ConfigParser

import yaml
import json
from common.logger import logger


class MyConfigParserf(ConfigParser):

    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def optionxform(self, optionstr: str) -> str:
        return optionstr


class ReadFileData():

    def __init__(self):
        pass

    def load_ini(self, file_path):
        """
        加载ini配置文件
        :param file_path: 文件路径
        :return: data
        """
        logger.info(f"【加载配置文件】：{file_path} ")
        config = MyConfigParserf()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        return data

# 初始化实例
data = ReadFileData()

if __name__ == '__main__':
    # 获取项目的根目录
    BASE_PATH = os.path.dirname(os.path.dirname(__file__))

    # 组装mysql配置文件的路径
    MYSQL_CONFIG = os.path.join(BASE_PATH, "config", "mysql.ini")
    data.load_ini(file_path=MYSQL_CONFIG)
