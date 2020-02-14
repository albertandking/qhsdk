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

0.0.7
更新 README 文档

0.0.8
第二版接口测试

0.0.9
更新说明文档

0.1.0
更新测试文件
"""

__version__ = '0.1.0'
__author__ = 'Albert King'


"""
for qhsdk pro api
"""
from qhsdk.pro.data_pro import pro_api

"""
for qhsdk pro api token set
"""
from qhsdk.utils.token_process import set_token
