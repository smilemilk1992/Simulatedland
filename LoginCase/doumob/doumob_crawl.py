# -*- coding: utf-8 -*-
import datetime
import json
import LoginCase.LogHelp as log;
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
media_dict={
    "盖饭娱乐":9206,
    "阿里云-负屏":9244,
    "yunos-详情页底部":9351,
    "金立锁屏-car2":9352,
    "金立锁屏-car1":9353,
    "搜狗浏览器-详情页底部":9358,
    "yunos锁屏：详情页中间":9359,
    "yunos负一屏：详情页中间":9360,
    "金立养生-首页":9368,
    "金立浏览器搞笑-首页-feed1":9369,
    "返回WIFI-APP-首页-feed1":9370,
    "金立锁屏娱乐-底部banner":9408,
    "360详情页底部":9460,
    "360详情页中间2":9461,
    "360详情页中间1":9462,
    "60猜你喜欢":9463,
    "金立锁屏":9219,
    "360悬浮广告":9464,
    "360今日爆点":9465,
    "360为你推荐":9466,
    "今立锁屏3":9853,
    "阿里名站":9879,
    "驾考宝典":9289,
    "盖范wap":10035,
    "中华万年历":10398
}
list_url="https://www.doumob.com/end/app/mediaList"
DATA_URL="https://www.doumob.com/end/app/loadHdggData?startDate={startDate}%2000%3A00%3A00&endDate={endDate}%2023%3A59%3A59&mediaId={mediaId}&hdggadspaceId={hdggadspaceId}"

def get_info(session,token):
    '''
    :param session: 登陆session
    :param token: 登陆token
    :return: 内容数据
    :name:豆盟   5
    '''
    logger = log.getLog("doumob")
    data = {"platformId": 5, "accountId": 1}
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    data["date"]=datetime.datetime.now().strftime('%Y%m%d')

    header = {
        "Referer": "https://www.doumob.com/front/",
        "token": token,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }
    data_list = []
    name_list = session.get(list_url,headers=header)
    lists = json.loads(name_list.text)
    list = lists.get("list",[])
    # print list
    # for k,i in media_dict.items():
    for li in list:
        k=li.get("medianame","")
        i=li.get("id","")
        url = "https://www.doumob.com/end/app/getHdggAdSpaceList?mediaId={}".format(i)
        response = session.get(url, headers=header)
        json_data = json.loads(response.text)
        lists = json_data['list']
        for list in lists:
            adspacename = list['adspacename']
            id = list['id']
            _url = DATA_URL.format(startDate=yesterday, endDate=yesterday,mediaId=i,hdggadspaceId=id)
            content = session.get(_url, headers=header)
            content_json = json.loads(content.text)
            if(content_json['list']):
                data_dict = {}
                data_dict["logTime"]=yesterday.replace("-","")
                data_dict["mediaName"]=k
                data_dict['sourceName']=adspacename
                data_dict['uv']=content_json['list'][0]['uv']
                data_dict['income']=content_json['list'][0]['hdggMoney']
                data_list.append(data_dict)
                print k,adspacename,content_json['list'][0]['uv'],content_json['list'][0]['hdggMoney']
    data["data"] = data_list
    logger.info(data)
    print data


if __name__ == "__main__":
    from login import login
    session,token = login(user = "xxx", pwd = "xxxx")
    get_info(session,token)
