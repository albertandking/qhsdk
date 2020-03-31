# 基本面

## 基差数据

### 接口名称

basis

### 接口描述

基差数据接口

### 请求参数

|参数名|说明|举例|
|:-----  |:-----|-----                           |
|variety |品种编码   |RB|
|date |查询日期   |2018-08-08|

### 返回参数

|参数名|类型|说明|
|:-----  |:-----|-----                           |
|trans_date |date   |查询日期  |
|spot |float   |现货价格  |
|basis |float   |基差，基差 = 现货价格 - 期货价格  |
|basis_rate |float   |基差率，基差率 = (现货价格 - 期货价格) / 现货价格 x 100%  |

### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")  # 此处token默认会转存到您本地，仅需要输入一次
basis_df = pro.basis(variety="RB", date="2018-08-08")
print(basis_df)
```

### 返回示例

```
                 basis
trans_date  2018-08-08
spot              4429
basis              193
basis_rate     4.35764
```

## 期限结构

### 接口名称

term_structure

### 接口描述

期限结构接口

### 请求参数

|参数名|说明|举例|
|:-----  |:-----|-----                           |
|variety |品种编码   |RB|
|date |查询日期   |2018-08-08|

### 返回参数

|参数名|类型|说明|
|:-----  |:-----|-----                           |
|code |string   |合约代号  |
|close |float   |收盘价  |

### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")  # 此处token默认会转存到您本地，仅需要输入一次
term_structure_df = pro.term_structure(variety="RB", date="2018-08-08")
print(term_structure_df)
```

### 返回示例

```
    close    code
0    4200  rb1808
1    4322  rb1809
2    4236  rb1810
3    4191  rb1811
4    4139  rb1812
5    4094  rb1901
6    4017  rb1902
7    3987  rb1903
8    3977  rb1904
9    3918  rb1905
10   3889  rb1906
11   3881  rb1907
```

## 库存数据

### 接口名称

inventory

### 接口描述

库存数据接口

### 请求参数

|参数名|说明|举例|
|:-----  |:-----|-----                           |
|variety |品种编码   |RB|
|date |查询日期   |2018-08-08|

### 返回参数

|参数名|类型|说明|
|:-----  |:-----|-----                           |
|trans_date |date   |查询日期  |
|vol |float   |库存数据量  |

### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")  # 此处token默认会转存到您本地，仅需要输入一次
inventory_df = pro.inventory(variety="RB", date="2018-08-08")
print(inventory_df)
```

### 返回示例

```
             inventory
trans_date  2018-08-08
vol             605.76
```

## 利润数据

### 接口名称

profit

### 接口描述

利润数据接口

### 请求参数

|参数名|说明|举例|
|:-----  |:-----|-----                           |
|variety |品种编码   |RB|
|date |查询日期   |2018-12-08|

### 返回参数

|参数名|类型|说明|
|:-----  |:-----|-----                           |
|trans_date |date   |查询日期  |
|profit |float   |利润，折盘面价格  |
|profit_rate |float   |利润率  |

### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")  # 此处token默认会转存到您本地，仅需要输入一次
profit_df = pro.profit(variety="RB", date="2019-12-12")
print(profit_df)
```

### 返回示例

```
                 profit
trans_date   2019-12-12
profit              559
profit_rate       16.58
```

## 现货贸易商报价

### 接口名称

trader_prices

### 接口描述

现货贸易商报价接口

### 请求参数

|参数名|说明|举例|
|:-----  |:-----|-----                           |
|variety |品种编码   |RB|
|date |查询日期   |2018-08-08|

### 返回参数

|参数名|类型|说明|
|:-----  |:-----|-----                           |
|name |string   |品种名称  |
|price |float   |贸易商报价  |
|band |string   |品牌  |
|model |string   |型号、规格  |
|unit |string   |单位  |

### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")  # 此处token默认会转存到您本地，仅需要输入一次
trader_prices_df = pro.trader_prices(variety="RB", date="2020-03-30")
print(trader_prices_df)
```

### 返回示例

```
  band                      model name  price unit
