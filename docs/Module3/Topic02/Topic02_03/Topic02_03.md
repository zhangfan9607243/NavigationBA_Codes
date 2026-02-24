# Topic 2.3 - Pandas 中的数据索引

Pandas 中的索引，是指将 DataFrame 中的数据进行标识和定位的方式，说白了就是将一部分数据提取出来，这种提取可以是：

- 提取出某列或某些列的数据
- 提取出某行或某些行的数据
- 既提取出某行又提取出某列的数据

我们就分别来讲解这几种提取数据的方式，我们先导入 pandas 库：


```python
import pandas as pd
```

## 1. 按列索引

在 Pandas 中，按列索引是指通过列名来提取 DataFrame 中的一列或多列数据。常用的方法有以下几种：

### (1) 提取单列数据为 Series

我们之前提到过，如果想要提取 DataFrame 中的一列数据，提取出来以后其实是 Series，可以使用以下两种方式：

- 一种是使用方括号 `df['列名']`，这里必须使用引号将列名括起来：


```python
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Melbourne', 'Sydney', 'Brisbane']
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
      <th>Name</th>
      <th>Age</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>25</td>
      <td>Melbourne</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>30</td>
      <td>Sydney</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>35</td>
      <td>Brisbane</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1['Name']
```




    0      Alice
    1        Bob
    2    Charlie
    Name: Name, dtype: object



- 还有一种是使用点号 `df.列名`：

    - 这种方式只能用于列名符合 Python 变量命名规则的情况，比如不能包含空格、不能以数字开头等
    - 例如 如果列名是 `First Name`，`Middle-Name` 或 `1stName`，就不能使用这种方式提取数据
    - 这就是为什么我们常说，在编程时，不论是给什么东西命名，最好都遵循变量命名规则，这样可以避免很多麻烦


```python
df1.Name
```




    0      Alice
    1        Bob
    2    Charlie
    Name: Name, dtype: object



### (2) 提取多列数据为 DataFrame

如果想要提取多列数据，提取出来以后还是 DataFrame，可以使用以下方式：

- 使用方括号 `df[['列名1', '列名2', ...]]`，这里需要使用双重方括号，外层方括号表示提取列，内层方括号表示列名的列表：


```python
df1[["Name", "Age"]]
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
      <th>Name</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>



- 这种方式提取一列数据时：`df[['列名']]`，提取出来的结果也是 DataFrame，而不是 Series，我们在前面的章节讨论过它们的区别


```python
df1[["Name"]]
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
      <th>Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
    </tr>
  </tbody>
</table>
</div>



## 2. 按行索引

如果想将行提取出来，主要有以下两种方式，我们之前其实介绍过：

- 使用 `iloc[行号]` 方法按顺序位置提取行数据，这种方式是不论行名是什么，谁在第几行就提取第几行
- 使用 `loc[行名]` 方法按行标签提取行数据

### (1) 使用 `iloc` 提取行数据

之前我们介绍过使用 `iloc` 方法提取一行数据，提取出来的一行其实是一个 Series：


```python
df1.iloc[0]
```




    Name        Alice
    Age            25
    City    Melbourne
    Name: 0, dtype: object



事实上，`iloc` 方法还可以提取多行数据，提取出来的结果是一个 DataFrame：

- 一种语法结构是和 Python 中的列表切片类似的：`.iloc[起始行号:结束行号:步长]`


```python
df1.iloc[0:2]
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
      <th>Name</th>
      <th>Age</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>25</td>
      <td>Melbourne</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>30</td>
      <td>Sydney</td>
    </tr>
  </tbody>
</table>
</div>



- 另一种语法结构是传入一个行号列表：`.iloc[[行号1, 行号2, ...]]`


```python
df1.iloc[[0,2]]
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
      <th>Name</th>
      <th>Age</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>25</td>
      <td>Melbourne</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>35</td>
      <td>Brisbane</td>
    </tr>
  </tbody>
</table>
</div>



### (2) 使用 `loc` 提取行数据

#### (a) 使用 `loc` 提取单行或多行数据

使用 `loc` 方法可以根据行标签（索引标签）提取行数据，提取出来的结果可以是 Series 或 DataFrame，具体取决于提取的是单行还是多行：

- 使用 `df.loc[行名]` 提取单行数据（这里传进去的是一个行标签），结果是一个 Series


```python
df1.loc[0]
```




    Name        Alice
    Age            25
    City    Melbourne
    Name: 0, dtype: object



- 使用 `df.loc[[行名1, 行名2, ...]]` 提取多行数据（这里传进去的是一个列表），结果是一个 DataFrame


```python
df1.loc[[0,1]]
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
      <th>Name</th>
      <th>Age</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>25</td>
      <td>Melbourne</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>30</td>
      <td>Sydney</td>
    </tr>
  </tbody>
</table>
</div>



- 使用 `df.loc[起始行名:结束行名]` 提取多行数据也是可以的，但是这种方法并不推荐：

    - 第一个原因是它**仅适用于行名是连续整数的情况**
    - 第二个原因是，这种方式和大家理解的切片有些出入，最终的结果是**包含结束行名对应的那一行数据的**


```python
df1.loc[0:1] 
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
      <th>Name</th>
      <th>Age</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>25</td>
      <td>Melbourne</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>30</td>
      <td>Sydney</td>
    </tr>
  </tbody>
</table>
</div>



