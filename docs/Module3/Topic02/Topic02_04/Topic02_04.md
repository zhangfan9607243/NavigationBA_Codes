# Topic 2.4 - Pandas 中的数据基本运算

本节开始前，我们先导入 Pandas 库：


```python
import pandas as pd
```

## 1. Pandas 中的列计算

### (1) 简单的列计算

在 Pandas 中，我们可以对 DataFrame 或 Series 进行各种数学运算，例如加、减、乘、除等。Pandas 会自动对齐索引，确保运算的正确性。


```python
df1 = pd.DataFrame({
    "Date": pd.date_range(start='2023-01-01', periods=5, freq='D'),
    "Security": ["A", "A", "A", "A", "A"],
    "Close": [100, 102, 101, 105, 107],
    "Open": [99, 101, 100, 104, 106],
    "High": [101, 103, 102, 106, 108],
    "Low": [98, 100, 99, 103, 105],
    "VWAP": [100.5, 102.5, 101.5, 105.5, 107.5],
    "Volume": [1000, 1100, 1050, 1200, 1300],
})

df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Security</th>
      <th>Close</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>VWAP</th>
      <th>Volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023-01-01</td>
      <td>A</td>
      <td>100</td>
      <td>99</td>
      <td>101</td>
      <td>98</td>
      <td>100.5</td>
      <td>1000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023-01-02</td>
      <td>A</td>
      <td>102</td>
      <td>101</td>
      <td>103</td>
      <td>100</td>
      <td>102.5</td>
      <td>1100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023-01-03</td>
      <td>A</td>
      <td>101</td>
      <td>100</td>
      <td>102</td>
      <td>99</td>
      <td>101.5</td>
      <td>1050</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023-01-04</td>
      <td>A</td>
      <td>105</td>
      <td>104</td>
      <td>106</td>
      <td>103</td>
      <td>105.5</td>
      <td>1200</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023-01-05</td>
      <td>A</td>
      <td>107</td>
      <td>106</td>
      <td>108</td>
      <td>105</td>
      <td>107.5</td>
      <td>1300</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1["Intraday_Return"] = (df1["Close"] - df1["Open"]) / df1["Open"]
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Security</th>
      <th>Close</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>VWAP</th>
      <th>Volume</th>
      <th>Intraday_Return</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023-01-01</td>
      <td>A</td>
      <td>100</td>
      <td>99</td>
      <td>101</td>
      <td>98</td>
      <td>100.5</td>
      <td>1000</td>
      <td>0.010101</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023-01-02</td>
      <td>A</td>
      <td>102</td>
      <td>101</td>
      <td>103</td>
      <td>100</td>
      <td>102.5</td>
      <td>1100</td>
      <td>0.009901</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023-01-03</td>
      <td>A</td>
      <td>101</td>
      <td>100</td>
      <td>102</td>
      <td>99</td>
      <td>101.5</td>
      <td>1050</td>
      <td>0.010000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023-01-04</td>
      <td>A</td>
      <td>105</td>
      <td>104</td>
      <td>106</td>
      <td>103</td>
      <td>105.5</td>
      <td>1200</td>
      <td>0.009615</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023-01-05</td>
      <td>A</td>
      <td>107</td>
      <td>106</td>
      <td>108</td>
      <td>105</td>
      <td>107.5</td>
      <td>1300</td>
      <td>0.009434</td>
    </tr>
  </tbody>
</table>
</div>



在上面的操作中：

- 我们计算了每一天的日内收益率，计算公式为 (收盘价 - 开盘价) / 开盘价
- 本身这个结果是一个新的 Series，我们接下来做的是把这个 Series 存储在一个新的列 "Intraday_Return" 中
- Pandas 在进行列计算时，会自动对齐索引，确保每一行的数据正确地一一对应

### (2) 列的向前向后运算

Pandas 中还提供了对列进行向前或向后的运算，就是 `shift()` 函数

- 这个函数可以将数据向上或向下移动指定的行数，正数是向下移动（或者说取上一行数据），负数是向上移动（或者说取下一行数据），从而实现与前一行或者后一行数据的计算
- 例如，在下面的例子中，我们计算了前一日的收盘价，并基于此计算了每日的收益率：今日收盘价 / 昨日收盘价 - 1


```python
df1["Close_Lag1"] = df1["Close"].shift(1)
df1["Return"] = df1["Close"] / df1["Close"].shift(1) - 1
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Security</th>
      <th>Close</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>VWAP</th>
      <th>Volume</th>
      <th>Intraday_Return</th>
      <th>Close_Lag1</th>
      <th>Return</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023-01-01</td>
      <td>A</td>
      <td>100</td>
      <td>99</td>
      <td>101</td>
      <td>98</td>
      <td>100.5</td>
      <td>1000</td>
      <td>0.010101</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023-01-02</td>
      <td>A</td>
      <td>102</td>
      <td>101</td>
      <td>103</td>
      <td>100</td>
      <td>102.5</td>
      <td>1100</td>
      <td>0.009901</td>
      <td>100.0</td>
      <td>0.020000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023-01-03</td>
      <td>A</td>
      <td>101</td>
      <td>100</td>
      <td>102</td>
      <td>99</td>
      <td>101.5</td>
      <td>1050</td>
      <td>0.010000</td>
      <td>102.0</td>
      <td>-0.009804</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023-01-04</td>
      <td>A</td>
      <td>105</td>
      <td>104</td>
      <td>106</td>
      <td>103</td>
      <td>105.5</td>
      <td>1200</td>
      <td>0.009615</td>
      <td>101.0</td>
      <td>0.039604</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023-01-05</td>
      <td>A</td>
      <td>107</td>
      <td>106</td>
      <td>108</td>
      <td>105</td>
      <td>107.5</td>
      <td>1300</td>
      <td>0.009434</td>
      <td>105.0</td>
      <td>0.019048</td>
    </tr>
  </tbody>
