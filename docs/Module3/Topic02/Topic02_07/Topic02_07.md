# Topic 2.6 - Pandas 中的数据清洗

在本节开始前，我们先导入一下 Pandas 库：


```python
import pandas as pd
```

## 1. 缺失值处理

在数据处理任务中，很有可能拿到的数据中会有缺失值：

- 缺失值是指没有数据，并不是0或者空字符串：

    - 缺失值的产生可能是因为数据采集过程中出现问题，比方说调查身高时张三没有填写
    - 也有可能是因为数据本身就不存在，比方说张三没有社保号，因为他还没有参加社保

- 对于缺失值的处理，是数据处理中的一个重要环节，我们要先统计缺失值的情况，然后再决定如何处理，是补充缺失值，还是删除含有缺失值的记录

在 Pandas 中 通常会以 `NaN`来表示缺失值，这个类似于 Python 自带的 `None`


### (1) 缺失值统计

#### (a) 统计所有列的缺失值数量

在 Pandas 中，检测缺失值主要有两个方法：

- `df.isna()`：用于检测缺失值，会返回一个新的 DataFrame 和原 DataFrame 对应，缺失值位置为 `True`，非缺失值位置为 `False`
- `df.notna()`：用于检测非缺失值，会返回一个新的 DataFrame 和原 DataFrame 对应，非缺失值位置为 `True`，缺失值位置为 `False`


```python
df1 = pd.DataFrame({
    "date": pd.date_range(start="2024-01-01", periods=15, freq="D"),
    "c1": [1, 2, 3, 4, None, 6, 7, 8, None, 10, None, 12, 13, None, 15],
    "c2": [1, None, 3, 4, 5, None, 7, 8, None, 10, 11, 12, None, 14, 15],
    "c3": [1, 0, 3, 4, 5, 0, 7, 8, 0, 10, 11, 12, 0, 14, 15],
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
      <th>date</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-01-01</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-01-02</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-01-03</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-01-04</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-01-05</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-01-06</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-01-07</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-01-08</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024-01-09</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-01-10</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2024-01-11</td>
      <td>NaN</td>
      <td>11.0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2024-01-12</td>
      <td>12.0</td>
      <td>12.0</td>
      <td>12</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2024-01-13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2024-01-14</td>
      <td>NaN</td>
      <td>14.0</td>
      <td>14</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2024-01-15</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
display(df1.isna())
display(df1.notna())
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
      <th>date</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>5</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>6</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>7</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>8</th>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>9</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>10</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>11</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>12</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>13</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>14</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



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
      <th>date</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>6</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>7</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>8</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>9</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>10</th>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>11</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>12</th>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>13</th>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>


通过这两个方法，我们可以很方便地统计缺失值的数量：

- `df.isna().sum()` 和 `df.notna().sum()` 分别用于统计每一列中的缺失值和非缺失值的**数量**
- `df.isna().mean()` 和 `df.notna().mean()` 分别用于统计每一列中缺失值和非缺失值的**比例**


```python
display(df1.isna().sum())
display(df1.notna().sum())
```


    date    0
    c1      4
    c2      4
    c3      0
    dtype: int64



    date    15
    c1      11
    c2      11
    c3      15
    dtype: int64



```python
display(df1.isna().mean())
display(df1.notna().mean())
```


    date    0.000000
    c1      0.266667
    c2      0.266667
    c3      0.000000
    dtype: float64



    date    1.000000
    c1      0.733333
    c2      0.733333
    c3      1.000000
    dtype: float64


#### (b) 统计某一列的缺失值数量

上面两个方法也是可以应用到列上的：

- `df['列名'].isna().sum()` 与 `df['列名'].notna().sum()` 用于统计某一列中的缺失值和非缺失值的**数量**
- `df['列名'].isna().mean()` 与 `df['列名'].notna().mean()` 用于统计某一列中缺失值和非缺失值的**比例**


```python
display(df1['c1'].isna().sum())
display(df1['c1'].notna().sum())
display(df1['c1'].isna().mean())
display(df1['c1'].notna().mean())
```


    np.int64(4)



    np.int64(11)



    np.float64(0.26666666666666666)



    np.float64(0.7333333333333333)


如果仿照上一节数据筛选中的思路：

- 使用 `df[df['列名'].isna()]` 可以筛选出某一列中缺失值的记录
- 使用 `df[df['列名'].notna()]` 可以筛选出某一列中非缺失值的记录
- 之所以可以这样操作，是因为 `df['列名'].isna()` 和 `df['列名'].notna()` 都是返回的是一个布尔类型的 Series，可以作为行索引来筛选记录


```python
display(df1[df1['c1'].isna()])
display(df1[df1['c1'].notna()])
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
      <th>date</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>2024-01-05</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024-01-09</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2024-01-11</td>
      <td>NaN</td>
      <td>11.0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2024-01-14</td>
      <td>NaN</td>
      <td>14.0</td>
      <td>14</td>
    </tr>
  </tbody>
