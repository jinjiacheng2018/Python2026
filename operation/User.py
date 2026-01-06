'''
@Project    ：Python2026
@File       ：User.py
@Date       ：2026/1/3 21:53:15
@Author     ：JinJiacheng
@description：用户关键字封装类
'''

from common.logger import logger
from api.User import user
from core.result_base import ResultBase


def get_all_users_info() -> ResultBase:
    """
    获取所有的用户
    :return: 自定义个关键字返回结果
    """
    result = user.list_all_users()
    if result.code == 0:
        result.success = True
    else:
        logger.error("【获取所有用户信息失败】")

    # 关键字中根据项目要求是否需要返回业务数据，若不需求则删除该行代码
    return result


def get_one_user_info(username: str) -> ResultBase:
    """
    获取某个用户信息
    :param username: 用户名
    :return: 自定义个关键字返回结果
    """
    result = user.list_user_by_name(username)
    if result.code == 0:
        result.success = True
    else:
        logger.error("【获取单个用户信息失败】")

    # 关键字中根据项目要求是否需要返回业务数据，若不需求则删除该行代码
    return result