</table>
</div>



在上面的代码中：

- 由于我们使用了 `shift(1)`，所以 "Close_Lag1" 列中的每个值都是 "Close" 列中前一行的值
- 而第一行没有前一行数据，因此对应的值为 NaN

本质上来说， `shift()` 函数就是将上一行数据挪到本行，或者将下一行数据挪到本行，从而实现与前后行数据的计算：

- 这种上下挪数据的操作一定要注意是否有明确的意义
- 比方说，本数据是个时间序列数据，将上一天的收盘价挪到今天来计算收益率是有意义的
- 但是，如果是截面数据，将A公司的数据挪到B公司来就没有意义了

## 2. 数据统计计算

### (1) 按行统计计算

Pandas 提供了丰富的统计计算功能，可以方便地对数据进行描述性统计分析，如求和、均值、中位数、标准差等。

如果按照行进行统计计算，就是将所有行的数据进行计算，得到结果是一个**单一值**。例如：

- 计算均值使用 `mean()` 函数（注意只能应用于数值型的列）：


```python
display(df1['Close'].mean())  # 应用于 Series - 返回单一值
display(df1[['Close', 'Open']].mean())  # 应用于 DataFrame - 返回包含单一值的 Series
```


    np.float64(103.0)



    Close    103.0
    Open     102.0
    dtype: float64


- 计算总和使用 `sum()` 函数：


```python
display(df1['Close'].sum())  # 应用于 Series - 返回单一值
display(df1[['Close', 'Open']].sum())  # 应用于 DataFrame - 返回包含单一值的 Series
```


    np.int64(515)



    Close    515
    Open     510
    dtype: int64


- 计算标准差使用 `std()` 函数：


```python
display(df1['Close'].std())  # 应用于 Series - 返回单一值
display(df1[['Close', 'Open']].std())  # 应用于 DataFrame - 返回包含单一值的 Series
```


    2.9154759474226504



    Close    2.915476
    Open     2.915476
    dtype: float64


- 除此之外还有以下常用的统计计算函数，我们就不一一展示了：

  - `min()`：计算最小值
  - `max()`：计算最大值
  - `median()`：计算中位数
  - `skew()`：计算偏度
  - `kurt()`：计算峰度
  - `var()`：计算方差
  - `count()`：计算非空值的数量，可应用于任何数据类型

除此之外，两列之间的统计计算也可以直接进行，例如：

- 计算两列的相关系数使用 `corr()` 函数：


```python
df1["Close"].corr(df1["Volume"])  # 计算两个 Series 之间的相关系数
```




    np.float64(0.9969527608177988)



- 计算两列之间的协方差使用 `cov()` 函数：


```python
df1["Close"].cov(df1["Volume"])  # 计算两列之间的协方差
```




    np.float64(350.0)



### (2) 按列统计计算

按列统计计算是指对每一列的数据进行计算，得到的结果是一个 Series，我们可以将这个 Series 作为新的行添加到 DataFrame 中

