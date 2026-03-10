# Topic 2.2 - WHERE 条件过滤

## 1. WHERE 语句

### (1) 按单一条件查询

WHERE 语句用于在 SQL 查询中指定查询条件，只有满足条件的行才会被返回。

WHERE 语句的基本语法如下：

```sql
SELECT 列名1, 列名2, ...
FROM 表名
WHERE 条件;
```

其中，如果是在数值型列上进行条件判断，可以使用我们熟悉的比较运算符：

- `=`：等于（注意，在 SQL 中，判断等于使用 `=`，而不是 `==`，因为）
- `<>` 或 `!=`：不等于
- `>`：大于
- `<`：小于
- `>=`：大于或等于
- `<=`：小于或等于

我们来看以下几个例子：

- 查询 `Album` 表中 `ArtistId` 列的值等于 1 的行：


```sql
%%sql
SELECT *
FROM Album
WHERE ArtistId = 1
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
      <th>AlbumId</th>
      <th>Title</th>
      <th>ArtistId</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>For Those About To Rock We Salute You</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>Let There Be Rock</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



- 查询 `Track` 表中的 `TrackId`、`Name`、`UnitPrice` 三列，只要 `UnitPrice` 列的值大于 0.99 的行：


```sql
%%sql
SELECT
    TrackId,
    Name,
    UnitPrice
FROM Track
WHERE UnitPrice > 0.99
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
      <th>TrackId</th>
      <th>Name</th>
      <th>UnitPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2819</td>
      <td>Battlestar Galactica: The Story So Far</td>
      <td>1.99</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2820</td>
      <td>Occupation / Precipice</td>
      <td>1.99</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2821</td>
      <td>Exodus, Pt. 1</td>
      <td>1.99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2822</td>
      <td>Exodus, Pt. 2</td>
      <td>1.99</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2823</td>
      <td>Collaborators</td>
      <td>1.99</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>208</th>
      <td>3362</td>
      <td>There's No Place Like Home, Pt. 1</td>
      <td>1.99</td>
    </tr>
    <tr>
      <th>209</th>
      <td>3363</td>
      <td>There's No Place Like Home, Pt. 2</td>
      <td>1.99</td>
    </tr>
    <tr>
      <th>210</th>
      <td>3364</td>
      <td>There's No Place Like Home, Pt. 3</td>
      <td>1.99</td>
    </tr>
    <tr>
      <th>211</th>
      <td>3428</td>
      <td>Branch Closing</td>
      <td>1.99</td>
    </tr>
    <tr>
      <th>212</th>
      <td>3429</td>
      <td>The Return</td>
      <td>1.99</td>
    </tr>
  </tbody>
</table>
<p>213 rows × 3 columns</p>
</div>



- 查询 `Invoice` 表中所有 `BillingCountry` 列的值等于 `Brazil` 的行，只展示 `CustomerId` 与 `InvoiceDate` 两列：


```sql
%%sql
SELECT
    CustomerId,
    InvoiceDate
FROM Invoice
WHERE BillingCountry = 'Brazil'
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
      <th>CustomerId</th>
      <th>InvoiceDate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>2021-04-09 00:00:00.000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>12</td>
      <td>2021-05-23 00:00:00.000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13</td>
      <td>2021-06-05 00:00:00.000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11</td>
      <td>2021-09-06 00:00:00.000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>13</td>
      <td>2021-09-07 00:00:00.000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11</td>
      <td>2021-10-17 00:00:00.000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>13</td>
      <td>2021-12-10 00:00:00.000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1</td>
      <td>2022-03-11 00:00:00.000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1</td>
      <td>2022-06-13 00:00:00.000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>11</td>
      <td>2022-06-17 00:00:00.000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>13</td>
      <td>2022-07-31 00:00:00.000</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1</td>
      <td>2022-09-15 00:00:00.000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>10</td>
      <td>2022-11-14 00:00:00.000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>12</td>
      <td>2022-11-14 00:00:00.000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>12</td>
      <td>2022-12-25 00:00:00.000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>10</td>
      <td>2023-02-16 00:00:00.000</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1</td>
      <td>2023-05-06 00:00:00.000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>10</td>
      <td>2023-05-21 00:00:00.000</td>
    </tr>
    <tr>
      <th>18</th>
      <td>12</td>
      <td>2023-08-25 00:00:00.000</td>
    </tr>
    <tr>
      <th>19</th>
      <td>10</td>
      <td>2024-01-09 00:00:00.000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>11</td>
      <td>2024-01-22 00:00:00.000</td>
    </tr>
    <tr>
      <th>21</th>
      <td>13</td>
      <td>2024-01-22 00:00:00.000</td>
    </tr>
    <tr>
      <th>22</th>
      <td>13</td>
      <td>2024-03-03 00:00:00.000</td>
    </tr>
    <tr>
      <th>23</th>
      <td>11</td>
      <td>2024-04-25 00:00:00.000</td>
    </tr>
    <tr>
      <th>24</th>
      <td>11</td>
      <td>2024-07-28 00:00:00.000</td>
    </tr>
    <tr>
      <th>25</th>
      <td>1</td>
      <td>2024-10-27 00:00:00.000</td>
    </tr>
    <tr>
      <th>26</th>
      <td>13</td>
      <td>2024-11-01 00:00:00.000</td>
    </tr>
    <tr>
      <th>27</th>
      <td>1</td>
      <td>2024-12-07 00:00:00.000</td>
    </tr>
    <tr>
      <th>28</th>
      <td>11</td>
      <td>2025-03-18 00:00:00.000</td>
    </tr>
    <tr>
      <th>29</th>
      <td>12</td>
      <td>2025-03-31 00:00:00.000</td>
    </tr>
    <tr>
      <th>30</th>
      <td>10</td>
      <td>2025-07-02 00:00:00.000</td>
    </tr>
    <tr>
      <th>31</th>
      <td>12</td>
      <td>2025-07-03 00:00:00.000</td>
    </tr>
    <tr>
      <th>32</th>
      <td>1</td>
      <td>2025-08-07 00:00:00.000</td>
    </tr>
    <tr>
      <th>33</th>
      <td>10</td>
      <td>2025-08-12 00:00:00.000</td>
    </tr>
    <tr>
      <th>34</th>
      <td>12</td>
      <td>2025-10-05 00:00:00.000</td>
    </tr>
  </tbody>
</table>
</div>



### (2) 按多个条件查询

在按照多个条件查询时，我们就要使用到逻辑运算符 `AND` & `OR` & `NOT` 来连接多个条件

- 这三个逻辑运算符和大家在 Python 中使用的逻辑运算符的含义是完全一样的
- 并且我们推荐大家，在逻辑表达比较复杂的时候，使用括号 `()` 来明确表达式的优先级

我们来看以下几个例子：

- 查询 `Track` 表中 `UnitPrice` 列的值大于 0.99 且 `Milliseconds` 列的值大于 50000000 的行：


```sql
%%sql
SELECT *
FROM Track
WHERE UnitPrice > 0.99
AND Milliseconds > 5000000
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
      <th>TrackId</th>
      <th>Name</th>
      <th>AlbumId</th>
      <th>MediaTypeId</th>
      <th>GenreId</th>
      <th>Composer</th>
      <th>Milliseconds</th>
      <th>Bytes</th>
      <th>UnitPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2820</td>
      <td>Occupation / Precipice</td>
      <td>227</td>
      <td>3</td>
      <td>19</td>
      <td>NaN</td>
      <td>5286953</td>
      <td>1054423946</td>
      <td>1.99</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3224</td>
      <td>Through a Looking Glass</td>
      <td>229</td>
      <td>3</td>
      <td>21</td>
      <td>NaN</td>
      <td>5088838</td>
      <td>1059546140</td>
      <td>1.99</td>
    </tr>
  </tbody>
