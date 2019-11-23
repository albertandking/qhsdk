# [qhsdk](https://pypi.org/project/qhsdk/)
(本文档更新于 **2019-11-23**; 如发现库和文档相关问题, 请联系 [qhsdk](https://github.com/jindaxiang/qhsdk) 的作者 **奇货可查**)

## [qhsdk](https://pypi.org/project/qhsdk/) 的介绍

[qhsdk](https://pypi.org/project/qhsdk/) 主要是为 **https://qhkch.com/** 提供 SDK 的 Python 库, 您可以通过 [qhsdk文档](https://pypi.org/project/qhsdk/) 了解和查询详细数据接口！


## [qhsdk](https://pypi.org/project/qhsdk/) 服务于 **www.qhkch.com**

<img src="https://static.qhkch.com/dist//style/res/logo.png" align = center/>

## [qhsdk](https://pypi.org/project/qhsdk/) 的特色

[qhsdk](https://pypi.org/project/qhsdk/) 主要改进如下:

1. 设计符合 RESTful 规范的 API 接口;
2. 支持 Python 3.7.3 及以上版本;
3. 目前提供奇货可查-工具板块接口, 正在开发其他 API 接口;   
4. 提供完善的接口文档, 提高 [qhsdk](https://pypi.org/project/qhsdk/) 的易用性;

# 安装方法

```
pip install qhsdk
```

# 升级方法

**由于目前版本更新迭代, 请在使用前先升级库**

```
pip install qhsdk --upgrade
```

# 快速入门

## 1. 先按照 [Anaconda安装说明及环境配置](#Anaconda安装说明及环境配置)

## 2. 使用 [qhsdk](https://pypi.org/project/qhsdk/) 提供的数据接口

目标网页: https://qhkch.com/ajax/toolbox_nebula.php

路径: 奇货可查-工具-龙虎星云图

查看 [奇货可查-工具-龙虎星云图](https://qhkch.com/ajax/toolbox_nebula.php) 提供的数据

代码:
```python
import qhsdk as qh
pro = qh.pro_api("帐号", "密码")
df = pro.toolbox_nebula()
print(df)
```

结果显示:
```
         0          1           2       3   4
a2001    5 -10.679325   349463900   a2001  豆一
ag1912   3   2.653326  1947907804  ag1912  沪银
ag2006   3  13.353891   846397165  ag2006  沪银
al1911   5 -33.254705   382253375  al1911  沪铝
al1912   3 -10.072681  1012827354  al1912  沪铝
     ..        ...         ...     ...  ..
zc2001   9  -4.527521  1084279140  zc2001  郑煤
zc2005   7  20.085050   452214336  zc2005  郑煤
zn1912  23 -10.902040  1188122720  zn1912  沪锌
zn2001  12  -9.745322  1282685360  zn2001  沪锌
zn2002   2  -8.354605   599360000  zn2002  沪锌
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
```