# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import requests
import datetime
import LoginCase.LogHelp as log;

DATA_URL="http://sspdev.gionee.com/adslotincome/report?start_date={}&end_date={}&app_id=&pn=1"
import logging
def get_info(session):
    '''
    :param session: 登陆session
    :return: 内容数据
    :name: 金立ssp广告数据
    '''
    logger = log.getLog("sspdev")
    data = {"platformId": 6, "accountId": 1}
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    data["date"] = datetime.datetime.now().strftime('%Y%m%d')
    session.get("http://sspdev.gionee.com/report/index")
    PHPSESSID = session.cookies.items()[-1][1]
    header = {
        "Cookie":"PHPSESSID={}".format(PHPSESSID),
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer":"http://sspdev.gionee.com/report/index",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }
    data_list = []
    response = session.get(DATA_URL.format(yesterday,yesterday), headers=header)
    soup = BeautifulSoup(response.text,"lxml")
    trs = soup.find("table",{"class":"table"}).find("tbody").find_all("tr")
    for tr in trs[1:]:
        data_dict={}
        tds = tr.find_all("td")
        name = tds[0].get_text().strip()
        shownum = tds[4].get_text().strip()
        clicknum = tds[5].get_text().strip()
        money = tds[-1].get_text().strip()
        data_dict["logTime"]=yesterday.replace("-","")
        data_dict["sourceName"]=name
        data_dict["sourcePv"]=shownum
        data_dict["clickCount"]=clicknum
        data_dict["income"]=money
        data_list.append(data_dict)
        print yesterday,name,shownum,clicknum,money
    data["data"] = data_list
    logger.info(data)
    print data


if __name__ == "__main__":
    from login import login
    session = login(user = "xxxx", pwd = "xxxx")
    get_info(session)
