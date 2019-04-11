# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import requests
import datetime
import json

LOGIN_URL="https://id.gionee.com/members/loginauthorize?developer=true&redirect_uri=http:%2F%2Fsspdev.gionee.com%2Findex%2Findex"
def get_session(session, user_name, password):

    header = {
        "Content-Type":"application/json;charset=UTF-8",
        "Referer":"https://id.gionee.com/members/developer?redirect_uri=http%3A%2F%2Fsspdev.gionee.com%2Findex%2Findex",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",

    }
    data={"tn":user_name,"vid":"","vtx":"","p":password,"vty":"vtext"}
    response = session.post(LOGIN_URL, json=data, headers=header)
    return session



def login(**kwargs):
    user_name = kwargs.get("user","")
    password = kwargs.get("pwd","")
    session = requests.Session()
    token = get_session(session,user_name,password)
    return session

if __name__ == "__main__":
   login(user = "xxxx", pwd = "xxxx")