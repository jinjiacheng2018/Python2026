from api.User import user


def search_all_users():
    """
    查询所有用户
    """
    print(user.list_all_users().json())


def search_user_by_name():
    """
    根据名字查询用户
    """
    print(user.list_user_by_name("周芷若").json())


def register():
    """
    注册用户
    """
    user_json = {
        "username": "纪晓芙",
        "password": "123456",
        "role": 2,
        "sex": "0",
        "telephone": "15000000004",
        "address": "上海"
    }
    headers = {
        "Content-Type": "application/json"
    }
    print(user.register(headers=headers, json=user_json).json())


def login():
    """
    登录用户
    """
    data = {
        "username": "纪晓芙",
        "password": "123456"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    print(user.login(data=data, headers=headers).json())


def update():
    """
    修改用户信息
    """
    user_json = {}
    headers = {
        "Content-Type": "application/json"
    }
    user.update(4, headers=headers, json=user_json)


if __name__ == '__main__':
    update()