</table>
</div>



- 查询 `Invoice` 表中 `BillingCountry` 列的值等于 `Brazil` 或者 `Austria` 的行：


```sql
%%sql
SELECT *
FROM Invoice
WHERE BillingCountry = 'Brazil'
OR BillingCountry = 'Austria'
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
      <th>InvoiceId</th>
      <th>CustomerId</th>
      <th>InvoiceDate</th>
      <th>BillingAddress</th>
      <th>BillingCity</th>
      <th>BillingState</th>
      <th>BillingCountry</th>
      <th>BillingPostalCode</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>25</td>
      <td>10</td>
      <td>2021-04-09 00:00:00.000</td>
      <td>Rua Dr. Falcão Filho, 155</td>
      <td>São Paulo</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>01007-010</td>
      <td>8.91</td>
    </tr>
    <tr>
      <th>1</th>
      <td>34</td>
      <td>12</td>
      <td>2021-05-23 00:00:00.000</td>
      <td>Praça Pio X, 119</td>
      <td>Rio de Janeiro</td>
      <td>RJ</td>
      <td>Brazil</td>
      <td>20040-020</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>2</th>
      <td>35</td>
      <td>13</td>
      <td>2021-06-05 00:00:00.000</td>
      <td>Qe 7 Bloco G</td>
      <td>Brasília</td>
      <td>DF</td>
      <td>Brazil</td>
      <td>71020-677</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>3</th>
      <td>57</td>
      <td>11</td>
      <td>2021-09-06 00:00:00.000</td>
      <td>Av. Paulista, 2022</td>
      <td>São Paulo</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>01310-200</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>4</th>
      <td>58</td>
      <td>13</td>
      <td>2021-09-07 00:00:00.000</td>
      <td>Qe 7 Bloco G</td>
      <td>Brasília</td>
      <td>DF</td>
      <td>Brazil</td>
      <td>71020-677</td>
      <td>3.96</td>
    </tr>
    <tr>
      <th>5</th>
      <td>68</td>
      <td>11</td>
      <td>2021-10-17 00:00:00.000</td>
      <td>Av. Paulista, 2022</td>
      <td>São Paulo</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>01310-200</td>
      <td>13.86</td>
    </tr>
    <tr>
      <th>6</th>
      <td>78</td>
      <td>7</td>
      <td>2021-12-08 00:00:00.000</td>
      <td>Rotenturmstraße 4, 1010 Innere Stadt</td>
      <td>Vienne</td>
      <td>NaN</td>
      <td>Austria</td>
      <td>1010</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>7</th>
      <td>80</td>
      <td>13</td>
      <td>2021-12-10 00:00:00.000</td>
      <td>Qe 7 Bloco G</td>
      <td>Brasília</td>
      <td>DF</td>
      <td>Brazil</td>
      <td>71020-677</td>
      <td>5.94</td>
    </tr>
    <tr>
      <th>8</th>
      <td>89</td>
      <td>7</td>
      <td>2022-01-18 00:00:00.000</td>
      <td>Rotenturmstraße 4, 1010 Innere Stadt</td>
      <td>Vienne</td>
      <td>NaN</td>
      <td>Austria</td>
      <td>1010</td>
      <td>18.86</td>
    </tr>
    <tr>
      <th>9</th>
      <td>98</td>
      <td>1</td>
      <td>2022-03-11 00:00:00.000</td>
      <td>Av. Brigadeiro Faria Lima, 2170</td>
      <td>São José dos Campos</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>12227-000</td>
      <td>3.98</td>
    </tr>
    <tr>
      <th>10</th>
      <td>121</td>
      <td>1</td>
      <td>2022-06-13 00:00:00.000</td>
      <td>Av. Brigadeiro Faria Lima, 2170</td>
      <td>São José dos Campos</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>12227-000</td>
      <td>3.96</td>
    </tr>
    <tr>
      <th>11</th>
      <td>123</td>
      <td>11</td>
      <td>2022-06-17 00:00:00.000</td>
      <td>Av. Paulista, 2022</td>
      <td>São Paulo</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>01310-200</td>
      <td>8.91</td>
    </tr>
    <tr>
      <th>12</th>
      <td>132</td>
      <td>13</td>
      <td>2022-07-31 00:00:00.000</td>
      <td>Qe 7 Bloco G</td>
      <td>Brasília</td>
      <td>DF</td>
      <td>Brazil</td>
      <td>71020-677</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>13</th>
      <td>143</td>
      <td>1</td>
      <td>2022-09-15 00:00:00.000</td>
      <td>Av. Brigadeiro Faria Lima, 2170</td>
      <td>São José dos Campos</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>12227-000</td>
      <td>5.94</td>
    </tr>
    <tr>
      <th>14</th>
      <td>144</td>
      <td>7</td>
      <td>2022-09-18 00:00:00.000</td>
      <td>Rotenturmstraße 4, 1010 Innere Stadt</td>
      <td>Vienne</td>
      <td>NaN</td>
      <td>Austria</td>
      <td>1010</td>
      <td>8.91</td>
    </tr>
    <tr>
      <th>15</th>
      <td>154</td>
      <td>10</td>
      <td>2022-11-14 00:00:00.000</td>
      <td>Rua Dr. Falcão Filho, 155</td>
      <td>São Paulo</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>01007-010</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>16</th>
      <td>155</td>
      <td>12</td>
      <td>2022-11-14 00:00:00.000</td>
      <td>Praça Pio X, 119</td>
      <td>Rio de Janeiro</td>
      <td>RJ</td>
      <td>Brazil</td>
      <td>20040-020</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>17</th>
      <td>166</td>
      <td>12</td>
      <td>2022-12-25 00:00:00.000</td>
      <td>Praça Pio X, 119</td>
      <td>Rio de Janeiro</td>
      <td>RJ</td>
      <td>Brazil</td>
      <td>20040-020</td>
      <td>13.86</td>
    </tr>
    <tr>
      <th>18</th>
      <td>177</td>
      <td>10</td>
      <td>2023-02-16 00:00:00.000</td>
      <td>Rua Dr. Falcão Filho, 155</td>
      <td>São Paulo</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>01007-010</td>
      <td>3.96</td>
    </tr>
    <tr>
      <th>19</th>
      <td>195</td>
      <td>1</td>
      <td>2023-05-06 00:00:00.000</td>
      <td>Av. Brigadeiro Faria Lima, 2170</td>
      <td>São José dos Campos</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>12227-000</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>20</th>
      <td>199</td>
      <td>10</td>
      <td>2023-05-21 00:00:00.000</td>
      <td>Rua Dr. Falcão Filho, 155</td>
      <td>São Paulo</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>01007-010</td>
      <td>5.94</td>
    </tr>
    <tr>
      <th>21</th>
      <td>221</td>
      <td>12</td>
      <td>2023-08-25 00:00:00.000</td>
      <td>Praça Pio X, 119</td>
      <td>Rio de Janeiro</td>
      <td>RJ</td>
      <td>Brazil</td>
      <td>20040-020</td>
      <td>8.91</td>
    </tr>
    <tr>
      <th>22</th>
      <td>251</td>
      <td>10</td>
      <td>2024-01-09 00:00:00.000</td>
      <td>Rua Dr. Falcão Filho, 155</td>
      <td>São Paulo</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>01007-010</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>23</th>
      <td>252</td>
      <td>11</td>
      <td>2024-01-22 00:00:00.000</td>
      <td>Av. Paulista, 2022</td>
      <td>São Paulo</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>01310-200</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>24</th>
      <td>253</td>
      <td>13</td>
      <td>2024-01-22 00:00:00.000</td>
      <td>Qe 7 Bloco G</td>
      <td>Brasília</td>
      <td>DF</td>
      <td>Brazil</td>
      <td>71020-677</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>25</th>
      <td>264</td>
      <td>13</td>
      <td>2024-03-03 00:00:00.000</td>
      <td>Qe 7 Bloco G</td>
      <td>Brasília</td>
      <td>DF</td>
      <td>Brazil</td>
      <td>71020-677</td>
      <td>13.86</td>
    </tr>
    <tr>
      <th>26</th>
      <td>273</td>
      <td>7</td>
      <td>2024-04-24 00:00:00.000</td>
      <td>Rotenturmstraße 4, 1010 Innere Stadt</td>
      <td>Vienne</td>
      <td>NaN</td>
      <td>Austria</td>
      <td>1010</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>27</th>
      <td>275</td>
      <td>11</td>
      <td>2024-04-25 00:00:00.000</td>
      <td>Av. Paulista, 2022</td>
      <td>São Paulo</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>01310-200</td>
      <td>3.96</td>
    </tr>
    <tr>
      <th>28</th>
      <td>296</td>
      <td>7</td>
      <td>2024-07-27 00:00:00.000</td>
      <td>Rotenturmstraße 4, 1010 Innere Stadt</td>
      <td>Vienne</td>
      <td>NaN</td>
      <td>Austria</td>
      <td>1010</td>
      <td>3.96</td>
    </tr>
    <tr>
      <th>29</th>
      <td>297</td>
      <td>11</td>
      <td>2024-07-28 00:00:00.000</td>
      <td>Av. Paulista, 2022</td>
      <td>São Paulo</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>01310-200</td>
      <td>5.94</td>
    </tr>
    <tr>
      <th>30</th>
      <td>316</td>
      <td>1</td>
      <td>2024-10-27 00:00:00.000</td>
      <td>Av. Brigadeiro Faria Lima, 2170</td>
      <td>São José dos Campos</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>12227-000</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>31</th>
      <td>318</td>
      <td>7</td>
      <td>2024-10-29 00:00:00.000</td>
      <td>Rotenturmstraße 4, 1010 Innere Stadt</td>
      <td>Vienne</td>
      <td>NaN</td>
      <td>Austria</td>
      <td>1010</td>
      <td>5.94</td>
    </tr>
    <tr>
      <th>32</th>
      <td>319</td>
      <td>13</td>
      <td>2024-11-01 00:00:00.000</td>
      <td>Qe 7 Bloco G</td>
      <td>Brasília</td>
      <td>DF</td>
      <td>Brazil</td>
      <td>71020-677</td>
      <td>8.91</td>
    </tr>
    <tr>
      <th>33</th>
      <td>327</td>
      <td>1</td>
      <td>2024-12-07 00:00:00.000</td>
      <td>Av. Brigadeiro Faria Lima, 2170</td>
      <td>São José dos Campos</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>12227-000</td>
      <td>13.86</td>
    </tr>
    <tr>
      <th>34</th>
      <td>349</td>
      <td>11</td>
      <td>2025-03-18 00:00:00.000</td>
      <td>Av. Paulista, 2022</td>
      <td>São Paulo</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>01310-200</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>35</th>
      <td>350</td>
      <td>12</td>
      <td>2025-03-31 00:00:00.000</td>
      <td>Praça Pio X, 119</td>
      <td>Rio de Janeiro</td>
      <td>RJ</td>
      <td>Brazil</td>
      <td>20040-020</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>36</th>
      <td>370</td>
      <td>7</td>
      <td>2025-06-19 00:00:00.000</td>
      <td>Rotenturmstraße 4, 1010 Innere Stadt</td>
      <td>Vienne</td>
      <td>NaN</td>
      <td>Austria</td>
      <td>1010</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>37</th>
      <td>372</td>
      <td>10</td>
      <td>2025-07-02 00:00:00.000</td>
      <td>Rua Dr. Falcão Filho, 155</td>
      <td>São Paulo</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>01007-010</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>38</th>
      <td>373</td>
      <td>12</td>
      <td>2025-07-03 00:00:00.000</td>
      <td>Praça Pio X, 119</td>
      <td>Rio de Janeiro</td>
      <td>RJ</td>
      <td>Brazil</td>
      <td>20040-020</td>
      <td>3.96</td>
    </tr>
    <tr>
      <th>39</th>
      <td>382</td>
      <td>1</td>
      <td>2025-08-07 00:00:00.000</td>
      <td>Av. Brigadeiro Faria Lima, 2170</td>
      <td>São José dos Campos</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>12227-000</td>
      <td>8.91</td>
    </tr>
    <tr>
      <th>40</th>
      <td>383</td>
      <td>10</td>
      <td>2025-08-12 00:00:00.000</td>
      <td>Rua Dr. Falcão Filho, 155</td>
      <td>São Paulo</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>01007-010</td>
      <td>13.86</td>
    </tr>
    <tr>
      <th>41</th>
      <td>395</td>
      <td>12</td>
      <td>2025-10-05 00:00:00.000</td>
      <td>Praça Pio X, 119</td>
      <td>Rio de Janeiro</td>
      <td>RJ</td>
      <td>Brazil</td>
      <td>20040-020</td>
      <td>5.94</td>
    </tr>
  </tbody>
</table>
</div>



- 查询 `Track` 表中 `UnitPrice` 列的值大于 0.99 且 `Milliseconds` 列的值大于 50000000 的行，或者 `UnitPrice` 列的值小于等于 0.99 且 `Milliseconds` 列的值小于等于 50000000 的行：


```sql
%%sql
SELECT *
FROM Track
WHERE (UnitPrice > 0.99 AND Milliseconds > 5000000)
OR (UnitPrice <= 0.99 AND Milliseconds <= 5000000)
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
      <th>TrackId</th>
      <th>Name</th>
      <th>AlbumId</th>
      <th>MediaTypeId</th>
      <th>GenreId</th>
      <th>Composer</th>
      <th>Milliseconds</th>
      <th>Bytes</th>
      <th>UnitPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>For Those About To Rock (We Salute You)</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Angus Young, Malcolm Young, Brian Johnson</td>
      <td>343719</td>
      <td>11170334</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Balls to the Wall</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>U. Dirkschneider, W. Hoffmann, H. Frank, P. Ba...</td>
      <td>342562</td>
      <td>5510424</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Fast As a Shark</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>F. Baltes, S. Kaufman, U. Dirkscneider &amp; W. Ho...</td>
      <td>230619</td>
      <td>3990994</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Restless and Wild</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>F. Baltes, R.A. Smith-Diesel, S. Kaufman, U. D...</td>
      <td>252051</td>
      <td>4331779</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Princess of the Dawn</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>Deaffy &amp; R.A. Smith-Diesel</td>
      <td>375418</td>
      <td>6290521</td>
      <td>0.99</td>
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
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3287</th>
      <td>3499</td>
      <td>Pini Di Roma (Pinien Von Rom) \ I Pini Della V...</td>
      <td>343</td>
      <td>2</td>
      <td>24</td>
      <td>NaN</td>
      <td>286741</td>
      <td>4718950</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>3288</th>
      <td>3500</td>
      <td>String Quartet No. 12 in C Minor, D. 703 "Quar...</td>
      <td>344</td>
      <td>2</td>
      <td>24</td>
      <td>Franz Schubert</td>
      <td>139200</td>
      <td>2283131</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>3289</th>
      <td>3501</td>
      <td>L'orfeo, Act 3, Sinfonia (Orchestra)</td>
      <td>345</td>
      <td>2</td>
      <td>24</td>
      <td>Claudio Monteverdi</td>
      <td>66639</td>
      <td>1189062</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>3290</th>
      <td>3502</td>
      <td>Quintet for Horn, Violin, 2 Violas, and Cello ...</td>
      <td>346</td>
      <td>2</td>
      <td>24</td>
      <td>Wolfgang Amadeus Mozart</td>
      <td>221331</td>
      <td>3665114</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>3291</th>
      <td>3503</td>
      <td>Koyaanisqatsi</td>
      <td>347</td>
      <td>2</td>
      <td>10</td>
      <td>Philip Glass</td>
      <td>206005</td>
      <td>3305164</td>
      <td>0.99</td>
    </tr>
  </tbody>
