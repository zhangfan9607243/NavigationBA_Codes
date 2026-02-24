# Topic 2.8 - Pandas 中的数据连接与拼接

在本节开始之前，我们先导入 pandas 库：


```python
import pandas as pd
```

## 1. 数据连接

### (1) 数据连接的概念

数据连接的概念，是将两个表按照某些公共的列，将它们连接在一起，类似于数据库中的 `JOIN` 操作：

- 这个操作听上去有点高大上，但是底层逻辑十分简单，我们先来看个以下例子：

<div align="center">
    <img src="../截屏2026-02-01 23.25.32.png" width="800">
</div>


- 上图中，我们有两个表，一个表中包含的列是姓名和班级，另一个表中包含的列是班级和班主任
- 我们可以通过 `班级` 这个公共列，将两个表连接在一起，得到一个新的表，这个新表中包含了姓名、班级和班主任三列

数据连接的操作，可以使用 Pandas 中的 `merge()` 函数来实现：


```python
df1a = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六", "牛七", "马八", "杨九"],
    "班级": ["一班", "一班", "一班", "二班", "二班", "三班", "三班"]
})

df1a
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
      <th>姓名</th>
      <th>班级</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>4</th>
      <td>牛七</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>5</th>
      <td>马八</td>
      <td>三班</td>
    </tr>
    <tr>
      <th>6</th>
      <td>杨九</td>
      <td>三班</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1b = pd.DataFrame({
    "班级": ["一班", "二班", "三班"],
    "班主任": ["老A", "老B", "老C"]
})

df1b
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
      <th>班级</th>
      <th>班主任</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>三班</td>
      <td>老C</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged1 = pd.merge(df1a, df1b, on="班级")
df_merged1
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
      <th>姓名</th>
      <th>班级</th>
      <th>班主任</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>4</th>
      <td>牛七</td>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>5</th>
      <td>马八</td>
      <td>三班</td>
      <td>老C</td>
    </tr>
    <tr>
      <th>6</th>
      <td>杨九</td>
      <td>三班</td>
      <td>老C</td>
    </tr>
  </tbody>
</table>
</div>



### (2) 常见的连接方式

连接方式这个概念，是建立在两表连接键（公共列）上，决定如何连接两表的规则，我们这里来介绍一些常见的连接方式。


#### (a) 内连接

内连接（Inner Join）：只保留两个表中连接键匹配的行：

- 使用集合来表示，内连接就是两个表连接键的交集：

<div align="center">
    <img src="../UI25E_副本.jpg" width="200">
</div>


- 回到班级的这个例子中，一个内连接的例子可以用下图来表示：

<div align="center">
    <img src="../截屏2026-02-02 14.35.11.png" width="800">
</div>

- 通过内连接，我们只保留了两个表中 `班级` 列匹配的行：

    - 左表中 `Alice`、`Bob` 和 `Charlie` 三行的 `班级` 分别是 `四班`、`四班` 和 `六班`，在右表中没有对应的 `班级`，所以这三行被丢弃了
    - 右表中，`五班` 的班主任 `老E`，在左表中没有对应的 `班级`，所以这一行也被丢弃了

- 事实上，在 Pandas 中，`merge()` 函数的默认连接方式就是内连接，如果想强调是内连接，可以通过 `how='inner'` 参数来指定：


```python
df2a = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六", "牛七", "马八", "杨九", "Alice", "Bob", "Charlie"],
    "班级": ["一班", "一班", "一班", "二班", "二班", "三班", "三班", "四班", "四班", "六班"]
})

df2a
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
      <th>姓名</th>
      <th>班级</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>4</th>
      <td>牛七</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>5</th>
      <td>马八</td>
      <td>三班</td>
    </tr>
    <tr>
      <th>6</th>
      <td>杨九</td>
      <td>三班</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Alice</td>
      <td>四班</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bob</td>
      <td>四班</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Charlie</td>
      <td>六班</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2b = pd.DataFrame({
    "班级": ["一班", "二班", "三班", "五班"],
    "班主任": ["老A", "老B", "老C", "老E"]
})

df2b
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
      <th>班级</th>
      <th>班主任</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>三班</td>
      <td>老C</td>
    </tr>
    <tr>
      <th>3</th>
      <td>五班</td>
      <td>老E</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged2 = pd.merge(df2a, df2b, on="班级", how="inner")
