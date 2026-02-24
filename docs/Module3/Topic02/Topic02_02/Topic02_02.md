# Topic 2.2 - Pandas 中的数据创建与存储

本节开始之前，我们先导入 pandas 库： 


```python
import pandas as pd
```

## 1. 数据的创建

### (1) 自创 DataFrame 数据

在上一节，我们介绍了可以使用 Python 自带的数据结构（如列表、字典等）来创建 DataFrame 数据：

- 一种是列表套列表的形式，需要指定列名：


```python
data_df_1 = pd.DataFrame([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ],
    columns=['A', 'B', 'C']
)
data_df_1
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



- 另一种是字典套列表的形式，使用键作为列名：


```python
data_df_2 = pd.DataFrame({
    'A': [1, 4, 7],
    'B': [2, 5, 8],
    'C': [3, 6, 9]
})
data_df_2
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



在创建好数据之后，也可以插入新列和新行：

- 插入新列可以直接通过列名赋值一个列表的方式实现：


```python
data_df_2["D"] = [10, 11, 12]
data_df_2
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



- 插入新行有两种方法，一种是使用 `loc` 方法，指定新行的行名，然后赋值一个列表：


```python
data_df_2.loc[3] = [13, 14, 15, 16]
data_df_2
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13</td>
      <td>14</td>
      <td>15</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>



- 插入新行的另一种方法是使用 `concat` 方法，这种方法比较复杂，需要传入一个新的 DataFrame，然后通过 `ignore_index=True` 参数来重置索引：


```python
data_df_2 = pd.concat([data_df_2, pd.DataFrame({'A': [17], 'B': [18], 'C': [19], 'D': [20]})], ignore_index=True)
data_df_2
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13</td>
      <td>14</td>
      <td>15</td>
      <td>16</td>
    </tr>
    <tr>
      <th>4</th>
      <td>17</td>
      <td>18</td>
      <td>19</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>



### (2) 从文件中读取数据

Pandas 支持从多种文件格式中读取数据，包括 CSV、Excel、JSON 等。

从 CSV 文件读取数据可以使用 `pd.read_csv()` 函数，当中要强调文件路径：


```python
df_students = pd.read_csv('../data/students.csv')
df_students
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
      <th>name</th>
      <th>class</th>
      <th>gender</th>
      <th>age</th>
      <th>chinese</th>
      <th>math</th>
      <th>english</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice Johnson</td>
      <td>1</td>
      <td>Female</td>
      <td>18</td>
      <td>85</td>
      <td>88</td>
      <td>90</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob Smith</td>
      <td>2</td>
      <td>Male</td>
      <td>19</td>
      <td>78</td>
      <td>75</td>
      <td>80</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie Brown</td>
      <td>3</td>
      <td>Male</td>
      <td>18</td>
      <td>92</td>
      <td>90</td>
      <td>94</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David Miller</td>
      <td>1</td>
      <td>Male</td>
      <td>20</td>
      <td>88</td>
      <td>85</td>
      <td>87</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Emma Wilson</td>
      <td>2</td>
      <td>Female</td>
      <td>19</td>
      <td>76</td>
      <td>78</td>
      <td>74</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>86</th>
      <td>Jonah Larson</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>78</td>
      <td>76</td>
      <td>77</td>
    </tr>
    <tr>
      <th>87</th>
      <td>Kylie Newman</td>
      <td>1</td>
      <td>Female</td>
      <td>18</td>
      <td>85</td>
      <td>83</td>
      <td>84</td>
    </tr>
    <tr>
      <th>88</th>
      <td>Lucas Porter</td>
      <td>2</td>
      <td>Male</td>
      <td>22</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>89</th>
      <td>Megan Arnold</td>
      <td>3</td>
      <td>Female</td>
      <td>19</td>
      <td>79</td>
      <td>77</td>
      <td>78</td>
    </tr>
    <tr>
      <th>90</th>
      <td>Nick Keller</td>
      <td>1</td>
      <td>Male</td>
      <td>20</td>
      <td>87</td>
      <td>85</td>
      <td>88</td>
    </tr>
  </tbody>
