# 项目说明
```text
项目基于Python+pytest+request+allure编写的自动化测试框架的demo。

参考测试接口源码：https://github.com/jinjiacheng2018/flaskDemo
参考框架搭建源码：https://github.com/jinjiacheng2018/pytestDemo
```

# 项目结构说明
```yaml
Python2026/
├── common/           # 公共模块
├── config/           # 配置文件
│   ├── __init__.py
│   └── settings.py
├── core/             # requests请求方法封装、关键字返回结果类
├── data/             # 数据文件
├── logs/             # 日志文件
├── report/           # 测试报告
├── testcase/         # 测试用例
├── utils/            # 工具函数
│   ├── __init__.py
│   └── logger.py
├── main.py           # 主程序入口
├── py.unittest.ini       # pytest配置
├── requirements.txt  # 依赖列表
├── README.md         # 项目说明
└── .gitignore        # Git忽略配置
```

# 测试系统说明
```text
system: xxx数字协同平台
url: http://39.174.76.164:29020/
username: 19000000004
password: 123456
code: 123456
```

# 关于查看python依赖包版本地址
```text
最常用 & 最推荐（工程师首选）
1️⃣ PyPI 官方网站（权威源头）
👉 https://pypi.org
以 urllib3 为例,打开：https://pypi.org/project/urllib3/

看右侧 Release history点进去能看到：
所有版本号
发布时间
是否 yanked（撤回）
📌 这是最权威的版本来源
```


# 参考地址
https://mp.weixin.qq.com/s/tp-CXm6adA0z9CrubpiEhA