# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Author: Albert King
date: 2019/11/14 23:27
contact: jindaxiang@163.com
desc:
"""
tool_gdp = "https://static.qhkch.com/dist/views/toolbox/gdp.html"
url_api_map = {
    "cdmu": (
        "toolbox_foreign",
    ),
    "cdm": (
        "toolbox_nebula",
        "toolbox_nebula2",
        "toolbox_brokers",
        "env",
        "fund_compare",
        "fund_bs_pie",
        "fund_position_pie",
        "fund_position_chge_pie",
        "fund_deal_pie",
        "fund_big_chge",
        "fund_all"),
    "cddm": (
        "toolbox_lhnx",
    ),
    "non": (
        "gdp",
    ),
}
dict_list = [{value: key} for key, value in url_api_map.items()]
flag = [list(item.values())[0]
        for item in dict_list if "toolbox_lhnx" in list(item.keys())[0]][0]