</table>
</div>



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
      <th>date</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-01-01</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-01-02</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-01-03</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-01-04</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-01-06</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-01-07</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-01-08</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-01-10</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2024-01-12</td>
      <td>12.0</td>
      <td>12.0</td>
      <td>12</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2024-01-13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2024-01-15</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>


### (2) 缺失值填充

#### (a) 使用固定值填充

在 Pandas 中，`fillna(value)` 方法可以用来将缺失值填充为指定的固定值 `value`，常见的操作有：

- `df['列名'].fillna(0)`：将缺失值填充为0，或者其他常数值


```python
df1_new1 = df1.copy()
df1_new1["c1"] = df1_new1["c1"].fillna(0)
df1_new1
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
      <th>date</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-01-01</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-01-02</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-01-03</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-01-04</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-01-05</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-01-06</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-01-07</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-01-08</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024-01-09</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-01-10</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2024-01-11</td>
      <td>0.0</td>
      <td>11.0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2024-01-12</td>
      <td>12.0</td>
      <td>12.0</td>
      <td>12</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2024-01-13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2024-01-14</td>
      <td>0.0</td>
      <td>14.0</td>
      <td>14</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2024-01-15</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>



- `df['列名'].fillna(df['列名'].mean())`：将某一列的缺失值填充为该列的均值，当然中位数（.median()）和众数（.mode()[0]）也比较常见


```python
df1_new2 = df1.copy()
df1_new2["c1"] = df1_new2["c1"].fillna(df1_new2["c1"].mean())
df1_new2
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
      <th>date</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-01-01</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-01-02</td>
      <td>2.000000</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-01-03</td>
      <td>3.000000</td>
      <td>3.0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-01-04</td>
      <td>4.000000</td>
      <td>4.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-01-05</td>
      <td>7.363636</td>
      <td>5.0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-01-06</td>
      <td>6.000000</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-01-07</td>
      <td>7.000000</td>
      <td>7.0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-01-08</td>
      <td>8.000000</td>
      <td>8.0</td>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024-01-09</td>
      <td>7.363636</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-01-10</td>
      <td>10.000000</td>
      <td>10.0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2024-01-11</td>
      <td>7.363636</td>
      <td>11.0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2024-01-12</td>
      <td>12.000000</td>
      <td>12.0</td>
      <td>12</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2024-01-13</td>
      <td>13.000000</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2024-01-14</td>
      <td>7.363636</td>
      <td>14.0</td>
      <td>14</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2024-01-15</td>
      <td>15.000000</td>
      <td>15.0</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>



#### (b) 向前填充或向后填充

除了填充为固定值，Pandas 还提供了向前填充和向后填充两种方法：

- `ffill()`：使用前一个非缺失值填充缺失值，也就是向上查找，将缺失值替换为上方最近的非缺失值


