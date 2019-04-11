# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import requests
import datetime
import json

LOGIN_URL="https://mmp.levect.com/basic/login"
def get_session(session, user_name, password):
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Referer":"https://mmp.levect.com/page/login/?redirect=https://mmp.levect.com/"
    }
    data={
        "username":user_name,
        "password":password
    }
    rs = session.post(LOGIN_URL, data=data, headers=header)




def login(**kwargs):
    user_name = kwargs.get("user","")
    password = kwargs.get("pwd","")
    session = requests.Session()
    token = get_session(session,user_name,password)
    return session

if __name__ == "__main__":
   login(user = "xxx", pwd = "xxxx")