'''
@Project    ：Python2026
@File       ：test_01_get_user_info.py
@Date       ：2026/1/5 22:33:03
@Author     ：JinJiacheng
@description：描述信息
'''

import allure
import pytest

from operation.User import *
from testcase.conftest import api_data


@allure.step("步骤1 ==>> 获取所有用户信息")
def step_1():
    logger.info("步骤1 ==>> 获取所有用户信息")


@allure.step("步骤2 ==>> 获取某个用户的信息")
def step_2(username):
    logger.info(f"步骤2 ==>> 获取【{username}】的信息")


class TestGetUserInfo():

    @allure.story("【01】用户管理模块")
    @allure.description("获取所有用户的用例")
    @pytest.mark.single
    @pytest.mark.parametrize("except_result,except_code,except_msg", api_data["test_get_all_user_info"])
    def test_get_all_user_info(self, except_result, except_code, except_msg):
        """获取所有用户的用例"""
        logger.info("\n******************** 开始执行用例 ********************")
        step_1()
        result = get_all_users_info()
        assert result.response.status_code == 200
        assert result.success == except_result, logger.error("用例执行失败")
        logger.info(f"code ==>> 期望结果是：{except_code}，实际结果是：{result.code}")
        assert result.code == except_code
        assert except_msg in result.msg
        logger.info("******************** 结束执行用例 ********************")

    @allure.story("【01】用户管理模块")
    @allure.description("获取某个用户的用例")
    @pytest.mark.single
    @pytest.mark.parametrize("username,except_result,except_code,except_msg", api_data["test_get_one_user_info"])
    def test_get_one_user_info(self, username, except_result, except_code, except_msg):
        """获取某个用户的用例"""
        logger.info("\n******************** 开始执行用例 ********************")
        step_1()
        result = get_one_user_info(username)
        assert result.response.status_code == 200
        assert result.success == except_result, logger.error("用例执行失败")
        logger.info(f"code ==>> 期望结果是：{except_code}，实际结果是：{result.code}")
        assert result.code == except_code
        assert except_msg in result.msg
        logger.info("******************** 结束执行用例 ********************")


if __name__ == "__main__":
    pytest.main(["-q", "-s", "test_01_get_user_info.py"])
