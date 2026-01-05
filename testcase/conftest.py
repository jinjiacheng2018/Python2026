'''
@Project    ：Python2026
@File       ：conftest.py
@Date       ：2026/1/3 23:33:19
@Author     ：JinJiacheng
@description：描述信息
'''

import os
from common.mysql_operate import mysql_db

import allure
import pytest
from common.read_data import data
from common.logger import logger
from api.User import user

BASE_PATH = os.path.dirname(os.path.dirname(__file__))


def get_data(yaml_file_name):
    """
    定义方法获取yaml文件数据
    """
    try:
        yaml_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(file_path=yaml_file_path)
    except Exception as e:
        pytest.skip("没有找到yaml文件")
    else:
        return yaml_data


base_data = get_data("base_data.yaml")
api_data = get_data("api_test_data.yml")


@allure.step("前置步骤 ==>> 清理数据")
def step_first():
    logger.info("*****************************")
    logger.info("前置步骤开始 ==>> 清理数据")


@allure.step("后置步骤 ==>> 清理数据")
def step_last():
    logger.info("后置步骤开始 ==>> 清理数据")


@allure.step("登录")
def step_login(username, password):
    logger.info(f"管理员【{username}】登录。")


@pytest.fixture(scope="session")
def login_fixture():
    """
    登录
    """
    username = base_data["init_admin_user"]["username"]
    passwodd = base_data["init_admin_user"]["password"]

    user_data = {
        "username": username,
        "password": passwodd
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = user.login(data=user_data, headers=headers)
    step_login(username, passwodd)

    # yield前是setup，yield后是teardown。yield 的值就是注入到测试用例中的fixture返回值
    yield response.json()


@pytest.fixture(scope="session")
def insert_delete_user():
    """删除用户前，先往数据库中插入1条数据"""
    insert_sql = base_data["init_sql"]["insert_delete_user"][0]
    mysql_db.execute_db(insert_sql)
    step_first()
    logger.info(f"【删除用户操作：插入新用户。并执行前置SQL：{insert_sql}】")
    yield
    # yield是在测试用例执行完后执行(ps：有些情况下不给删除管理员用户，需要手动清理插入的数据)
    del_sql = base_data["init_sql"]["del_delete_user"][1]
    mysql_db.execute_db(del_sql)
    step_last()
    logger.info(f"【清理用户操作：清理用户，并执行后置SQL：{del_sql}】")

@pytest.fixture(scope="session")
def delete_register_user():
    """注册用户前，先删除数据，用例执行后要再次清理数据"""
    del_sql = base_data["init_sql"]["delete_register_user"]
    mysql_db.execute_db(del_sql)
    step_first()
    logger.info(f"【注册用户操作：清理用户，并执行前置SQL：{del_sql}】")
    yield
    mysql_db.execute_db(del_sql)
    step_last()
    logger.info(f"【注册用户操作：清理用户，并执行后置SQL：{del_sql}】")

@pytest.fixture(scope="session")
def update_user_telephone():
    """修改用户前，因手机号唯一，为了可以使用例重复执行，每次要先修改手机号再执行用例"""
    update_sql = base_data["init_sql"]["update_user_telephone"]
    mysql_db.execute_db(update_sql)
    step_first()
    logger.info(f"【修改用户操作：修改用户手机号，并执行前置SQL：{update_sql}】")