由于我们使用的示例数据集的行名是默认的整数索引（0, 1, 2, ...），所以在这个例子中，`loc` 和 `iloc` 的效果类似，这里我们来看一个行名和顺序位置不一样的例子：


```python
df2 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Melbourne', 'Sydney', 'Brisbane']
}, index=[2, 1, 0])

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
      <th>Name</th>
      <th>Age</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>Alice</td>
      <td>25</td>
      <td>Melbourne</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>30</td>
      <td>Sydney</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Charlie</td>
      <td>35</td>
      <td>Brisbane</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.loc[0]
```




    Name     Charlie
    Age           35
    City    Brisbane
    Name: 0, dtype: object




```python
df2.iloc[0]
```




    Name        Alice
    Age            25
    City    Melbourne
    Name: 2, dtype: object



在上面这个例子中：

- `df2.loc[0]` 提取的是行名为 0 的那一行数据，也就是 Charlie 的数据
- `df2.iloc[0]` 提取的是第 0 行数据，也就是 Alice 的数据
- 由于行名和行的顺序位置不一样，所以 `loc` 和 `iloc` 提取出来的数据也不一样

#### (b) Pandas 中常见的行名类型

在 Pandas 中，行名可以是多种类型，常见的有以下几种：

- 整数索引：这是最常见的行名类型，默认情况下，Pandas 会为 DataFrame 分配从 0 开始的整数索引，但是也有可能是混乱的整数顺序


```python
df_rowname_1 = pd.DataFrame({
    'Name': ['David', 'Eva', 'Frank'],
    'Age': [28, 32, 29],
    'City': ['Adelaide', 'Perth', 'Hobart']
}, index=[0, 1, 2])

display(df_rowname_1)
display(df_rowname_1.loc[1])
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
      <th>Name</th>
      <th>Age</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>David</td>
      <td>28</td>
      <td>Adelaide</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Eva</td>
      <td>32</td>
      <td>Perth</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Frank</td>
      <td>29</td>
      <td>Hobart</td>
    </tr>
  </tbody>
</table>
</div>



    Name      Eva
    Age        32
    City    Perth
    Name: 1, dtype: object


- 字符串索引：行名可以是字符串类型，这种情况下，行名通常是有意义的标签，例如人名、城市名等


```python
df_rowname_2 = pd.DataFrame({
    'Name': ['George', 'Hannah', 'Ian'],
    'Age': [40, 38, 45],
    'City': ['Canberra', 'Darwin', 'Cairns']
}, index=['person001', 'person002', 'person003'])

display(df_rowname_2)
display(df_rowname_2.loc['person002'])
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
      <th>Name</th>
      <th>Age</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>person001</th>
      <td>George</td>
      <td>40</td>
      <td>Canberra</td>
    </tr>
    <tr>
      <th>person002</th>
      <td>Hannah</td>
      <td>38</td>
      <td>Darwin</td>
    </tr>
    <tr>
      <th>person003</th>
      <td>Ian</td>
      <td>45</td>
      <td>Cairns</td>
    </tr>
  </tbody>
</table>
</div>



    Name    Hannah
    Age         38
    City    Darwin
    Name: person002, dtype: object


- 日期时间索引：行名可以是日期时间类型，这在时间序列数据中非常常见


```python
df_rowname_3 = pd.DataFrame({
    'Product': ['A', 'B', 'C'],
    'Value': [100, 200, 300],
}, index=pd.date_range(start='2023-01-01', periods=3, freq='D'))

display(df_rowname_3)
display(df_rowname_3.index)
display(df_rowname_3.loc['2023-01-02'])
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
      <th>Product</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2023-01-01</th>
      <td>A</td>
      <td>100</td>
    </tr>
    <tr>
      <th>2023-01-02</th>
      <td>B</td>
      <td>200</td>
    </tr>
    <tr>
      <th>2023-01-03</th>
      <td>C</td>
      <td>300</td>
    </tr>
  </tbody>
</table>
</div>



    DatetimeIndex(['2023-01-01', '2023-01-02', '2023-01-03'], dtype='datetime64[ns]', freq='D')



    Product      B
    Value      200
    Name: 2023-01-02 00:00:00, dtype: object


- 区间索引：行名可以是区间类型，这在某些特定应用中可能会用到，例如表示年龄段、收入区间等，在取行名的时候，只要是在这个区间内的值，都可以取到对应的行数据


```python
df_rowname_4 = pd.DataFrame({
    "tax_rate": [0.1, 0.15, 0.2, 0.25],
    "bracket_name": ["low", "medium", "high", "very_high"]
}, index=pd.IntervalIndex.from_tuples([(0, 20000), (20000, 50000), (50000, 100000), (100000, float('inf'))]))

display(df_rowname_4)
display(df_rowname_4.index)
display(df_rowname_4.loc[25000])
display(df_rowname_4.loc[35000])
display(df_rowname_4.loc[75000])
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
      <th>tax_rate</th>
      <th>bracket_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>(0.0, 20000.0]</th>
      <td>0.10</td>
      <td>low</td>
    </tr>
    <tr>
      <th>(20000.0, 50000.0]</th>
      <td>0.15</td>
      <td>medium</td>
    </tr>
    <tr>
      <th>(50000.0, 100000.0]</th>
      <td>0.20</td>
      <td>high</td>
    </tr>
    <tr>
      <th>(100000.0, inf]</th>
      <td>0.25</td>
      <td>very_high</td>
    </tr>
  </tbody>
