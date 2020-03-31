# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Author: Albert King
date: 2020/2/13 21:33
contact: jindaxiang@163.com
desc: 接口测试文件
"""
from qhsdk.pro.data_pro import pro_api

pro = pro_api(token="")

# 商品-持仓数据-多头龙虎榜
variety_positions_longs_df = pro.variety_positions(fields="longs", code="rb1810", date="2018-08-08")
print(variety_positions_longs_df)

# 商品-持仓数据-空头龙虎榜
variety_positions_shorts_df = pro.variety_positions(fields="shorts", code="rb1810", date="2018-08-08")
print(variety_positions_shorts_df)

# 商品-合约行情数据
variety_quotes_df = pro.variety_quotes(fields="", code="rb1810", date="2018-08-08")
print(variety_quotes_df)

# 商品-商品沉淀资金数据接口
variety_money_df = pro.variety_money(fields="", symbol="RB", date="2018-08-08")
print(variety_money_df)

# 商品-合约多空比数据
variety_bbr_df = pro.variety_bbr(fields="", code="rb1810", date="2018-08-08")
print(variety_bbr_df)



variety_net_positions_df = pro.variety_net_positions(fields="", symbol="RB", broker="永安期货", date="2018-08-08")
print(variety_net_positions_df)

variety_quotes_df = pro.variety_quotes(fields="", code="rb1810", date="2018-08-08")
print(variety_quotes_df)

variety_money_df = pro.variety_money(fields="", symbol="RB", date="2018-08-08")
print(variety_money_df)

variety_bbr_df = pro.variety_bbr(fields="", code="rb1810", date="2018-08-08")
print(variety_bbr_df)

variety_net_money_chge_df = pro.variety_net_money_chge(fields="", code="rb1810", date="2018-08-08")
print(variety_net_money_chge_df)

variety_net_money_df = pro.variety_net_money(fields="", code="rb1810", date="2018-08-08")
print(variety_net_money_df)

variety_total_money_df = pro.variety_total_money(fields="", code="rb1810", date="2018-08-08")
print(variety_total_money_df)

# 席位
broker_positions_df = pro.broker_positions(fields="", broker="永安期货", date="2018-08-08")
print(broker_positions_df)

# 指数
index_info_df = pro.index_info(fields="", index_id="index0070c0eb-93ba-2da9-6633-fa70cb90e959")
print(index_info_df)
