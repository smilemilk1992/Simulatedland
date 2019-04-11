# -*- coding: utf-8 -*-
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
import requests
import datetime
import json

import LoginCase.LogHelp as log;
LIST_URL="https://web.umeng.com/main.php?c=site&a=show&ajax=module=getsitelist&pc=site&pa=show&_=1534065167838"
INFO_URL="https://web.umeng.com/main.php?c=flow&a=trend&ajax=module%3Dsummary%7Cmodule%3DfluxList_currentPage%3D1_pageType%3D30&siteid={}&st={}&et={}"
import logging
def get_list(token):
    logger = log.getLog("umeng")
    data = {"platformId": 9, "accountId": 1}
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    data["date"] = datetime.datetime.now().strftime('%Y%m%d')
    # header = {
    #     "Cookie":"umplus_uc_token={}".format(token),
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    # }
    rs = token.get(LIST_URL)

    json_data = rs.json()
    lists = json_data.get("data",{}).get("getsitelist",{}).get("items",{}).get("main",[])
    data_list=[]
    for list in lists:
        data_dict={}
        siteid = list.get("siteid","")
        name = list.get("name","")
        domain = list.get("domain","")
        url = INFO_URL.format(siteid,yesterday,yesterday)
        info = token.get(url)
        info_json = info.json()
        items = info_json.get("data",{}).get("summary",{}).get("items",{})
        if items:
            pv=items.get("pv",0)
            uv=items.get("uv",0)
            data_dict["logTime"]=yesterday.replace("-","")
            data_dict["url"]=name+"-"+domain
            data_dict["pagePv"]=pv
            data_dict["uv"]=uv
            data_list.append(data_dict)
            print name,pv,uv
    data["data"] = data_list
    logger.info(data)
    print data


if __name__ == "__main__":
    from login import login
    umplus_uc_token = login(user = "xxxx", pwd = "xxxx")
    get_list(umplus_uc_token)
