# [qhsdk](https://pypi.org/project/qhsdk/)
(本文档更新于 **2019-11-11**; 如发现库和文档相关问题, 请联系 [qhsdk](https://github.com/jindaxiang/qhsdk) 的作者 **Albert King**: jindaxiang@163.com)

您也可以加入QQ群答疑解难: 326900231

<a target="_blank" href="https://shang.qq.com/wpa/qunwpa?idkey=aacb87089dd5ecb8c6620ce391de15b92310cfb65e3b37f37eb465769e3fc1a3"><img border="0" src="https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/qq/akshare_md_fold_1569925684166.png" alt="qhsdk官方" title="qhsdk官方"></a>

## [qhsdk](https://pypi.org/project/qhsdk/) 的介绍


[qhsdk](https://pypi.org/project/qhsdk/) 于 **2019-11-11** 正式发布, 请访问 [qhsdk文档](https://pypi.org/project/qhsdk/) 了解和查询数据接口！


[qhsdk](https://pypi.org/project/qhsdk/) 的特点是获取的是相对权威的金融数据网站公布的原始数据, 广大数据科学家可以利用原始数据进行各数据源之间的交叉验证, 进而再加工, 从而得出科学的结论.

**[qhsdk](https://pypi.org/project/qhsdk/) 后续会基于学术论文和金融工程研究报告来添加更多指标, 提供相应的计算方法, 敬请关注.**

## [qhsdk](https://pypi.org/project/qhsdk/) 的服务于 **www.qhkch.com**


<img src="https://static.qhkch.com/dist//style/res/logo.png" align = center/>

## [qhsdk](https://pypi.org/project/qhsdk/) 的特色

[qhsdk](https://pypi.org/project/qhsdk/) 主要改进如下:

1. Python 语法符合 [PEP8](https://www.python.org/dev/peps/pep-0008/) 规范, 统一接口函数的命名;
2. 支持 Python 3.7 以上版本;
3. 持续维护由于目标网页变化而导致的部分函数运行异常问题;

    3.1 增加[奇货可查网站](https://qhkch.com/)数据接口, 提供奇货可查指数数据(开发中);
    
4. 提供完善的接口文档, 提高 [qhsdk](https://pypi.org/project/qhsdk/) 的易用性;


# 安装方法

```
pip install qhsdk
```

# 升级方法

**p.s. 由于目前版本更新迭代比较频繁, 请在使用前先升级库**
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

# Anaconda安装说明及环境配置

## Anaconda 安装说明

Anaconda 是集成了上千个常用库的 Python 发行版本, 通过安装 Anaconda 能简化环境管理工作, 非常推荐使用. 
作者基于目前 Python2 即将停止更新, 且目前大部分使用者电脑系统基本都是 64 位, 所以建议选择 Python3.7.3 64 位版本
同时, 根据您电脑的操作系统选择相对应的版本: Windows 版, MacOS 或 Linux 版的 64 位安装包.

## 安装演示(以 64 位 windows 版本为例)

下图中红框为 64 位 Windows 选择的版本:

![](https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/readme/anaconda/anaconda_download.png)

在这里, 作者建议下载 Anaconda3-2019.07, 点击下载 [最新版 Anaconda 官方下载链接](https://repo.anaconda.com/archive/Anaconda3-2019.07-Windows-x86_64.exe)

双击如下图标进行安装:

![](https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/readme/anaconda/anaconda_icon.png)

点击 Next:

![](https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/readme/anaconda/anaconda_install_1.png)

点击 I Agree:

![](https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/readme/anaconda/anaconda_install_2.png)

点击 Just me --> Next:

![](https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/readme/anaconda/anaconda_install_3.png)

修改 Destination Folder 为如图所示:

![](https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/readme/anaconda/anaconda_install_4.png)

勾选下图红框选项(以便于把安装的环境加入系统路径) --> Install:

![](https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/readme/anaconda/anaconda_install_5.png)

安装好后, 找到 Anaconda Prompt 窗口:

![](https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/readme/anaconda/virtual_env/anaconda_prompt.png)

输入 python, 如果如下图所示, 即已经在系统目录中安装好 anaconda3 的环境. 

![](https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/readme/anaconda/virtual_env/anaconda_prompt_1.png)

创建虚拟环境命令:

```
conda create -n ak_test python=3.7.3
```

输入上述命令后出现确认, 输入 y

```
Proceed 输入 y
```

显示出最后一个红框内容则创建虚拟环境成功.

![](https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/readme/anaconda/virtual_env/anaconda_prompt_2.png)

在虚拟环境中安装 [qhsdk](https://pypi.org/project/qhsdk/). 输入如下内容, 会在全新的环境中自动安装所需要的依赖包

激活已经创建好的 ak_test 虚拟环境

```
conda activate ak_test
```

在 ak_test 虚拟环境中安装并更新 [qhsdk](https://pypi.org/project/qhsdk/)

```
pip install qhsdk --upgrade
```

![](https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/readme/anaconda/virtual_env/anaconda_prompt_3.png)

在安装完毕后, 输入 **python** 进入虚拟环境中的 Python

```
python
```

在 ak_test 虚拟环境的 Python 环境里面输入:

```python
import qhsdk as qh
qh.__doc__
```

显示出如下图则虚拟环境和 [qhsdk](https://pypi.org/project/qhsdk/) 安装成功:

![](https://jfds-1252952517.cos.ap-chengdu.myqcloud.com/akshare/readme/anaconda/virtual_env/anaconda_prompt_4.png)

还可以在 ak_test 虚拟环境的 Python 环境中输入如下代码可以显示 [qhsdk](https://pypi.org/project/qhsdk/) 的版本

```python
import qhsdk as qh
qh.__version__
```


# 每日监控下载配置
本地配置好 Anaconda, 以及通过 pip 安装好 qhsdk 后, 在 github 上下载示例文件, 即按照下图选择. 

[https://github.com/jindaxiang/akshare](https://github.com/jindaxiang/akshare)

![image](http://m.qpic.cn/psb?/V12c0Jww0zKwzz/oT9PEhN0Knbv7Q.hPIO9TyuDkHl*il8K92GILqm4QHQ!/b/dL4AAAAAAAAA&bo=EgTRAwAAAAADB.Y!&rf=viewer_4)

解压下载的文件, 然后来到 example 目录下, 设置 setting 配置文件
root 设置为 [qhsdk](https://pypi.org/project/qhsdk/) 爬数据时存储的默认目录(需要保证目录存在), qqEmail 和 secret 为爬取到数据时把数据发送给自己的 qq 邮箱账号和密码. 需要开通SMTP服务, 如果不需要自己邮件提醒, 就不用设置(也不要改默认的qqEmail和secret). 
![](http://m.qpic.cn/psb?/V12c0Jww0zKwzz/Ja.CVdg.fgrxFKW2jBGJqT53b7qCNSY*DwmbGDBS928!/b/dL8AAAAAAAAA&bo=aQRbAwAAAAADBxc!&rf=viewer_4)

最后双击 monitor.cmd 即完成, 每日 17 点自动下载数据. 


# QQ邮箱SMTP服务设置
在利用 Python 程序发送 QQ 邮件时, 需要开启 QQ 邮件的 SMTP 服务, 操作方法如下, 第一步打开 QQ 邮箱, 点"设置". 

![](http://m.qpic.cn/psb?/V12c0Jww0zKwzz/bvaIA.HUOZL.pKsEPMB4gj8dvT*9TLy*6x7zIKwzPQE!/b/dLwAAAAAAAAA&bo=HgR5AgAAAAADB0M!&rf=viewer_4)

找到"账户", 并下拉
![](http://m.qpic.cn/psb?/V12c0Jww0zKwzz/umgOdgp4tRuhiDOmtbLXiVVIPZ*87HeSQBaVHd1jPcY!/b/dL8AAAAAAAAA&bo=HATrAAAAAAADF8E!&rf=viewer_4)

开启以下的两项服务, 并生成授权码, 授权码为 Python 程序通过 SMTP 发送邮件的密码, 即上一节文档的 secret(不同于QQ邮箱登录密码)
![](http://m.qpic.cn/psb?/V12c0Jww0zKwzz/XavUKCeQ3fSqFXFTPBU0kJN9eIoFMtOApCEp7ZNDRqs!/b/dL8AAAAAAAAA&bo=iAOWAgAAAAADFy0!&rf=viewer_4)

在启动服务的过程中, 如果该 QQ 账户没有绑定过手机号, 可能会需要验证, 这里不再赘述. 


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
```

# 开发问题反馈
```
奇货可查-工具
    1. 做映射到每个接口
    2. 做每个映射的解析函数

```