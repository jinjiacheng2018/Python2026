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
        "username": "张无忌",
        "password": "123456"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = user.login(data=data, headers=headers)
    print(response.json())
    return response.json()["login_info"]["token"]


def update():
    """
    修改用户信息
    """
    user_json = {
        "admin_user": "张无忌",
        "password": "123456",
        "token": f"{login()}",
        "sex": "1",
        "address": "广州市天河区",
        "telephone": "13500010003"
    }
    headers = {
        "Content-Type": "application/json"
    }
    print(user.update(user_id=4, headers=headers, json=user_json).json())


if __name__ == '__main__':
    update()
