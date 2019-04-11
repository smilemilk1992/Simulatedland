# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import requests
import datetime
import simplejson
import json
import fateadm_api
import LoginCase.LogHelp as log;
import logging
def get_session(session, user_name, password):
    '''
    :param session: 登陆session
    :param user_name: 用户名
    :param password: 密码
    :return: 内容数据
    :name: 搜狗
    '''

    logger = log.getLog("sogou")
    data = {"platformId": 7, "accountId": 1}
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y%m%d')
    data["date"] = datetime.datetime.now().strftime('%Y%m%d')
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }
    pic = get_picsnum(session)

    datas = {
        "systemType": 1,
        "loginFromPage": "homePage",
        "username": user_name,
        "password": password,
        "activecode": pic
    }
    session.post("http://union.sogou.com/loginauth.action", headers=header, data=datas)
    xx = session.get("http://union.sogou.com/stat/product_stat!query.action?unionid=17getfun",headers=header)
    soup = BeautifulSoup(xx.text,"lxml")
    data_list = []
    content_data = soup.find_all("span",{"class":"pronumauto"})
    data_dict = {}
    data_dict["logTime"]=yesterday
    data_dict["sourcePv"]=content_data[0].get_text().strip().replace(",","")
    data_dict["clickCount"]=content_data[1].get_text().strip()
    data_dict["income"]=content_data[2].get_text().strip()
    data_list.append(data_dict)
    data["data"] = data_list
    logger.info(data)
    print data




def get_picsnum(session):
    url = "http://union.sogou.com/validateCode"
    imgresponse = session.get(url, stream=True)  # 以流的方式打开
    image = imgresponse.content
    # print image
    with open("img.jpg", "wb") as jpg:
        jpg.write(image)

    x = fateadm_api.TestFunc();
    return x

def login(**kwargs):
    user_name = kwargs.get("user","")
    password = kwargs.get("pwd","")
    session = requests.Session()
    token = get_session(session,user_name,password)
    return session

if __name__ == "__main__":
   login(user = "xxx", pwd = "xxxxx")