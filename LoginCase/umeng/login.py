# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import requests
import datetime
import json



LOGIN_URL="https://passport.alibaba.com/newlogin/login.do?fromSite=-2&appName=youmeng"
def get_session(session, user_name, password):
    header = {
        "Referer":"https://passport.alibaba.com/mini_login.htm?lang=zh_cn&appName=youmeng&appEntrance=default&styleType=auto&bizParams=&notLoadSsoView=true&notKeepLogin=false&isMobile=false&cssLink=https://passport.umeng.com/css/loginIframe.css&rnd=0.5017435280672744",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }
    data={
        "loginId":user_name,
        "password":password
    }
    response = session.post(LOGIN_URL, data=data, headers=header)
    st = response.json().get("content",{}).get("data",{}).get("st","")
    if st:
        url = "https://passport.umeng.com/login/register?st={}&appId=&redirectUrl=http%3A%2F%2Fevents.umeng.com%2F".format(st)
        session.get(url).text
        umplus_uc_token = session.cookies.get("umplus_uc_token")
        return umplus_uc_token
    else:
        print "登陆失败！"

def login(**kwargs):
    user_name = kwargs.get("user","")
    password = kwargs.get("pwd","")
    session = requests.Session()
    umplus_uc_token = get_session(session,user_name,password)
    return session



if __name__ == "__main__":
   login(user = "xxxx", pwd = "xxxx")