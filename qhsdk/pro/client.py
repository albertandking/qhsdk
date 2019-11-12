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
        res = requests.post(self.__http_url + api_name + ".php", timeout=self.__timeout, cookies={"PHPSESSID": self.__token})
        result = res.json()
        if "date" not in result.keys():
            if result["code"] != 0:
                raise Exception(result["msg"])
            data = result["data"]
            columns = data["codes"]
            items = data["data"]
            return pd.DataFrame(items, index=columns)
        else:
            if result["code"] != 0:
                raise Exception(result["msg"])
            data = result["data"]
            date = [result["date"]] * len(data)
            return pd.DataFrame(data, index=date)

    def __getattr__(self, name):
        return partial(self.query, name)