</table>
<p>3292 rows × 9 columns</p>
</div>



- 查询 `Invoice` 表中 `BillingCountry` 列的值不等于 `Brazil` 的行：


```sql
%%sql
SELECT *
FROM Invoice
WHERE NOT (BillingCountry = 'Brazil')
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
      <th>InvoiceId</th>
      <th>CustomerId</th>
      <th>InvoiceDate</th>
      <th>BillingAddress</th>
      <th>BillingCity</th>
      <th>BillingState</th>
      <th>BillingCountry</th>
      <th>BillingPostalCode</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>Theodor-Heuss-Straße 34</td>
      <td>Stuttgart</td>
      <td>NaN</td>
      <td>Germany</td>
      <td>70174</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>4</td>
      <td>2021-01-02 00:00:00.000</td>
      <td>Ullevålsveien 14</td>
      <td>Oslo</td>
      <td>NaN</td>
      <td>Norway</td>
      <td>0171</td>
      <td>3.96</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>8</td>
      <td>2021-01-03 00:00:00.000</td>
      <td>Grétrystraat 63</td>
      <td>Brussels</td>
      <td>NaN</td>
      <td>Belgium</td>
      <td>1000</td>
      <td>5.94</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>14</td>
      <td>2021-01-06 00:00:00.000</td>
      <td>8210 111 ST NW</td>
      <td>Edmonton</td>
      <td>AB</td>
      <td>Canada</td>
      <td>T6G 2C7</td>
      <td>8.91</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>23</td>
      <td>2021-01-11 00:00:00.000</td>
      <td>69 Salem Street</td>
      <td>Boston</td>
      <td>MA</td>
      <td>USA</td>
      <td>2113</td>
      <td>13.86</td>
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
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>372</th>
      <td>408</td>
      <td>25</td>
      <td>2025-12-05 00:00:00.000</td>
      <td>319 N. Frances Street</td>
      <td>Madison</td>
      <td>WI</td>
      <td>USA</td>
      <td>53703</td>
      <td>3.96</td>
    </tr>
    <tr>
      <th>373</th>
      <td>409</td>
      <td>29</td>
      <td>2025-12-06 00:00:00.000</td>
      <td>796 Dundas Street West</td>
      <td>Toronto</td>
      <td>ON</td>
      <td>Canada</td>
      <td>M6J 1V1</td>
      <td>5.94</td>
    </tr>
    <tr>
      <th>374</th>
      <td>410</td>
      <td>35</td>
      <td>2025-12-09 00:00:00.000</td>
      <td>Rua dos Campeões Europeus de Viena, 4350</td>
      <td>Porto</td>
      <td>NaN</td>
      <td>Portugal</td>
      <td>NaN</td>
      <td>8.91</td>
    </tr>
    <tr>
      <th>375</th>
      <td>411</td>
      <td>44</td>
      <td>2025-12-14 00:00:00.000</td>
      <td>Porthaninkatu 9</td>
      <td>Helsinki</td>
      <td>NaN</td>
      <td>Finland</td>
      <td>00530</td>
      <td>13.86</td>
    </tr>
    <tr>
      <th>376</th>
      <td>412</td>
      <td>58</td>
      <td>2025-12-22 00:00:00.000</td>
      <td>12,Community Centre</td>
      <td>Delhi</td>
      <td>NaN</td>
      <td>India</td>
      <td>110017</td>
      <td>1.99</td>
    </tr>
  </tbody>
</table>
<p>377 rows × 9 columns</p>
</div>



### (3) 条件查询注意事项

这里我们强调关于 `WHERE` 语句的几个注意事项

- `WHERE` 语句中用来筛选的字段，可以不出现在 `SELECT` 语句中
- 在 SQL 中，字符串类型的值需要使用单引号 `'` 包裹起来，而不是双引号 `"`，这是 SQL 语言的语法规定

