# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Author: qhsdk
Date: 2023/3/3 19:20
Desc: qhsdk 的 pypi 基本信息文件
"""
import re
import ast

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


def get_version_string():
    """
    get the qhsdk version number
    :return: str version number
    """
    with open("qhsdk/__init__.py", "rb") as f:
        version_line = re.search(
            r"__version__\s+=\s+(.*)", f.read().decode("utf-8")
        ).group(1)
        return str(ast.literal_eval(version_line))


setuptools.setup(
    name="qhsdk",
    version=get_version_string(),
    author="qhkch",
    author_email="jindaxiang@163.com",
    license="MIT",
    description="A Python SDK for www.qhkch.com!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jindaxiang/qhsdk",
    packages=setuptools.find_packages(),
    install_requires=[
        "pandas>=0.25.3",
        "requests>=2.22.0",
    ],
    package_data={'': ['*.py', '*.json', "*.pk"]},
    keywords=['futures finance sdk'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7',
)