</table>
</div>



    IntervalIndex([(0.0, 20000.0], (20000.0, 50000.0], (50000.0, 100000.0],
                   (100000.0, inf]],
                  dtype='interval[float64, right]')



    tax_rate          0.15
    bracket_name    medium
    Name: (20000.0, 50000.0], dtype: object



    tax_rate          0.15
    bracket_name    medium
    Name: (20000.0, 50000.0], dtype: object



    tax_rate         0.2
    bracket_name    high
    Name: (50000.0, 100000.0], dtype: object


## 3. 按行与列同时索引

如果想同时提取某行和某列的数据：

- 一个比较直接的方法就是先提取列数据为一个新的 DataFrame，然后再从中提取行数据，或者反过来先行后列也行
- 这个大家组合我们上面介绍的内容就行，`loc` 与 `iloc` 混用也是可以的，这里我们就不赘述了

但是，其实 `loc` 和 `iloc` 方法都支持同时传入行和列的参数，可以一步到位地提取出某行某列的数据。

### (1) 使用 `iloc` 同时提取行和列数据

使用 `iloc` 方法时，可以同时传入行号和列号，语法结构如下：

- 第一个参数是行号，第二个参数是列号，都是基于位置的索引 `df.iloc[行号, 列号]`
- 例如，`df.iloc[1, 2]` 提取第 1 行第 2 列的数据


```python
df3 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'George', 'Hannah', 'Ian'],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', 'M', 'F', 'M'],
    'Age': [25, 30, 35, 28, 32, 29, 40, 38, 45],
    'City': ['Melbourne', 'Sydney', 'Brisbane', 'Adelaide', 'Perth', 'Hobart', 'Canberra', 'Darwin', 'Cairns'],
    'Height_cm': [165, 175, 180, 170, 160, 178, 182, 168, 185],
    'Weight_kg': [60, 80, 75, 70, 55, 78, 85, 58, 90]
})

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
      <th>Name</th>
      <th>Gender</th>
      <th>Age</th>
      <th>City</th>
      <th>Height_cm</th>
      <th>Weight_kg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>F</td>
      <td>25</td>
      <td>Melbourne</td>
      <td>165</td>
      <td>60</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>M</td>
      <td>30</td>
      <td>Sydney</td>
      <td>175</td>
      <td>80</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>M</td>
      <td>35</td>
      <td>Brisbane</td>
      <td>180</td>
      <td>75</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>M</td>
      <td>28</td>
      <td>Adelaide</td>
      <td>170</td>
      <td>70</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eva</td>
      <td>F</td>
      <td>32</td>
      <td>Perth</td>
      <td>160</td>
      <td>55</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Frank</td>
      <td>M</td>
      <td>29</td>
      <td>Hobart</td>
      <td>178</td>
      <td>78</td>
    </tr>
    <tr>
      <th>6</th>
      <td>George</td>
      <td>M</td>
      <td>40</td>
      <td>Canberra</td>
      <td>182</td>
      <td>85</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Hannah</td>
      <td>F</td>
      <td>38</td>
      <td>Darwin</td>
      <td>168</td>
      <td>58</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Ian</td>
      <td>M</td>
      <td>45</td>
      <td>Cairns</td>
      <td>185</td>
      <td>90</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.iloc[1, 2]
```




    np.int64(30)



并且，`iloc` 也支持传入行号和列号的列表，以提取多行多列的数据：

- 一种是使用切片语法：`df.iloc[起始行号:结束行号:行号步长, 起始列号:结束列号:列号步长]`


```python
df3.iloc[0:2, 1:3]
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
      <th>Gender</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>M</td>
      <td>30</td>
    </tr>
  </tbody>
</table>
</div>



- 另一种是传入行号和列号的列表：`df.iloc[[行号1, 行号2, ...], [列号1, 列号2, ...]]`


```python
df3.iloc[[0,2,3], [0,1,2]]
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
      <th>Name</th>
      <th>Gender</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>F</td>
      <td>25</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>M</td>
      <td>35</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>M</td>
      <td>28</td>
    </tr>
  </tbody>
</table>
</div>



- 当然，这两种结合使用也是可以的


```python
df3.iloc[0:2, [0,1,2]]
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
      <th>Name</th>
      <th>Gender</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>F</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>M</td>
      <td>30</td>
    </tr>
  </tbody>
</table>
</div>



除此之外，额外要说明的是：

- 如果想按列提取所有行的数据，可以在行号位置使用冒号 `:`，表示提取所有行
- 例如：`df.iloc[:, 列号]` 提取所有行的某些列数据


```python
df3.iloc[:, [0,2]]
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
      <th>Name</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>35</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>28</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eva</td>
      <td>32</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Frank</td>
      <td>29</td>
    </tr>
    <tr>
      <th>6</th>
      <td>George</td>
      <td>40</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Hannah</td>
      <td>38</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Ian</td>
      <td>45</td>
    </tr>
  </tbody>
</table>
</div>



### (2) 使用 `loc` 同时提取行和列数据

使用 `loc` 方法时，可以同时传入行名和列名，语法结构就是 `df.loc[行名, 列名]`


```python
df3.loc[0, 'Name']
```




    'Alice'