还有一个比较重要的注意事项就是：

- `WHERE` 语句中出现的字段，必须是查询的表中存在的字段，否则会报错
- 不可以使用计算出来的字段来进行条件查询
- 要想使用计算出来的字段来进行条件查询，我们需要使用子查询或者 CTE 来实现，后续我们会在课程中介绍这两种方法
- 我们先来看个反面例子，使用计算字段查询报错的例子：


```sql
%%sql
SELECT
    InvoiceId,
    UnitPrice * Quantity AS TotalPrice
FROM InvoiceLine
WHERE TotalPrice > 1.00
```


    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    Cell In[26], line 1
    ----> 1 raise Exception(__import__('base64').b64decode('W1MwMDAxXVsyMDddIOihjCAxOiBJbnZhbGlkIGNvbHVtbiBuYW1lICdUb3RhbFByaWNlJy4=').decode('utf-8'))


    Exception: [S0001][207] 行 1: Invalid column name 'TotalPrice'.


## 2. 条件查询的进阶技巧

### (1) 字符串匹配

在 SQL 的 `WHERE` 语句中，如果一列是**字符串类型**，那么我们可以使用 `LIKE` 关键字来进行字符串匹配查询：

- `LIKE` 关键字的基本语法如下：

```sql
SELECT 列名1, 列名2, ...
FROM 表名
WHERE 列名 LIKE 模式;
```

