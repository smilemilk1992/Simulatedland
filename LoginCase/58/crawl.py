# -*- coding: utf-8 -*-
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
import datetime
import LoginCase.LogHelp as log;

def get_info(session):
    '''
    :param session: 登陆session
    :return: 内容数据
    :name:58内容平台数据   11
    '''
    logger = log.getLog("58")
    data = {"platformId": 10, "accountId": 1}
    yesteray = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    data["date"] = datetime.datetime.now().strftime('%Y%m%d')
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }
    d = {
        "endDate": yesteray,
        "page": 1,
        "rows": 10000,
        "startDate": yesteray,
        "type": "byArticle"
    }
    r = session.post("http://mp.58.com/getStatisticsList", data=d,headers=header)
    data_json = r.json()
    rows = data_json.get("rows")
    data_list = []
    for row in rows:
        data_dict={}
        title = row.get("title","")
        pv=row.get("pv",0)
        goodclick=row.get("goodclick",0)
        badclick = row.get("badclick",0)
        share = row.get("share",0)
        data_dict["logTime"]=yesteray.replace("-","")
        data_dict["title"]=title
        data_dict["pv"]=pv
        data_dict["goodclick"]=goodclick
        data_dict["badclick"]=badclick
        data_dict["share"]=share
        data_list.append(data_dict)
        logger.info(title+" "+str(pv)+" "+str(goodclick)+" "+str(badclick)+" "+str(share))
    data["data"] = data_list
    print data


if __name__ == "__main__":
    from login import login
    session = login(user = "xxxxx", pwd = "xxxxxx")
    get_info(session)



