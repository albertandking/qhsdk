# DeepView

## 多头合约池接口

### 接口名称

long_pool

### 接口描述

DeepView多头合约池接口

### 请求参数

|参数名|说明|举例|
|:-----  |:-----|-----   |
|date |查询日期   |2018-08-08|

### 返回参数

|参数名|类型|说明|
|:-----  |:-----|-----      |
|symbol |string   |品种编码  |
|code |string   |合约代号  |

### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")
long_pool_df = pro.long_pool(date="2018-08-08")
print(long_pool_df)
```

### 返回示例

```
      code symbol
0   rb1810     RB
1   rb1901     RB
2    j1809      J
3    j1901      J
4   ap1810     AP
5   ap1901     AP
6   ap1903     AP
7   ap1905     AP
8   cf1809     CF
9   fg1809     FG
10  ma1809     MA
11  rm1901     RM
12  sf1901     SF
13  sm1901     SM
14  sr1809     SR
15  sr1905     SR
16  ta1808     TA
17  ta1903     TA
18  cu1811     CU
19  cu1905     CU
20  al1808     AL
21  zn1808     ZN
22  ni1809     NI
23  au1812     AU
24   b1901      B
25   c1905      C
26  cs1901     CS
27  jd1809     JD
28  jd1901     JD
29   m1809      M
30  pp1809     PP
31  pp1901     PP
32   v1901      V
```

## 空头合约池接口

### 接口名称

short_pool

### 接口描述

DeepView空头合约池

### 请求参数

|参数名|说明|举例|
|:-----  |:-----|-----  |
|date |查询日期   |2018-08-08|

### 返回参数

|参数名|类型|说明|
|:-----  |:-----|-----    |
|symbol |string   |品种编码  |
|code |string   |合约代号  |

### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")
short_pool_df = pro.short_pool(date="2018-08-08")
print(short_pool_df)
```

### 返回示例

```
      code symbol
0    i1901      I
1   hc1810     HC
2   ap1811     AP
3   cf1901     CF
4   oi1809     OI
5   oi1905     OI
6   rm1905     RM
7   sf1809     SF
8   ta1811     TA
9   zc1809     ZC
10  zc1811     ZC
11  zc1901     ZC
12  cu1809     CU
13  cu1810     CU
14  cu1901     CU
15  al1811     AL
16  al1812     AL
17  zn1810     ZN
18  pb1810     PB
19  sn1809     SN
20  ag1812     AG
21  fu1901     FU
22  ru1809     RU
23  ru1811     RU
24  ru1901     RU
25  ru1905     RU
26   a1901      A
27   c1811      C
28  cs1809     CS
29   l1809      L
30   l1901      L
31   m1811      M
32   m1901      M
33   p1809      P
34   p1905      P
35   v1809      V
36   y1809      Y
37   y1901      Y
38   y1905      Y
39  if1808     IF
40  if1809     IF
41  ih1808     IH
```

## 多空领先指标

### 接口名称

market_line

### 接口描述

DeepView多空领先指标

### 请求参数

|参数名|说明|举例|
|:-----  |:-----|-----  |
|- |-   |-|

### 返回参数

|参数名|类型|说明|
|:-----  |:-----|-----    |
|time |int   |时间，格式为“年月日时分”  |
|price |float   |多空领先指标|

### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")
market_line_df = pro.market_line()
print(market_line_df)
```

### 返回示例

```
              time  price
0     202111191459   66.0
1     202111191458   66.0
2     202111191457   67.0
3     202111191456   66.0
4     202111191455   64.0
            ...    ...
8893  202110281342   28.0
8894  202110281341   28.0
8895  202110281340   27.0
8896  202110281339   26.0
8897  202110281338   26.0
```

## 支撑压力位

### 接口名称

hg

### 接口描述

DeepView支撑压力位

### 请求参数

|参数名|说明|举例|
|:-----  |:-----|-----  |
|- |-   |-|

### 返回参数

|参数名|类型|说明|
|:-----  |:-----|-----    |
|variety |string   |品种名称  |
|code |string   |合约编码|
|current_price |float   |最新价格|
|time |time   |最新交易时间|
|min3 |string   |3分钟周期信息|
|min15 |string   |15分钟周期信息|
|min60 |string   |60分钟周期信息|

### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")
hg_df = pro.hg()
print(hg_df)
```

### 返回示例

