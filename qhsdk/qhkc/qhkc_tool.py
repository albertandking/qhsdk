# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Author: Albert King
date: 2019/9/30 13:58
contact: jindaxiang@163.com
desc: 奇货可查网站目前已经商业化运营, 特提供奇货可查-工具数据接口, 方便您程序化调用
注：期货价格为收盘价; 现货价格来自网络; 基差=现货价格-期货价格; 基差率=(现货价格-期货价格)/现货价格 * 100 %.
"""
from typing import AnyStr

import pandas as pd
import requests

from qhsdk.qhkc.cons import (QHKC_TOOL_FOREIGN_URL,
                             QHKC_TOOL_GDP_URL)


def tool_foreign(url: AnyStr = QHKC_TOOL_FOREIGN_URL):
    """
    奇货可查-工具-外盘比价
    实时更新数据, 暂不能查询历史数据
    :param url: 网址
    :return: pd.DataFrame
    name    base_time base_price latest_price   rate
     伦敦铜  10/08 01:00       5704       5746.5  0.745
     伦敦锌  10/08 01:00    2291.25      2305.75  0.633
     伦敦镍  10/08 01:00      17720      17372.5 -1.961
     伦敦铝  10/08 01:00     1743.5      1742.75 -0.043
     伦敦锡  10/07 15:00      16550        16290 -1.571
     伦敦铅  10/08 01:00    2181.25       2177.5 -0.172
    美原油1  10/08 02:30      52.81        53.05  0.454
    美原油2  10/07 23:00      53.94        53.05  -1.65
    布原油1  10/08 02:30      58.41        58.67  0.445
    布原油2  10/07 23:00      59.54        58.67 -1.461
     美燃油  10/07 23:00     1.9287       1.9102 -0.959
    CMX金  10/08 02:30     1495.9       1496.5   0.04
    CMX银  10/08 02:30     17.457       17.457      0
      美豆  10/07 23:00     916.12       915.88 -0.026
     美豆粕  10/07 23:00     302.75       302.65 -0.033
     美豆油  10/07 23:00      30.02        29.91 -0.366
     美玉米  10/07 23:00     386.38       387.88  0.388
      美糖  10/07 23:30      12.37        12.53  1.293
     美棉花  10/07 23:30      61.69        61.05 -1.037
    """
    payload_id = {
        "page": 1,
        "limit": 10
    }
    r = requests.post(url, data=payload_id)
    print("数据获取成功")
    json_data = r.json()
    name = []
    base_time = []
    base_price = []
    latest_price = []
    rate = []
    for item in json_data["data"]:
        name.append(item["name"])
        base_time.append(item["base_time"])
        base_price.append(item["base_price"])
        latest_price.append(item["latest_price"])
        rate.append(item["rate"])
    temp_df = pd.DataFrame([name, base_time, base_price, latest_price, rate]).T
    temp_df.columns = ["name", "base_time", "base_price", "latest_price", "rate"]
    return temp_df


def tool_nebula(url: AnyStr = QHKC_TOOL_FOREIGN_URL):
    """
    奇货可查-工具-龙虎星云图
    :param url: 网址
    :return: pd.DataFrame
    name    base_time base_price latest_price   rate
     伦敦铜  10/08 01:00       5704       5746.5  0.745
     伦敦锌  10/08 01:00    2291.25      2305.75  0.633
     伦敦镍  10/08 01:00      17720      17372.5 -1.961
     伦敦铝  10/08 01:00     1743.5      1742.75 -0.043
     伦敦锡  10/07 15:00      16550        16290 -1.571
     伦敦铅  10/08 01:00    2181.25       2177.5 -0.172
    美原油1  10/08 02:30      52.81        53.05  0.454
    美原油2  10/07 23:00      53.94        53.05  -1.65
    布原油1  10/08 02:30      58.41        58.67  0.445
    布原油2  10/07 23:00      59.54        58.67 -1.461
     美燃油  10/07 23:00     1.9287       1.9102 -0.959
    CMX金  10/08 02:30     1495.9       1496.5   0.04
    CMX银  10/08 02:30     17.457       17.457      0
      美豆  10/07 23:00     916.12       915.88 -0.026
     美豆粕  10/07 23:00     302.75       302.65 -0.033
     美豆油  10/07 23:00      30.02        29.91 -0.366
     美玉米  10/07 23:00     386.38       387.88  0.388
      美糖  10/07 23:30      12.37        12.53  1.293
     美棉花  10/07 23:30      61.69        61.05 -1.037
    """
    payload_id = {
        "page": 1,
        "limit": 10
    }
    r = requests.post(url, data=payload_id)
    print("数据获取成功")
    json_data = r.json()
    name = []
    base_time = []
    base_price = []
    latest_price = []
    rate = []
    for item in json_data["data"]:
        name.append(item["name"])
        base_time.append(item["base_time"])
        base_price.append(item["base_price"])
        latest_price.append(item["latest_price"])
        rate.append(item["rate"])
    temp_df = pd.DataFrame([name, base_time, base_price, latest_price, rate]).T
    temp_df.columns = ["name", "base_time", "base_price", "latest_price", "rate"]
    return temp_df


def tool_nebula2(url: AnyStr = QHKC_TOOL_FOREIGN_URL):
    """
    奇货可查-工具-牛熊星云图
    :param url: str web-site
    :return: pandas.DataFrame
    name    base_time base_price latest_price   rate
     伦敦铜  10/08 01:00       5704       5746.5  0.745
     伦敦锌  10/08 01:00    2291.25      2305.75  0.633
     伦敦镍  10/08 01:00      17720      17372.5 -1.961
     伦敦铝  10/08 01:00     1743.5      1742.75 -0.043
     伦敦锡  10/07 15:00      16550        16290 -1.571
     伦敦铅  10/08 01:00    2181.25       2177.5 -0.172
    美原油1  10/08 02:30      52.81        53.05  0.454
    美原油2  10/07 23:00      53.94        53.05  -1.65
    布原油1  10/08 02:30      58.41        58.67  0.445
    布原油2  10/07 23:00      59.54        58.67 -1.461
     美燃油  10/07 23:00     1.9287       1.9102 -0.959
    CMX金  10/08 02:30     1495.9       1496.5   0.04
    CMX银  10/08 02:30     17.457       17.457      0
      美豆  10/07 23:00     916.12       915.88 -0.026
     美豆粕  10/07 23:00     302.75       302.65 -0.033
     美豆油  10/07 23:00      30.02        29.91 -0.366
     美玉米  10/07 23:00     386.38       387.88  0.388
      美糖  10/07 23:30      12.37        12.53  1.293
     美棉花  10/07 23:30      61.69        61.05 -1.037
    """
    payload_id = {
        "page": 1,
        "limit": 10
    }
    r = requests.post(url, data=payload_id)
    print("数据获取成功")
    json_data = r.json()
    name = []
    base_time = []
    base_price = []
    latest_price = []
    rate = []
    for item in json_data["data"]:
        name.append(item["name"])
        base_time.append(item["base_time"])
        base_price.append(item["base_price"])
        latest_price.append(item["latest_price"])
        rate.append(item["rate"])
    temp_df = pd.DataFrame([name, base_time, base_price, latest_price, rate]).T
    temp_df.columns = ["name", "base_time", "base_price", "latest_price", "rate"]
    return temp_df


def tool_gdp(url: AnyStr = QHKC_TOOL_GDP_URL):
    """
    奇货可查-工具-各地区经济数据
    实时更新数据, 暂不能查询历史数据
    :param url:
    :return: pandas.DataFrame
    国家  国内生产总值 国内生产总值YoY 国内生产总值QoQ  ...       预算       债务   经常账户       人口
     美国   20494     2.30%     2.00%  ...   -3.80%  106.10%  -2.40   327.17
    欧元区   13670     1.20%     0.20%  ...   -0.50%   85.10%   2.90   341.15
     中国   13608     6.20%     1.60%  ...   -4.20%   50.50%   0.40  1395.38
     日本    4971     1.00%     0.30%  ...   -3.80%  238.20%   3.50   126.25
     德国    3997     0.40%    -0.10%  ...    1.70%   60.90%   7.30    82.85
     英国    2825     1.30%    -0.20%  ...   -2.00%   84.70%  -3.90    66.19
     法国    2778     1.40%     0.30%  ...   -2.50%   98.40%  -0.30    67.19
     印度    2726     5.00%     1.00%  ...   -3.42%   68.30%  -2.30  1298.04
    意大利    2074    -0.10%     0.00%  ...   -2.10%  134.80%   2.50    60.48
     巴西    1869     1.00%     0.40%  ...   -7.10%   77.22%  -0.77   208.49
    加拿大    1709     1.60%     0.90%  ...   -0.70%   90.60%  -2.60    37.31
    俄罗斯    1658     0.90%     0.20%  ...    2.70%   13.50%   7.00   146.90
     韩国    1619     2.00%     1.00%  ...   -1.60%   36.60%   4.70    51.61
   澳大利亚    1432     1.40%     0.50%  ...   -0.60%   40.70%  -1.50    25.18
    西班牙    1426     2.00%     0.40%  ...   -2.50%   97.10%   0.90    46.66
    墨西哥    1224    -0.80%     0.00%  ...   -2.00%   46.00%  -1.80   125.33
     印尼    1042     5.05%     4.20%  ...   -1.76%   29.80%  -3.00   264.20
     荷兰     913     1.80%     0.40%  ...    1.50%   52.40%  10.80    17.12
  沙特阿拉伯     782     0.50%     0.00%  ...   -9.20%   19.10%   9.20    33.41
    土耳其     767    -1.50%     1.20%  ...   -2.00%   30.40%  -3.50    82.00
     瑞士     706     0.20%     0.30%  ...    1.30%   27.70%  10.20     8.48
     台湾     589     2.40%     0.67%  ...   -1.90%   30.90%  11.60    23.58
     波兰     586     4.50%     0.80%  ...   -0.40%   48.90%  -0.70    37.98
     瑞典     551     1.00%     0.10%  ...    0.90%   38.80%   2.00    10.12
    比利时     532     1.20%     0.20%  ...   -0.70%  102.00%  -1.30    11.41
    阿根廷     519     0.60%    -0.30%  ...   -5.50%   86.20%  -5.40    44.50
     泰国     505     2.30%     0.60%  ...   -2.50%   41.80%   7.50    66.41
   委内瑞拉     482   -22.50%    -5.40%  ...  -20.00%   23.00%   6.00    31.83
    奥地利     456     1.50%     0.30%  ...    0.10%   73.80%   2.30     8.82
     伊朗     454     1.80%       NaN  ...   -3.90%   44.20%   1.30    82.10
     挪威     435    -0.70%     0.30%  ...    7.30%   36.30%   8.10     5.30
    阿联酋     414     2.20%     1.70%  ...   -1.80%   18.60%   9.10     9.60
   尼日利亚     397     1.94%     2.85%  ...   -2.80%   18.20%   2.30   195.87
    爱尔兰     376     5.80%     0.70%  ...    0.00%   64.80%   9.10     4.84
    以色列     370     3.20%     0.30%  ...   -1.90%   61.00%   1.90     8.97
     南非     366     0.90%     3.10%  ...   -4.40%   55.80%  -3.60    58.78
    新加坡     364     0.10%    -3.30%  ...    0.40%  112.20%  17.70     5.64
     香港     363     0.50%    -0.40%  ...    2.10%   38.40%   4.30     7.48
   马来西亚     354     4.90%     1.00%  ...   -3.70%   51.80%   2.30    32.40
     丹麦     351     2.60%     0.90%  ...    0.50%   34.10%   6.10     5.78
    菲律宾     331     5.50%     1.40%  ...   -3.20%   41.90%  -2.40   107.00
   哥伦比亚     330     3.00%     1.40%  ...   -3.10%   50.50%  -3.80    49.83
   巴基斯坦     313     5.20%     5.79%  ...   -6.60%   72.50%  -4.80   212.22
     智利     298     1.90%     0.80%  ...   -1.70%   25.60%  -3.10    18.75
     芬兰     276     1.20%     0.50%  ...   -0.70%   58.90%  -1.90     5.51
   孟加拉国     274     7.90%     7.90%  ...   -4.80%   27.90%  -3.60   163.70
     埃及     251     5.70%     5.40%  ...   -8.20%   90.50%  -2.40    98.00
     越南     245     7.31%     6.88%  ...   -3.50%   57.50%   3.00    94.67
  捷克共和国     244     2.70%     0.70%  ...    0.90%   32.70%   0.30    10.61
    """
    data = pd.read_html(url, encoding="utf-8")
    columns_list = data[0].columns.tolist()
    columns_list[0] = "国家"
    data[0].columns = columns_list
    return data[0]


if __name__ == "__main__":
    df = tool_foreign()
    print(df)
    df = tool_gdp()
    print(df)
    df = tool_nebula()
    print(df)