如果想提取多行多列的数据，也可以传入行名和列名的列表：`df.loc[[行名1, 行名2, ...], [列名1, 列名2, ...]]`


```python
df3.loc[[0,1], ['Name', 'Age', 'City']]
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
      <th>Name</th>
      <th>Age</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>25</td>
      <td>Melbourne</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>30</td>
      <td>Sydney</td>
    </tr>
  </tbody>
</table>
</div>



和 `iloc` 方法类似，`loc` 方法如果想提取某些列的所有行数据，也可以在行名位置使用冒号 `:`，表示提取所有行：


```python
df3.loc[:, ['Name', 'Age', 'City']]
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
      <th>Name</th>
      <th>Age</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>25</td>
      <td>Melbourne</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>30</td>
      <td>Sydney</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>35</td>
      <td>Brisbane</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>28</td>
      <td>Adelaide</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eva</td>
      <td>32</td>
      <td>Perth</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Frank</td>
      <td>29</td>
      <td>Hobart</td>
    </tr>
    <tr>
      <th>6</th>
      <td>George</td>
      <td>40</td>
      <td>Canberra</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Hannah</td>
      <td>38</td>
      <td>Darwin</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Ian</td>
      <td>45</td>
      <td>Cairns</td>
    </tr>
  </tbody>
</table>
</div>



## 4. Pandas 数据索引的注意事项

大家在看别人代码时，可能会发现一种写法，就是直接 `df[数字或切片]` 的形式来提取数据，不用 `.loc` 或 `.iloc`

这种写法我们其实是不推荐的，因为它的使用有些复杂和抽象，容易引起误解：

- 首先，如果直接传入一个数字，例如 `df[3]`，Pandas 会尝试将其解释为**列名**，而不是行号：

    - 如果 DataFrame 中存在名为 3 的列，那么就会提取该列的数据
    - 如果不存在名为 3 的列，那么就会报错，提示找不到该列

- 其次，如果传入一个切片对象，例如 `df[1:4]`，Pandas 会将其解释为**行切片**：

    - 这时的效果是等同于 `df.iloc[1:4]`，也就是提取第 1 行到第 3 行的数据（不包含第 4 行）
    - 其他注意事项也和 `iloc` 方法类似

因此，大家会发现：

- 这种写法在提取数据时，行为和我们预期的不一样，传入数字提取列，传入切片提取行，很容易引起混淆
- 为了代码的可读性和一致性，建议大家始终使用 `loc` 或 `iloc` 方法来进行数据索引操作

## 5. Pandas 中的多级索引

### (1) 多级索引简介

在 Pandas 的表格中，有时候会遇到需要用多个层级来标识行或列的情况，这时就需要使用多级索引（MultiIndex）。

我们先来看下面这个表格：

<div align="center">
    <img src="../截屏2026-01-30 14.34.44.png" width="400"/>
</div>

- 这种表格在我们生活中十分常见，行名和列名都有多级结构，比如行名是年份和季度的组合，列名是品类和口味的组合
- 如果想定位到某个数值，就必须使用多级索引来指定行和列
- 比方说我们想要定位到2025年第二季度，薯片的烧烤味销量 61，这时就需要同时指定两个行级别和两个列级别的信息

在 Pandas 中定义这样一个多级索引的 DataFrame，可以使用 `pd.MultiIndex` 来创建行和列的多级索引：

- 具体来说，多级索引又分为常见的两种情况：

    - `pd.MultiIndex.from_product` 表示的是各级别之间是全组合关系，比如年份和季度的组合，2024年有四个季度，2025年也有四个季度，所以总共有 2 x 4 = 8 个行索引
    - `pd.MultiIndex.from_tuples` 则表示的是各级别之间是非全组合关系，比如品类和口味的组合，薯片有两种口味，饮料有两种口味，但是并不是每种品类都有所有的口味组合，这就需要我们手动指定每个组合的元组列表

- 这两种情况中，都还要指定每个级别的名称，方便后续定位数据时使用