```python
df1_new3 = df1.copy()
df1_new3
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
      <th>date</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-01-01</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-01-02</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-01-03</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-01-04</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-01-05</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-01-06</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-01-07</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-01-08</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024-01-09</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-01-10</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2024-01-11</td>
      <td>NaN</td>
      <td>11.0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2024-01-12</td>
      <td>12.0</td>
      <td>12.0</td>
      <td>12</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2024-01-13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2024-01-14</td>
      <td>NaN</td>
      <td>14.0</td>
      <td>14</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2024-01-15</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1_new3["c1"] = df1_new3["c1"].ffill()
df1_new3
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
      <th>date</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-01-01</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-01-02</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-01-03</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-01-04</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-01-05</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-01-06</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-01-07</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-01-08</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024-01-09</td>
      <td>8.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-01-10</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2024-01-11</td>
      <td>10.0</td>
      <td>11.0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2024-01-12</td>
      <td>12.0</td>
      <td>12.0</td>
      <td>12</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2024-01-13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2024-01-14</td>
      <td>13.0</td>
      <td>14.0</td>
      <td>14</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2024-01-15</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>



- `bfill()`：使用后一个非缺失值填充缺失值，也就是向下查找，将缺失值替换为下方最近的非缺失值


```python
df1_new4 = df1.copy()
df1_new4
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
      <th>date</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-01-01</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-01-02</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-01-03</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-01-04</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-01-05</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-01-06</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-01-07</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-01-08</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024-01-09</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-01-10</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2024-01-11</td>
      <td>NaN</td>
      <td>11.0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2024-01-12</td>
      <td>12.0</td>
      <td>12.0</td>
      <td>12</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2024-01-13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2024-01-14</td>
      <td>NaN</td>
      <td>14.0</td>
      <td>14</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2024-01-15</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1_new4["c1"] = df1_new4["c1"].bfill()
df1_new4
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
      <th>date</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-01-01</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-01-02</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-01-03</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-01-04</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-01-05</td>
      <td>6.0</td>
      <td>5.0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-01-06</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-01-07</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-01-08</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024-01-09</td>
      <td>10.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-01-10</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2024-01-11</td>
      <td>12.0</td>
      <td>11.0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2024-01-12</td>
      <td>12.0</td>
      <td>12.0</td>
      <td>12</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2024-01-13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2024-01-14</td>
      <td>15.0</td>
      <td>14.0</td>
      <td>14</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2024-01-15</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>



### (3) 缺失值删除

还有一个处理缺失值的常见方法是删除含有缺失值的行：

- `df.dropna()`：删除含有缺失值的行，只要任意一列有缺失值，该行记录就会被删除


```python
df1_new5 = df1.copy()
df1_new5
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
      <th>date</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-01-01</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-01-02</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-01-03</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-01-04</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-01-05</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-01-06</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-01-07</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-01-08</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024-01-09</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-01-10</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2024-01-11</td>
      <td>NaN</td>
      <td>11.0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2024-01-12</td>
      <td>12.0</td>
      <td>12.0</td>
      <td>12</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2024-01-13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2024-01-14</td>
      <td>NaN</td>
      <td>14.0</td>
      <td>14</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2024-01-15</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1_new5 = df1_new5.dropna()
df1_new5
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
      <th>date</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-01-01</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-01-03</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-01-04</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-01-07</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-01-08</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-01-10</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2024-01-12</td>
      <td>12.0</td>
      <td>12.0</td>
      <td>12</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2024-01-15</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>



- `df.dropna(subset=['列名1', '列名2'])`：只删除在指定列中含有缺失值的行，其他类中的缺失值不影响该行的保留与否


```python
df1_new6 = df1.copy()
df1_new6
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
      <th>date</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-01-01</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-01-02</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-01-03</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-01-04</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-01-05</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-01-06</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-01-07</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-01-08</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024-01-09</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-01-10</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2024-01-11</td>
      <td>NaN</td>
      <td>11.0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2024-01-12</td>
      <td>12.0</td>
      <td>12.0</td>
      <td>12</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2024-01-13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2024-01-14</td>
      <td>NaN</td>
      <td>14.0</td>
      <td>14</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2024-01-15</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1_new6 = df1_new6.dropna(subset=['c1'])
