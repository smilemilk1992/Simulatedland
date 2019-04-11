# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import requests
import datetime
import json

LOGIN_URL="http://union.aiclk.com/login"
def get_session(session, user_name, password):
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Referer":"http://union.aiclk.com/"
    }
    data={
        "username":user_name,
        "password":password
    }
    session.post(LOGIN_URL, json=data, headers=header)
    return session



def login(**kwargs):
    user_name = kwargs.get("user","")
    password = kwargs.get("pwd","")
    session = requests.Session()
    token = get_session(session,user_name,password)
    return session

if __name__ == "__main__":
   login(user = "xxxx", pwd = "xxx")