```python
df_multi = pd.DataFrame(
    [
        [10, 11, 12, 13],
        [20, 21, 22, 23],
        [30, 31, 32, 33],
        [40, 41, 42, 43],
        [50, 51, 52, 53],
        [60, 61, 62, 63],
        [70, 71, 72, 73],
        [80, 81, 82, 83],
    ],
    # 年和季度：全组合关系，使用 pd.MultiIndex.from_product
    index=pd.MultiIndex.from_product(
        [["2024年", "2025年"],
         ["第一季度", "第二季度", "第三季度", "第四季度"]],
        names=["年份", "季度"]
    ),
    # 品类和口味：非全组合关系，使用 pd.MultiIndex.from_tuples
    columns=pd.MultiIndex.from_tuples(
        [
            ("薯片", "番茄味"),
            ("薯片", "烧烤味"),
            ("冰淇淋", "香草味"),
            ("冰淇淋", "巧克力味"),
        ],
        names=["品类", "口味"]
    )
)

df_multi
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>品类</th>
      <th colspan="2" halign="left">薯片</th>
      <th colspan="2" halign="left">冰淇淋</th>
    </tr>
    <tr>
      <th></th>
      <th>口味</th>
      <th>番茄味</th>
      <th>烧烤味</th>
      <th>香草味</th>
      <th>巧克力味</th>
    </tr>
    <tr>
      <th>年份</th>
      <th>季度</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">2024年</th>
      <th>第一季度</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
    </tr>
    <tr>
      <th>第二季度</th>
      <td>20</td>
      <td>21</td>
      <td>22</td>
      <td>23</td>
    </tr>
    <tr>
      <th>第三季度</th>
      <td>30</td>
      <td>31</td>
      <td>32</td>
      <td>33</td>
    </tr>
    <tr>
      <th>第四季度</th>
      <td>40</td>
      <td>41</td>
      <td>42</td>
      <td>43</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">2025年</th>
      <th>第一季度</th>
      <td>50</td>
      <td>51</td>
      <td>52</td>
      <td>53</td>
    </tr>
    <tr>
      <th>第二季度</th>
      <td>60</td>
      <td>61</td>
      <td>62</td>
      <td>63</td>
    </tr>
    <tr>
      <th>第三季度</th>
      <td>70</td>
      <td>71</td>
      <td>72</td>
      <td>73</td>
    </tr>
    <tr>
      <th>第四季度</th>
      <td>80</td>
      <td>81</td>
      <td>82</td>
      <td>83</td>
    </tr>
  </tbody>
</table>
</div>



在定义好多级索引的 DataFrame 以后，我们就可以使用 `loc` 方法来定位数据了：

- 这里的多级索引是通过元组来表示的，元组中的每个元素对应一个级别
- 例如：

    - `df_multi.loc[('2024年', '第一季度')]` 就表示定位到 2024 年第一季度的这一行数据
    - `df_multi.loc[:, ('薯片', '烧烤味')]` 就表示定位到薯片的烧烤味这一列数据
    - `df_multi.loc[('2025年', '第二季度'), ('薯片', '烧烤味')]` 就表示定位到 2025 年第二季度，薯片的烧烤味销量 61


```python
df_multi.loc[('2024年', '第一季度')]
```




    品类   口味  
    薯片   番茄味     10
         烧烤味     11
    冰淇淋  香草味     12
         巧克力味    13
    Name: (2024年, 第一季度), dtype: int64




```python
df_multi.loc[:, ('薯片', '烧烤味')]
```




    年份     季度  
    2024年  第一季度    11
           第二季度    21
           第三季度    31
           第四季度    41
    2025年  第一季度    51
           第二季度    61
           第三季度    71
           第四季度    81
    Name: (薯片, 烧烤味), dtype: int64




```python
df_multi.loc[('2025年', '第二季度'), ('薯片', '烧烤味')]
```




    np.int64(61)



### (2) 多级索引转换为单级索引

这种多级索引的表格，其实常常被用作数据透视表（Pivot Table），它可以帮助我们更好地展示数据。

- 但是，这种多级索引的数据透视表格式，在数据处理和分析时，可能会增加一些复杂度
- 因为多级索引的 DataFrame 在进行数据操作时，需要同时考虑多个级别的索引，这可能会导致代码变得复杂且难以维护
- 因此，在实际应用中，我们还是想用一种更简单的扁平化结构来存储和处理数据，也就是将多级索引转换为单级索引的形式

我们来看一个多级索引和单级索引转换的例子：

- 还是表达薯条和冰淇淋销量，多级索引的数据透视表是一种很直观的表示方式：

<div align="center">
    <img src="../截屏2026-01-30 14.34.44.png" width="500">
</div>

- 如果用单级索引，则是用一个长表格来表示相同的数据，这里其实就是讲索引全部变成新列中的值：

<div align="center">
    <img src="../截屏2026-01-31 23.16.29.png" width="500">
</div>

在 Pandas 中，将多级索引转换为单级索引，可以使用 `stack()` 方法：

- 具体来说，`stack()` 方法可以将 DataFrame 的某个级别的索引转换为行索引，从而实现多级索引到单级索引的转换
- 也就是说，想把列上的索引，想挪到行上，就填到 `stack()` 方法里面去
- 在我们这个例子中，数据的定位需要四个级别的信息，分别是年份、季度、品类、口味
- 而年份和季度本身就是行索引，所以我们只需要将品类和口味这两个列索引展开到行索引即可，也就是 `stack(["品类", "口味"])`
- 之后还要做两件事：

    - 一是多级索引的数据透视表中没有销量这一列名，需要用 `rename("销量")` 来命名
    - 二是将多级索引转换为普通列，可以使用 `reset_index()` 方法


```python
df_multi_new1 = pd.DataFrame(
    [
        [10, 11, 12, 13],
        [20, 21, 22, 23],
        [30, 31, 32, 33],
        [40, 41, 42, 43],
        [50, 51, 52, 53],
        [60, 61, 62, 63],
        [70, 71, 72, 73],
        [80, 81, 82, 83],
    ],
    # 年和季度：全组合关系，使用 pd.MultiIndex.from_product
    index=pd.MultiIndex.from_product(
        [["2024年", "2025年"],
         ["第一季度", "第二季度", "第三季度", "第四季度"]],
        names=["年份", "季度"]
    ),
    # 品类和口味：非全组合关系，使用 pd.MultiIndex.from_tuples
    columns=pd.MultiIndex.from_tuples(
        [
            ("薯片", "番茄味"),
            ("薯片", "烧烤味"),
            ("冰淇淋", "香草味"),
            ("冰淇淋", "巧克力味"),
        ],
        names=["品类", "口味"]
    )
)

