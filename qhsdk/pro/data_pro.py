# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Author: Albert King
date: 2019/11/10 22:52
contact: jindaxiang@163.com
desc: 数据接口初始化
"""
from qhsdk.pro import client


def pro_api(username='', password=""):
    """
    初始化 pro API, 传入您的用户名和密码
    """
    if (username and password) is not None and (username != "" and password != ""):
        pro = client.DataApi(username, password)
        return pro
    else:
        raise Exception('api init error.')


if __name__ == '__main__':
    pro_api = pro_api("18328746465", "jindaxiang")
    # df = pro_api.toolbox_foreign()
    # print(df)
    # df = pro_api.toolbox_nebula()
    # print(df)
    # df = pro_api.toolbox_nebula2()
    # print(df)
    # df = pro_api.toolbox_brokers()
    # print(df)
    # df = pro_api.toolbox_lhnx()
    # print(df)
    # df = pro_api.env()
    # print(df)
    # df = pro_api.gdp()
    # print(df)
    # df = pro_api.fund_compare()
    # print(df)
    # df1, df2 = pro_api.fund_bs_pie()
    # print(df1)
    # print(df2)
    # df1, df2 = pro_api.fund_position_pie()
    # print(df1)
    # print(df2)
    # df1, df2 = pro_api.fund_position_chge_pie()
    # print(df1)
    # print(df2)
    # df = pro_api.fund_deal_pie()
    # print(df)
    # df = pro_api.fund_big_chge()
    # print(df)
    df1, df2 = pro_api.fund_all()
    print(df1)
    print(df2)





