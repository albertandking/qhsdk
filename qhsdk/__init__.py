"""qhsdk 是基于 Python 的为奇货可查客户服务的专用API接口"""

"""
0.0.1
发布测试版本

0.0.2
调试接口

0.0.3
增加lxml=4.4.1

0.0.4
更新说明文档

0.0.5
新增通过用户名和密码登录并访问VIP资源功能

0.0.6
修正导入问题
"""

__version__ = '0.0.6'
__author__ = 'Albert King'

"""
奇货可查-工具
"""
from qhsdk.qhkc.qhkc_tool import (tool_foreign,
                                  tool_gdp,
                                  tool_nebula)

"""
for qhsdk pro api
"""
from qhsdk.pro.data_pro import (pro_api)