df_multi_new1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>品类</th>
      <th colspan="2" halign="left">薯片</th>
      <th colspan="2" halign="left">冰淇淋</th>
    </tr>
    <tr>
      <th></th>
      <th>口味</th>
      <th>番茄味</th>
      <th>烧烤味</th>
      <th>香草味</th>
      <th>巧克力味</th>
    </tr>
    <tr>
      <th>年份</th>
      <th>季度</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">2024年</th>
      <th>第一季度</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
    </tr>
    <tr>
      <th>第二季度</th>
      <td>20</td>
      <td>21</td>
      <td>22</td>
      <td>23</td>
    </tr>
    <tr>
      <th>第三季度</th>
      <td>30</td>
      <td>31</td>
      <td>32</td>
      <td>33</td>
    </tr>
    <tr>
      <th>第四季度</th>
      <td>40</td>
      <td>41</td>
      <td>42</td>
      <td>43</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">2025年</th>
      <th>第一季度</th>
      <td>50</td>
      <td>51</td>
      <td>52</td>
      <td>53</td>
    </tr>
    <tr>
      <th>第二季度</th>
      <td>60</td>
      <td>61</td>
      <td>62</td>
      <td>63</td>
    </tr>
    <tr>
      <th>第三季度</th>
      <td>70</td>
      <td>71</td>
      <td>72</td>
      <td>73</td>
    </tr>
    <tr>
      <th>第四季度</th>
      <td>80</td>
      <td>81</td>
      <td>82</td>
      <td>83</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_single_new1 = (
    df_multi_new1
    .stack(["品类", "口味"], future_stack=True)      # 把列索引展开到行索引，并且保留未来版本兼容性，因为 stack 方法未来版本会改变默认行为
    .rename("销量")              # Series 命名
    .reset_index()              # 变成普通列：年份、季度、品类、口味、销量
)

df_single_new1
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
      <th>年份</th>
      <th>季度</th>
      <th>品类</th>
      <th>口味</th>
      <th>销量</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024年</td>
      <td>第一季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024年</td>
      <td>第一季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024年</td>
      <td>第一季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024年</td>
      <td>第一季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>13</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024年</td>
      <td>第二季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>20</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024年</td>
      <td>第二季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>21</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024年</td>
      <td>第二季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>22</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024年</td>
      <td>第二季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>23</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024年</td>
      <td>第三季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>30</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024年</td>
      <td>第三季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>31</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2024年</td>
      <td>第三季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>32</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2024年</td>
      <td>第三季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>33</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2024年</td>
      <td>第四季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>40</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2024年</td>
      <td>第四季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>41</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2024年</td>
      <td>第四季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>42</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2024年</td>
      <td>第四季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>43</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2025年</td>
      <td>第一季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>50</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2025年</td>
      <td>第一季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>51</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2025年</td>
      <td>第一季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>52</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2025年</td>
      <td>第一季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>53</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2025年</td>
      <td>第二季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>60</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2025年</td>
      <td>第二季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>61</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2025年</td>
      <td>第二季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>62</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2025年</td>
      <td>第二季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>63</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2025年</td>
      <td>第三季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>70</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2025年</td>
      <td>第三季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>71</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2025年</td>
      <td>第三季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>72</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2025年</td>
      <td>第三季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>73</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2025年</td>
      <td>第四季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>80</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2025年</td>
      <td>第四季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>81</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2025年</td>
      <td>第四季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>82</td>
    </tr>
    <tr>
      <th>31</th>
      <td>2025年</td>
      <td>第四季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>83</td>
    </tr>
  </tbody>
</table>
</div>



这里我们来看一下，如果不加 `reset_index()` 会怎么样：

- 这里我们需加上 `.to_frame()` 否则结果不是 DataFrame，只是个 Series：


