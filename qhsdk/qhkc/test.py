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
variety_quotes_df = pro.variety_quotes(code="rb1810", date="2018-08-08")
print(variety_quotes_df)

# 商品-商品沉淀资金数据接口
variety_money_df = pro.variety_money(symbol="RB", date="2018-08-08")
print(variety_money_df)

# 商品-合约多空比数据
variety_bbr_df = pro.variety_bbr(code="rb1810", date="2018-08-08")
print(variety_bbr_df)

# 商品-合约净持仓保证金变化数据
variety_net_money_chge_df = pro.variety_net_money_chge(code="rb1810", date="2018-08-08")
print(variety_net_money_chge_df)

# 商品-合约净持仓保证金数据
variety_net_money_df = pro.variety_net_money(code="rb1810", date="2018-08-08")
print(variety_net_money_df)

# 商品-合约总持仓保证金数据
variety_total_money_df = pro.variety_total_money(code="rb1810", date="2018-08-08")
print(variety_total_money_df)

# 商品-商品的席位盈亏数据
variety_profit_df = pro.variety_profit(symbol="RB", start_date="2018-02-08", end_date="2018-08-08")
print(variety_profit_df)

# 商品-自研指标数据
variety_strategies_df = pro.variety_strategies(code="rb1810", date="2018-08-08")
print(variety_strategies_df)

# 商品-龙虎比排行数据-多头排行
variety_longhu_long_top_df = pro.variety_longhu_top(fields="long", date="2018-08-08")
print(variety_longhu_long_top_df)

# 商品-龙虎比排行数据-空头排行
variety_longhu_short_top_df = pro.variety_longhu_top(fields="short", date="2018-08-08")
print(variety_longhu_short_top_df)

# 商品-牛熊线排行数据-多头排行
variety_niuxiong_long_top_df = pro.variety_niuxiong_top(fields="long", date="2018-08-08")
print(variety_niuxiong_long_top_df)

# 商品-牛熊线排行数据-空头排行
variety_niuxiong_short_top_df = pro.variety_niuxiong_top(fields="short", date="2018-08-08")
print(variety_niuxiong_short_top_df)

# 商品-商品相关研报数据
variety_reports_df = pro.variety_reports(csymbolode="RB", date="2018-08-08")
print(variety_reports_df)

# 商品-商品列表数据
variety_all_df = pro.variety_all()
print(variety_all_df)





variety_net_positions_df = pro.variety_net_positions(symbol="RB", broker="永安期货", date="2018-08-08")
print(variety_net_positions_df)

variety_quotes_df = pro.variety_quotes(code="rb1810", date="2018-08-08")
print(variety_quotes_df)

variety_money_df = pro.variety_money(symbol="RB", date="2018-08-08")
print(variety_money_df)

variety_bbr_df = pro.variety_bbr(code="rb1810", date="2018-08-08")
print(variety_bbr_df)

variety_net_money_chge_df = pro.variety_net_money_chge(code="rb1810", date="2018-08-08")
print(variety_net_money_chge_df)

variety_net_money_df = pro.variety_net_money(code="rb1810", date="2018-08-08")
print(variety_net_money_df)

variety_total_money_df = pro.variety_total_money(code="rb1810", date="2018-08-08")
print(variety_total_money_df)

# 席位
broker_positions_df = pro.broker_positions(broker="永安期货", date="2018-08-08")
print(broker_positions_df)

# 指数
index_info_df = pro.index_info(index_id="index0070c0eb-93ba-2da9-6633-fa70cb90e959")
print(index_info_df)