df_merged2
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
      <th>姓名</th>
      <th>班级</th>
      <th>班主任</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>4</th>
      <td>牛七</td>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>5</th>
      <td>马八</td>
      <td>三班</td>
      <td>老C</td>
    </tr>
    <tr>
      <th>6</th>
      <td>杨九</td>
      <td>三班</td>
      <td>老C</td>
    </tr>
  </tbody>
</table>
</div>



#### (b) 左连接

左连接（Left Join）：左表是老大，保留左表的所有行，在左表但不在右表中的键用 NaN 填充

- 使用集合来表示，左连接就是左表连接键的全集：

<div align="center">
    <img src="../UI25E_副本2.jpg" width="200">
</div>

- 回到班级的这个例子中，一个左连接的例子可以用下图来表示：

<div align="center">
    <img src="../截屏2026-02-02 14.49.59.png" width="800">
</div>

- 通过左连接，我们保留了左表中的所有行：

    - 左表中 `Alice`、`Bob` 和 `Charlie` 三行的 `班级` 分别是 `四班`、`四班` 和 `六班`，在右表中没有对应的 `班级`，所以这三行的 `班主任` 列被填充为 NaN
    - 右表中，`五班` 的班主任 `老E`，在左表中没有对应的 `班级`，所以这一行被丢弃了

- 在 Pandas 中，可以通过在 `merge()` 函数中指定 `how='left'` 参数来指定左连接：


```python
df3a = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六", "牛七", "马八", "杨九", "Alice", "Bob", "Charlie"],
    "班级": ["一班", "一班", "一班", "二班", "二班", "三班", "三班", "四班", "四班", "六班"]
})

df3a
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
      <th>姓名</th>
      <th>班级</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>4</th>
      <td>牛七</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>5</th>
      <td>马八</td>
      <td>三班</td>
    </tr>
    <tr>
      <th>6</th>
      <td>杨九</td>
      <td>三班</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Alice</td>
      <td>四班</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bob</td>
      <td>四班</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Charlie</td>
      <td>六班</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3b = pd.DataFrame({
    "班级": ["一班", "二班", "三班", "五班"],
    "班主任": ["老A", "老B", "老C", "老E"]
})

df3b
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
      <th>班级</th>
      <th>班主任</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>三班</td>
      <td>老C</td>
    </tr>
    <tr>
      <th>3</th>
      <td>五班</td>
      <td>老E</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged3 = pd.merge(df3a, df3b, on="班级", how="left")
df_merged3
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
      <th>姓名</th>
      <th>班级</th>
      <th>班主任</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>4</th>
      <td>牛七</td>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>5</th>
      <td>马八</td>
      <td>三班</td>
      <td>老C</td>
    </tr>
    <tr>
      <th>6</th>
      <td>杨九</td>
      <td>三班</td>
      <td>老C</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Alice</td>
      <td>四班</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bob</td>
      <td>四班</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Charlie</td>
      <td>六班</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



#### (c) 右连接

右连接（Right Join）：右表是老大，保留右表的所有行，在右表但不在左表中的键用 NaN 填充

- 使用集合来表示，右连接就是右表连接键的全集：

<div align="center">
    <img src="../UI25E_副本3.jpg" width="200">
</div>

- 回到班级的这个例子中，一个右连接的例子可以用下图来表示：

<div align="center">
    <img src="../截屏2026-02-02 15.16.01.png" width="800">
</div>

- 通过右连接，我们保留了右表中的所有行：

    - 左表中 `Alice`、`Bob` 和 `Charlie` 三行的 `班级` 分别是 `四班`、`四班` 和 `六班`，在右表中没有对应的 `班级`，所以这三行被丢弃了
    - 右表中，`五班` 的班主任 `老E`，在左表中没有对应的 `班级`，所以这一行的 `姓名` 列被填充为 NaN

- 在 Pandas 中，可以通过在 `merge()` 函数中指定 `how='right'` 参数来指定右连接：


```python
df4a = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六", "牛七", "马八", "杨九", "Alice", "Bob", "Charlie"],
    "班级": ["一班", "一班", "一班", "二班", "二班", "三班", "三班", "四班", "四班", "六班"]
})

df4a
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
      <th>姓名</th>
      <th>班级</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>4</th>
      <td>牛七</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>5</th>
      <td>马八</td>
      <td>三班</td>
    </tr>
    <tr>
      <th>6</th>
      <td>杨九</td>
      <td>三班</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Alice</td>
      <td>四班</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bob</td>
      <td>四班</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Charlie</td>
      <td>六班</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4b = pd.DataFrame({
    "班级": ["一班", "二班", "三班", "五班"],
    "班主任": ["老A", "老B", "老C", "老E"]
})

