# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Author: Albert King
date: 2019/11/10 22:52
contact: jindaxiang@163.com
desc: 数据接口源代码
"""
import pandas as pd
from functools import partial
import requests

from qhsdk.cons import dict_list, tool_gdp


class DataApi:
    __username = ""
    __password = ""
    __token = ""
    __login_url = "https://api.qhkch.com/login"
    __http_url = "https://qhkch.com/ajax/"

    def __init__(self, username, password, timeout=15):
        """
        API接口 username 和 password, 用于用户认证
        :param username: str
        :param password: str
        :param timeout: int
        """
        self.__username = username
        self.__password = password
        self.__timeout = timeout

        res = requests.post(self.__login_url, data={"username": self.__username, "password": self.__password})
        result = res.json()
        if result["code"] != 0:
            raise Exception(result["msg"])
        else:
            self.__token = result["data"]

    def query(self, api_name, fields="", **kwargs):
        flag = [list(item.values())[0] for item in dict_list if api_name in list(item.keys())[0]][0]
        if flag != "non":
            res = requests.post(self.__http_url + api_name + ".php", timeout=self.__timeout, cookies={"PHPSESSID": self.__token})
            result = res.json()
        print(flag)
        if flag == "cdm":
            if result["code"] != 0:
                raise Exception(result["msg"])
            data = result["data"]
            if api_name == "toolbox_brokers":
                return pd.DataFrame([data["dates"], data["series"]]).T
            elif api_name == "env":
                return pd.DataFrame([data["date"], data["data"], data["info"]]).T
            elif api_name == "fund_compare":
                return pd.DataFrame(data["data"])
            elif api_name in ("fund_bs_pie", "fund_position_pie", "fund_position_chge_pie"):
                return pd.DataFrame([data["legends"], data["datas1"]]).T, pd.DataFrame(data["datas2"])
            elif api_name == "fund_deal_pie":
                return pd.DataFrame([data["legends"], data["datas"]]).T
            elif api_name == "fund_all":
                return pd.DataFrame([[data["date"]] * len(data["data"]), data["data"]]).T, pd.DataFrame([[data["date"]] * len(data["data"]), data["links"]])

            else:
                return pd.DataFrame(data)
        elif flag == "cddm":
            if result["code"] != 0:
                raise Exception(result["msg"])
            data = result["data"]
            date = [result["date"]] * len(data)
            return pd.DataFrame(data, index=date)
        elif flag == "cdmu":
            if result["code"] != 0:
                raise Exception(result["msg"])
            data = result["data"]
            return pd.DataFrame(data)
        elif flag == "non":
            if api_name == "gdp":
                data = pd.read_html(tool_gdp, encoding="utf-8")
                columns_list = data[0].columns.tolist()
                columns_list[0] = "国家"
                data[0].columns = columns_list
                return data[0]

    def __getattr__(self, name):
        return partial(self.query, name)
