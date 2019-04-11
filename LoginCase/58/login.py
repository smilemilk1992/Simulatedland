# -*- coding: utf-8 -*-
import requests
session = requests.Session()


def get_session(session, username, password):
    url = "http://passport.58.com/login/pc/dologin"
    header = {
        "Referer": "http://passport.58.com/login?path=http://mp.58.com/home",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "source": "passport",
        "password": password,
        "isremember": "false",
        "callback": "successFun",
        "username": username,
        "fingerprint": "12A3F277755156FA0DF8B3FDDBD2AEB6BB6C1C58C5C0E38F_011",
        "path": "http://mp.58.com/home?pts=1534046192816",
        "finger2": "zh-CN|24|2|8|1440_900|1440_828|-480|1|1|1|undefined|undefined|unknown|MacIntel|unspecified|1|false|false|false|false|false|0_false_false|d41d8cd98f00b204e9800998ecf8427e|f32e913c0c8c3fe6b5bbae4f08e1ed30",
    }
    rs = session.post(url, data=data, headers=header)


def login(**kwargs):
    user_name = kwargs.get("user", "")
    password = kwargs.get("pwd", "")
    session = requests.Session()
    get_session(session, user_name, password)
    return session


if __name__ == "__main__":
    # 注意这个pwd不是我们登陆的密码，需要我们在登陆后抓包看最后加密的格式，直接写死在这里就好
    login(user="xxxxx",pwd="xxxxx")