df4b
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
      <th>班级</th>
      <th>班主任</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>三班</td>
      <td>老C</td>
    </tr>
    <tr>
      <th>3</th>
      <td>五班</td>
      <td>老E</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged4 = pd.merge(df4a, df4b, on="班级", how="right")
df_merged4
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
      <th>姓名</th>
      <th>班级</th>
      <th>班主任</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>4</th>
      <td>牛七</td>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>5</th>
      <td>马八</td>
      <td>三班</td>
      <td>老C</td>
    </tr>
    <tr>
      <th>6</th>
      <td>杨九</td>
      <td>三班</td>
      <td>老C</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>五班</td>
      <td>老E</td>
    </tr>
  </tbody>
</table>
</div>



#### (d) 外连接

外连接（Outer Join）：左连接和右连接的结合，保留两个表中的所有行，不匹配的键用 NaN 填充

- 使用集合来表示，外连接就是两个表连接键的并集：

<div align="center">
    <img src="../UI25E_副本4.jpg" width="200">
</div>

- 回到班级的这个例子中，一个外连接的例子可以用下图来表示：

<div align="center">
    <img src="../截屏2026-02-02 15.28.19.png" width="800">
</div>

- 通过外连接，我们保留了两个表中的所有行：

    - 左表中 `Alice`、`Bob` 和 `Charlie` 三行的 `班级` 分别是 `四班`、`四班` 和 `六班`，在右表中没有对应的 `班级`，所以这三行的 `班主任` 列被填充为 NaN
    - 右表中，`五班` 的班主任 `老E`，在左表中没有对应的 `班级`，所以这一行的 `姓名` 列被填充为 NaN

- 在 Pandas 中，可以通过在 `merge()` 函数中指定 `how='outer'` 参数来指定外连接：


```python
df5a = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六", "牛七", "马八", "杨九", "Alice", "Bob", "Charlie"],
    "班级": ["一班", "一班", "一班", "二班", "二班", "三班", "三班", "四班", "四班", "六班"]
})

df5a
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
      <th>姓名</th>
      <th>班级</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>4</th>
      <td>牛七</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>5</th>
      <td>马八</td>
      <td>三班</td>
    </tr>
    <tr>
      <th>6</th>
      <td>杨九</td>
      <td>三班</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Alice</td>
      <td>四班</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bob</td>
      <td>四班</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Charlie</td>
      <td>六班</td>
    </tr>
  </tbody>
</table>
</div>




```python
df5b = pd.DataFrame({
    "班级": ["一班", "二班", "三班", "五班"],
    "班主任": ["老A", "老B", "老C", "老E"]
})

df5b
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
      <th>班级</th>
      <th>班主任</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>三班</td>
      <td>老C</td>
    </tr>
    <tr>
      <th>3</th>
      <td>五班</td>
      <td>老E</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged5 = pd.merge(df5a, df5b, on="班级", how="outer")
df_merged5
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
      <th>姓名</th>
      <th>班级</th>
      <th>班主任</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>马八</td>
      <td>三班</td>
      <td>老C</td>
    </tr>
    <tr>
      <th>4</th>
      <td>杨九</td>
      <td>三班</td>
      <td>老C</td>
    </tr>
    <tr>
      <th>5</th>
      <td>赵六</td>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>6</th>
      <td>牛七</td>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>五班</td>
      <td>老E</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Charlie</td>
      <td>六班</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Alice</td>
      <td>四班</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Bob</td>
      <td>四班</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### (3) 特殊的连接方式

上面四种连接方式是比较常见的连接方式，除此之外，还有一些特殊的连接方式，使用场景相对较少，这里我们简单介绍。

#### (a) 左反连接

左反连接（Left Anti Join）：只保留左表中不在右表中的行

- 从集合的角度来看，左反连接就是左连接的基础上，去掉了交集部分：

<div align="center">
    <img src="../UI25E_副本5.jpg" width="200">
</div>

- 回到班级的这个例子中，一个左反连接的例子可以用下图来表示：

<div align="center">
    <img src="../截屏2026-02-02 15.47.25.png" width="800">
</div>

- 通过左反连接，我们只保留了左表中的特有行