df1_new6
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
      <th>date</th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-01-01</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-01-02</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-01-03</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-01-04</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-01-06</td>
      <td>6.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-01-07</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-01-08</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-01-10</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2024-01-12</td>
      <td>12.0</td>
      <td>12.0</td>
      <td>12</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2024-01-13</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2024-01-15</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>



### (4) 缺失值处理小结

对于缺失值的处理方法选择是十分谨慎的，因为不同的处理方法会对后续的数据分析和建模产生较大的影响：

- 在实际的数据分析中，缺失值的删除虽然会导致数据量的减少，但是可以保证数据的真实性和一致性
- 缺失值的填充其实是比较少见的：

    - 在时间序列数据中，我们偶尔会选择使用向前填充或向后填充的方法来处理缺失值，因为时间序列数据的连续性比较强
    - 使用固定值填充的方法在实际中并不常用，因为这样会引入额外的偏差，影响后续的分析结果

## 2. 异常值处理

有时候数据中虽然没有缺失值，但是有可能会存在一些异常值，这些异常值可能是以下几种类型：

- 特定值：比方说年龄为负数、体重大于200公斤、价格为0等
- 极端值：比方说小于均值减去3倍标准差，或者大于均值加上3倍标准差的值
- 重复值：比方说同一条记录出现了多次，就是很多行数据都是一样的

这里我们分别介绍一下如何处理这些异常值。

### (1) 特定值处理

对于特定的异常值，我们通常是先把这些数据定位出来，之后可以决定是替换还是删除：

- 不论是替换还是删除，核心都是使用条件表达式来定位到这些异常值
- 如果要将这些异常值替换为特定的值，可以使用 `df.loc[条件表达式, 列名] = 新值` 的形式来进行替换
- 如果要删除这些异常值，可以使用布尔索引来筛选出非异常值的记录，形式是 `df[~(条件表达式)]` 或者直接 `df[条件表达式取反]`

这里我们先定义一个新的 DataFrame：


```python
import random

df2 = pd.DataFrame({
    "date": pd.date_range(start="2024-01-01", periods=10, freq="D"),
    "c1": [random.choice([0, i]) for i in range(10)],
    "c2": [random.randint(1, 10) for _ in range(10)],
})

df2
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
      <th>date</th>
      <th>c1</th>
      <th>c2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-01-01</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-01-02</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-01-03</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-01-04</td>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-01-05</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-01-06</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-01-07</td>
      <td>6</td>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-01-08</td>
      <td>7</td>
      <td>5</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024-01-09</td>
      <td>8</td>
      <td>7</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-01-10</td>
      <td>9</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



- 之后，我们想把 `c1` 列中值为0的异常值替换为1（这里0为异常是我们自己定义的）


```python
df2_new1 = df2.copy()
df2_new1.loc[df2_new1['c1'] == 0, 'c1'] = 1
df2_new1
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
      <th>date</th>
      <th>c1</th>
      <th>c2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-01-01</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-01-02</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-01-03</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-01-04</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-01-05</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-01-06</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-01-07</td>
      <td>6</td>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-01-08</td>
      <td>7</td>
      <td>5</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024-01-09</td>
      <td>8</td>
      <td>7</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-01-10</td>
      <td>9</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



- 再比方说，我们想把 `c2` 列中大于5的异常值删除掉（这里大于5为异常是我们自己定义的）