- 按列统计计算使用的函数与按行统计计算相同，例如 `mean()`、`sum()`、`std()` 等
- 只不过我们需要指定参数 `axis=1`，表示按列进行计算


```python
df1["prices_mean_v1"] = df1[["Close", "Open", "High", "Low"]].mean(axis=1)
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Security</th>
      <th>Close</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>VWAP</th>
      <th>Volume</th>
      <th>Intraday_Return</th>
      <th>Close_Lag1</th>
      <th>Return</th>
      <th>prices_mean_v1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023-01-01</td>
      <td>A</td>
      <td>100</td>
      <td>99</td>
      <td>101</td>
      <td>98</td>
      <td>100.5</td>
      <td>1000</td>
      <td>0.010101</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>99.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023-01-02</td>
      <td>A</td>
      <td>102</td>
      <td>101</td>
      <td>103</td>
      <td>100</td>
      <td>102.5</td>
      <td>1100</td>
      <td>0.009901</td>
      <td>100.0</td>
      <td>0.020000</td>
      <td>101.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023-01-03</td>
      <td>A</td>
      <td>101</td>
      <td>100</td>
      <td>102</td>
      <td>99</td>
      <td>101.5</td>
      <td>1050</td>
      <td>0.010000</td>
      <td>102.0</td>
      <td>-0.009804</td>
      <td>100.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023-01-04</td>
      <td>A</td>
      <td>105</td>
      <td>104</td>
      <td>106</td>
      <td>103</td>
      <td>105.5</td>
      <td>1200</td>
      <td>0.009615</td>
      <td>101.0</td>
      <td>0.039604</td>
      <td>104.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023-01-05</td>
      <td>A</td>
      <td>107</td>
      <td>106</td>
      <td>108</td>
      <td>105</td>
      <td>107.5</td>
      <td>1300</td>
      <td>0.009434</td>
      <td>105.0</td>
      <td>0.019048</td>
      <td>106.5</td>
    </tr>
  </tbody>
</table>
</div>



- 上面的运算相当于把每一行的收盘价、开盘价、最高价和最低价求了均值，其实等同于直接进行列计算：


```python
df1["prices_mean_v2"] = (df1["Close"] + df1["Open"] + df1["High"] + df1["Low"]) / 4
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Security</th>
      <th>Close</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>VWAP</th>
      <th>Volume</th>
      <th>Intraday_Return</th>
      <th>Close_Lag1</th>
      <th>Return</th>
      <th>prices_mean_v1</th>
      <th>prices_mean_v2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023-01-01</td>
      <td>A</td>
      <td>100</td>
      <td>99</td>
      <td>101</td>
      <td>98</td>
      <td>100.5</td>
      <td>1000</td>
      <td>0.010101</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>99.5</td>
      <td>99.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023-01-02</td>
      <td>A</td>
      <td>102</td>
      <td>101</td>
      <td>103</td>
      <td>100</td>
      <td>102.5</td>
      <td>1100</td>
      <td>0.009901</td>
      <td>100.0</td>
      <td>0.020000</td>
      <td>101.5</td>
      <td>101.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023-01-03</td>
      <td>A</td>
      <td>101</td>
      <td>100</td>
      <td>102</td>
      <td>99</td>
      <td>101.5</td>
      <td>1050</td>
      <td>0.010000</td>
      <td>102.0</td>
      <td>-0.009804</td>
      <td>100.5</td>
      <td>100.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023-01-04</td>
      <td>A</td>
      <td>105</td>
      <td>104</td>
      <td>106</td>
      <td>103</td>
      <td>105.5</td>
      <td>1200</td>
      <td>0.009615</td>
      <td>101.0</td>
      <td>0.039604</td>
      <td>104.5</td>
      <td>104.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023-01-05</td>
      <td>A</td>
      <td>107</td>
      <td>106</td>
      <td>108</td>
      <td>105</td>
      <td>107.5</td>
      <td>1300</td>
      <td>0.009434</td>
      <td>105.0</td>
      <td>0.019048</td>
      <td>106.5</td>
      <td>106.5</td>
    </tr>
  </tbody>
</table>
</div>



## 3. 自定义函数进行计算

### (1) 自定义函数应用到一列

有的时候，我们想要对数据进行一些复杂运算：