0   永钢  品种:Ⅲ级螺纹钢;牌号:HRB400;规格:Φ16  螺纹钢   3500  元/吨
1   永钢  品种:Ⅲ级螺纹钢;牌号:HRB400;规格:Φ16  螺纹钢   3440  元/吨
2   永钢  品种:Ⅲ级螺纹钢;牌号:HRB400;规格:Φ16  螺纹钢   3440  元/吨
3   中新  品种:Ⅲ级螺纹钢;牌号:HRB400;规格:Φ16  螺纹钢   3320  元/吨
4   镔鑫  品种:Ⅲ级螺纹钢;牌号:HRB400;规格:Φ16  螺纹钢   3380  元/吨
5   永钢  品种:Ⅲ级螺纹钢;牌号:HRB400;规格:Φ16  螺纹钢   3470  元/吨
6   中天  品种:Ⅲ级螺纹钢;牌号:HRB400;规格:Φ16  螺纹钢   3490  元/吨
7   长达  品种:Ⅲ级螺纹钢;牌号:HRB400;规格:Φ16  螺纹钢   3400  元/吨
8   兴鑫  品种:Ⅲ级螺纹钢;牌号:HRB400;规格:Φ16  螺纹钢   3380  元/吨
```

## 跨期套利数据

### 接口名称

intertemporal_arbitrage

### 接口描述

跨期套利数据接口

### 请求参数

|参数名|说明|举例|
|:-----  |:-----|-----                           |
|variety |品种编码   |RB|
|code1 |合约月份1   |01|
|code2 |合约月份2   |05|
|date |查询日期   |2018-08-08|

### 返回参数

|参数名|类型|说明|
|:-----  |:-----|-----                           |
|trans_date |date   |查询日期  |
|code1 |string   |合约1  |
|code2 |string   |合约2  |
|close1 |float   |合约1价格  |
|close2 |float   |合约2价格  |
|spread |float   |价差，合约1价格 - 合约2价格  |

### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")  # 此处token默认会转存到您本地，仅需要输入一次
intertemporal_arbitrage_df = pro.intertemporal_arbitrage(variety="RB", code1="01", code2="05", date="2018-08-08")
print(intertemporal_arbitrage_df)
```

### 返回示例

```
           intertemporal_arbitrage
trans_date              2018-08-08
code1                       rb1901
code2                       rb1905
close1                        4109
close2                        3930
spread                         179
```

## 自由价差数据

### 接口名称

free_spread

### 接口描述

自由价差数据接口

### 请求参数

|参数名|说明|举例|
|:-----  |:-----|-----                           |
|variety1 |品种编码1   |RB|
|code1 |合约月份1   |01|
|variety2 |品种编码2   |HC|
|code2 |合约月份2   |01|
|date |查询日期   |2018-08-08|

### 返回参数

|参数名|类型|说明|
|:-----  |:-----|-----                           |
|trans_date |string   |查询日期  |
|code1 |string   |合约代号1  |
|code2 |string   |合约代号2  |
|code1_close |float   |合约1价格  |
|code2_close |float   |合约2价格  |
|spread |float   |价差，合约1价格 - 合约2价格  |

### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")  # 此处token默认会转存到您本地，仅需要输入一次
free_spread_df = pro.free_spread(variety1="RB", code1="01", variety2="HC", code2="01", date="2018-08-08")
print(free_spread_df)
```

### 返回示例

```
            free_spread
trans_date   2018-08-08
code1            rb1901
code2            hc1901
code1_close        4094
code2_close        4100
spread               -6
```

## 自由价差数据

### 接口名称

free_spread

### 接口描述

自由价差数据接口

### 请求参数

|参数名|说明|举例|
|:-----  |:-----|-----                           |
|variety1 |品种编码1   |RB|
|code1 |合约月份1   |01|
|variety2 |品种编码2   |HC|
|code2 |合约月份2   |01|
|date |查询日期   |2018-08-08|

### 返回参数

|参数名|类型|说明|
|:-----  |:-----|-----                           |
|trans_date |string   |查询日期  |
|code1 |string   |合约代号1  |
|code2 |string   |合约代号2  |
|code1_close |float   |合约1价格  |
|code2_close |float   |合约2价格  |
|spread |float   |价差，合约1价格 - 合约2价格  |

### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")  # 此处token默认会转存到您本地，仅需要输入一次
free_spread_df = pro.free_spread(variety1="RB", code1="01", variety2="HC", code2="01", date="2018-08-08")
print(free_spread_df)
```

### 返回示例

```
            free_spread
trans_date   2018-08-08
code1            rb1901
code2            hc1901
code1_close        4094
code2_close        4100
spread               -6
```
