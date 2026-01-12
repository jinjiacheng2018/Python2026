'''
@Project    ：Python2026
@File       ：run.py
@Date       ：2026/1/11 23:04:03
@Author     ：JinJiacheng
@description：新建模块运行用例（PyCharm 内置的 pytest 启动器不会启动allure，所以要单独写）
'''

import os
import pytest

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALLURE_RESULTS = os.path.join(BASE_DIR, "report", "allure-results")

os.makedirs(ALLURE_RESULTS, exist_ok=True)

pytest.main([
    "-s",
    "--alluredir=" + ALLURE_RESULTS,
    "testcases/api_test/test_01_get_user_info.py"

    # 执行用例后，进入到报告的目录下，生成allure报告
    # cd /d/MyWorkspaces/Python2026/report
    # allure generate allure-results -o allure-html --clean
    # allure open allure-html
])