- 有可能这个运算是 Pandas 内置函数，甚至其他第三方库都无法实现的
- 这个时候我们就可以自定义函数，然后使用 `apply()` 方法将这个函数应用到某一列上

这里我们想做一个稍微复杂一点的操作，查看一下收益率是正还是负，正为1，负为0，并且要注意空值的处理：

- 首先，我们定义一个函数 `label_return_v1(x)`，这个函数接受一个参数 `x`，表示收益率


```python
def label_return_v1(x):
    if not pd.isna(x):
        if x > 0:
            return 1
        else:
            return 0
    else:
        return None
```

- 之后，我们使用 `apply()` 方法将这个函数应用到 `return` 列上，并将结果存储在一个新的列 `return_label_v1` 中


```python
df1["Return_Label_V1"] = df1["Return"].apply(label_return_v1)
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Security</th>
      <th>Close</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>VWAP</th>
      <th>Volume</th>
      <th>Intraday_Return</th>
      <th>Close_Lag1</th>
      <th>Return</th>
      <th>prices_mean_v1</th>
      <th>prices_mean_v2</th>
      <th>Return_Label_V1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023-01-01</td>
      <td>A</td>
      <td>100</td>
      <td>99</td>
      <td>101</td>
      <td>98</td>
      <td>100.5</td>
      <td>1000</td>
      <td>0.010101</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>99.5</td>
      <td>99.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023-01-02</td>
      <td>A</td>
      <td>102</td>
      <td>101</td>
      <td>103</td>
      <td>100</td>
      <td>102.5</td>
      <td>1100</td>
      <td>0.009901</td>
      <td>100.0</td>
      <td>0.020000</td>
      <td>101.5</td>
      <td>101.5</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023-01-03</td>
      <td>A</td>
      <td>101</td>
      <td>100</td>
      <td>102</td>
      <td>99</td>
      <td>101.5</td>
      <td>1050</td>
      <td>0.010000</td>
      <td>102.0</td>
      <td>-0.009804</td>
      <td>100.5</td>
      <td>100.5</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023-01-04</td>
      <td>A</td>
      <td>105</td>
      <td>104</td>
      <td>106</td>
      <td>103</td>
      <td>105.5</td>
      <td>1200</td>
      <td>0.009615</td>
      <td>101.0</td>
      <td>0.039604</td>
      <td>104.5</td>
      <td>104.5</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023-01-05</td>
      <td>A</td>
      <td>107</td>
      <td>106</td>
      <td>108</td>
      <td>105</td>
      <td>107.5</td>
      <td>1300</td>
      <td>0.009434</td>
      <td>105.0</td>
      <td>0.019048</td>
      <td>106.5</td>
      <td>106.5</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



在这个操作当中：

- `Return` 这一列的每一个值都会被传递到 `label_return_v1(x)` 函数中进行处理
- 并且返回的值会按位置填充到 `Return_Label_V1` 这一列中

### (2) 自定义函数应用到多列

有的时候，我们需要根据多列的数据来进行计算，这时候我们也可以使用 `apply()` 方法，并设置参数 `axis=1`，表示按行应用函数。

这里我们定义一个函数 `label_return_v2(row)`：

- 这个函数接受一个参数 `row`，表示 DataFrame 的一行数据
- 有了行之后，定位到列，只需要使用 `row["列名"]` 即可获取对应列的值


```python
def label_return_v2(row):
    if not pd.isna(row["Return"]):
        if row["Return"] > 0:
            return 1
        else:
            return 0
    else:
        return None
