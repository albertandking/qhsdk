# 商品

## 持仓数据

### 多头龙虎榜

#### 接口名称

variety_positions

#### 接口描述

持仓数据接口

#### 请求参数

|参数名|说明|举例|
|-----  |-----|-----|
|code |合约代号   |rb1810  |
|date |查询日期   |2018-08-08  |

#### 返回参数

|参数名|类型|说明|
|:-----  |:-----|:-----|
|longs |array   |多头龙虎榜  |
|shorts |array   |空头龙虎榜  |
|broker |string   |席位  |
|long |int   |该席位多头持仓量  |
|long_chge |int   |该席位多头持仓变化量  |
|short |int   |该席位空头持仓量  |
|short_chge |int   |该席位空头持仓变化量  |

#### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")  # 此处token默认会转存到您本地，仅需要输入一次
variety_positions_df = pro.variety_positions(fields="longs", code="rb1810", date="2018-08-08")
print(variety_positions_df)
```

#### 返回示例

```
   broker   long  long_chge
0    永安期货  80565       3075
1    申银万国  65572       2992
2    华泰期货  49279      -1552
3    中信期货  46272       4286
4    海通期货  42596       -286
5    方正中期  41839      -7504
6    鲁证期货  41520       -550
7    银河期货  38892      -2800
8    一德期货  34618      -1378
9    国泰君安  25854      -2188
10   广发期货  21496      -1695
11   国投安信  21494       2193
12   大地期货  20705         23
13   兴证期货  20166       4071
14   浙商期货  20001       -817
15   南华期货  19311      -2173
16   东海期货  18912      -1259
17   东证期货  15956       -192
18   瑞达期货  15648      -2091
19   光大期货  14758       -910
20   中国国际  12772      12772
21   国海良时      0     -15721
```

### 空头龙虎榜

#### 接口名称

variety_positions

#### 接口描述

持仓数据接口

#### 请求参数

|参数名|说明|举例|
|-----  |-----|-----|
|code |合约代号   |rb1810  |
|date |查询日期   |2018-08-08  |

#### 返回参数

|参数名|类型|说明|
|:-----  |:-----|:-----|
|broker |string   |席位  |
|short |int   |该席位空头持仓量  |
|short_chge |int   |该席位空头持仓变化量  |

#### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")  # 此处token默认会转存到您本地，仅需要输入一次
variety_positions_df = pro.variety_positions(fields="shorts", code="rb1810", date="2018-08-08")
print(variety_positions_df)
```

#### 返回示例

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

## 合约行情数据

### 接口名称

variety_quotes

### 接口描述

合约行情数据接口

### 请求参数

|参数名|说明|举例|
|:-----  |:-----|-----|
|code |具体合约代号   |rb1810|
|date |查询日期   |2018-08-08|

### 返回参数

|参数名|类型|说明|
|:-----  |:-----|-----|
|open |float   |开盘价  |
|close |float   |收盘价  |
|high |float   |最高价  |
|low |float   |最低价  |
|volume |int   |成交量  |
|openint |int   |持仓量  |

### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")  # 此处token默认会转存到您本地，仅需要输入一次
variety_quotes_df = pro.variety_quotes(fields="", code="rb1810", date="2018-08-08")
print(variety_quotes_df)
```

### 返回示例

```
              variety_quotes
open                    4237
close                   4236
high                    4278
low                     4205
volume               2620386
openint              2160052
settle_price            4240
```

## 商品沉淀资金数据接口

### 接口名称

variety_money

### 接口描述

商品沉淀资金数据接口

### 请求参数

|参数名|说明|举例|
|:-----  |:-----|-----|
|symbol |品种编码   |RB|
|date |查询日期   |2018-08-08|

### 返回参数

|参数名|类型|说明|
|:-----  |:-----|-----|
|trans_date |date   |查询日期  |
|total_value |float   |沉淀资金量，单位元  |

### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")  # 此处token默认会转存到您本地，仅需要输入一次
variety_money_df = pro.variety_money(fields="", symbol="RB", date="2018-08-08")
print(variety_money_df)
```

### 返回示例

```
            variety_money
trans_date     2018-08-08
total_value   7.46824e+09
```

## 合约多空比数据

### 接口名称

variety_bbr

### 接口描述

合约多空比数据

### 请求参数

|参数名|说明|举例|
|:-----  |:-----|-----|
|code |具体合约代号   |rb1810|
|date |查询日期   |2018-08-08|

### 返回参数

|参数名|类型|说明|
|:-----  |:-----|-----|
|trans_date |date   |查询日期  |
|bbr |float   |多空比  |

### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")  # 此处token默认会转存到您本地，仅需要输入一次
variety_bbr_df = pro.variety_bbr(fields="", code="rb1810", date="2018-08-08")
print(variety_bbr_df)
```

### 返回示例

```
           variety_bbr
trans_date  2018-08-08
bbr            54.5111
```