```
   variety  ...                             min60
0       沪铅  ...  震荡，压力：15425-15455，支撑：15210-15240
1       花生  ...                   偏空，压力：8516-8528
2       豆粕  ...                   偏多，支撑：3082-3088
3       棉花  ...  震荡，压力：21445-21475，支撑：20950-20980
4       豆油  ...      震荡，压力：9580-9592，支撑：9434-9446
5       沪银  ...                   偏空，压力：5073-5079
6       菜粕  ...      震荡，压力：2722-2728，支撑：2644-2650
7       纯碱  ...                   偏多，支撑：2321-2327
8       焦煤  ...               偏空，压力：2501.5-2504.5
9       鸡蛋  ...      震荡，压力：4574-4580，支撑：4453-4459
10      玻璃  ...                   偏多，支撑：1764-1770
11      焦炭  ...                   偏多，支撑：2370-2373
12     棕榈油  ...                   偏多，支撑：9200-9212
13      沪铝  ...  震荡，压力：19315-19345，支撑：18855-18885
14      PP  ...                   偏空，压力：9238-9244
15      原油  ...                 偏多，支撑：492.3-492.9
16     PTA  ...                   偏空，压力：5014-5026
17     螺纹钢  ...                   偏多，支撑：4319-4325
18      热卷  ...                   偏多，支撑：4503-4509
19      苹果  ...                   偏多，支撑：5999-6005
20      豆一  ...      震荡，压力：6242-6248，支撑：6175-6181
21      沪镍  ...               偏空，压力：153940-154000
22     燃料油  ...                   偏多，支撑：2797-2803
23      NR  ...                 偏空，压力：12220-12250
24      沪铜  ...                 偏多，支撑：70210-70270
25     不锈钢  ...  震荡，压力：17560-17590，支撑：17105-17135
26      沪锌  ...  震荡，压力：23850-23880，支撑：23030-23060
27      尿素  ...                   偏多，支撑：2236-2242
28     PVC  ...                   偏空，压力：8839-8869
29     动力煤  ...                 偏空，压力：918.4-919.6
30      白糖  ...                   偏空，压力：5930-5936
31      纸浆  ...                   偏多，支撑：5314-5326
32      塑料  ...                   偏空，压力：9200-9230
33      沥青  ...                   偏空，压力：3096-3108
34      菜油  ...  震荡，压力：12783-12789，支撑：12582-12588
35     苯乙烯  ...                   偏空，压力：8159-8165
36      淀粉  ...      震荡，压力：3187-3193，支撑：3085-3091
37      玉米  ...                   偏空，压力：2665-2671
38     铁矿石  ...                 偏多，支撑：542.5-545.5
39      红枣  ...  震荡，压力：17635-17665，支撑：16785-16815
40      锰硅  ...                   偏空，压力：7946-7958
41     低硫油  ...                   偏多，支撑：3625-3631
42      豆二  ...      震荡，压力：4225-4231，支撑：4177-4183
43      沪锡  ...               偏空，压力：286300-286360
44     乙二醇  ...                   偏空，压力：6766-6772
45      硅铁  ...      震荡，压力：8986-8998，支撑：8574-8586
46      甲醇  ...                   偏空，压力：3475-3481
47      短纤  ...      震荡，压力：6944-6956，支撑：6824-6836
48      橡胶  ...                 偏空，压力：15285-15315
49      生猪  ...                 偏多，支撑：15765-15795
50      沪金  ...               偏空，压力：373.84-373.96
```

## 相关性

### 接口名称

correlation

### 接口描述

DeepView相关性

### 请求参数

|参数名|说明|举例|
|:-----  |:-----|-----  |
|varieties |查询品种，多品种用半角逗号（,）分割   |螺纹钢,铁矿石|
|start	 |查询开始日期	   |2020-11-25|
|end		 |查询结束日期		   |2020-11-25|

### 返回参数

|参数名|类型|说明|
|:-----  |:-----|-----    |
|code_a:code_b |string   |a、b两个合约在指定时间段的相关性，取值范围是[-100, 100]  |

### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")
correlation_df = pro.correlation(varieties='螺纹钢,铁矿石', start='2020-11-25', end='2020-11-25')
print(correlation_df)
```

### 返回示例

```
         correlation
RB0:RB0            1
RB0:I0             0
I0:RB0             0
I0:I0              1
```