```

- 之后，我们使用 `apply()` 方法将这个函数应用到**整个 DataFrame 上**，并设置参数 `axis=1`，将结果存储在一个新的列 `Return_Label_V2` 中


```python
df1["Return_Label_V2"] = df1.apply(label_return_v2, axis=1)
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Security</th>
      <th>Close</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>VWAP</th>
      <th>Volume</th>
      <th>Intraday_Return</th>
      <th>Close_Lag1</th>
      <th>Return</th>
      <th>prices_mean_v1</th>
      <th>prices_mean_v2</th>
      <th>Return_Label_V1</th>
      <th>Return_Label_V2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023-01-01</td>
      <td>A</td>
      <td>100</td>
      <td>99</td>
      <td>101</td>
      <td>98</td>
      <td>100.5</td>
      <td>1000</td>
      <td>0.010101</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>99.5</td>
      <td>99.5</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023-01-02</td>
      <td>A</td>
      <td>102</td>
      <td>101</td>
      <td>103</td>
      <td>100</td>
      <td>102.5</td>
      <td>1100</td>
      <td>0.009901</td>
      <td>100.0</td>
      <td>0.020000</td>
      <td>101.5</td>
      <td>101.5</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023-01-03</td>
      <td>A</td>
      <td>101</td>
      <td>100</td>
      <td>102</td>
      <td>99</td>
      <td>101.5</td>
      <td>1050</td>
      <td>0.010000</td>
      <td>102.0</td>
      <td>-0.009804</td>
      <td>100.5</td>
      <td>100.5</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023-01-04</td>
      <td>A</td>
      <td>105</td>
      <td>104</td>
      <td>106</td>
      <td>103</td>
      <td>105.5</td>
      <td>1200</td>
      <td>0.009615</td>
      <td>101.0</td>
      <td>0.039604</td>
      <td>104.5</td>
      <td>104.5</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023-01-05</td>
      <td>A</td>
      <td>107</td>
      <td>106</td>
      <td>108</td>
      <td>105</td>
      <td>107.5</td>
      <td>1300</td>
      <td>0.009434</td>
      <td>105.0</td>
      <td>0.019048</td>
      <td>106.5</td>
      <td>106.5</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



### (3) `apply()` 与 `lambda` 联用

有的时候，我们定义的函数非常简单，只需要一行代码就能实现，这时候我们可以使用 `lambda` 匿名函数来简化代码。

- 例如，对于上面的收益率标签，我们可以使用 `lambda` 函数来实现同样的功能：`lambda x: 1 if x > 0 else (0 if x < 0 else None)` 
- 这里我们定义了一个匿名函数，接受一个参数 `x`，整个函数的逻辑是两个三元表达式的嵌套，根据条件返回相应的值
- 我们来用代码实现一下：


```python
df1["Return_Label_V3"] = df1["Return"].apply(lambda x: 1 if x > 0 else (0 if x < 0 else None))
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Security</th>
      <th>Close</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>VWAP</th>
      <th>Volume</th>
      <th>Intraday_Return</th>
      <th>Close_Lag1</th>
      <th>Return</th>
      <th>prices_mean_v1</th>
      <th>prices_mean_v2</th>
      <th>Return_Label_V1</th>
      <th>Return_Label_V2</th>
      <th>Return_Label_V3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023-01-01</td>
      <td>A</td>
      <td>100</td>
      <td>99</td>
      <td>101</td>
      <td>98</td>
      <td>100.5</td>
      <td>1000</td>
      <td>0.010101</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>99.5</td>
      <td>99.5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023-01-02</td>
      <td>A</td>
      <td>102</td>
      <td>101</td>
      <td>103</td>
      <td>100</td>
      <td>102.5</td>
      <td>1100</td>
      <td>0.009901</td>
      <td>100.0</td>
      <td>0.020000</td>
      <td>101.5</td>
      <td>101.5</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023-01-03</td>
      <td>A</td>
      <td>101</td>
      <td>100</td>
      <td>102</td>
      <td>99</td>
      <td>101.5</td>
      <td>1050</td>
      <td>0.010000</td>
      <td>102.0</td>
      <td>-0.009804</td>
      <td>100.5</td>
      <td>100.5</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023-01-04</td>
      <td>A</td>
      <td>105</td>
      <td>104</td>
      <td>106</td>
      <td>103</td>
      <td>105.5</td>
      <td>1200</td>
      <td>0.009615</td>
      <td>101.0</td>
      <td>0.039604</td>
      <td>104.5</td>
      <td>104.5</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023-01-05</td>
      <td>A</td>
      <td>107</td>
      <td>106</td>
      <td>108</td>
      <td>105</td>
      <td>107.5</td>
      <td>1300</td>
      <td>0.009434</td>
      <td>105.0</td>
      <td>0.019048</td>
      <td>106.5</td>
      <td>106.5</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



### (4) `apply()` 方法的小结

`apply()` 方法是 Pandas 中非常强大且灵活的工具，能够让我们实现复杂的数据处理和计算需求：

- 如果是应用于某一列（本质上是应用在 Series 上），则传入的函数应该接受**单个元素**作为输入，返回一个新的值
- 如果是应用于整个 DataFrame（通过设置 `axis=1`），则传入的函数应该接受**一行数据**作为输入，返回一个新的值，当中访问列的值可以使用 `row["列名"]` 的方式进行访问
