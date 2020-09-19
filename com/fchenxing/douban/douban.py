import requests
import json


def douban_login(username, password):
    url = "https://accounts.douban.com/j/mobile/login/basic"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
        "Referer": "https://accounts.douban.com/passport/login_popup?login_source=anony"
    }
    val = {
        "ck": "",
        "name": username,
        "password": password,
        "remember": "false"
    }
    # 不同于urllib的是data可以直接用字典对象
    response = requests.post(url, headers=headers, data=val)
    try:
        if response.status_code == 200:
            parse_resopnse(response.content)
    except requests.RequestException:
        print("请求失败")


def parse_resopnse(content):
    contentJson = json.loads(content)
    info = contentJson["payload"]["account_info"]
    name = info["name"]
    phone = info["phone"]
    print("用户{}登录成功，手机号为{}".format(name, phone))


username = input("输入用户名/邮箱:")
password = input("请输入密码:")

# 记录一个异常requests.exceptions.SSLError: HTTPSConnectionPool
# 原因由于开着fiddler所致,
douban_login(username, password)