- 具体来说，`LIKE` 关键字中可以使用以下通配符：

    - `%`：表示任意数量的字符，包括零个字符，也就是空字符
    - `_`：表示任意的单个字符

- 使用这两个通配符，我们可以实现比较灵活的字符串匹配查询，例如：

    - `LIKE 'a%'`：匹配以字母 a 开头的字符串，注意 SQL 中的字符串匹配是区分大小写的
    - `LIKE '%a'`：匹配以字母 a 结尾的字符串
    - `LIKE '%a%'`：匹配包含字母 a 的字符串
    - `LIKE 'a%b'`：匹配以字母 a 开头，以字母 b 结尾的字符串
    - `LIKE 'a_c'`：匹配以字母 a 开头，以字母 c 结尾，并且中间有一个任意字符的字符串
    - `LIKE '_a%'`：匹配第二个字符是 a 的字符串
    - `LIKE 'a_%_%'`：匹配以字母 a 开头，并且至少三个字符长度的字符串

我们来看以下几个例子：

- 查询 `Artist` 表中 `Name` 中带有 `John` 的行：


```sql
%%sql
SELECT *
FROM Artist
WHERE Name LIKE '%John%'
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
      <th>ArtistId</th>
      <th>Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>170</td>
      <td>Jack Johnson</td>
    </tr>
    <tr>
      <th>1</th>
      <td>218</td>
      <td>Orchestre Révolutionnaire et Romantique &amp; John...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>222</td>
      <td>Academy of St. Martin in the Fields, John Birc...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>263</td>
      <td>Equale Brass Ensemble, John Eliot Gardiner &amp; M...</td>
    </tr>
  </tbody>
</table>
</div>



- 查询 `Artist` 表中 `Name` 是 4 个字符长度的行：


```sql
%%sql
SELECT *
FROM Artist
WHERE Name LIKE '____'
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
      <th>ArtistId</th>
      <th>Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>52</td>
      <td>Kiss</td>
    </tr>
    <tr>
      <th>1</th>
      <td>128</td>
      <td>Rush</td>
    </tr>
    <tr>
      <th>2</th>
      <td>149</td>
      <td>Lost</td>
    </tr>
    <tr>
      <th>3</th>
      <td>151</td>
      <td>UB40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>189</td>
      <td>Otto</td>
    </tr>
    <tr>
      <th>5</th>
      <td>196</td>
      <td>Cake</td>
    </tr>
  </tbody>