</table>
<p>91 rows × 7 columns</p>
</div>



从 Excel 文件读取数据可以使用 `pd.read_excel()` 函数，同样需要指定文件路径，并且还需要指定工作表名称（如果有多个工作表的话）：


```python
df_sales = pd.read_excel('../data/sales.xlsx', sheet_name='sales')
df_sales
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
      <th>product</th>
      <th>price</th>
      <th>quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-01-01</td>
      <td>Camera</td>
      <td>4599</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-01-01</td>
      <td>Monitor</td>
      <td>1599</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2024-01-01</td>
      <td>Tablet</td>
      <td>2999</td>
      <td>11</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2024-01-01</td>
      <td>Phone</td>
      <td>4999</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2024-01-01</td>
      <td>Laptop</td>
      <td>6999</td>
      <td>10</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>328</th>
      <td>2024-02-29</td>
      <td>Speaker</td>
      <td>899</td>
      <td>11</td>
    </tr>
    <tr>
      <th>329</th>
      <td>2024-02-29</td>
      <td>Keyboard</td>
      <td>399</td>
      <td>11</td>
    </tr>
    <tr>
      <th>330</th>
      <td>2024-02-29</td>
      <td>Laptop</td>
      <td>6999</td>
      <td>10</td>
    </tr>
    <tr>
      <th>331</th>
      <td>2024-02-29</td>
      <td>Keyboard</td>
      <td>399</td>
      <td>14</td>
    </tr>
    <tr>
      <th>332</th>
      <td>2024-02-29</td>
      <td>Laptop</td>
      <td>6999</td>
      <td>14</td>
    </tr>
  </tbody>
</table>
<p>333 rows × 4 columns</p>
</div>



从 JSON 文件读取数据可以使用 `pd.read_json()` 函数，指定文件路径即可：


```python
df_records = pd.read_json('../data/records.json')
df_records
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
      <th>id</th>
      <th>date</th>
      <th>category</th>
      <th>value</th>
      <th>status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2024-01-01</td>
      <td>A</td>
      <td>12.5</td>
      <td>ok</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2024-01-01</td>
      <td>B</td>
      <td>9.8</td>
      <td>ok</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2024-01-02</td>
      <td>A</td>
      <td>15.2</td>
      <td>warning</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2024-01-02</td>
      <td>C</td>
      <td>7.1</td>
      <td>ok</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>2024-01-03</td>
      <td>B</td>
      <td>11.4</td>
      <td>error</td>
    </tr>
  </tbody>
</table>
</div>



## 2. 数据的存储

Pandas 也支持将 DataFrame 数据存储为多种文件格式，包括 CSV、Excel、JSON 等。

- 将数据存储为 CSV 文件可以使用 `to_csv()` 方法，指定文件路径即可

    - 这当中可以通过 `index=False` 参数来避免存储行索引
    - 如果设置 `index=True`，则会将行索引，也就是行号存储到文件中


```python
data_people_info = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["Melbourne", "Sydney", "Brisbane"]
})

data_people_info
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
      <th>name</th>
      <th>age</th>
      <th>city</th>
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
data_people_info.to_csv('../data/people_info.csv', index=False)
```

- 将数据存储为 Excel 文件可以使用 `to_excel()` 方法，指定文件路径和工作表名称即可：


```python
data_people_info.to_excel('../data/people_info.xlsx', sheet_name='info', index=False)
```

- 将数据存储为 JSON 文件可以使用 `to_json()` 方法，指定文件路径即可

    - 这当中可以通过 `orient` 参数来指定 JSON 的格式，如果设置为 `records`，则**每行**数据会被存储为一个 JSON 对象，如果设置为 `columns`，则**每列**数据会被存储为一个 JSON 对象
    - 还可以通过 `lines` 参数来指定是否将每个 JSON 对象存储在单独的一行，如果设置为 `True`，则每个 JSON 对象会被存储在单独的一行
    - 另外，还可以通过 `indent` 参数来指定缩进的空格数，以便于阅读


```python
data_people_info.to_json('../data/people_info.json', orient='records', lines=False, indent=4)
```
