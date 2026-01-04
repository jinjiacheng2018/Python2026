# 项目说明
```text
项目基于Python+pytest+request+allure编写的自动化测试框架的demo。

参考测试接口源码：https://github.com/jinjiacheng2018/flaskDemo
参考框架搭建源码：https://github.com/jinjiacheng2018/pytestDemo

参考博客文章：https://www.cnblogs.com/wintest/p/13423231.html
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
├── operation/        # 自定义关键字
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

# 框架搭建步骤
```text
1. 创建项目的各个包、文件夹
2. 搭建基础的框架
    - a) config: 添加mysql.ini、setting.ini配置文件
    - b) common: 添加基础的工具类
        - logger.py: 首先添加日志框架，构建基础的日志打印
        - read_data.py: 添加数据读取模块，读取配置文件
        - mysql_operate.py: 添加MySQL数据库操作模块，查询、插入、更新、删除
    - c) core: 
        - 添加rest_client.py模块，用于reques基础的请求方法封装、关键字返回结果类
        - 添加result.py模块，封装关键字返回结果类
    - d) api: 添加User.py模块并集成封装的接口类，进一步封装接口API
    - e) operation: 添加User关键字封装模块，封装关键字
    - f) data: 准备测试数据
        - base_data.yaml: 添加基础的准备数据
    - g) testcase: 添加测试用例
        - config.py: 添加测试用例配置文件(基础配置文件)
 3. todo
```

# 关键字封装说明
```text
关键字应该是具有一定业务意义的，在封装关键字的时候，可以通过调用多个Python接口来完成。
在某些情况下，比如测试一个充值接口的时候，在充值后可能需要调用查询接口得到最新账户余额，来判断查询结果与预期结果是否一致，那么可以这样来进行测试：

1, 首先，可以把 充值-查询 的操作封装为一个关键字，在这个关键字中依次调用充值和查询的接口，并可以自定义关键字的返回结果。
2, 接着，在编写测试用例的时候，直接调用关键字来进行测试，这时就可以拿到关键字返回的结果，那么断言的时候，就可以直接对关键字返回结果进行断言。

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

# 关于封装request的好处
```text
公众号内容：https://mp.weixin.qq.com/s/jU_3Ag8p2LAlMkBjFzX_fw

| 目标           | 对应封装能力                          |
| --------      | ------------------------------- |
| 减少重复代码     | 统一 request 入口                   |
| 提升健壮性      | 统一异常处理 + 重试                     |
| 降低环境切换成本  | base_url / headers / token 集中管理 |
| 适配测试生态    | 日志、断言、allure、pytest             |
| 降低使用门槛     | 屏蔽 requests 细节，提供业务级接口          |

```

# 参考地址
https://mp.weixin.qq.com/s/tp-CXm6adA0z9CrubpiEhA