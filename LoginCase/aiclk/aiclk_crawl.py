# -*- coding: utf-8 -*-
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
import datetime
import json
import LoginCase.LogHelp as log;

DATA_URL="http://union.aiclk.com/homeReport/adslot?range={}-{}"
def get_info(session):
    '''
   :param param: 登陆session
   :return: 内容数据
   :name:点冠   8
    '''
    logger = log.getLog("aiclk")
    datas = {"platformId": 8, "accountId": 1}
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y%m%d')
    datas["date"] = datetime.datetime.now().strftime('%Y%m%d')
    cpc_ssp=session.cookies.items()[0][-1]
    header = {
        "Cookie":"cpc-ssp={}".format(cpc_ssp),
        "Referer":"http://union.aiclk.com/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }
    response = session.get(DATA_URL.format(yesterday,yesterday), headers=header)
    soup = BeautifulSoup(response.text,"lxml")
    if soup:
        data_list = []
        json_data = json.loads(soup.text)
        for data in json_data:
            data_dict={}
            adslot_name = data.get("adslot_name","") #广告位
            click = data.get("click",0) #点击数
            impression = data.get("impression",0) #展现数
            income = data.get("income",0) #收入
            ctr = data.get("ctr",0.0); #点击率
            data_dict["logTime"]=yesterday
            data_dict["sourceName"]=adslot_name
            data_dict["sourcePv"]=impression
            data_dict["clickCount"]=click
            data_dict["income"]=income
            data_list.append(data_dict)
            print yesterday,adslot_name,click,impression,income,ctr
    datas["data"] = data_list
    print datas


if __name__ == "__main__":
    from login import login
    session = login(user = "xxxx", pwd = "xxxx")
    get_info(session)
