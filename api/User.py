#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project    ：Python2026 
@File       ：User.py.py
@IDE        ：PyCharm 
@Date       ：2025/12/28 20:33:36 
@Author     ：JinJiacheng
@description：描述信息用户
'''
import os.path
from common.read_data import data
from core.rest_client import RestClient

# 获取base_url
BAST_PATH = os.path.dirname(os.path.dirname(__file__))
CONFIG_FILE_PATH = os.path.join(BAST_PATH, "config", "setting.ini")
base_url = data.load_ini(CONFIG_FILE_PATH)["host"]["base_url"]


class User(RestClient):

    def __init__(self, base_url, **kwargs):
        super().__init__(base_url, **kwargs)

    def list_all_users(self, **kwargs):
        """
        获取所有的用户
        """
        return self.get("/users", **kwargs)


user = User(base_url)

if __name__ == '__main__':
    users = user.list_all_users()
    for user in users:
        print(user)