```python
df2_new2 = df2.copy()
df2_new2 = df2_new2[~(df2_new2['c2'] > 5)]
df2_new2
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
      <th>date</th>
      <th>c1</th>
      <th>c2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-01-01</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-01-03</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-01-04</td>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-01-05</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024-01-06</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024-01-07</td>
      <td>6</td>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024-01-08</td>
      <td>7</td>
      <td>5</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024-01-10</td>
      <td>9</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



### (2) 极端值处理

极端值的处理方法，其实是和特定值处理类似的：

- 首先就是要用条件表达式来定位到这些极端值：

    - 如果极端值的定义是加减三倍标准差，则可以使用 `df['列名'] > df['列名'].mean() + 3 * df['列名'].std()` 或 `df['列名'] < df['列名'].mean() - 3 * df['列名'].std()` 的条件表达式来定位极端值
    - 如果使用分位数来定义极端值，则可以使用类似 `df['列名'] > df['列名'].quantile(0.99)` 或 `df['列名'] < df['列名'].quantile(0.01)` 的条件表达式来定位极端值

- 之后，和特定值处理一样，可以选择替换或者删除这些极端值：

    - 替换可以使用 `df.loc[条件表达式, 列名] = 新值`
    - 删除可以使用布尔索引 `df[~(条件表达式)]`

我们先来定义一个新的 DataFrame，当中包括明显的极端值：


```python
df3 = pd.DataFrame({
    "c1": [random.randint(-10, 10) for _ in range(19)] + [-100, 100],
    "c2": [random.randint(-10, 10) for _ in range(19)] + [-200, 200],
})

df3['c1'] = df3['c1'].astype(float)
df3['c2'] = df3['c2'].astype(float)

df3
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
      <th>c1</th>
      <th>c2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-8.0</td>
      <td>-4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7.0</td>
      <td>-10.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>-5.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.0</td>
      <td>-4.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>-9.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-7.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-8.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7.0</td>
      <td>-6.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>-1.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>4.0</td>
      <td>-4.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>5.0</td>
      <td>-7.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>-10.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>-2.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>-7.0</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>8.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>-10.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>7.0</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>-100.0</td>
      <td>-200.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>100.0</td>
      <td>200.0</td>
    </tr>
  </tbody>
</table>
</div>



- 首先，我们演示一下使用标准差来定义极端值：

    - 在极端值场景下，通常是将极端值替换为对应的上下限，比方说均值加减3倍标准差的值，而不是均值或者其他值
    - 当然，也可以选择删除这样的极端值


```python
df3_new1 = df3.copy()

df3_new1_c1_mean = df3_new1['c1'].mean()
df3_new1_c1_std = df3_new1['c1'].std()
df3_new1_c1_lower_bound = df3_new1_c1_mean - 3 * df3_new1_c1_std
df3_new1_c1_upper_bound = df3_new1_c1_mean + 3 * df3_new1_c1_std

df3_new1.loc[df3_new1['c1'] < df3_new1_c1_lower_bound, 'c1'] = df3_new1_c1_lower_bound
df3_new1.loc[df3_new1['c1'] > df3_new1_c1_upper_bound, 'c1'] = df3_new1_c1_upper_bound

df3_new1
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
      <th>c1</th>
      <th>c2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-8.000000</td>
      <td>-4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7.000000</td>
      <td>-10.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.000000</td>
      <td>-5.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.000000</td>
      <td>-4.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.000000</td>
      <td>-9.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-7.000000</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-8.000000</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7.000000</td>
      <td>-6.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9.000000</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>-1.000000</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>4.000000</td>
      <td>-4.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>5.000000</td>
      <td>-7.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>-10.000000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>-2.000000</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>-7.000000</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>8.000000</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>-10.000000</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>7.000000</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.000000</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>-96.705222</td>
      <td>-200.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>96.705222</td>
      <td>200.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3_new2 = df3.copy()

df3_new2_c1_mean = df3_new2['c1'].mean()
df3_new2_c1_std = df3_new2['c1'].std()
df3_new2_c1_lower_bound = df3_new2_c1_mean - 3 * df3_new2_c1_std
df3_new2_c1_upper_bound = df3_new2_c1_mean + 3 * df3_new2_c1_std

df3_new2 = df3_new2[(df3_new2['c1'] >= df3_new2_c1_lower_bound) & (df3_new2['c1'] <= df3_new2_c1_upper_bound)]
df3_new2
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
      <th>c1</th>
      <th>c2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-8.0</td>
      <td>-4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7.0</td>
      <td>-10.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>-5.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.0</td>
      <td>-4.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>-9.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-7.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-8.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7.0</td>
      <td>-6.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>-1.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>4.0</td>
      <td>-4.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>5.0</td>
      <td>-7.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>-10.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>-2.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>-7.0</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>8.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>-10.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>7.0</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.0</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>



- 之后，我们在 `c2` 列中使用分位数来定义极端值，演示一下替换和删除的方法：


```python
df3_new3 = df3.copy()