</table>
</div>



- 查询 `Track` 表中 `Name` 中带有 `Love` 或 `love` 的行（大小写都可以）：


```sql
%%sql
SELECT *
FROM Track
WHERE Name LIKE '%Love%'
OR Name LIKE '%love%'
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
      <th>TrackId</th>
      <th>Name</th>
      <th>AlbumId</th>
      <th>MediaTypeId</th>
      <th>GenreId</th>
      <th>Composer</th>
      <th>Milliseconds</th>
      <th>Bytes</th>
      <th>UnitPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>24</td>
      <td>Love In An Elevator</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>Steven Tyler, Joe Perry</td>
      <td>321828</td>
      <td>10552051</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>1</th>
      <td>56</td>
      <td>Love, Hate, Love</td>
      <td>7</td>
      <td>1</td>
      <td>1</td>
      <td>Jerry Cantrell, Layne Staley</td>
      <td>387134</td>
      <td>12575396</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>2</th>
      <td>195</td>
      <td>Let Me Love You Baby</td>
      <td>20</td>
      <td>1</td>
      <td>6</td>
      <td>Willie Dixon</td>
      <td>175386</td>
      <td>5716994</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>335</td>
      <td>My Love</td>
      <td>29</td>
      <td>1</td>
      <td>9</td>
      <td>Jauperi/Zeu Góes</td>
      <td>203493</td>
      <td>6772813</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>4</th>
      <td>341</td>
      <td>The Girl I Love She Got Long Black Wavy Hair</td>
      <td>30</td>
      <td>1</td>
      <td>1</td>
      <td>Jimmy Page/John Bonham/John Estes/John Paul Jo...</td>
      <td>183327</td>
      <td>5995686</td>
      <td>0.99</td>
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
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>109</th>
      <td>3355</td>
      <td>Love Comes</td>
      <td>265</td>
      <td>5</td>
      <td>1</td>
      <td>Darius "Take One" Minwalla/Jon Auer/Ken String...</td>
      <td>199923</td>
      <td>3240609</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>110</th>
      <td>3377</td>
      <td>Arms Around Your Love</td>
      <td>270</td>
      <td>2</td>
      <td>23</td>
      <td>Chris Cornell</td>
      <td>214016</td>
      <td>3516224</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>111</th>
      <td>3460</td>
      <td>Love Is a Losing Game</td>
      <td>321</td>
      <td>2</td>
      <td>14</td>
      <td>NaN</td>
      <td>154386</td>
      <td>2509409</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>112</th>
      <td>3470</td>
      <td>I Heard Love Is Blind</td>
      <td>322</td>
      <td>2</td>
      <td>9</td>
      <td>NaN</td>
      <td>129666</td>
      <td>2190831</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>113</th>
      <td>3471</td>
      <td>(There Is) No Greater Love (Teo Licks)</td>
      <td>322</td>
      <td>2</td>
      <td>9</td>
      <td>Isham Jones &amp; Marty Symes</td>
      <td>167933</td>
      <td>2773507</td>
      <td>0.99</td>
    </tr>
  </tbody>
</table>
<p>114 rows × 9 columns</p>
</div>



### (2) 数值范围查询

在 SQL 的 `WHERE` 语句中，如果一列是**数值类型**，我们可以使用 `BETWEEN` 关键字来进行数值范围查询：

- `BETWEEN` 关键字的基本语法是 `数值字段 BETWEEN a AND b` ，表示查询数值字段的值在 a 和 b 之间的行，**包含 a 和 b 两个端点值**
- 这个语法相当于 `数值字段 >= a AND 数值字段 <= b` 的简写形式

我们来看一个简单例子，查询 `Track` 表中 `Milliseconds` 列的值在 200000 到 300000 之间的行：


```sql
%%sql
SELECT *
FROM Track
WHERE Milliseconds BETWEEN 200000 AND 300000
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
      <th>TrackId</th>
      <th>Name</th>
      <th>AlbumId</th>
      <th>MediaTypeId</th>
      <th>GenreId</th>
      <th>Composer</th>
      <th>Milliseconds</th>
      <th>Bytes</th>
      <th>UnitPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>Fast As a Shark</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>F. Baltes, S. Kaufman, U. Dirkscneider &amp; W. Ho...</td>
      <td>230619</td>
      <td>3990994</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>Restless and Wild</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>F. Baltes, R.A. Smith-Diesel, S. Kaufman, U. D...</td>
      <td>252051</td>
      <td>4331779</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>Put The Finger On You</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Angus Young, Malcolm Young, Brian Johnson</td>
      <td>205662</td>
      <td>6713451</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>Let's Get It Up</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Angus Young, Malcolm Young, Brian Johnson</td>
      <td>233926</td>
      <td>7636561</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8</td>
      <td>Inject The Venom</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Angus Young, Malcolm Young, Brian Johnson</td>
      <td>210834</td>
      <td>6852860</td>
      <td>0.99</td>
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
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1675</th>
      <td>3495</td>
      <td>24 Caprices, Op. 1, No. 24, for Solo Violin, i...</td>
      <td>339</td>
      <td>2</td>
      <td>24</td>
      <td>Niccolò Paganini</td>
      <td>265541</td>
      <td>4371533</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>1676</th>
      <td>3497</td>
      <td>Erlkonig, D.328</td>
      <td>341</td>
      <td>2</td>
      <td>24</td>
      <td>NaN</td>
      <td>261849</td>
      <td>4307907</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>1677</th>
      <td>3499</td>
      <td>Pini Di Roma (Pinien Von Rom) \ I Pini Della V...</td>
      <td>343</td>
      <td>2</td>
      <td>24</td>
      <td>NaN</td>
      <td>286741</td>
      <td>4718950</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>1678</th>
      <td>3502</td>
      <td>Quintet for Horn, Violin, 2 Violas, and Cello ...</td>
      <td>346</td>
      <td>2</td>
      <td>24</td>
      <td>Wolfgang Amadeus Mozart</td>
      <td>221331</td>
      <td>3665114</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>1679</th>
      <td>3503</td>
      <td>Koyaanisqatsi</td>
      <td>347</td>
      <td>2</td>
      <td>10</td>
      <td>Philip Glass</td>
      <td>206005</td>
      <td>3305164</td>
      <td>0.99</td>
    </tr>
  </tbody>
