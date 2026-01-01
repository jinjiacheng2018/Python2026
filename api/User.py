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

    def list_user_by_name(self, user_name, **kwargs):
        """
        根据名字获取用户
        """
        return self.get(f"/users/{user_name}", **kwargs)

    def register(self, **kwargs):
        """
        注册用户
        """
        return self.post("/register", **kwargs)

    def login(self, **kwargs):
        """
        登录用户
        """
        return self.post("/login", **kwargs)


user = User(base_url)

if __name__ == '__main__':
    # 查询所有用户
    # print(user.list_all_users().json())

    # 根据名字查询用户
    # print(user.list_user_by_name("周芷若").json())

    # 注册用户
    '''
    user_json = {
        "username": "周芷若",
        "password": "123456",
        "role": 2,
        "sex": "0",
        "telephone": "15000000003",
        "address": "上海"
    }
    headers = {
        "Content-Type": "application/json"
    }
    print(user.register(headers=headers, json=user_json).json())
    '''

    # 登录用户
    data = {
        "username": "周芷若",
        "password": "123456"
    }
    print(user.login(data=data).json())