df3_new3_c2_q1 = df3_new3['c2'].quantile(0.25)
df3_new3_c2_q3 = df3_new3['c2'].quantile(0.75)

df3_new3.loc[df3_new3['c2'] < df3_new3_c2_q1, 'c2'] = df3_new3_c2_q1
df3_new3.loc[df3_new3['c2'] > df3_new3_c2_q3, 'c2'] = df3_new3_c2_q3

df3_new3
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
      <th>c1</th>
      <th>c2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-8.0</td>
      <td>-4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7.0</td>
      <td>-5.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>-5.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.0</td>
      <td>-4.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>-5.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-7.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-8.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7.0</td>
      <td>-5.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>-1.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>4.0</td>
      <td>-4.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>5.0</td>
      <td>-5.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>-10.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>-2.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>-7.0</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>8.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>-10.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>7.0</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>-100.0</td>
      <td>-5.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>100.0</td>
      <td>6.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3_new_4 = df3.copy()

df3_new_4_c2_q1 = df3_new_4['c2'].quantile(0.25)
df3_new_4_c2_q3 = df3_new_4['c2'].quantile(0.75)
df3_new_4_c2_iqr = df3_new_4_c2_q3 - df3_new_4_c2_q1

df3_new_4 = df3_new_4[(df3_new_4['c2'] >= (df3_new_4_c2_q1 - 1.5 * df3_new_4_c2_iqr)) & (df3_new_4['c2'] <= (df3_new_4_c2_q3 + 1.5 * df3_new_4_c2_iqr))]
df3_new_4
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
      <th>c1</th>
      <th>c2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-8.0</td>
      <td>-4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7.0</td>
      <td>-10.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>-5.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.0</td>
      <td>-4.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>-9.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-7.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-8.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7.0</td>
      <td>-6.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>-1.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>4.0</td>
      <td>-4.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>5.0</td>
      <td>-7.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>-10.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>-2.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>-7.0</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>8.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>-10.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>7.0</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.0</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>



### (3) 重复值处理

重复值的处理相对来说比较简单，使用的方法是 `drop_duplicates()`：

- 默认的 `df.drop_duplicates()` 会删除所有列都相同的重复记录，只保留第一条出现的记录，也就是说，两行长得一模一样的记录，只会保留第一行，第二行会被删除


```python
df4 = pd.DataFrame({
    "c1": [1, 1, 2, 2, 3, 4, 4, 4, 5],
    "c2": ['A', 'B', 'B', 'B', 'C', 'D', 'D', 'E', 'E'],
})

df4
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
      <th>c1</th>
      <th>c2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>B</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>B</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>C</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4</td>
      <td>D</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4</td>
      <td>D</td>
    </tr>
    <tr>
      <th>7</th>
      <td>4</td>
      <td>E</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5</td>
      <td>E</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4.drop_duplicates()
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
      <th>c1</th>
      <th>c2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>B</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>C</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4</td>
      <td>D</td>
    </tr>
    <tr>
      <th>7</th>
      <td>4</td>
      <td>E</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5</td>
      <td>E</td>
    </tr>
  </tbody>
</table>
</div>



- 如果只想根据某几列来判断是否重复，可以使用 `df.drop_duplicates(subset=['列名1', '列名2'])`，这样只有在指定的列中完全相同的记录才会被视为重复记录并删除


```python
df4.drop_duplicates(subset=['c1'])
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
      <th>c1</th>
      <th>c2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>B</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>C</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4</td>
      <td>D</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5</td>
      <td>E</td>
    </tr>
  </tbody>
</table>
</div>


