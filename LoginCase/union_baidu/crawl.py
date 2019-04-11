# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import requests
import datetime
import json
import time
import sys
reload(sys);
sys.setdefaultencoding('utf8');
import fateadm_api
LOGIN_URL="https://cas.baidu.com/?action=login"

import LoginCase.LogHelp as log;

login_name=[
    {"name":"name1","pwd":"pwd1"},
            {"name":"name2","pwd":"pwd2"}]
#百度统计
def get_session(session,imgcode,name,pwd):
    '''
    :param session:登陆seeeion
    :param imgcode:验证码
    :return: 内容数据
    :name: 百度收入
    '''
    data = {
        "appid": "6",
        "entered_login":name,
        "entered_password":pwd,
        "charset":"utf-8",
        "entered_imagecode":imgcode,
        "fromu":"http://union.baidu.com/assets/jump.html",
        "selfu":"http://union.baidu.com/assets/jump.html",
        "senderr":"1",
        "isajax":"1",
        "login2":""
    }
    header={
        "Referer":"http://union.baidu.com/customerLogin.html?fromu=http://union.baidu.com/client/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }
    rs = session.post(LOGIN_URL,headers=header,data=data)
    session.get("http://union.baidu.com/client/",headers=header)
    get_info(session)
#
#分代码位
def get_info(session):
    logger = log.getLog("union_baidu")
    datas = {"platformId": 1, "accountId": 1}
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y%m%d')
    datas["date"] = datetime.datetime.now().strftime('%Y%m%d')
    url="http://union.baidu.com/v2/client/report/query?begin={begin}&end={end}&timeGranularity=sum&metrics=adPositionView%2Cpageview%2Cclick%2CclickRatio%2Cecpm%2Cincome&pageNo=1&order=desc&orderBy=adPositionName&dimensions=adPositionId%2CadPositionName&filterFields=unionBizTypeId&filterValues=1&pageSize=500".format(
        begin=yesterday,
        end=yesterday
    )
    header={
        # "Cookie":"__cas__st__6={}; __cas__id__6=19548885".format(cas),
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    }
    rs = session.get(url,headers=header)
    json_data = json.loads(rs.text)
    results = json_data.get("data",{}).get("results",[])
    data_list=[]
    for data in results:
        data_dict={}
        sourceId=data.get("adPositionId","")
        sourceName=data.get("adPositionName","")
        sourcePv=data.get("adPositionView",0)
        pagePv = data.get("pageview",0)
        if pagePv==None:
            pagePv=0
        clickCount=data.get("click",0)
        clickRate=data.get("clickRatio",0)
        income=data.get("income",0)
        cpm=data.get("ecpm",0)
        if cpm==None:
            cpm = 0
        if sourcePv==None:
            sourcePv=0
        if clickCount==None:
            clickCount=0
        if clickRate==None:
            clickRate=0
        if income==None:
            income=0
        if clickRate==None:
            clickRate=0

        data_dict["logTime"]=yesterday
        data_dict["sourceId"]=sourceId
        data_dict["sourceName"]=sourceName
        data_dict["sourcePv"]=sourcePv
        data_dict["pagePv"]=pagePv
        data_dict["clickCount"]=clickCount
        data_dict["clickRate"]=clickRate
        data_dict["income"]=income
        data_dict["cpm"]=cpm

        data_list.append(data_dict)
        print sourceId,sourceName,sourcePv,pagePv,clickCount,clickRate,income,cpm

    datas["data"] = data_list
    logger.info(datas)
    print datas






def dowloadimg(name,pwd):
    session = requests.Session()
    tm = int(time.time())
    url="https://cas.baidu.com/?action=image2&appid=6&key={}".format(tm)
    # url="http://cas.baidu.com/?action=image"
    imgresponse = session.get(url, stream=True)  # 以流的方式打开
    image = imgresponse.content
    with open("img.jpg", "wb") as jpg:
        jpg.write(image)

    x = fateadm_api.TestFunc();
    print x
    get_session(session,x,name,pwd)


if __name__ == "__main__":
    for log in login_name:
        name = log.get("name", "")
        pwd = log.get("pwd", "")
        print "start crawl {}".format(name)
        dowloadimg(name,pwd)
    # get_info("")