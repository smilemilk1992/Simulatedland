# -*- coding: utf-8 -*-
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
import LoginCase.LogHelp as log;
import datetime
import json
import logging
import time
def get_info(session):
    '''
    :param session: 登陆session
    :return: 内容数据
    :name: 好看
    '''
    logger = log.getLog("mmp")
    data = {"platformId": 10, "accountId": 1}
    data["date"] = datetime.datetime.now().strftime('%Y%m%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    url = "https://mmp.levect.com/image/report?pageSize=10000&pageNo=1"
    header={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Referer":"https://mmp.levect.com/page/imageReport",
    }
    datas={
        "startReleaseTime":"2019-02-01",
        "endReleaseTime":yesterday
    }
    rs = session.post(url,headers=header,data=datas)
    json_data = json.loads(rs.text)
    data_list = json_data.get("data",{}).get("list",[])
    list_data = []
    for d in data_list:
        dict_data={}
        clickCount=d.get("imgPv",0)
        tm=d.get("releaseTime",0)
        title = d.get("title","")
        # dict_data["logTime"]=yesterday.replace("-","")
        dict_data["logttime"]=time.strftime("%Y%m%d", time.localtime(tm/1000))
        dict_data["title"]=title
        dict_data["isJingpin"]=1
        dict_data["clickCount"]=clickCount
        list_data.append(dict_data)
        print title,1,clickCount
    data["data"] = list_data
    logger.info(data)
    print data


if __name__ == "__main__":
    from login import login
    session = login(user = "xxxx", pwd = "xxxx")
    get_info(session)


