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
        logger.error(result.error)

    # 关键字中根据项目要求是否需要返回业务数据，若不需求则删除该行代码
    return result