</table>
<p>1680 rows × 9 columns</p>
</div>



### (3) 多值匹配查询

在 SQL 的 `WHERE` 语句中，如果我们想要查询某一列的值在多个指定值中的行，我们可以使用 `IN` 关键字来进行多值匹配查询：

- `IN` 关键字的基本语法是 `列名 IN (a, b, c, ...)`，表示查询列名的值在括号中的多个值之一的行
- 这个语法相当于 `列名 = a OR 列名 = a OR 列名 = c ...` 的简写形式

我们来看一个简单例子，查询 `Invoice` 表中 `BillingCountry` 列的值在 `Brazil`、`Austria` 和 `France` 这三个国家中的行：


```sql
%%sql
SELECT *
FROM Invoice
WHERE BillingCountry IN ('Brazil', 'Austria', 'France')
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
      <th>InvoiceId</th>
      <th>CustomerId</th>
      <th>InvoiceDate</th>
      <th>BillingAddress</th>
      <th>BillingCity</th>
      <th>BillingState</th>
      <th>BillingCountry</th>
      <th>BillingPostalCode</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8</td>
      <td>40</td>
      <td>2021-02-01 00:00:00.000</td>
      <td>8, Rue Hanovre</td>
      <td>Paris</td>
      <td>NaN</td>
      <td>France</td>
      <td>75002</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9</td>
      <td>42</td>
      <td>2021-02-02 00:00:00.000</td>
      <td>9, Place Louis Barthou</td>
      <td>Bordeaux</td>
      <td>NaN</td>
      <td>France</td>
      <td>33000</td>
      <td>3.96</td>
    </tr>
    <tr>
      <th>2</th>
      <td>19</td>
      <td>40</td>
      <td>2021-03-14 00:00:00.000</td>
      <td>8, Rue Hanovre</td>
      <td>Paris</td>
      <td>NaN</td>
      <td>France</td>
      <td>75002</td>
      <td>13.86</td>
    </tr>
    <tr>
      <th>3</th>
      <td>25</td>
      <td>10</td>
      <td>2021-04-09 00:00:00.000</td>
      <td>Rua Dr. Falcão Filho, 155</td>
      <td>São Paulo</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>01007-010</td>
      <td>8.91</td>
    </tr>
    <tr>
      <th>4</th>
      <td>31</td>
      <td>42</td>
      <td>2021-05-07 00:00:00.000</td>
      <td>9, Place Louis Barthou</td>
      <td>Bordeaux</td>
      <td>NaN</td>
      <td>France</td>
      <td>33000</td>
      <td>5.94</td>
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
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>72</th>
      <td>383</td>
      <td>10</td>
      <td>2025-08-12 00:00:00.000</td>
      <td>Rua Dr. Falcão Filho, 155</td>
      <td>São Paulo</td>
      <td>SP</td>
      <td>Brazil</td>
      <td>01007-010</td>
      <td>13.86</td>
    </tr>
    <tr>
      <th>73</th>
      <td>389</td>
      <td>39</td>
      <td>2025-09-07 00:00:00.000</td>
      <td>4, Rue Milton</td>
      <td>Paris</td>
      <td>NaN</td>
      <td>France</td>
      <td>75009</td>
      <td>8.91</td>
    </tr>
    <tr>
      <th>74</th>
      <td>395</td>
      <td>12</td>
      <td>2025-10-05 00:00:00.000</td>
      <td>Praça Pio X, 119</td>
      <td>Rio de Janeiro</td>
      <td>RJ</td>
      <td>Brazil</td>
      <td>20040-020</td>
      <td>5.94</td>
    </tr>
    <tr>
      <th>75</th>
      <td>398</td>
      <td>41</td>
      <td>2025-10-21 00:00:00.000</td>
      <td>11, Place Bellecour</td>
      <td>Lyon</td>
      <td>NaN</td>
      <td>France</td>
      <td>69002</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>76</th>
      <td>399</td>
      <td>42</td>
      <td>2025-11-03 00:00:00.000</td>
      <td>9, Place Louis Barthou</td>
      <td>Bordeaux</td>
      <td>NaN</td>
      <td>France</td>
      <td>33000</td>
      <td>1.98</td>
    </tr>
  </tbody>
</table>
<p>77 rows × 9 columns</p>
</div>



### (4) NULL 值查询

在 SQL 数据库中，NULL 表示缺失值或者未知值，NULL 值在 SQL 中有一些特殊的处理方式：

- 在 SQL 中，任何与 NULL 进行的比较操作都会返回 NULL，而不是 TRUE 或 FALSE
- 因此，我们不能使用 `=` 或 `<>` 来判断一个值是否为
- 在 SQL 中，判断一个值是否为 NULL，我们需要使用 `IS NULL` 来判断是否为 NULL，使用 `IS NOT NULL` 来判断是否不为 NULL

我们来看以下这个例子，在 `Track` 表中查询 `Composer` 列的值为 NULL 的行：


```sql
%%sql
SELECT *
FROM Track
WHERE Composer IS NULL
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
      <th>TrackId</th>
      <th>Name</th>
      <th>AlbumId</th>
      <th>MediaTypeId</th>
      <th>GenreId</th>
      <th>Composer</th>
      <th>Milliseconds</th>
      <th>Bytes</th>
      <th>UnitPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>63</td>
      <td>Desafinado</td>
      <td>8</td>
      <td>1</td>
      <td>2</td>
      <td>NaN</td>
      <td>185338</td>
      <td>5990473</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>1</th>
      <td>64</td>
      <td>Garota De Ipanema</td>
      <td>8</td>
      <td>1</td>
      <td>2</td>
      <td>NaN</td>
      <td>285048</td>
      <td>9348428</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>2</th>
      <td>65</td>
      <td>Samba De Uma Nota Só (One Note Samba)</td>
      <td>8</td>
      <td>1</td>
      <td>2</td>
      <td>NaN</td>
      <td>137273</td>
      <td>4535401</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>66</td>
      <td>Por Causa De Você</td>
      <td>8</td>
      <td>1</td>
      <td>2</td>
      <td>NaN</td>
      <td>169900</td>
      <td>5536496</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>4</th>
      <td>67</td>
      <td>Ligia</td>
      <td>8</td>
      <td>1</td>
      <td>2</td>
      <td>NaN</td>
      <td>251977</td>
      <td>8226934</td>
      <td>0.99</td>
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
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>972</th>
      <td>3478</td>
      <td>Slowness</td>
      <td>323</td>
      <td>2</td>
      <td>23</td>
      <td>NaN</td>
      <td>215386</td>
      <td>3644793</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>973</th>
      <td>3481</td>
      <td>A Midsummer Night's Dream, Op.61 Incidental Mu...</td>
      <td>326</td>
      <td>2</td>
      <td>24</td>
      <td>NaN</td>
      <td>387826</td>
      <td>6497867</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>974</th>
      <td>3496</td>
      <td>Étude 1, In C Major - Preludio (Presto) - Liszt</td>
      <td>340</td>
      <td>4</td>
      <td>24</td>
      <td>NaN</td>
      <td>51780</td>
      <td>2229617</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>975</th>
      <td>3497</td>
      <td>Erlkonig, D.328</td>
      <td>341</td>
      <td>2</td>
      <td>24</td>
      <td>NaN</td>
      <td>261849</td>
      <td>4307907</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>976</th>
      <td>3499</td>
      <td>Pini Di Roma (Pinien Von Rom) \ I Pini Della V...</td>
      <td>343</td>
      <td>2</td>
      <td>24</td>
      <td>NaN</td>
      <td>286741</td>
      <td>4718950</td>
      <td>0.99</td>
    </tr>
  </tbody>
</table>
<p>977 rows × 9 columns</p>
</div>