- 在 Pandas 中，可以通过在 `merge()` 函数中指定 `how='left'` 参数，并结合 `indicator=True` 参数来实现左反连接：

    - `indicator=True` 参数会在结果中添加一列 `_merge`，标识每一行的来源，原来是在左表中（`left_only`）还是右表中（`right_only`），还是两个表中都有（`both`）
    - 然后我们可以通过筛选仅仅在左表中的行 `left_only`，来实现左反连接
    - 之后再把 `_merge` 列删除即可


```python
df6a = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六", "牛七", "马八", "杨九", "Alice", "Bob", "Charlie"],
    "班级": ["一班", "一班", "一班", "二班", "二班", "三班", "三班", "四班", "四班", "六班"]
})

df6a
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
      <th>姓名</th>
      <th>班级</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>4</th>
      <td>牛七</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>5</th>
      <td>马八</td>
      <td>三班</td>
    </tr>
    <tr>
      <th>6</th>
      <td>杨九</td>
      <td>三班</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Alice</td>
      <td>四班</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bob</td>
      <td>四班</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Charlie</td>
      <td>六班</td>
    </tr>
  </tbody>
</table>
</div>




```python
df6b = pd.DataFrame({
    "班级": ["一班", "二班", "三班", "五班"],
    "班主任": ["老A", "老B", "老C", "老E"]
})

df6b
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
      <th>班级</th>
      <th>班主任</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>三班</td>
      <td>老C</td>
    </tr>
    <tr>
      <th>3</th>
      <td>五班</td>
      <td>老E</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged6 = pd.merge(df6a, df6b, on="班级", how="outer", indicator=True).query("_merge == 'left_only'").drop(columns="_merge")
df_merged6
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
      <th>姓名</th>
      <th>班级</th>
      <th>班主任</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>Charlie</td>
      <td>六班</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Alice</td>
      <td>四班</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Bob</td>
      <td>四班</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



#### (b) 右反连接

右反连接（Right Anti Join）：只保留右表中不在左表中的行

- 从集合的角度来看，右反连接就是右连接的基础上，去掉了交集部分：

<div align="center">
    <img src="../UI25E_副本6.jpg" width="200">
</div>

- 回到班级的这个例子中，一个右反连接的例子可以用下图来表示：

<div align="center">
    <img src="../截屏2026-02-02 15.57.45.png" width="800">
</div>

- 通过右反连接，我们只保留了右表中的特有行

- 在 Pandas 中，可以通过在 `merge()` 函数中指定 `how='right'` 参数，并结合 `indicator=True` 参数来实现右反连接：

    - `indicator=True` 参数会在结果中添加一列 `_merge`，标识每一行的来源，原来是在左表中（`left_only`）还是右表中（`right_only`），还是两个表中都有（`both`）
    - 然后我们可以通过筛选仅仅在右表中的行 `right_only`，来实现右反连接
    - 之后再把 `_merge` 列删除即可


```python
df7a = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六", "牛七", "马八", "杨九", "Alice", "Bob", "Charlie"],
    "班级": ["一班", "一班", "一班", "二班", "二班", "三班", "三班", "四班", "四班", "六班"]
})

df7a
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
      <th>姓名</th>
      <th>班级</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>4</th>
      <td>牛七</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>5</th>
      <td>马八</td>
      <td>三班</td>
    </tr>
    <tr>
      <th>6</th>
      <td>杨九</td>
      <td>三班</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Alice</td>
      <td>四班</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bob</td>
      <td>四班</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Charlie</td>
      <td>六班</td>
    </tr>
  </tbody>
</table>
</div>




```python
df7b = pd.DataFrame({
    "班级": ["一班", "二班", "三班", "五班"],
    "班主任": ["老A", "老B", "老C", "老E"]
})

df7b
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
      <th>班级</th>
      <th>班主任</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>三班</td>
      <td>老C</td>
    </tr>
    <tr>
      <th>3</th>
      <td>五班</td>
      <td>老E</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged7 = pd.merge(df7a, df7b, on="班级", how="outer", indicator=True).query("_merge == 'right_only'").drop(columns="_merge")
df_merged7
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
      <th>姓名</th>
      <th>班级</th>
      <th>班主任</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>五班</td>
      <td>老E</td>
    </tr>
  </tbody>
</table>
</div>



#### (c) 全反连接

全反连接（Full Anti Join）：只保留两个表中不匹配的行，可以看作左反连接和右反连接的结合