```python
df_multi_new1.stack(["品类", "口味"], future_stack=True).rename("销量").to_frame()
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
      <th></th>
      <th></th>
      <th></th>
      <th>销量</th>
    </tr>
    <tr>
      <th>年份</th>
      <th>季度</th>
      <th>品类</th>
      <th>口味</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="16" valign="top">2024年</th>
      <th rowspan="4" valign="top">第一季度</th>
      <th rowspan="2" valign="top">薯片</th>
      <th>番茄味</th>
      <td>10</td>
    </tr>
    <tr>
      <th>烧烤味</th>
      <td>11</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">冰淇淋</th>
      <th>香草味</th>
      <td>12</td>
    </tr>
    <tr>
      <th>巧克力味</th>
      <td>13</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">第二季度</th>
      <th rowspan="2" valign="top">薯片</th>
      <th>番茄味</th>
      <td>20</td>
    </tr>
    <tr>
      <th>烧烤味</th>
      <td>21</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">冰淇淋</th>
      <th>香草味</th>
      <td>22</td>
    </tr>
    <tr>
      <th>巧克力味</th>
      <td>23</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">第三季度</th>
      <th rowspan="2" valign="top">薯片</th>
      <th>番茄味</th>
      <td>30</td>
    </tr>
    <tr>
      <th>烧烤味</th>
      <td>31</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">冰淇淋</th>
      <th>香草味</th>
      <td>32</td>
    </tr>
    <tr>
      <th>巧克力味</th>
      <td>33</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">第四季度</th>
      <th rowspan="2" valign="top">薯片</th>
      <th>番茄味</th>
      <td>40</td>
    </tr>
    <tr>
      <th>烧烤味</th>
      <td>41</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">冰淇淋</th>
      <th>香草味</th>
      <td>42</td>
    </tr>
    <tr>
      <th>巧克力味</th>
      <td>43</td>
    </tr>
    <tr>
      <th rowspan="16" valign="top">2025年</th>
      <th rowspan="4" valign="top">第一季度</th>
      <th rowspan="2" valign="top">薯片</th>
      <th>番茄味</th>
      <td>50</td>
    </tr>
    <tr>
      <th>烧烤味</th>
      <td>51</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">冰淇淋</th>
      <th>香草味</th>
      <td>52</td>
    </tr>
    <tr>
      <th>巧克力味</th>
      <td>53</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">第二季度</th>
      <th rowspan="2" valign="top">薯片</th>
      <th>番茄味</th>
      <td>60</td>
    </tr>
    <tr>
      <th>烧烤味</th>
      <td>61</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">冰淇淋</th>
      <th>香草味</th>
      <td>62</td>
    </tr>
    <tr>
      <th>巧克力味</th>
      <td>63</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">第三季度</th>
      <th rowspan="2" valign="top">薯片</th>
      <th>番茄味</th>
      <td>70</td>
    </tr>
    <tr>
      <th>烧烤味</th>
      <td>71</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">冰淇淋</th>
      <th>香草味</th>
      <td>72</td>
    </tr>
    <tr>
      <th>巧克力味</th>
      <td>73</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">第四季度</th>
      <th rowspan="2" valign="top">薯片</th>
      <th>番茄味</th>
      <td>80</td>
    </tr>
    <tr>
      <th>烧烤味</th>
      <td>81</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">冰淇淋</th>
      <th>香草味</th>
      <td>82</td>
    </tr>
    <tr>
      <th>巧克力味</th>
      <td>83</td>
    </tr>
  </tbody>
</table>
</div>



- 可以看到，虽然四个级别的索引都展开到了行索引中，但是它们依然是多级索引的形式，类似于 Excel 中合并了单元格的产物，不是普通列
- 只有加了 `reset_index()`，才能将多级索引转换为普通列，变成我们想要的单级索引格式：


```python
df_multi_new1.stack(["品类", "口味"], future_stack=True).rename("销量").reset_index()
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
      <th>年份</th>
      <th>季度</th>
      <th>品类</th>
      <th>口味</th>
      <th>销量</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024年</td>
      <td>第一季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024年</td>
      <td>第一季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024年</td>
      <td>第一季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024年</td>
      <td>第一季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>13</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024年</td>
      <td>第二季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>20</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024年</td>
      <td>第二季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>21</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024年</td>
      <td>第二季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>22</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024年</td>
      <td>第二季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>23</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024年</td>
      <td>第三季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>30</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024年</td>
      <td>第三季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>31</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2024年</td>
      <td>第三季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>32</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2024年</td>
      <td>第三季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>33</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2024年</td>
      <td>第四季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>40</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2024年</td>
      <td>第四季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>41</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2024年</td>
      <td>第四季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>42</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2024年</td>
      <td>第四季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>43</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2025年</td>
      <td>第一季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>50</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2025年</td>
      <td>第一季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>51</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2025年</td>
      <td>第一季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>52</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2025年</td>
      <td>第一季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>53</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2025年</td>
      <td>第二季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>60</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2025年</td>
      <td>第二季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>61</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2025年</td>
      <td>第二季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>62</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2025年</td>
      <td>第二季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>63</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2025年</td>
      <td>第三季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>70</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2025年</td>
      <td>第三季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>71</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2025年</td>
      <td>第三季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>72</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2025年</td>
      <td>第三季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>73</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2025年</td>
      <td>第四季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>80</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2025年</td>
      <td>第四季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>81</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2025年</td>
      <td>第四季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>82</td>
    </tr>
    <tr>
      <th>31</th>
      <td>2025年</td>
      <td>第四季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>83</td>
    </tr>
  </tbody>
</table>
</div>



### (3) 单级索引转换为多级索引

当然，单级索引转换为多级索引也是可以的，可以使用 `unstack()` 方法：

- 和 `stack()` 方法相反，`unstack()` 方法是将行索引的某个级别转换为列索引，从而实现单级索引到多级索引的转换
- 也就是说，在行上的索引，想挪到列上，就填到 `unstack()` 方法里面去
- 在我们这个例子中，假如说我们手头有的是上面这个单级索引的 DataFrame，我们想把品类和口味挪到列上，就要用 `unstack(["品类", "口味"])`
- 除此之外，还有两件事需要注意：

    - 一是在使用 `unstack()` 方法之前，要先将**所有级别的索引设置为行索引**，可以使用 `set_index()` 方法
    - 二是要选择数值列，也就是将哪一列进行数据透视，比如 `["销量"]`



