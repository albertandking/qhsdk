# 商品

## 持仓数据

### 接口名称

variety_positions

### 接口描述

持仓数据接口

### 请求参数

|参数名|说明|举例|
|-----  |-----|-----|
|code |合约代号   |rb1810  |
|date |查询日期   |2018-08-08  |

### 返回参数

|参数名|类型|说明|
|:-----  |:-----|-----|
|longs |array   |多头龙虎榜  |
|shorts |array   |空头龙虎榜  |
|broker |string   |席位  |
|long |int   |该席位多头持仓量  |
|long_chge |int   |该席位多头持仓变化量  |
|short |int   |该席位空头持仓量  |
|short_chge |int   |该席位空头持仓变化量  |

### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")  # 此处token默认会转存到您本地，仅需要输入一次
variety_net_positions_df = pro.variety_net_positions(fields="", symbol="RB", broker="永安期货", date="2018-08-08")
print(variety_net_positions_df)
```

### 返回示例

```cmd
{
  "trans_date": "2018-08-08",
  "net_position": 58463
}
```

## 合约行情

### 接口名称

variety_positions

### 接口描述

持仓数据接口

### 请求参数

|参数名|说明|举例|
|-----  |-----|-----|
|code |合约代号   |rb1810  |
|date |查询日期   |2018-08-08  |

### 返回参数

|参数名|类型|说明|
|:-----  |:-----|-----|
|longs |array   |多头龙虎榜  |
|shorts |array   |空头龙虎榜  |
|broker |string   |席位  |
|long |int   |该席位多头持仓量  |
|long_chge |int   |该席位多头持仓变化量  |
|short |int   |该席位空头持仓量  |
|short_chge |int   |该席位空头持仓变化量  |

### 示例代码

```python
from qhsdk import pro_api
pro = pro_api(token="在此处输入您的token，可以通过联系管理员获取")  # 此处token默认会转存到您本地，仅需要输入一次
variety_net_positions_df = pro.variety_net_positions(fields="", symbol="RB", broker="永安期货", date="2018-08-08")
print(variety_net_positions_df)
```

### 返回示例

```cmd
{
  "trans_date": "2018-08-08",
  "net_position": 58463
}
```