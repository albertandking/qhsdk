# [qhsdk](https://pypi.org/project/qhsdk/)

## [qhsdk](https://pypi.org/project/qhsdk/) 的介绍

[qhsdk](https://pypi.org/project/qhsdk/) 主要是为 **https://qhkch.com/** 提供 SDK 的 Python 库, 您可以通过 [奇货可查机构VIP接口文档](https://www.showdoc.cc/qhkchapi?page_id=3878436763477725) 了解和查询详细数据接口！

## [qhsdk](https://pypi.org/project/qhsdk/) 服务于 **www.qhkch.com**

<img src="https://static.qhkch.com/dist//style/res/logo.png" align = center/>

## [qhsdk](https://pypi.org/project/qhsdk/) 的特色

[qhsdk](https://pypi.org/project/qhsdk/) 主要改进如下:

1. [qhsdk](https://pypi.org/project/qhsdk/)支持 **Python 3.7** 及以上版本;
2. 目前提供已提供奇货可查全部接口;
3. 提供完善的接口文档, 提高 [qhsdk](https://pypi.org/project/qhsdk/) 的易用性;

# 安装方法

```
pip install qhsdk
```

# 升级方法

```
pip install qhsdk --upgrade
```

# 快速入门

目标数据: 奇货可查-商品-持仓数据接口

示例代码:

```python
import qhsdk as qh
pro = qh.pro_api(token="此处输入您的token, 请联系奇货可查获取！")
variety_positions_df = pro.variety_positions(fields="shorts", code="rb1810", date="2018-08-08")
print(variety_positions_df)
```

示例结果:

```
   broker  short  short_chge
0    银河期货  60987       -4228
1    永安期货  57520       -1071
2    中信期货  38120        -620
3    国泰君安  36498         528
4    方正中期  32105        4444
5    海通期货  29638       -2783
6    东海期货  29250         450
7    光大期货  28458         -84
8    南华期货  27853        -144
9    中辉期货  26101        -553
10   中大期货  23761        1572
11   鲁证期货  22501        -598
12   兴证期货  22262        -842
13   东证期货  21675        -686
14   徽商期货  18966        -607
15   中信建投  18583        -625
16   华泰期货  17076       -5797
17   国投安信  16808         349
18   申银万国  14876         376
19   广发期货  14588       -2196
20   大地期货      0      -14603
```

# 特别说明

## 致谢

特别感谢 [AkShare](https://github.com/jindaxiang/akshare) 项目提供借鉴学习的机会;

## 声明

1. [qhsdk](https://pypi.org/project/qhsdk) 提供的数据仅供参考, 不构成任何投资建议;
2. 任何基于 [qhsdk](https://pypi.org/project/qhsdk) 进行研究的投资者请注意数据风险;
3. [qhsdk](https://pypi.org/project/qhsdk) 的使用请遵循奇货可查网站的用户协议;
4. [qhsdk](https://pypi.org/project/qhsdk) 使用产生的所有问题的最终解释权归奇货可查网站所有;

# 版本更新说明
```
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
```