```python
df_single_new2 = pd.DataFrame({
    "年份": [
        "2024年","2024年","2024年","2024年",
        "2024年","2024年","2024年","2024年",
        "2024年","2024年","2024年","2024年",
        "2024年","2024年","2024年","2024年",
        "2025年","2025年","2025年","2025年",
        "2025年","2025年","2025年","2025年",
        "2025年","2025年","2025年","2025年",
        "2025年","2025年","2025年","2025年",
    ],
    "季度": [
        "第一季度","第一季度","第一季度","第一季度",
        "第二季度","第二季度","第二季度","第二季度",
        "第三季度","第三季度","第三季度","第三季度",
        "第四季度","第四季度","第四季度","第四季度",
        "第一季度","第一季度","第一季度","第一季度",
        "第二季度","第二季度","第二季度","第二季度",
        "第三季度","第三季度","第三季度","第三季度",
        "第四季度","第四季度","第四季度","第四季度",
    ],
    "品类": [
        "薯片","薯片","冰淇淋","冰淇淋",
        "薯片","薯片","冰淇淋","冰淇淋",
        "薯片","薯片","冰淇淋","冰淇淋",
        "薯片","薯片","冰淇淋","冰淇淋",
        "薯片","薯片","冰淇淋","冰淇淋",
        "薯片","薯片","冰淇淋","冰淇淋",
        "薯片","薯片","冰淇淋","冰淇淋",
        "薯片","薯片","冰淇淋","冰淇淋",
    ],
    "口味": [
        "番茄味","烧烤味","香草味","巧克力味",
        "番茄味","烧烤味","香草味","巧克力味",
        "番茄味","烧烤味","香草味","巧克力味",
        "番茄味","烧烤味","香草味","巧克力味",
        "番茄味","烧烤味","香草味","巧克力味",
        "番茄味","烧烤味","香草味","巧克力味",
        "番茄味","烧烤味","香草味","巧克力味",
        "番茄味","烧烤味","香草味","巧克力味",
    ],
    "销量": [
        10,11,12,13,
        20,21,22,23,
        30,31,32,33,
        40,41,42,43,
        50,51,52,53,
        60,61,62,63,
        70,71,72,73,
        80,81,82,83,
    ]
})

df_single_new2
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
      <th>年份</th>
      <th>季度</th>
      <th>品类</th>
      <th>口味</th>
      <th>销量</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024年</td>
      <td>第一季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024年</td>
      <td>第一季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024年</td>
      <td>第一季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024年</td>
      <td>第一季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>13</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024年</td>
      <td>第二季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>20</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2024年</td>
      <td>第二季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>21</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2024年</td>
      <td>第二季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>22</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2024年</td>
      <td>第二季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>23</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2024年</td>
      <td>第三季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>30</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2024年</td>
      <td>第三季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>31</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2024年</td>
      <td>第三季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>32</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2024年</td>
      <td>第三季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>33</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2024年</td>
      <td>第四季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>40</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2024年</td>
      <td>第四季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>41</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2024年</td>
      <td>第四季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>42</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2024年</td>
      <td>第四季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>43</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2025年</td>
      <td>第一季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>50</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2025年</td>
      <td>第一季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>51</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2025年</td>
      <td>第一季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>52</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2025年</td>
      <td>第一季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>53</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2025年</td>
      <td>第二季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>60</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2025年</td>
      <td>第二季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>61</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2025年</td>
      <td>第二季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>62</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2025年</td>
      <td>第二季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>63</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2025年</td>
      <td>第三季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>70</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2025年</td>
      <td>第三季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>71</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2025年</td>
      <td>第三季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>72</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2025年</td>
      <td>第三季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>73</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2025年</td>
      <td>第四季度</td>
      <td>薯片</td>
      <td>番茄味</td>
      <td>80</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2025年</td>
      <td>第四季度</td>
      <td>薯片</td>
      <td>烧烤味</td>
      <td>81</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2025年</td>
      <td>第四季度</td>
      <td>冰淇淋</td>
      <td>香草味</td>
      <td>82</td>
    </tr>
    <tr>
      <th>31</th>
      <td>2025年</td>
      <td>第四季度</td>
      <td>冰淇淋</td>
      <td>巧克力味</td>
      <td>83</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_multi_new2 = (
    df_single_new2
    .set_index(["年份", "季度", "品类", "口味"])["销量"]
    .unstack(["品类", "口味"])
)

df_multi_new2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>品类</th>
      <th colspan="2" halign="left">薯片</th>
      <th colspan="2" halign="left">冰淇淋</th>
    </tr>
    <tr>
      <th></th>
      <th>口味</th>
      <th>番茄味</th>
      <th>烧烤味</th>
      <th>香草味</th>
      <th>巧克力味</th>
    </tr>
    <tr>
      <th>年份</th>
      <th>季度</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">2024年</th>
      <th>第一季度</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
    </tr>
    <tr>
      <th>第三季度</th>
      <td>30</td>
      <td>31</td>
      <td>32</td>
      <td>33</td>
    </tr>
    <tr>
      <th>第二季度</th>
      <td>20</td>
      <td>21</td>
      <td>22</td>
      <td>23</td>
    </tr>
    <tr>
      <th>第四季度</th>
      <td>40</td>
      <td>41</td>
      <td>42</td>
      <td>43</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">2025年</th>
      <th>第一季度</th>
      <td>50</td>
      <td>51</td>
      <td>52</td>
      <td>53</td>
    </tr>
    <tr>
      <th>第三季度</th>
      <td>70</td>
      <td>71</td>
      <td>72</td>
      <td>73</td>
    </tr>
    <tr>
      <th>第二季度</th>
      <td>60</td>
      <td>61</td>
      <td>62</td>
      <td>63</td>
    </tr>
    <tr>
      <th>第四季度</th>
      <td>80</td>
      <td>81</td>
      <td>82</td>
      <td>83</td>
    </tr>
  </tbody>
</table>
</div>