- 从集合的角度来看，全反连接就是外连接的基础上，去掉了交集部分：

<div align="center">
    <img src="../UI25E_副本7.jpg" width="200">
</div>

- 回到班级的这个例子中，一个全反连接的例子可以用下图来表示：

<div align="center">
    <img src="../截屏2026-02-02 16.06.01.png" width="800">
</div>

- 通过全反连接，我们只保留了两个表中的特有行

- 在 Pandas 中，可以通过在 `merge()` 函数中指定 `how='outer'` 参数，并结合 `indicator=True` 参数来实现全反连接：

    - `indicator=True` 参数会在结果中添加一列 `_merge`，标识每一行的来源，原来是在左表中（`left_only`）还是右表中（`right_only`），还是两个表中都有（`both`）
    - 然后我们可以通过筛选不是 `both` 的行，来实现全反连接
    - 之后再把 `_merge` 列删除即可


```python
df8a = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六", "牛七", "马八", "杨九", "Alice", "Bob", "Charlie"],
    "班级": ["一班", "一班", "一班", "二班", "二班", "三班", "三班", "四班", "四班", "六班"]
})

df8a
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
      <th>姓名</th>
      <th>班级</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>4</th>
      <td>牛七</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>5</th>
      <td>马八</td>
      <td>三班</td>
    </tr>
    <tr>
      <th>6</th>
      <td>杨九</td>
      <td>三班</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Alice</td>
      <td>四班</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bob</td>
      <td>四班</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Charlie</td>
      <td>六班</td>
    </tr>
  </tbody>
</table>
</div>




```python
df8b = pd.DataFrame({
    "班级": ["一班", "二班", "三班", "五班"],
    "班主任": ["老A", "老B", "老C", "老E"]
})

df8b
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
      <th>班级</th>
      <th>班主任</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>三班</td>
      <td>老C</td>
    </tr>
    <tr>
      <th>3</th>
      <td>五班</td>
      <td>老E</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged8 = pd.merge(df8a, df8b, on="班级", how="outer", indicator=True).query("_merge != 'both'").drop(columns="_merge")
df_merged8
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
      <th>姓名</th>
      <th>班级</th>
      <th>班主任</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>五班</td>
      <td>老E</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Charlie</td>
      <td>六班</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Alice</td>
      <td>四班</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Bob</td>
      <td>四班</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### (4) 多键连接

多键连接是指在连接两个表时，使用多个列作为连接键，而不是单一的列：

- 多键连接的应用情景是，有的时候数据的标识信息可能不止一个列能够唯一标识，这时候就需要使用多个列来进行连接
- 比方说，假设我们将学生表修改修改，班级的标识要使用 `年级` 和 `班级` 两列来共同标识：

<div align="center">
    <img src="../截屏2026-02-02 16.20.07.png" width="800">
</div>

在 Pandas 中，可以通过在 `merge()` 函数中传入一个包含多个列名的列表，来实现多键连接：


```python
df9a = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六", "牛七", "马八"],
    "年级": ["一年级", "一年级", "二年级", "二年级", "二年级", "二年级"],
    "班级": ["一班", "二班", "一班", "二班", "二班", "三班"]
})

df9a
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
      <th>姓名</th>
      <th>年级</th>
      <th>班级</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一年级</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一年级</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>二年级</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
      <td>二年级</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>4</th>
      <td>牛七</td>
      <td>二年级</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>5</th>
      <td>马八</td>
      <td>二年级</td>
      <td>三班</td>
    </tr>
  </tbody>
</table>
</div>




```python
df9b = pd.DataFrame({
    "年级": ["一年级", "一年级", "二年级", "二年级", "二年级"],
    "班级": ["一班", "二班", "一班", "二班", "三班"],
    "班主任": ["老A", "老B", "老C", "老D", "老E"]
})

df9b
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
      <th>年级</th>
      <th>班级</th>
      <th>班主任</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>一年级</td>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>一年级</td>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>二年级</td>
      <td>一班</td>
      <td>老C</td>
    </tr>
    <tr>
      <th>3</th>
      <td>二年级</td>
      <td>二班</td>
      <td>老D</td>
    </tr>
    <tr>
      <th>4</th>
      <td>二年级</td>
      <td>三班</td>
      <td>老E</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged9 = pd.merge(df9a, df9b, on=["年级", "班级"], how="inner")
