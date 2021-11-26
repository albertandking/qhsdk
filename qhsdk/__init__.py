"""qhsdk 是基于 Python 的用于奇货可查客户服务的专用 SDK 接口"""

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

0.1.1
预览版

0.1.2
增加 token 使用说明

0.1.3
增加 inventory 参数类型二

0.1.4
新增: 合约持仓数据接口, 商品持仓数据接口, 修复部分接口与文档一致

0.1.5
新增: 增加 broker_positions_process 中 start_date 和 end_date 可选参数

0.1.6
新增: 增加 variety_calc_positions 接口

0.1.7
修改: 修改 variety_all 接口, 新增 3 个字段

0.1.8
新增: 新增 variety_net_position_list 接口

0.1.9
新增: 同步文档 2021年11月25日 版本
"""

__version__ = '0.1.9'
__author__ = 'qhsdk'


"""
for qhsdk pro api
"""
from qhsdk.pro.data_pro import pro_api

"""
for qhsdk pro api token set
"""
from qhsdk.utils.token_process import set_token