df_merged9
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
      <th>姓名</th>
      <th>年级</th>
      <th>班级</th>
      <th>班主任</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一年级</td>
      <td>一班</td>
      <td>老A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一年级</td>
      <td>二班</td>
      <td>老B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>二年级</td>
      <td>一班</td>
      <td>老C</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
      <td>二年级</td>
      <td>二班</td>
      <td>老D</td>
    </tr>
    <tr>
      <th>4</th>
      <td>牛七</td>
      <td>二年级</td>
      <td>二班</td>
      <td>老D</td>
    </tr>
    <tr>
      <th>5</th>
      <td>马八</td>
      <td>二年级</td>
      <td>三班</td>
      <td>老E</td>
    </tr>
  </tbody>
</table>
</div>



在多键连接的情境下，我们上面介绍的各种连接方式依然适用，只不过连接键变成了多个列，这里我们就不再赘述了。

## 2. 数据拼接

数据拼接，其实要比数据连接简单很多，数据拼接就是将两个表在行或者列的方向上进行拼接，并不用考虑连接键的问题。

### (1) 按行拼接

将两个表或多个表按行拼接，也就是纵向拼接，也就是添加新行，可以使用 Pandas 中的 `concat()` 函数来实现：

- 在这个函数中，我们只需要传入一个包含多个 DataFrame 的列表，然后指定 `axis=0` 参数即可实现按行拼接
- 按行拼接的条件是，所有被拼接的表必须具有相同的列结构，也就是说**列名、列数、列顺序**必须一致
- 在使用完 `concat()` 函数拼接之后，行的索引会继承原表的索引，如果想要重新生成连续的索引，可以再接一个 `.reset_index(drop=True)` 方法


```python
df_new1 = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "班级": ["一班", "一班", "一班"]
})

df_new1
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
      <th>姓名</th>
      <th>班级</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>一班</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_new2 = pd.DataFrame({
    "姓名": ["赵六", "牛七"],
    "班级": ["二班", "二班"]
})

df_new2
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
      <th>姓名</th>
      <th>班级</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>赵六</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>1</th>
      <td>牛七</td>
      <td>二班</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_concatenated1 = pd.concat([df_new1, df_new2], axis=0).reset_index(drop=True)
df_concatenated1
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
      <th>姓名</th>
      <th>班级</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>3</th>
      <td>赵六</td>
      <td>二班</td>
    </tr>
    <tr>
      <th>4</th>
      <td>牛七</td>
      <td>二班</td>
    </tr>
  </tbody>
</table>
</div>



### (2) 按列拼接

将两个表或多个表按列拼接，也就是横向拼接，也就是添加新列，可以使用 Pandas 中的 `concat()` 函数来实现：

- 在这个函数中，我们只需要传入一个包含多个 DataFrame 的列表，然后指定 `axis=1` 参数即可实现按列拼接
- 按列拼接的条件是，所有被拼接的表必须具有相同的行数，也就是说**行数**必须一致，这里对列是没有什么要求的，因为横向拼接的操作其实就是添加新列
- 在使用完 `concat()` 函数拼接之后，列的索引会继承原表的列索引，如果想要重新生成连续的列索引，可以再接一个 `.reset_index(drop=True, axis=1)` 方法


```python
df_new3 = pd.DataFrame({
    "姓名": ["张三", "李四", "王五"],
    "班级": ["一班", "一班", "一班"]
})

df_new3
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
      <th>姓名</th>
      <th>班级</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一班</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>一班</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_new4 = pd.DataFrame({
    "数学": [80, 90, 85],
    "语文": [75, 88, 92],
    "英语": [78, 85, 80]
})

df_new4
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
      <th>数学</th>
      <th>语文</th>
      <th>英语</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>80</td>
      <td>75</td>
      <td>78</td>
    </tr>
    <tr>
      <th>1</th>
      <td>90</td>
      <td>88</td>
      <td>85</td>
    </tr>
    <tr>
      <th>2</th>
      <td>85</td>
      <td>92</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_concatenated2 = pd.concat([df_new3, df_new4], axis=1).reset_index(drop=True)
df_concatenated2
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
      <th>姓名</th>
      <th>班级</th>
      <th>数学</th>
      <th>语文</th>
      <th>英语</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>一班</td>
      <td>80</td>
      <td>75</td>
      <td>78</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>一班</td>
      <td>90</td>
      <td>88</td>
      <td>85</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>一班</td>
      <td>85</td>
      <td>92</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>


