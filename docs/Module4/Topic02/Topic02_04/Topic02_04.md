# Topic 2.4 - SELECT 语句中的进阶数据运算

## 1. SQL 中的数据类型

在我们本门课，大家只需要掌握三种 SQL 中的数据类型即可：

- 数字类型：例如 `INT`、`FLOAT` 等等，这些数据类型的值是数字，可以进行数学运算
- 字符串类型：例如 `VARCHAR`、`TEXT` 等等，这些数据类型的值是字符串，可以进行字符串拼接等运算
- 日期时间类型：例如 `DATE`、`DATETIME` 等等，这些数据类型的值是日期或者日期时间，可以进行日期时间的运算

我们本节将根据这三种数据类型，介绍在 SQL 中如何进行进阶的数据运算。

## 2. SQL 中数字类型的运算

### (1) 数学运算符

数学运算符，我们在之前的课程中已经介绍过了，这里我们再简单回顾一下：

- 加法符号：`+`
- 减法符号：`-`
- 乘法符号：`*`
- 除法符号：`/`
- 乘方符号：`^`
- 括号：`()` 可以改变运算的优先级

我们来看以下当时写的一些例子，就不运行了：

```sql
SELECT
    TrackId,
    UnitPrice,
    UnitPrice * 1.1 AS NewPrice -- 新价格
FROM Track
```

```sql
SELECT
    InvoiceId,
    TrackId,
    UnitPrice * Quantity AS TotalPrice -- 总价
FROM InvoiceLine
```

```sql
SELECT
    TrackId,
    UnitPrice / Milliseconds * 1000 AS PricePerSecond
FROM Track
```

### (2) SQL 中的计算函数

除了运算符号之外，SQL 中还有一些内置的计算函数：

- 注意，计算函数会根据数据库类型的不同而有所不同
- 我们来列举一些 Azure SQL Database 中常用的计算函数：

    - `ABS(x)`：返回 x 的绝对值
    - `ROUND(x, d)`：将 x 四舍五入到 d 位小数
    - `CEILING(x)`：返回大于或等于 x 的最小整数
    - `FLOOR(x)`：返回小于或等于 x 的最大整数
    - `POWER(x, y)`：返回 x 的 y 次幂
    - `SQRT(x)`：返回 x 的平方根
    - `LOG(x)`：返回 x 的自然对数
    - `EXP(x)`：返回 e 的 x 次幂

- 其实还有很多运算函数，比方说三角函数什么的，但是使用的频率实在太少了，这里我们就不列举了，大家可以自己查询一下，但是注意查询的时候一定要查询 Azure SQL Database 中的计算函数，因为不同数据库类型中的计算函数可能会有所不同
- 注意，这里我们推荐大家，运算函数和关键字一样，也使用大写字母来书写，这样可以和列名区分开来，代码也更清晰易读

这里我们来在 `Track` 表中使用一些计算函数（数值可能没什么实际意义，我们只是展示函数功能）：




```sql
%%sql
SELECT
    TrackId,
    UnitPrice,
    SQRT(UnitPrice) AS SqrtUnitPrice, -- 计算 UnitPrice 的平方根
    LOG(UnitPrice) AS LogUnitPrice, -- 计算 UnitPrice 的自然对数
    EXP(UnitPrice) AS ExpUnitPrice, -- 计算 e 的 UnitPrice 次幂
    ROUND(UnitPrice, 1) AS RoundedUnitPrice, -- 将 UnitPrice 四舍五入到 1 位小数
    CEILING(UnitPrice) AS CeilingUnitPrice, -- 将 UnitPrice 向上取整
    FLOOR(UnitPrice) AS FloorUnitPrice -- 将 UnitPrice 向下取整
FROM Track
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
      <th>UnitPrice</th>
      <th>SqrtUnitPrice</th>
      <th>LogUnitPrice</th>
      <th>ExpUnitPrice</th>
      <th>RoundedUnitPrice</th>
      <th>CeilingUnitPrice</th>
      <th>FloorUnitPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0.99</td>
      <td>0.994987</td>
      <td>-0.01005</td>
      <td>2.691234</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>0.99</td>
      <td>0.994987</td>
      <td>-0.01005</td>
      <td>2.691234</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>0.99</td>
      <td>0.994987</td>
      <td>-0.01005</td>
      <td>2.691234</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>0.99</td>
      <td>0.994987</td>
      <td>-0.01005</td>
      <td>2.691234</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0.99</td>
      <td>0.994987</td>
      <td>-0.01005</td>
      <td>2.691234</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
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
    </tr>
    <tr>
      <th>3498</th>
      <td>3499</td>
      <td>0.99</td>
      <td>0.994987</td>
      <td>-0.01005</td>
      <td>2.691234</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3499</th>
      <td>3500</td>
      <td>0.99</td>
      <td>0.994987</td>
      <td>-0.01005</td>
      <td>2.691234</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3500</th>
      <td>3501</td>
      <td>0.99</td>
      <td>0.994987</td>
      <td>-0.01005</td>
      <td>2.691234</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3501</th>
      <td>3502</td>
      <td>0.99</td>
      <td>0.994987</td>
      <td>-0.01005</td>
      <td>2.691234</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3502</th>
      <td>3503</td>
      <td>0.99</td>
      <td>0.994987</td>
      <td>-0.01005</td>
      <td>2.691234</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>3503 rows × 8 columns</p>
</div>



### (3) 条件计算

有时候我们需要根据某些条件来进行计算，这时候我们就可以使用 SQL 中的条件计算函数 `CASE WHEN` 来实现这个功能：

- `CASE WHEN` 的语法如下：

```sql
SELECT
    ...,
    CASE
        WHEN condition1 THEN result1
        WHEN condition2 THEN result2
        ...
        ELSE resultN
    END AS new_column
    ...
FROM table_name
```

- 在这个语法中，整个这个代码块，从 `CASE` 到 `END`，就是一个条件计算的表达式，产生一个计算出来的新列
- 这个列的计算逻辑是：
    - 当满足 `condition1` 条件时，这个新列的值就是 `result1`
    - 当满足 `condition2` 条件时，这个新列的值就是 `result2`
    - ...
    - 如果都不满足，那么这个新列的值就是 `resultN`

这里的条件运算和我们之前在 `WHERE` 语句中使用的条件表达式是一样的：

- 可以使用比较运算符，例如 `=`、`!=`、`>`、`<`、`>=`、`<=` 判断数值
- 可以使用 `AND`、`OR`、`NOT` 与括号 `()` 来组合多个条件
- 可以使用 `IN` 来判断某个值是否在一个列表中
- 可以使用 `LIKE` 来进行字符串模糊匹配
- ...

我们来看以下一些例子：

- 查询 `Track` 表中的每首歌的价格等级，如果价格小于等于 1 就是 "Cheap"，大于 1 就是 "Expensive"：


```sql
%%sql
SELECT
    TrackId,
    UnitPrice,
    CASE
        WHEN UnitPrice <= 1 THEN 'Cheap'
        ELSE                     'Expensive'  -- 这里我们可以多打点空格让值对齐
    END AS PriceLevel
FROM Track
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
      <th>UnitPrice</th>
      <th>PriceLevel</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0.99</td>
      <td>Cheap</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>0.99</td>
      <td>Cheap</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>0.99</td>
      <td>Cheap</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>0.99</td>
      <td>Cheap</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0.99</td>
      <td>Cheap</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3498</th>
      <td>3499</td>
      <td>0.99</td>
      <td>Cheap</td>
    </tr>
    <tr>
      <th>3499</th>
      <td>3500</td>
      <td>0.99</td>
      <td>Cheap</td>
    </tr>
    <tr>
      <th>3500</th>
      <td>3501</td>
      <td>0.99</td>
      <td>Cheap</td>
    </tr>
    <tr>
      <th>3501</th>
      <td>3502</td>
      <td>0.99</td>
      <td>Cheap</td>
    </tr>
    <tr>
      <th>3502</th>
      <td>3503</td>
      <td>0.99</td>
      <td>Cheap</td>
    </tr>
  </tbody>
</table>
<p>3503 rows × 3 columns</p>
</div>



- 查询 `Invoice` 表并创建一个新字段 `IsEnglishSpeakingCountry`，如果 BillingCountry 在 "USA"、"Canada"、"Australia"、"UK"、"New Zealand" 这五个国家中，那么这个新字段的值就是 1，否则就是 0：


```sql
%%sql
SELECT
    InvoiceId,
    BillingCountry,
    CASE
        WHEN BillingCountry IN ('USA', 'Canada', 'Australia', 'UK', 'New Zealand') THEN 1
        ELSE 0
    END AS IsEnglishSpeakingCountry
FROM Invoice
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
      <th>BillingCountry</th>
      <th>IsEnglishSpeakingCountry</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Germany</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Norway</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Belgium</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Canada</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>USA</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>407</th>
      <td>408</td>
      <td>USA</td>
      <td>1</td>
    </tr>
    <tr>
      <th>408</th>
      <td>409</td>
      <td>Canada</td>
      <td>1</td>
    </tr>
    <tr>
      <th>409</th>
      <td>410</td>
      <td>Portugal</td>
      <td>0</td>
    </tr>
    <tr>
      <th>410</th>
      <td>411</td>
      <td>Finland</td>
      <td>0</td>
    </tr>
    <tr>
      <th>411</th>
      <td>412</td>
      <td>India</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>412 rows × 3 columns</p>
</div>



- 查询 `Track` 表并创建一个新字段 `TrackType`，如果 `Milliseconds` 小于 180000 就是 "Short"，如果 `Milliseconds` 大于等于 180000 且小于 300000 就是 "Medium"，否则就是 "Long"：


```sql
%%sql
SELECT
    TrackId,
    Milliseconds,
    CASE
        WHEN Milliseconds < 180000                  THEN 'Short'
        WHEN Milliseconds BETWEEN 180000 AND 300000 THEN 'Medium'
        ELSE                                             'Long'
    END AS TrackType
FROM Track
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
      <th>Milliseconds</th>
      <th>TrackType</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>343719</td>
      <td>Long</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>342562</td>
      <td>Long</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>230619</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>252051</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>375418</td>
      <td>Long</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3498</th>
      <td>3499</td>
      <td>286741</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>3499</th>
      <td>3500</td>
      <td>139200</td>
      <td>Short</td>
    </tr>
    <tr>
      <th>3500</th>
      <td>3501</td>
      <td>66639</td>
      <td>Short</td>
    </tr>
    <tr>
      <th>3501</th>
      <td>3502</td>
      <td>221331</td>
      <td>Medium</td>
    </tr>
    <tr>
      <th>3502</th>
      <td>3503</td>
      <td>206005</td>
      <td>Medium</td>
    </tr>
  </tbody>
</table>
<p>3503 rows × 3 columns</p>
</div>



## 3. SQL 中的字符串类型数据运算

### (1) 字符串长度计算

在 SQL 中，如果想对一个字符串类型的字段进行长度计算，我们可以使用 `LEN(string)` 函数来计算字符串的长度。

例如，我们想计算 `Employee` 表中每个员工的名字长度，我们可以使用以下 SQL 查询语句：


```sql
%%sql
SELECT
    FirstName,
    LastName,
    LEN(FirstName) AS FirstNameLength, -- 计算名字的长度
    LEN(LastName) AS LastNameLength -- 计算姓氏的长度
FROM Employee
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
      <th>FirstName</th>
      <th>LastName</th>
      <th>FirstNameLength</th>
      <th>LastNameLength</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Andrew</td>
      <td>Adams</td>
      <td>6</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nancy</td>
      <td>Edwards</td>
      <td>5</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jane</td>
      <td>Peacock</td>
      <td>4</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Margaret</td>
      <td>Park</td>
      <td>8</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Steve</td>
      <td>Johnson</td>
      <td>5</td>
      <td>7</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Michael</td>
      <td>Mitchell</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Robert</td>
      <td>King</td>
      <td>6</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Laura</td>
      <td>Callahan</td>
      <td>5</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



### (2) 字符串取子串

在 SQL 中，如果一个字段是字符串类型，那么我们可以使用以下提取子串的方式：

- `SUBSTRING(string, start_index, length)`：从字符串 `string` 的第 `start_index` 个字符开始，取出长度为 `length` 的子串

    - 这里我们要注意一点，SQL 中的索引和 Python 中的索引有很大的区别
    - Python 中的索引是从 0 开始的，也就是说字符串中的第一个字符的索引是 0，第二个字符的索引是 1，以此类推
    - 而 SQL 中的索引是从 1 开始的，也就是说字符串中的第一个字符的索引是 1，第二个字符的索引是 2，以此类推
    - 但是有一点是一样的，那就是正数索引是从左往右数的，负数索引是从右往左数的，比方说 `-1` 就是字符串中的最后一个字符

- `LEFT(string, length)`：从字符串 `string` 的左边开始，取出长度为 `length` 的子串

- `RIGHT(string, length)`：从字符串 `string` 的右边开始，取出长度为 `length` 的子串

我们来看以下一些例子：

- 查询 `Invoice` 表中的 `BillingPostalCode` 字段，并提取出邮编的前 3 个字符作为新的字段 `PostalCodePrefix`：


```sql
%%sql
SELECT
    InvoiceId,
    BillingPostalCode,
    LEFT(BillingPostalCode, 3) AS PostalCodePrefix
FROM Invoice
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
      <th>BillingPostalCode</th>
      <th>PostalCodePrefix</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>70174</td>
      <td>701</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>0171</td>
      <td>017</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1000</td>
      <td>100</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>T6G 2C7</td>
      <td>T6G</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>2113</td>
      <td>211</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>407</th>
      <td>408</td>
      <td>53703</td>
      <td>537</td>
    </tr>
    <tr>
      <th>408</th>
      <td>409</td>
      <td>M6J 1V1</td>
      <td>M6J</td>
    </tr>
    <tr>
      <th>409</th>
      <td>410</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>410</th>
      <td>411</td>
      <td>00530</td>
      <td>005</td>
    </tr>
    <tr>
      <th>411</th>
      <td>412</td>
      <td>110017</td>
      <td>110</td>
    </tr>
  </tbody>
</table>
<p>412 rows × 3 columns</p>
</div>



- 查询 `Customer` 表中的 `Company` 字段，并提取出公司名称的后 4 个字符作为新的字段 `CompanySuffix`：


```sql
%%sql
SELECT
    CustomerId,
    Company,
    RIGHT(Company, 4) AS CompanySuffix
FROM Customer
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
      <th>Company</th>
      <th>CompanySuffix</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Embraer - Empresa Brasileira de Aeronáutica S.A.</td>
      <td>S.A.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>JetBrains s.r.o.</td>
      <td>r.o.</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>Woodstock Discos</td>
      <td>scos</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>Banco do Brasil S.A.</td>
      <td>S.A.</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>Riotur</td>
      <td>otur</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>Telus</td>
      <td>elus</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>Rogers Canada</td>
      <td>nada</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>Google Inc.</td>
      <td>Inc.</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>Microsoft Corporation</td>
      <td>tion</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>Apple Inc.</td>
      <td>Inc.</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>28</th>
      <td>29</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>30</th>
      <td>31</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>31</th>
      <td>32</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>32</th>
      <td>33</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33</th>
      <td>34</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>34</th>
      <td>35</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35</th>
      <td>36</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>36</th>
      <td>37</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>37</th>
      <td>38</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>38</th>
      <td>39</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>39</th>
      <td>40</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>40</th>
      <td>41</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>41</th>
      <td>42</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>42</th>
      <td>43</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>43</th>
      <td>44</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>44</th>
      <td>45</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>45</th>
      <td>46</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>46</th>
      <td>47</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>47</th>
      <td>48</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>48</th>
      <td>49</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>49</th>
      <td>50</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50</th>
      <td>51</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>51</th>
      <td>52</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>52</th>
      <td>53</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>53</th>
      <td>54</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>54</th>
      <td>55</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>55</th>
      <td>56</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>56</th>
      <td>57</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>57</th>
      <td>58</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>58</th>
      <td>59</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



- 查询 `Artist` 表中的 `Name` 字段，并提取出名字中的第 2 到第 4 个字符作为新的字段 `NameSubstring`：


```sql
%%sql
SELECT
    ArtistId,
    Name,
    SUBSTRING(Name, 2, 3) AS NameSubstring
FROM Artist
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
      <th>NameSubstring</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>AC/DC</td>
      <td>C/D</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Accept</td>
      <td>cce</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Aerosmith</td>
      <td>ero</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Alanis Morissette</td>
      <td>lan</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Alice In Chains</td>
      <td>lic</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>270</th>
      <td>271</td>
      <td>Mela Tenenbaum, Pro Musica Prague &amp; Richard Kapp</td>
      <td>ela</td>
    </tr>
    <tr>
      <th>271</th>
      <td>272</td>
      <td>Emerson String Quartet</td>
      <td>mer</td>
    </tr>
    <tr>
      <th>272</th>
      <td>273</td>
      <td>C. Monteverdi, Nigel Rogers - Chiaroscuro; Lon...</td>
      <td>. M</td>
    </tr>
    <tr>
      <th>273</th>
      <td>274</td>
      <td>Nash Ensemble</td>
      <td>ash</td>
    </tr>
    <tr>
      <th>274</th>
      <td>275</td>
      <td>Philip Glass Ensemble</td>
      <td>hil</td>
    </tr>
  </tbody>
</table>
<p>275 rows × 3 columns</p>
</div>



### (3) 字符串索引

#### (a) 按照子串查找字符串中的位置

在 SQL 中，我们可以使用 `CHARINDEX(substring, string)` 函数来查找一个子串在一个字符串中的位置：

- 如果子串存在于字符串中，那么 `CHARINDEX` 函数会返回子串在字符串中第一次出现的位置（索引从 1 开始）
- 如果子串不存在于字符串中，那么 `CHARINDEX` 函数会返回 0

我们来看以下一些例子：

- 查询 `Customer` 表中的 `Email` 字段，并查找 "@" 符号在邮箱地址中的位置，作为新的字段 `AtSymbolPosition`：


```sql
%%sql
SELECT
    CustomerId,
    Email,
    CHARINDEX('@', Email) AS AtSymbolPosition
FROM Customer
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
      <th>Email</th>
      <th>AtSymbolPosition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>luisg@embraer.com.br</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>leonekohler@surfeu.de</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>ftremblay@gmail.com</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>bjorn.hansen@yahoo.no</td>
      <td>13</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>frantisekw@jetbrains.com</td>
      <td>11</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>hholy@gmail.com</td>
      <td>6</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>astrid.gruber@apple.at</td>
      <td>14</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>daan_peeters@apple.be</td>
      <td>13</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>kara.nielsen@jubii.dk</td>
      <td>13</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>eduardo@woodstock.com.br</td>
      <td>8</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>alero@uol.com.br</td>
      <td>6</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>roberto.almeida@riotur.gov.br</td>
      <td>16</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>fernadaramos4@uol.com.br</td>
      <td>14</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>mphilips12@shaw.ca</td>
      <td>11</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>jenniferp@rogers.ca</td>
      <td>10</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>fharris@google.com</td>
      <td>8</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>jacksmith@microsoft.com</td>
      <td>10</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>michelleb@aol.com</td>
      <td>10</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>tgoyer@apple.com</td>
      <td>7</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>dmiller@comcast.com</td>
      <td>8</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>kachase@hotmail.com</td>
      <td>8</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>hleacock@gmail.com</td>
      <td>9</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>johngordon22@yahoo.com</td>
      <td>13</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24</td>
      <td>fralston@gmail.com</td>
      <td>9</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>vstevens@yahoo.com</td>
      <td>9</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26</td>
      <td>ricunningham@hotmail.com</td>
      <td>13</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27</td>
      <td>patrick.gray@aol.com</td>
      <td>13</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>jubarnett@gmail.com</td>
      <td>10</td>
    </tr>
    <tr>
      <th>28</th>
      <td>29</td>
      <td>robbrown@shaw.ca</td>
      <td>9</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>edfrancis@yachoo.ca</td>
      <td>10</td>
    </tr>
    <tr>
      <th>30</th>
      <td>31</td>
      <td>marthasilk@gmail.com</td>
      <td>11</td>
    </tr>
    <tr>
      <th>31</th>
      <td>32</td>
      <td>aaronmitchell@yahoo.ca</td>
      <td>14</td>
    </tr>
    <tr>
      <th>32</th>
      <td>33</td>
      <td>ellie.sullivan@shaw.ca</td>
      <td>15</td>
    </tr>
    <tr>
      <th>33</th>
      <td>34</td>
      <td>jfernandes@yahoo.pt</td>
      <td>11</td>
    </tr>
    <tr>
      <th>34</th>
      <td>35</td>
      <td>masampaio@sapo.pt</td>
      <td>10</td>
    </tr>
    <tr>
      <th>35</th>
      <td>36</td>
      <td>hannah.schneider@yahoo.de</td>
      <td>17</td>
    </tr>
    <tr>
      <th>36</th>
      <td>37</td>
      <td>fzimmermann@yahoo.de</td>
      <td>12</td>
    </tr>
    <tr>
      <th>37</th>
      <td>38</td>
      <td>nschroder@surfeu.de</td>
      <td>10</td>
    </tr>
    <tr>
      <th>38</th>
      <td>39</td>
      <td>camille.bernard@yahoo.fr</td>
      <td>16</td>
    </tr>
    <tr>
      <th>39</th>
      <td>40</td>
      <td>dominiquelefebvre@gmail.com</td>
      <td>18</td>
    </tr>
    <tr>
      <th>40</th>
      <td>41</td>
      <td>marc.dubois@hotmail.com</td>
      <td>12</td>
    </tr>
    <tr>
      <th>41</th>
      <td>42</td>
      <td>wyatt.girard@yahoo.fr</td>
      <td>13</td>
    </tr>
    <tr>
      <th>42</th>
      <td>43</td>
      <td>isabelle_mercier@apple.fr</td>
      <td>17</td>
    </tr>
    <tr>
      <th>43</th>
      <td>44</td>
      <td>terhi.hamalainen@apple.fi</td>
      <td>17</td>
    </tr>
    <tr>
      <th>44</th>
      <td>45</td>
      <td>ladislav_kovacs@apple.hu</td>
      <td>16</td>
    </tr>
    <tr>
      <th>45</th>
      <td>46</td>
      <td>hughoreilly@apple.ie</td>
      <td>12</td>
    </tr>
    <tr>
      <th>46</th>
      <td>47</td>
      <td>lucas.mancini@yahoo.it</td>
      <td>14</td>
    </tr>
    <tr>
      <th>47</th>
      <td>48</td>
      <td>johavanderberg@yahoo.nl</td>
      <td>15</td>
    </tr>
    <tr>
      <th>48</th>
      <td>49</td>
      <td>stanisław.wójcik@wp.pl</td>
      <td>17</td>
    </tr>
    <tr>
      <th>49</th>
      <td>50</td>
      <td>enrique_munoz@yahoo.es</td>
      <td>14</td>
    </tr>
    <tr>
      <th>50</th>
      <td>51</td>
      <td>joakim.johansson@yahoo.se</td>
      <td>17</td>
    </tr>
    <tr>
      <th>51</th>
      <td>52</td>
      <td>emma_jones@hotmail.com</td>
      <td>11</td>
    </tr>
    <tr>
      <th>52</th>
      <td>53</td>
      <td>phil.hughes@gmail.com</td>
      <td>12</td>
    </tr>
    <tr>
      <th>53</th>
      <td>54</td>
      <td>steve.murray@yahoo.uk</td>
      <td>13</td>
    </tr>
    <tr>
      <th>54</th>
      <td>55</td>
      <td>mark.taylor@yahoo.au</td>
      <td>12</td>
    </tr>
    <tr>
      <th>55</th>
      <td>56</td>
      <td>diego.gutierrez@yahoo.ar</td>
      <td>16</td>
    </tr>
    <tr>
      <th>56</th>
      <td>57</td>
      <td>luisrojas@yahoo.cl</td>
      <td>10</td>
    </tr>
    <tr>
      <th>57</th>
      <td>58</td>
      <td>manoj.pareek@rediff.com</td>
      <td>13</td>
    </tr>
    <tr>
      <th>58</th>
      <td>59</td>
      <td>puja_srivastava@yahoo.in</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>



- 查询 `Customer` 表中的 `Email` 字段，并查找 "@gmail" 符号在邮箱地址中的位置，作为新的字段 `GmailPosition`：


```sql
%%sql
SELECT
    CustomerId,
    Email,
    CHARINDEX('@gmail', Email) AS GmailPosition
FROM Customer
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
      <th>Email</th>
      <th>GmailPosition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>luisg@embraer.com.br</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>leonekohler@surfeu.de</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>ftremblay@gmail.com</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>bjorn.hansen@yahoo.no</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>frantisekw@jetbrains.com</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>hholy@gmail.com</td>
      <td>6</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>astrid.gruber@apple.at</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>daan_peeters@apple.be</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>kara.nielsen@jubii.dk</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>eduardo@woodstock.com.br</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>alero@uol.com.br</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>roberto.almeida@riotur.gov.br</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>fernadaramos4@uol.com.br</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>mphilips12@shaw.ca</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>jenniferp@rogers.ca</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>fharris@google.com</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>jacksmith@microsoft.com</td>
      <td>0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>michelleb@aol.com</td>
      <td>0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>tgoyer@apple.com</td>
      <td>0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>dmiller@comcast.com</td>
      <td>0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>kachase@hotmail.com</td>
      <td>0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>hleacock@gmail.com</td>
      <td>9</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>johngordon22@yahoo.com</td>
      <td>0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24</td>
      <td>fralston@gmail.com</td>
      <td>9</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>vstevens@yahoo.com</td>
      <td>0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26</td>
      <td>ricunningham@hotmail.com</td>
      <td>0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27</td>
      <td>patrick.gray@aol.com</td>
      <td>0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>jubarnett@gmail.com</td>
      <td>10</td>
    </tr>
    <tr>
      <th>28</th>
      <td>29</td>
      <td>robbrown@shaw.ca</td>
      <td>0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>edfrancis@yachoo.ca</td>
      <td>0</td>
    </tr>
    <tr>
      <th>30</th>
      <td>31</td>
      <td>marthasilk@gmail.com</td>
      <td>11</td>
    </tr>
    <tr>
      <th>31</th>
      <td>32</td>
      <td>aaronmitchell@yahoo.ca</td>
      <td>0</td>
    </tr>
    <tr>
      <th>32</th>
      <td>33</td>
      <td>ellie.sullivan@shaw.ca</td>
      <td>0</td>
    </tr>
    <tr>
      <th>33</th>
      <td>34</td>
      <td>jfernandes@yahoo.pt</td>
      <td>0</td>
    </tr>
    <tr>
      <th>34</th>
      <td>35</td>
      <td>masampaio@sapo.pt</td>
      <td>0</td>
    </tr>
    <tr>
      <th>35</th>
      <td>36</td>
      <td>hannah.schneider@yahoo.de</td>
      <td>0</td>
    </tr>
    <tr>
      <th>36</th>
      <td>37</td>
      <td>fzimmermann@yahoo.de</td>
      <td>0</td>
    </tr>
    <tr>
      <th>37</th>
      <td>38</td>
      <td>nschroder@surfeu.de</td>
      <td>0</td>
    </tr>
    <tr>
      <th>38</th>
      <td>39</td>
      <td>camille.bernard@yahoo.fr</td>
      <td>0</td>
    </tr>
    <tr>
      <th>39</th>
      <td>40</td>
      <td>dominiquelefebvre@gmail.com</td>
      <td>18</td>
    </tr>
    <tr>
      <th>40</th>
      <td>41</td>
      <td>marc.dubois@hotmail.com</td>
      <td>0</td>
    </tr>
    <tr>
      <th>41</th>
      <td>42</td>
      <td>wyatt.girard@yahoo.fr</td>
      <td>0</td>
    </tr>
    <tr>
      <th>42</th>
      <td>43</td>
      <td>isabelle_mercier@apple.fr</td>
      <td>0</td>
    </tr>
    <tr>
      <th>43</th>
      <td>44</td>
      <td>terhi.hamalainen@apple.fi</td>
      <td>0</td>
    </tr>
    <tr>
      <th>44</th>
      <td>45</td>
      <td>ladislav_kovacs@apple.hu</td>
      <td>0</td>
    </tr>
    <tr>
      <th>45</th>
      <td>46</td>
      <td>hughoreilly@apple.ie</td>
      <td>0</td>
    </tr>
    <tr>
      <th>46</th>
      <td>47</td>
      <td>lucas.mancini@yahoo.it</td>
      <td>0</td>
    </tr>
    <tr>
      <th>47</th>
      <td>48</td>
      <td>johavanderberg@yahoo.nl</td>
      <td>0</td>
    </tr>
    <tr>
      <th>48</th>
      <td>49</td>
      <td>stanisław.wójcik@wp.pl</td>
      <td>0</td>
    </tr>
    <tr>
      <th>49</th>
      <td>50</td>
      <td>enrique_munoz@yahoo.es</td>
      <td>0</td>
    </tr>
    <tr>
      <th>50</th>
      <td>51</td>
      <td>joakim.johansson@yahoo.se</td>
      <td>0</td>
    </tr>
    <tr>
      <th>51</th>
      <td>52</td>
      <td>emma_jones@hotmail.com</td>
      <td>0</td>
    </tr>
    <tr>
      <th>52</th>
      <td>53</td>
      <td>phil.hughes@gmail.com</td>
      <td>12</td>
    </tr>
    <tr>
      <th>53</th>
      <td>54</td>
      <td>steve.murray@yahoo.uk</td>
      <td>0</td>
    </tr>
    <tr>
      <th>54</th>
      <td>55</td>
      <td>mark.taylor@yahoo.au</td>
      <td>0</td>
    </tr>
    <tr>
      <th>55</th>
      <td>56</td>
      <td>diego.gutierrez@yahoo.ar</td>
      <td>0</td>
    </tr>
    <tr>
      <th>56</th>
      <td>57</td>
      <td>luisrojas@yahoo.cl</td>
      <td>0</td>
    </tr>
    <tr>
      <th>57</th>
      <td>58</td>
      <td>manoj.pareek@rediff.com</td>
      <td>0</td>
    </tr>
    <tr>
      <th>58</th>
      <td>59</td>
      <td>puja_srivastava@yahoo.in</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



- 接下来，我们和SUBSTRING 函数结合使用，提取出邮箱地址中的用户名（也就是 "@" 符号前面的部分）：


```sql
%%sql
SELECT
    CustomerId,
    Email,
    SUBSTRING(Email, 1, CHARINDEX('@', Email) - 1) AS Username -- 这里直接函数套用，和 Python 中的函数套用是一样的
FROM Customer
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
      <th>Email</th>
      <th>Username</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>luisg@embraer.com.br</td>
      <td>luisg</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>leonekohler@surfeu.de</td>
      <td>leonekohler</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>ftremblay@gmail.com</td>
      <td>ftremblay</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>bjorn.hansen@yahoo.no</td>
      <td>bjorn.hansen</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>frantisekw@jetbrains.com</td>
      <td>frantisekw</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>hholy@gmail.com</td>
      <td>hholy</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>astrid.gruber@apple.at</td>
      <td>astrid.gruber</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>daan_peeters@apple.be</td>
      <td>daan_peeters</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>kara.nielsen@jubii.dk</td>
      <td>kara.nielsen</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>eduardo@woodstock.com.br</td>
      <td>eduardo</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>alero@uol.com.br</td>
      <td>alero</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>roberto.almeida@riotur.gov.br</td>
      <td>roberto.almeida</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>fernadaramos4@uol.com.br</td>
      <td>fernadaramos4</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>mphilips12@shaw.ca</td>
      <td>mphilips12</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>jenniferp@rogers.ca</td>
      <td>jenniferp</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>fharris@google.com</td>
      <td>fharris</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>jacksmith@microsoft.com</td>
      <td>jacksmith</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>michelleb@aol.com</td>
      <td>michelleb</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>tgoyer@apple.com</td>
      <td>tgoyer</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>dmiller@comcast.com</td>
      <td>dmiller</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>kachase@hotmail.com</td>
      <td>kachase</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>hleacock@gmail.com</td>
      <td>hleacock</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>johngordon22@yahoo.com</td>
      <td>johngordon22</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24</td>
      <td>fralston@gmail.com</td>
      <td>fralston</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>vstevens@yahoo.com</td>
      <td>vstevens</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26</td>
      <td>ricunningham@hotmail.com</td>
      <td>ricunningham</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27</td>
      <td>patrick.gray@aol.com</td>
      <td>patrick.gray</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>jubarnett@gmail.com</td>
      <td>jubarnett</td>
    </tr>
    <tr>
      <th>28</th>
      <td>29</td>
      <td>robbrown@shaw.ca</td>
      <td>robbrown</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>edfrancis@yachoo.ca</td>
      <td>edfrancis</td>
    </tr>
    <tr>
      <th>30</th>
      <td>31</td>
      <td>marthasilk@gmail.com</td>
      <td>marthasilk</td>
    </tr>
    <tr>
      <th>31</th>
      <td>32</td>
      <td>aaronmitchell@yahoo.ca</td>
      <td>aaronmitchell</td>
    </tr>
    <tr>
      <th>32</th>
      <td>33</td>
      <td>ellie.sullivan@shaw.ca</td>
      <td>ellie.sullivan</td>
    </tr>
    <tr>
      <th>33</th>
      <td>34</td>
      <td>jfernandes@yahoo.pt</td>
      <td>jfernandes</td>
    </tr>
    <tr>
      <th>34</th>
      <td>35</td>
      <td>masampaio@sapo.pt</td>
      <td>masampaio</td>
    </tr>
    <tr>
      <th>35</th>
      <td>36</td>
      <td>hannah.schneider@yahoo.de</td>
      <td>hannah.schneider</td>
    </tr>
    <tr>
      <th>36</th>
      <td>37</td>
      <td>fzimmermann@yahoo.de</td>
      <td>fzimmermann</td>
    </tr>
    <tr>
      <th>37</th>
      <td>38</td>
      <td>nschroder@surfeu.de</td>
      <td>nschroder</td>
    </tr>
    <tr>
      <th>38</th>
      <td>39</td>
      <td>camille.bernard@yahoo.fr</td>
      <td>camille.bernard</td>
    </tr>
    <tr>
      <th>39</th>
      <td>40</td>
      <td>dominiquelefebvre@gmail.com</td>
      <td>dominiquelefebvre</td>
    </tr>
    <tr>
      <th>40</th>
      <td>41</td>
      <td>marc.dubois@hotmail.com</td>
      <td>marc.dubois</td>
    </tr>
    <tr>
      <th>41</th>
      <td>42</td>
      <td>wyatt.girard@yahoo.fr</td>
      <td>wyatt.girard</td>
    </tr>
    <tr>
      <th>42</th>
      <td>43</td>
      <td>isabelle_mercier@apple.fr</td>
      <td>isabelle_mercier</td>
    </tr>
    <tr>
      <th>43</th>
      <td>44</td>
      <td>terhi.hamalainen@apple.fi</td>
      <td>terhi.hamalainen</td>
    </tr>
    <tr>
      <th>44</th>
      <td>45</td>
      <td>ladislav_kovacs@apple.hu</td>
      <td>ladislav_kovacs</td>
    </tr>
    <tr>
      <th>45</th>
      <td>46</td>
      <td>hughoreilly@apple.ie</td>
      <td>hughoreilly</td>
    </tr>
    <tr>
      <th>46</th>
      <td>47</td>
      <td>lucas.mancini@yahoo.it</td>
      <td>lucas.mancini</td>
    </tr>
    <tr>
      <th>47</th>
      <td>48</td>
      <td>johavanderberg@yahoo.nl</td>
      <td>johavanderberg</td>
    </tr>
    <tr>
      <th>48</th>
      <td>49</td>
      <td>stanisław.wójcik@wp.pl</td>
      <td>stanisław.wójcik</td>
    </tr>
    <tr>
      <th>49</th>
      <td>50</td>
      <td>enrique_munoz@yahoo.es</td>
      <td>enrique_munoz</td>
    </tr>
    <tr>
      <th>50</th>
      <td>51</td>
      <td>joakim.johansson@yahoo.se</td>
      <td>joakim.johansson</td>
    </tr>
    <tr>
      <th>51</th>
      <td>52</td>
      <td>emma_jones@hotmail.com</td>
      <td>emma_jones</td>
    </tr>
    <tr>
      <th>52</th>
      <td>53</td>
      <td>phil.hughes@gmail.com</td>
      <td>phil.hughes</td>
    </tr>
    <tr>
      <th>53</th>
      <td>54</td>
      <td>steve.murray@yahoo.uk</td>
      <td>steve.murray</td>
    </tr>
    <tr>
      <th>54</th>
      <td>55</td>
      <td>mark.taylor@yahoo.au</td>
      <td>mark.taylor</td>
    </tr>
    <tr>
      <th>55</th>
      <td>56</td>
      <td>diego.gutierrez@yahoo.ar</td>
      <td>diego.gutierrez</td>
    </tr>
    <tr>
      <th>56</th>
      <td>57</td>
      <td>luisrojas@yahoo.cl</td>
      <td>luisrojas</td>
    </tr>
    <tr>
      <th>57</th>
      <td>58</td>
      <td>manoj.pareek@rediff.com</td>
      <td>manoj.pareek</td>
    </tr>
    <tr>
      <th>58</th>
      <td>59</td>
      <td>puja_srivastava@yahoo.in</td>
      <td>puja_srivastava</td>
    </tr>
  </tbody>
</table>
</div>



#### (b) 按照模式查找字符串中的位置

查找字符串中子串位置，还有一个 `PATINDEX(pattern, string)` 函数，这个函数比较复杂：

- 它首先会判断，在字符串 `string` 中，是否存在一个子串能够匹配模式 `pattern`：

    - 这里的模式 `pattern` 和我们在 `LIKE` 语句中使用的模式是一样的
    - 使用通配符 `%` 和 `_` 来表示任意长度的字符串和任意单个字符

- 这个模式如果存在，它再去查找这个模式在字符串 `string` 中第一次出现的位置（索引从 1 开始），并返回这个位置
- 如果模式不存在于字符串中，那么 `PATINDEX` 函数会返回 0

我们来看几个具体的例子，假设我们有一个字符串 `'abcde'`，我们想找以下一些模式：

- 如果模式是 `'cd'` 那么 `PATINDEX` 函数会返回 0，因为 `'cd'` 这个模式表示的是，字符串是正正好好长成了 `'cd'` 这个样子的，而 "abcde" 这个字符串并不是正正好好长成了 `'cd'` 这个样子的，所以这个模式在这个字符串中是不存在的，因此 `PATINDEX` 函数会返回 0
- 如果模式是 `'%cd'` 那么 `PATINDEX` 函数会返回 0，因为这个模式表示的是，开头无所谓，结尾必须是 `'cd'`，而 `'abcde'` 这个字符串的结尾不是 `'cd'`，所以这个模式在这个字符串中也是不存在的，因此 `PATINDEX` 函数会返回 0
- 如果模式是 `'cd%'` 那么 `PATINDEX` 函数会返回 0，因为这个模式表示的是，开头必须是 `'cd'`，结尾无所谓，而 `'abcde'` 这个字符串的开头不是 `'cd'`，所以这个模式在这个字符串中也是不存在的，因此 `PATINDEX` 函数会返回 0
- 如果模式是 `'%cd%'` 那么 `PATINDEX` 函数会返回 3，因为这个模式表示的是，开头无所谓，结束无所谓，中间包含了 `'cd'`，这一点 `'abcde'` 是满足的，并且 `'cd'` 这个子串在 `'abcde'` 这个字符串中的位置是从第 3 个字符开始的，因此 `PATINDEX` 函数会返回 3，注意，此时的函数效果和 `CHARINDEX('cd', 'abcde')` 是一样的

通过以上例子，我们也可以看到，`PATINDEX` 函数和 `CHARINDEX` 是有很大区别的：

- 在 `CHARINDEX` 函数中，`CHARINDEX('cd', 'abcde')` 会返回 3，因为 `CHARINDEX` 函数只需要找到 `'cd'` 这个子串在字符串中第一次出现的位置就可以了，而不需要考虑这个子串前面和后面是什么样子的
- 在 `PATINDEX` 函数中，`PATINDEX('cd', 'abcde')` 会返回 0，这里的 `'cd'` 并不是子串，而是模式，这个模式要求字符串必须正正好好长成 `'cd'` 这个样子的，而 `'abcde'` 这个字符串并不是正正好好长成了 `'cd'` 这个样子的，所以这个模式在这个字符串中是不存在的，因此 `PATINDEX` 函数会返回 0

我们来看以下一些例子：

- 查询 `Customer` 表中的 `Email` 字段，先检查 `Email` 是否已 `'com'` 结尾，再查找 `'com'` 的位置，作为新的字段 `ComPosition`：


```sql
%%sql
SELECT
    CustomerId,
    Email,
    PATINDEX('%com', Email) AS ComPosition
FROM Customer
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
      <th>Email</th>
      <th>ComPosition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>luisg@embraer.com.br</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>leonekohler@surfeu.de</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>ftremblay@gmail.com</td>
      <td>17</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>bjorn.hansen@yahoo.no</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>frantisekw@jetbrains.com</td>
      <td>22</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>hholy@gmail.com</td>
      <td>13</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>astrid.gruber@apple.at</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>daan_peeters@apple.be</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>kara.nielsen@jubii.dk</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>eduardo@woodstock.com.br</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>alero@uol.com.br</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>roberto.almeida@riotur.gov.br</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>fernadaramos4@uol.com.br</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>mphilips12@shaw.ca</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>jenniferp@rogers.ca</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>fharris@google.com</td>
      <td>16</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>jacksmith@microsoft.com</td>
      <td>21</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>michelleb@aol.com</td>
      <td>15</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>tgoyer@apple.com</td>
      <td>14</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>dmiller@comcast.com</td>
      <td>17</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>kachase@hotmail.com</td>
      <td>17</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>hleacock@gmail.com</td>
      <td>16</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>johngordon22@yahoo.com</td>
      <td>20</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24</td>
      <td>fralston@gmail.com</td>
      <td>16</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>vstevens@yahoo.com</td>
      <td>16</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26</td>
      <td>ricunningham@hotmail.com</td>
      <td>22</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27</td>
      <td>patrick.gray@aol.com</td>
      <td>18</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>jubarnett@gmail.com</td>
      <td>17</td>
    </tr>
    <tr>
      <th>28</th>
      <td>29</td>
      <td>robbrown@shaw.ca</td>
      <td>0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>edfrancis@yachoo.ca</td>
      <td>0</td>
    </tr>
    <tr>
      <th>30</th>
      <td>31</td>
      <td>marthasilk@gmail.com</td>
      <td>18</td>
    </tr>
    <tr>
      <th>31</th>
      <td>32</td>
      <td>aaronmitchell@yahoo.ca</td>
      <td>0</td>
    </tr>
    <tr>
      <th>32</th>
      <td>33</td>
      <td>ellie.sullivan@shaw.ca</td>
      <td>0</td>
    </tr>
    <tr>
      <th>33</th>
      <td>34</td>
      <td>jfernandes@yahoo.pt</td>
      <td>0</td>
    </tr>
    <tr>
      <th>34</th>
      <td>35</td>
      <td>masampaio@sapo.pt</td>
      <td>0</td>
    </tr>
    <tr>
      <th>35</th>
      <td>36</td>
      <td>hannah.schneider@yahoo.de</td>
      <td>0</td>
    </tr>
    <tr>
      <th>36</th>
      <td>37</td>
      <td>fzimmermann@yahoo.de</td>
      <td>0</td>
    </tr>
    <tr>
      <th>37</th>
      <td>38</td>
      <td>nschroder@surfeu.de</td>
      <td>0</td>
    </tr>
    <tr>
      <th>38</th>
      <td>39</td>
      <td>camille.bernard@yahoo.fr</td>
      <td>0</td>
    </tr>
    <tr>
      <th>39</th>
      <td>40</td>
      <td>dominiquelefebvre@gmail.com</td>
      <td>25</td>
    </tr>
    <tr>
      <th>40</th>
      <td>41</td>
      <td>marc.dubois@hotmail.com</td>
      <td>21</td>
    </tr>
    <tr>
      <th>41</th>
      <td>42</td>
      <td>wyatt.girard@yahoo.fr</td>
      <td>0</td>
    </tr>
    <tr>
      <th>42</th>
      <td>43</td>
      <td>isabelle_mercier@apple.fr</td>
      <td>0</td>
    </tr>
    <tr>
      <th>43</th>
      <td>44</td>
      <td>terhi.hamalainen@apple.fi</td>
      <td>0</td>
    </tr>
    <tr>
      <th>44</th>
      <td>45</td>
      <td>ladislav_kovacs@apple.hu</td>
      <td>0</td>
    </tr>
    <tr>
      <th>45</th>
      <td>46</td>
      <td>hughoreilly@apple.ie</td>
      <td>0</td>
    </tr>
    <tr>
      <th>46</th>
      <td>47</td>
      <td>lucas.mancini@yahoo.it</td>
      <td>0</td>
    </tr>
    <tr>
      <th>47</th>
      <td>48</td>
      <td>johavanderberg@yahoo.nl</td>
      <td>0</td>
    </tr>
    <tr>
      <th>48</th>
      <td>49</td>
      <td>stanisław.wójcik@wp.pl</td>
      <td>0</td>
    </tr>
    <tr>
      <th>49</th>
      <td>50</td>
      <td>enrique_munoz@yahoo.es</td>
      <td>0</td>
    </tr>
    <tr>
      <th>50</th>
      <td>51</td>
      <td>joakim.johansson@yahoo.se</td>
      <td>0</td>
    </tr>
    <tr>
      <th>51</th>
      <td>52</td>
      <td>emma_jones@hotmail.com</td>
      <td>20</td>
    </tr>
    <tr>
      <th>52</th>
      <td>53</td>
      <td>phil.hughes@gmail.com</td>
      <td>19</td>
    </tr>
    <tr>
      <th>53</th>
      <td>54</td>
      <td>steve.murray@yahoo.uk</td>
      <td>0</td>
    </tr>
    <tr>
      <th>54</th>
      <td>55</td>
      <td>mark.taylor@yahoo.au</td>
      <td>0</td>
    </tr>
    <tr>
      <th>55</th>
      <td>56</td>
      <td>diego.gutierrez@yahoo.ar</td>
      <td>0</td>
    </tr>
    <tr>
      <th>56</th>
      <td>57</td>
      <td>luisrojas@yahoo.cl</td>
      <td>0</td>
    </tr>
    <tr>
      <th>57</th>
      <td>58</td>
      <td>manoj.pareek@rediff.com</td>
      <td>21</td>
    </tr>
    <tr>
      <th>58</th>
      <td>59</td>
      <td>puja_srivastava@yahoo.in</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



- 查询 `Customer` 表中的 `Email` 字段，先检查 `Email` 是否含有 `'gmail'`，再查找 `'gmail'` 的位置，作为新的字段 `GmailPosition`：


```sql
%%sql
SELECT
    CustomerId,
    Email,
    PATINDEX('%gmail%', Email) AS GmailPosition1,
    CHARINDEX('gmail', Email) AS GmailPosition2 -- 这里我们也使用 CHARINDEX 来查找 gmail 的位置，和 PATINDEX 的结果进行对比
FROM Customer
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
      <th>Email</th>
      <th>GmailPosition1</th>
      <th>GmailPosition2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>luisg@embraer.com.br</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>leonekohler@surfeu.de</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>ftremblay@gmail.com</td>
      <td>11</td>
      <td>11</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>bjorn.hansen@yahoo.no</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>frantisekw@jetbrains.com</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>hholy@gmail.com</td>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>astrid.gruber@apple.at</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>daan_peeters@apple.be</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>kara.nielsen@jubii.dk</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>eduardo@woodstock.com.br</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>alero@uol.com.br</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>roberto.almeida@riotur.gov.br</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>fernadaramos4@uol.com.br</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>mphilips12@shaw.ca</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>jenniferp@rogers.ca</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>fharris@google.com</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>jacksmith@microsoft.com</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>michelleb@aol.com</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>tgoyer@apple.com</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>dmiller@comcast.com</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>kachase@hotmail.com</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>hleacock@gmail.com</td>
      <td>10</td>
      <td>10</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>johngordon22@yahoo.com</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24</td>
      <td>fralston@gmail.com</td>
      <td>10</td>
      <td>10</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>vstevens@yahoo.com</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26</td>
      <td>ricunningham@hotmail.com</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27</td>
      <td>patrick.gray@aol.com</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>jubarnett@gmail.com</td>
      <td>11</td>
      <td>11</td>
    </tr>
    <tr>
      <th>28</th>
      <td>29</td>
      <td>robbrown@shaw.ca</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>edfrancis@yachoo.ca</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>30</th>
      <td>31</td>
      <td>marthasilk@gmail.com</td>
      <td>12</td>
      <td>12</td>
    </tr>
    <tr>
      <th>31</th>
      <td>32</td>
      <td>aaronmitchell@yahoo.ca</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>32</th>
      <td>33</td>
      <td>ellie.sullivan@shaw.ca</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>33</th>
      <td>34</td>
      <td>jfernandes@yahoo.pt</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>34</th>
      <td>35</td>
      <td>masampaio@sapo.pt</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>35</th>
      <td>36</td>
      <td>hannah.schneider@yahoo.de</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>36</th>
      <td>37</td>
      <td>fzimmermann@yahoo.de</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>37</th>
      <td>38</td>
      <td>nschroder@surfeu.de</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>38</th>
      <td>39</td>
      <td>camille.bernard@yahoo.fr</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>39</th>
      <td>40</td>
      <td>dominiquelefebvre@gmail.com</td>
      <td>19</td>
      <td>19</td>
    </tr>
    <tr>
      <th>40</th>
      <td>41</td>
      <td>marc.dubois@hotmail.com</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>41</th>
      <td>42</td>
      <td>wyatt.girard@yahoo.fr</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>42</th>
      <td>43</td>
      <td>isabelle_mercier@apple.fr</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>43</th>
      <td>44</td>
      <td>terhi.hamalainen@apple.fi</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>44</th>
      <td>45</td>
      <td>ladislav_kovacs@apple.hu</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>45</th>
      <td>46</td>
      <td>hughoreilly@apple.ie</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>46</th>
      <td>47</td>
      <td>lucas.mancini@yahoo.it</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>47</th>
      <td>48</td>
      <td>johavanderberg@yahoo.nl</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>48</th>
      <td>49</td>
      <td>stanisław.wójcik@wp.pl</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>49</th>
      <td>50</td>
      <td>enrique_munoz@yahoo.es</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>50</th>
      <td>51</td>
      <td>joakim.johansson@yahoo.se</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>51</th>
      <td>52</td>
      <td>emma_jones@hotmail.com</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>52</th>
      <td>53</td>
      <td>phil.hughes@gmail.com</td>
      <td>13</td>
      <td>13</td>
    </tr>
    <tr>
      <th>53</th>
      <td>54</td>
      <td>steve.murray@yahoo.uk</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>54</th>
      <td>55</td>
      <td>mark.taylor@yahoo.au</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>55</th>
      <td>56</td>
      <td>diego.gutierrez@yahoo.ar</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>56</th>
      <td>57</td>
      <td>luisrojas@yahoo.cl</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>57</th>
      <td>58</td>
      <td>manoj.pareek@rediff.com</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>58</th>
      <td>59</td>
      <td>puja_srivastava@yahoo.in</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### (4) 字符串拼接

在 SQL 中，我们可以使用以下的一些方式进行字符串的拼接：

- 使用 `+` 运算符进行字符串拼接：`string1 + string2` 会将 `string1` 和 `string2` 连接在一起形成一个新的字符串
- 使用 `CONCAT(string1, string2, ...)` 函数进行字符串拼接：`CONCAT` 函数可以接受多个字符串参数，并将它们连接在一起形成一个新的字符串
- 使用 `CONCAT_WS(separator, string1, string2, ...)` 函数进行字符串拼接：`CONCAT_WS` 函数与 `CONCAT` 函数类似，但它允许你指定一个分隔符 `separator`，这个分隔符会被插入到每个字符串之间

我们使用以上方法，来做同一件事：查询 `Employee` 表，并将 `Title`、`FirstName` 和 `LastName` 这三个字段拼接成一个新的字段 `FullName`，并且在每个字段之间添加一个空格作为分隔符：


```sql
%%sql
SELECT
    EmployeeID,
    -- 使用 + 运算符进行字符串拼接
    Title + ' ' + FirstName + ' ' + LastName AS FullNameV1,
    -- 使用 CONCAT 函数进行字符串拼接
    CONCAT(Title, ' ', FirstName, ' ', LastName) AS FullNameV2,
    -- 使用 CONCAT_WS 函数进行字符串拼接，指定空格作为分隔符
    CONCAT_WS(' ', Title, FirstName, LastName) AS FullNameV3
FROM Employee
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
      <th>EmployeeID</th>
      <th>FullNameV1</th>
      <th>FullNameV2</th>
      <th>FullNameV3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>General Manager Andrew Adams</td>
      <td>General Manager Andrew Adams</td>
      <td>General Manager Andrew Adams</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Sales Manager Nancy Edwards</td>
      <td>Sales Manager Nancy Edwards</td>
      <td>Sales Manager Nancy Edwards</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Sales Support Agent Jane Peacock</td>
      <td>Sales Support Agent Jane Peacock</td>
      <td>Sales Support Agent Jane Peacock</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Sales Support Agent Margaret Park</td>
      <td>Sales Support Agent Margaret Park</td>
      <td>Sales Support Agent Margaret Park</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Sales Support Agent Steve Johnson</td>
      <td>Sales Support Agent Steve Johnson</td>
      <td>Sales Support Agent Steve Johnson</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>IT Manager Michael Mitchell</td>
      <td>IT Manager Michael Mitchell</td>
      <td>IT Manager Michael Mitchell</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>IT Staff Robert King</td>
      <td>IT Staff Robert King</td>
      <td>IT Staff Robert King</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>IT Staff Laura Callahan</td>
      <td>IT Staff Laura Callahan</td>
      <td>IT Staff Laura Callahan</td>
    </tr>
  </tbody>
</table>
</div>



### (5) 字符串的其他操作

除了以上介绍的字符串运算之外，SQL 中还有一些其他的字符串操作函数，例如：

- `UPPER(string)`：将字符串转换为大写
- `LOWER(string)`：将字符串转换为小写
- `LTRIM(string)`：去除字符串左边的空格
- `RTRIM(string)`：去除字符串右边的空格
- `TRIM(string)`：去除字符串两边的空格
- `REPLACE(string, old_substring, new_substring)`：将字符串中的 `old_substring` 替换为 `new_substring`
- `REPLICATE(string, count)`：将字符串重复 `count` 次
- `REVERSE(string)`：将字符串反转

我们统一在 `Customer` 表中的 `Email` 字段上使用这些函数来展示它们的功能：


```sql
%%sql
SELECT
    CustomerId,
    Email,
    UPPER(Email) AS UpperEmail, -- 将邮箱地址转换为大写
    LOWER(Email) AS LowerEmail, -- 将邮箱地址转换为小写
    LTRIM(Email) AS LeftTrimmedEmail, -- 去除邮箱地址左边的空格
    RTRIM(Email) AS RightTrimmedEmail, -- 去除邮箱地址右边的空格
    TRIM(Email) AS TrimmedEmail, -- 去除邮箱地址两边的空格
    REPLACE(Email, '@', '[at]') AS ReplacedEmail, -- 将邮箱地址中的 @ 符号替换为 [at]
    REPLICATE(Email, 2) AS ReplicatedEmail, -- 将邮箱地址重复两次
    REVERSE(Email) AS ReversedEmail -- 将邮箱地址反转
FROM Customer
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
      <th>Email</th>
      <th>UpperEmail</th>
      <th>LowerEmail</th>
      <th>LeftTrimmedEmail</th>
      <th>RightTrimmedEmail</th>
      <th>TrimmedEmail</th>
      <th>ReplacedEmail</th>
      <th>ReplicatedEmail</th>
      <th>ReversedEmail</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>luisg@embraer.com.br</td>
      <td>LUISG@EMBRAER.COM.BR</td>
      <td>luisg@embraer.com.br</td>
      <td>luisg@embraer.com.br</td>
      <td>luisg@embraer.com.br</td>
      <td>luisg@embraer.com.br</td>
      <td>luisg[at]embraer.com.br</td>
      <td>luisg@embraer.com.brluisg@embraer.com.br</td>
      <td>rb.moc.rearbme@gsiul</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>leonekohler@surfeu.de</td>
      <td>LEONEKOHLER@SURFEU.DE</td>
      <td>leonekohler@surfeu.de</td>
      <td>leonekohler@surfeu.de</td>
      <td>leonekohler@surfeu.de</td>
      <td>leonekohler@surfeu.de</td>
      <td>leonekohler[at]surfeu.de</td>
      <td>leonekohler@surfeu.deleonekohler@surfeu.de</td>
      <td>ed.uefrus@relhokenoel</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>ftremblay@gmail.com</td>
      <td>FTREMBLAY@GMAIL.COM</td>
      <td>ftremblay@gmail.com</td>
      <td>ftremblay@gmail.com</td>
      <td>ftremblay@gmail.com</td>
      <td>ftremblay@gmail.com</td>
      <td>ftremblay[at]gmail.com</td>
      <td>ftremblay@gmail.comftremblay@gmail.com</td>
      <td>moc.liamg@yalbmertf</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>bjorn.hansen@yahoo.no</td>
      <td>BJORN.HANSEN@YAHOO.NO</td>
      <td>bjorn.hansen@yahoo.no</td>
      <td>bjorn.hansen@yahoo.no</td>
      <td>bjorn.hansen@yahoo.no</td>
      <td>bjorn.hansen@yahoo.no</td>
      <td>bjorn.hansen[at]yahoo.no</td>
      <td>bjorn.hansen@yahoo.nobjorn.hansen@yahoo.no</td>
      <td>on.oohay@nesnah.nrojb</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>frantisekw@jetbrains.com</td>
      <td>FRANTISEKW@JETBRAINS.COM</td>
      <td>frantisekw@jetbrains.com</td>
      <td>frantisekw@jetbrains.com</td>
      <td>frantisekw@jetbrains.com</td>
      <td>frantisekw@jetbrains.com</td>
      <td>frantisekw[at]jetbrains.com</td>
      <td>frantisekw@jetbrains.comfrantisekw@jetbrains.com</td>
      <td>moc.sniarbtej@wkesitnarf</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>hholy@gmail.com</td>
      <td>HHOLY@GMAIL.COM</td>
      <td>hholy@gmail.com</td>
      <td>hholy@gmail.com</td>
      <td>hholy@gmail.com</td>
      <td>hholy@gmail.com</td>
      <td>hholy[at]gmail.com</td>
      <td>hholy@gmail.comhholy@gmail.com</td>
      <td>moc.liamg@ylohh</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>astrid.gruber@apple.at</td>
      <td>ASTRID.GRUBER@APPLE.AT</td>
      <td>astrid.gruber@apple.at</td>
      <td>astrid.gruber@apple.at</td>
      <td>astrid.gruber@apple.at</td>
      <td>astrid.gruber@apple.at</td>
      <td>astrid.gruber[at]apple.at</td>
      <td>astrid.gruber@apple.atastrid.gruber@apple.at</td>
      <td>ta.elppa@reburg.dirtsa</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>daan_peeters@apple.be</td>
      <td>DAAN_PEETERS@APPLE.BE</td>
      <td>daan_peeters@apple.be</td>
      <td>daan_peeters@apple.be</td>
      <td>daan_peeters@apple.be</td>
      <td>daan_peeters@apple.be</td>
      <td>daan_peeters[at]apple.be</td>
      <td>daan_peeters@apple.bedaan_peeters@apple.be</td>
      <td>eb.elppa@sreteep_naad</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>kara.nielsen@jubii.dk</td>
      <td>KARA.NIELSEN@JUBII.DK</td>
      <td>kara.nielsen@jubii.dk</td>
      <td>kara.nielsen@jubii.dk</td>
      <td>kara.nielsen@jubii.dk</td>
      <td>kara.nielsen@jubii.dk</td>
      <td>kara.nielsen[at]jubii.dk</td>
      <td>kara.nielsen@jubii.dkkara.nielsen@jubii.dk</td>
      <td>kd.iibuj@neslein.arak</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>eduardo@woodstock.com.br</td>
      <td>EDUARDO@WOODSTOCK.COM.BR</td>
      <td>eduardo@woodstock.com.br</td>
      <td>eduardo@woodstock.com.br</td>
      <td>eduardo@woodstock.com.br</td>
      <td>eduardo@woodstock.com.br</td>
      <td>eduardo[at]woodstock.com.br</td>
      <td>eduardo@woodstock.com.breduardo@woodstock.com.br</td>
      <td>rb.moc.kcotsdoow@odraude</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>alero@uol.com.br</td>
      <td>ALERO@UOL.COM.BR</td>
      <td>alero@uol.com.br</td>
      <td>alero@uol.com.br</td>
      <td>alero@uol.com.br</td>
      <td>alero@uol.com.br</td>
      <td>alero[at]uol.com.br</td>
      <td>alero@uol.com.bralero@uol.com.br</td>
      <td>rb.moc.lou@orela</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>roberto.almeida@riotur.gov.br</td>
      <td>ROBERTO.ALMEIDA@RIOTUR.GOV.BR</td>
      <td>roberto.almeida@riotur.gov.br</td>
      <td>roberto.almeida@riotur.gov.br</td>
      <td>roberto.almeida@riotur.gov.br</td>
      <td>roberto.almeida@riotur.gov.br</td>
      <td>roberto.almeida[at]riotur.gov.br</td>
      <td>roberto.almeida@riotur.gov.brroberto.almeida@r...</td>
      <td>rb.vog.rutoir@adiemla.otrebor</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>fernadaramos4@uol.com.br</td>
      <td>FERNADARAMOS4@UOL.COM.BR</td>
      <td>fernadaramos4@uol.com.br</td>
      <td>fernadaramos4@uol.com.br</td>
      <td>fernadaramos4@uol.com.br</td>
      <td>fernadaramos4@uol.com.br</td>
      <td>fernadaramos4[at]uol.com.br</td>
      <td>fernadaramos4@uol.com.brfernadaramos4@uol.com.br</td>
      <td>rb.moc.lou@4somaradanref</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>mphilips12@shaw.ca</td>
      <td>MPHILIPS12@SHAW.CA</td>
      <td>mphilips12@shaw.ca</td>
      <td>mphilips12@shaw.ca</td>
      <td>mphilips12@shaw.ca</td>
      <td>mphilips12@shaw.ca</td>
      <td>mphilips12[at]shaw.ca</td>
      <td>mphilips12@shaw.camphilips12@shaw.ca</td>
      <td>ac.wahs@21spilihpm</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>jenniferp@rogers.ca</td>
      <td>JENNIFERP@ROGERS.CA</td>
      <td>jenniferp@rogers.ca</td>
      <td>jenniferp@rogers.ca</td>
      <td>jenniferp@rogers.ca</td>
      <td>jenniferp@rogers.ca</td>
      <td>jenniferp[at]rogers.ca</td>
      <td>jenniferp@rogers.cajenniferp@rogers.ca</td>
      <td>ac.sregor@prefinnej</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>fharris@google.com</td>
      <td>FHARRIS@GOOGLE.COM</td>
      <td>fharris@google.com</td>
      <td>fharris@google.com</td>
      <td>fharris@google.com</td>
      <td>fharris@google.com</td>
      <td>fharris[at]google.com</td>
      <td>fharris@google.comfharris@google.com</td>
      <td>moc.elgoog@sirrahf</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>jacksmith@microsoft.com</td>
      <td>JACKSMITH@MICROSOFT.COM</td>
      <td>jacksmith@microsoft.com</td>
      <td>jacksmith@microsoft.com</td>
      <td>jacksmith@microsoft.com</td>
      <td>jacksmith@microsoft.com</td>
      <td>jacksmith[at]microsoft.com</td>
      <td>jacksmith@microsoft.comjacksmith@microsoft.com</td>
      <td>moc.tfosorcim@htimskcaj</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>michelleb@aol.com</td>
      <td>MICHELLEB@AOL.COM</td>
      <td>michelleb@aol.com</td>
      <td>michelleb@aol.com</td>
      <td>michelleb@aol.com</td>
      <td>michelleb@aol.com</td>
      <td>michelleb[at]aol.com</td>
      <td>michelleb@aol.commichelleb@aol.com</td>
      <td>moc.loa@bellehcim</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>tgoyer@apple.com</td>
      <td>TGOYER@APPLE.COM</td>
      <td>tgoyer@apple.com</td>
      <td>tgoyer@apple.com</td>
      <td>tgoyer@apple.com</td>
      <td>tgoyer@apple.com</td>
      <td>tgoyer[at]apple.com</td>
      <td>tgoyer@apple.comtgoyer@apple.com</td>
      <td>moc.elppa@reyogt</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>dmiller@comcast.com</td>
      <td>DMILLER@COMCAST.COM</td>
      <td>dmiller@comcast.com</td>
      <td>dmiller@comcast.com</td>
      <td>dmiller@comcast.com</td>
      <td>dmiller@comcast.com</td>
      <td>dmiller[at]comcast.com</td>
      <td>dmiller@comcast.comdmiller@comcast.com</td>
      <td>moc.tsacmoc@rellimd</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>kachase@hotmail.com</td>
      <td>KACHASE@HOTMAIL.COM</td>
      <td>kachase@hotmail.com</td>
      <td>kachase@hotmail.com</td>
      <td>kachase@hotmail.com</td>
      <td>kachase@hotmail.com</td>
      <td>kachase[at]hotmail.com</td>
      <td>kachase@hotmail.comkachase@hotmail.com</td>
      <td>moc.liamtoh@esahcak</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>hleacock@gmail.com</td>
      <td>HLEACOCK@GMAIL.COM</td>
      <td>hleacock@gmail.com</td>
      <td>hleacock@gmail.com</td>
      <td>hleacock@gmail.com</td>
      <td>hleacock@gmail.com</td>
      <td>hleacock[at]gmail.com</td>
      <td>hleacock@gmail.comhleacock@gmail.com</td>
      <td>moc.liamg@kcocaelh</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>johngordon22@yahoo.com</td>
      <td>JOHNGORDON22@YAHOO.COM</td>
      <td>johngordon22@yahoo.com</td>
      <td>johngordon22@yahoo.com</td>
      <td>johngordon22@yahoo.com</td>
      <td>johngordon22@yahoo.com</td>
      <td>johngordon22[at]yahoo.com</td>
      <td>johngordon22@yahoo.comjohngordon22@yahoo.com</td>
      <td>moc.oohay@22nodrognhoj</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24</td>
      <td>fralston@gmail.com</td>
      <td>FRALSTON@GMAIL.COM</td>
      <td>fralston@gmail.com</td>
      <td>fralston@gmail.com</td>
      <td>fralston@gmail.com</td>
      <td>fralston@gmail.com</td>
      <td>fralston[at]gmail.com</td>
      <td>fralston@gmail.comfralston@gmail.com</td>
      <td>moc.liamg@notslarf</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>vstevens@yahoo.com</td>
      <td>VSTEVENS@YAHOO.COM</td>
      <td>vstevens@yahoo.com</td>
      <td>vstevens@yahoo.com</td>
      <td>vstevens@yahoo.com</td>
      <td>vstevens@yahoo.com</td>
      <td>vstevens[at]yahoo.com</td>
      <td>vstevens@yahoo.comvstevens@yahoo.com</td>
      <td>moc.oohay@snevetsv</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26</td>
      <td>ricunningham@hotmail.com</td>
      <td>RICUNNINGHAM@HOTMAIL.COM</td>
      <td>ricunningham@hotmail.com</td>
      <td>ricunningham@hotmail.com</td>
      <td>ricunningham@hotmail.com</td>
      <td>ricunningham@hotmail.com</td>
      <td>ricunningham[at]hotmail.com</td>
      <td>ricunningham@hotmail.comricunningham@hotmail.com</td>
      <td>moc.liamtoh@mahgninnucir</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27</td>
      <td>patrick.gray@aol.com</td>
      <td>PATRICK.GRAY@AOL.COM</td>
      <td>patrick.gray@aol.com</td>
      <td>patrick.gray@aol.com</td>
      <td>patrick.gray@aol.com</td>
      <td>patrick.gray@aol.com</td>
      <td>patrick.gray[at]aol.com</td>
      <td>patrick.gray@aol.compatrick.gray@aol.com</td>
      <td>moc.loa@yarg.kcirtap</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>jubarnett@gmail.com</td>
      <td>JUBARNETT@GMAIL.COM</td>
      <td>jubarnett@gmail.com</td>
      <td>jubarnett@gmail.com</td>
      <td>jubarnett@gmail.com</td>
      <td>jubarnett@gmail.com</td>
      <td>jubarnett[at]gmail.com</td>
      <td>jubarnett@gmail.comjubarnett@gmail.com</td>
      <td>moc.liamg@ttenrabuj</td>
    </tr>
    <tr>
      <th>28</th>
      <td>29</td>
      <td>robbrown@shaw.ca</td>
      <td>ROBBROWN@SHAW.CA</td>
      <td>robbrown@shaw.ca</td>
      <td>robbrown@shaw.ca</td>
      <td>robbrown@shaw.ca</td>
      <td>robbrown@shaw.ca</td>
      <td>robbrown[at]shaw.ca</td>
      <td>robbrown@shaw.carobbrown@shaw.ca</td>
      <td>ac.wahs@nworbbor</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>edfrancis@yachoo.ca</td>
      <td>EDFRANCIS@YACHOO.CA</td>
      <td>edfrancis@yachoo.ca</td>
      <td>edfrancis@yachoo.ca</td>
      <td>edfrancis@yachoo.ca</td>
      <td>edfrancis@yachoo.ca</td>
      <td>edfrancis[at]yachoo.ca</td>
      <td>edfrancis@yachoo.caedfrancis@yachoo.ca</td>
      <td>ac.oohcay@sicnarfde</td>
    </tr>
    <tr>
      <th>30</th>
      <td>31</td>
      <td>marthasilk@gmail.com</td>
      <td>MARTHASILK@GMAIL.COM</td>
      <td>marthasilk@gmail.com</td>
      <td>marthasilk@gmail.com</td>
      <td>marthasilk@gmail.com</td>
      <td>marthasilk@gmail.com</td>
      <td>marthasilk[at]gmail.com</td>
      <td>marthasilk@gmail.commarthasilk@gmail.com</td>
      <td>moc.liamg@klisahtram</td>
    </tr>
    <tr>
      <th>31</th>
      <td>32</td>
      <td>aaronmitchell@yahoo.ca</td>
      <td>AARONMITCHELL@YAHOO.CA</td>
      <td>aaronmitchell@yahoo.ca</td>
      <td>aaronmitchell@yahoo.ca</td>
      <td>aaronmitchell@yahoo.ca</td>
      <td>aaronmitchell@yahoo.ca</td>
      <td>aaronmitchell[at]yahoo.ca</td>
      <td>aaronmitchell@yahoo.caaaronmitchell@yahoo.ca</td>
      <td>ac.oohay@llehctimnoraa</td>
    </tr>
    <tr>
      <th>32</th>
      <td>33</td>
      <td>ellie.sullivan@shaw.ca</td>
      <td>ELLIE.SULLIVAN@SHAW.CA</td>
      <td>ellie.sullivan@shaw.ca</td>
      <td>ellie.sullivan@shaw.ca</td>
      <td>ellie.sullivan@shaw.ca</td>
      <td>ellie.sullivan@shaw.ca</td>
      <td>ellie.sullivan[at]shaw.ca</td>
      <td>ellie.sullivan@shaw.caellie.sullivan@shaw.ca</td>
      <td>ac.wahs@navillus.eille</td>
    </tr>
    <tr>
      <th>33</th>
      <td>34</td>
      <td>jfernandes@yahoo.pt</td>
      <td>JFERNANDES@YAHOO.PT</td>
      <td>jfernandes@yahoo.pt</td>
      <td>jfernandes@yahoo.pt</td>
      <td>jfernandes@yahoo.pt</td>
      <td>jfernandes@yahoo.pt</td>
      <td>jfernandes[at]yahoo.pt</td>
      <td>jfernandes@yahoo.ptjfernandes@yahoo.pt</td>
      <td>tp.oohay@sednanrefj</td>
    </tr>
    <tr>
      <th>34</th>
      <td>35</td>
      <td>masampaio@sapo.pt</td>
      <td>MASAMPAIO@SAPO.PT</td>
      <td>masampaio@sapo.pt</td>
      <td>masampaio@sapo.pt</td>
      <td>masampaio@sapo.pt</td>
      <td>masampaio@sapo.pt</td>
      <td>masampaio[at]sapo.pt</td>
      <td>masampaio@sapo.ptmasampaio@sapo.pt</td>
      <td>tp.opas@oiapmasam</td>
    </tr>
    <tr>
      <th>35</th>
      <td>36</td>
      <td>hannah.schneider@yahoo.de</td>
      <td>HANNAH.SCHNEIDER@YAHOO.DE</td>
      <td>hannah.schneider@yahoo.de</td>
      <td>hannah.schneider@yahoo.de</td>
      <td>hannah.schneider@yahoo.de</td>
      <td>hannah.schneider@yahoo.de</td>
      <td>hannah.schneider[at]yahoo.de</td>
      <td>hannah.schneider@yahoo.dehannah.schneider@yaho...</td>
      <td>ed.oohay@redienhcs.hannah</td>
    </tr>
    <tr>
      <th>36</th>
      <td>37</td>
      <td>fzimmermann@yahoo.de</td>
      <td>FZIMMERMANN@YAHOO.DE</td>
      <td>fzimmermann@yahoo.de</td>
      <td>fzimmermann@yahoo.de</td>
      <td>fzimmermann@yahoo.de</td>
      <td>fzimmermann@yahoo.de</td>
      <td>fzimmermann[at]yahoo.de</td>
      <td>fzimmermann@yahoo.defzimmermann@yahoo.de</td>
      <td>ed.oohay@nnamremmizf</td>
    </tr>
    <tr>
      <th>37</th>
      <td>38</td>
      <td>nschroder@surfeu.de</td>
      <td>NSCHRODER@SURFEU.DE</td>
      <td>nschroder@surfeu.de</td>
      <td>nschroder@surfeu.de</td>
      <td>nschroder@surfeu.de</td>
      <td>nschroder@surfeu.de</td>
      <td>nschroder[at]surfeu.de</td>
      <td>nschroder@surfeu.denschroder@surfeu.de</td>
      <td>ed.uefrus@redorhcsn</td>
    </tr>
    <tr>
      <th>38</th>
      <td>39</td>
      <td>camille.bernard@yahoo.fr</td>
      <td>CAMILLE.BERNARD@YAHOO.FR</td>
      <td>camille.bernard@yahoo.fr</td>
      <td>camille.bernard@yahoo.fr</td>
      <td>camille.bernard@yahoo.fr</td>
      <td>camille.bernard@yahoo.fr</td>
      <td>camille.bernard[at]yahoo.fr</td>
      <td>camille.bernard@yahoo.frcamille.bernard@yahoo.fr</td>
      <td>rf.oohay@dranreb.ellimac</td>
    </tr>
    <tr>
      <th>39</th>
      <td>40</td>
      <td>dominiquelefebvre@gmail.com</td>
      <td>DOMINIQUELEFEBVRE@GMAIL.COM</td>
      <td>dominiquelefebvre@gmail.com</td>
      <td>dominiquelefebvre@gmail.com</td>
      <td>dominiquelefebvre@gmail.com</td>
      <td>dominiquelefebvre@gmail.com</td>
      <td>dominiquelefebvre[at]gmail.com</td>
      <td>dominiquelefebvre@gmail.comdominiquelefebvre@g...</td>
      <td>moc.liamg@ervbefeleuqinimod</td>
    </tr>
    <tr>
      <th>40</th>
      <td>41</td>
      <td>marc.dubois@hotmail.com</td>
      <td>MARC.DUBOIS@HOTMAIL.COM</td>
      <td>marc.dubois@hotmail.com</td>
      <td>marc.dubois@hotmail.com</td>
      <td>marc.dubois@hotmail.com</td>
      <td>marc.dubois@hotmail.com</td>
      <td>marc.dubois[at]hotmail.com</td>
      <td>marc.dubois@hotmail.commarc.dubois@hotmail.com</td>
      <td>moc.liamtoh@siobud.cram</td>
    </tr>
    <tr>
      <th>41</th>
      <td>42</td>
      <td>wyatt.girard@yahoo.fr</td>
      <td>WYATT.GIRARD@YAHOO.FR</td>
      <td>wyatt.girard@yahoo.fr</td>
      <td>wyatt.girard@yahoo.fr</td>
      <td>wyatt.girard@yahoo.fr</td>
      <td>wyatt.girard@yahoo.fr</td>
      <td>wyatt.girard[at]yahoo.fr</td>
      <td>wyatt.girard@yahoo.frwyatt.girard@yahoo.fr</td>
      <td>rf.oohay@drarig.ttayw</td>
    </tr>
    <tr>
      <th>42</th>
      <td>43</td>
      <td>isabelle_mercier@apple.fr</td>
      <td>ISABELLE_MERCIER@APPLE.FR</td>
      <td>isabelle_mercier@apple.fr</td>
      <td>isabelle_mercier@apple.fr</td>
      <td>isabelle_mercier@apple.fr</td>
      <td>isabelle_mercier@apple.fr</td>
      <td>isabelle_mercier[at]apple.fr</td>
      <td>isabelle_mercier@apple.frisabelle_mercier@appl...</td>
      <td>rf.elppa@reicrem_ellebasi</td>
    </tr>
    <tr>
      <th>43</th>
      <td>44</td>
      <td>terhi.hamalainen@apple.fi</td>
      <td>TERHI.HAMALAINEN@APPLE.FI</td>
      <td>terhi.hamalainen@apple.fi</td>
      <td>terhi.hamalainen@apple.fi</td>
      <td>terhi.hamalainen@apple.fi</td>
      <td>terhi.hamalainen@apple.fi</td>
      <td>terhi.hamalainen[at]apple.fi</td>
      <td>terhi.hamalainen@apple.fiterhi.hamalainen@appl...</td>
      <td>if.elppa@nenialamah.ihret</td>
    </tr>
    <tr>
      <th>44</th>
      <td>45</td>
      <td>ladislav_kovacs@apple.hu</td>
      <td>LADISLAV_KOVACS@APPLE.HU</td>
      <td>ladislav_kovacs@apple.hu</td>
      <td>ladislav_kovacs@apple.hu</td>
      <td>ladislav_kovacs@apple.hu</td>
      <td>ladislav_kovacs@apple.hu</td>
      <td>ladislav_kovacs[at]apple.hu</td>
      <td>ladislav_kovacs@apple.huladislav_kovacs@apple.hu</td>
      <td>uh.elppa@scavok_valsidal</td>
    </tr>
    <tr>
      <th>45</th>
      <td>46</td>
      <td>hughoreilly@apple.ie</td>
      <td>HUGHOREILLY@APPLE.IE</td>
      <td>hughoreilly@apple.ie</td>
      <td>hughoreilly@apple.ie</td>
      <td>hughoreilly@apple.ie</td>
      <td>hughoreilly@apple.ie</td>
      <td>hughoreilly[at]apple.ie</td>
      <td>hughoreilly@apple.iehughoreilly@apple.ie</td>
      <td>ei.elppa@yllierohguh</td>
    </tr>
    <tr>
      <th>46</th>
      <td>47</td>
      <td>lucas.mancini@yahoo.it</td>
      <td>LUCAS.MANCINI@YAHOO.IT</td>
      <td>lucas.mancini@yahoo.it</td>
      <td>lucas.mancini@yahoo.it</td>
      <td>lucas.mancini@yahoo.it</td>
      <td>lucas.mancini@yahoo.it</td>
      <td>lucas.mancini[at]yahoo.it</td>
      <td>lucas.mancini@yahoo.itlucas.mancini@yahoo.it</td>
      <td>ti.oohay@inicnam.sacul</td>
    </tr>
    <tr>
      <th>47</th>
      <td>48</td>
      <td>johavanderberg@yahoo.nl</td>
      <td>JOHAVANDERBERG@YAHOO.NL</td>
      <td>johavanderberg@yahoo.nl</td>
      <td>johavanderberg@yahoo.nl</td>
      <td>johavanderberg@yahoo.nl</td>
      <td>johavanderberg@yahoo.nl</td>
      <td>johavanderberg[at]yahoo.nl</td>
      <td>johavanderberg@yahoo.nljohavanderberg@yahoo.nl</td>
      <td>ln.oohay@grebrednavahoj</td>
    </tr>
    <tr>
      <th>48</th>
      <td>49</td>
      <td>stanisław.wójcik@wp.pl</td>
      <td>STANISŁAW.WÓJCIK@WP.PL</td>
      <td>stanisław.wójcik@wp.pl</td>
      <td>stanisław.wójcik@wp.pl</td>
      <td>stanisław.wójcik@wp.pl</td>
      <td>stanisław.wójcik@wp.pl</td>
      <td>stanisław.wójcik[at]wp.pl</td>
      <td>stanisław.wójcik@wp.plstanisław.wójcik@wp.pl</td>
      <td>lp.pw@kicjów.wałsinats</td>
    </tr>
    <tr>
      <th>49</th>
      <td>50</td>
      <td>enrique_munoz@yahoo.es</td>
      <td>ENRIQUE_MUNOZ@YAHOO.ES</td>
      <td>enrique_munoz@yahoo.es</td>
      <td>enrique_munoz@yahoo.es</td>
      <td>enrique_munoz@yahoo.es</td>
      <td>enrique_munoz@yahoo.es</td>
      <td>enrique_munoz[at]yahoo.es</td>
      <td>enrique_munoz@yahoo.esenrique_munoz@yahoo.es</td>
      <td>se.oohay@zonum_euqirne</td>
    </tr>
    <tr>
      <th>50</th>
      <td>51</td>
      <td>joakim.johansson@yahoo.se</td>
      <td>JOAKIM.JOHANSSON@YAHOO.SE</td>
      <td>joakim.johansson@yahoo.se</td>
      <td>joakim.johansson@yahoo.se</td>
      <td>joakim.johansson@yahoo.se</td>
      <td>joakim.johansson@yahoo.se</td>
      <td>joakim.johansson[at]yahoo.se</td>
      <td>joakim.johansson@yahoo.sejoakim.johansson@yaho...</td>
      <td>es.oohay@nossnahoj.mikaoj</td>
    </tr>
    <tr>
      <th>51</th>
      <td>52</td>
      <td>emma_jones@hotmail.com</td>
      <td>EMMA_JONES@HOTMAIL.COM</td>
      <td>emma_jones@hotmail.com</td>
      <td>emma_jones@hotmail.com</td>
      <td>emma_jones@hotmail.com</td>
      <td>emma_jones@hotmail.com</td>
      <td>emma_jones[at]hotmail.com</td>
      <td>emma_jones@hotmail.comemma_jones@hotmail.com</td>
      <td>moc.liamtoh@senoj_amme</td>
    </tr>
    <tr>
      <th>52</th>
      <td>53</td>
      <td>phil.hughes@gmail.com</td>
      <td>PHIL.HUGHES@GMAIL.COM</td>
      <td>phil.hughes@gmail.com</td>
      <td>phil.hughes@gmail.com</td>
      <td>phil.hughes@gmail.com</td>
      <td>phil.hughes@gmail.com</td>
      <td>phil.hughes[at]gmail.com</td>
      <td>phil.hughes@gmail.comphil.hughes@gmail.com</td>
      <td>moc.liamg@sehguh.lihp</td>
    </tr>
    <tr>
      <th>53</th>
      <td>54</td>
      <td>steve.murray@yahoo.uk</td>
      <td>STEVE.MURRAY@YAHOO.UK</td>
      <td>steve.murray@yahoo.uk</td>
      <td>steve.murray@yahoo.uk</td>
      <td>steve.murray@yahoo.uk</td>
      <td>steve.murray@yahoo.uk</td>
      <td>steve.murray[at]yahoo.uk</td>
      <td>steve.murray@yahoo.uksteve.murray@yahoo.uk</td>
      <td>ku.oohay@yarrum.evets</td>
    </tr>
    <tr>
      <th>54</th>
      <td>55</td>
      <td>mark.taylor@yahoo.au</td>
      <td>MARK.TAYLOR@YAHOO.AU</td>
      <td>mark.taylor@yahoo.au</td>
      <td>mark.taylor@yahoo.au</td>
      <td>mark.taylor@yahoo.au</td>
      <td>mark.taylor@yahoo.au</td>
      <td>mark.taylor[at]yahoo.au</td>
      <td>mark.taylor@yahoo.aumark.taylor@yahoo.au</td>
      <td>ua.oohay@rolyat.kram</td>
    </tr>
    <tr>
      <th>55</th>
      <td>56</td>
      <td>diego.gutierrez@yahoo.ar</td>
      <td>DIEGO.GUTIERREZ@YAHOO.AR</td>
      <td>diego.gutierrez@yahoo.ar</td>
      <td>diego.gutierrez@yahoo.ar</td>
      <td>diego.gutierrez@yahoo.ar</td>
      <td>diego.gutierrez@yahoo.ar</td>
      <td>diego.gutierrez[at]yahoo.ar</td>
      <td>diego.gutierrez@yahoo.ardiego.gutierrez@yahoo.ar</td>
      <td>ra.oohay@zerreitug.ogeid</td>
    </tr>
    <tr>
      <th>56</th>
      <td>57</td>
      <td>luisrojas@yahoo.cl</td>
      <td>LUISROJAS@YAHOO.CL</td>
      <td>luisrojas@yahoo.cl</td>
      <td>luisrojas@yahoo.cl</td>
      <td>luisrojas@yahoo.cl</td>
      <td>luisrojas@yahoo.cl</td>
      <td>luisrojas[at]yahoo.cl</td>
      <td>luisrojas@yahoo.clluisrojas@yahoo.cl</td>
      <td>lc.oohay@sajorsiul</td>
    </tr>
    <tr>
      <th>57</th>
      <td>58</td>
      <td>manoj.pareek@rediff.com</td>
      <td>MANOJ.PAREEK@REDIFF.COM</td>
      <td>manoj.pareek@rediff.com</td>
      <td>manoj.pareek@rediff.com</td>
      <td>manoj.pareek@rediff.com</td>
      <td>manoj.pareek@rediff.com</td>
      <td>manoj.pareek[at]rediff.com</td>
      <td>manoj.pareek@rediff.commanoj.pareek@rediff.com</td>
      <td>moc.ffider@keerap.jonam</td>
    </tr>
    <tr>
      <th>58</th>
      <td>59</td>
      <td>puja_srivastava@yahoo.in</td>
      <td>PUJA_SRIVASTAVA@YAHOO.IN</td>
      <td>puja_srivastava@yahoo.in</td>
      <td>puja_srivastava@yahoo.in</td>
      <td>puja_srivastava@yahoo.in</td>
      <td>puja_srivastava@yahoo.in</td>
      <td>puja_srivastava[at]yahoo.in</td>
      <td>puja_srivastava@yahoo.inpuja_srivastava@yahoo.in</td>
      <td>ni.oohay@avatsavirs_ajup</td>
    </tr>
  </tbody>
</table>
</div>



## 4. SQL 中的日期时间类型数据运算

### (1) 日期时间的基本概念

首先，我们来介绍一下时间日期类型的数据：

- 时间日期在 SQL 中是一种特殊格式，类似于我们在 Python 中给大家拓展的 `datetime` 模块中的 `datetime` 对象
- 时间日期类型本质上来说就是时间戳，只不过展示出来是 `'YYYY-MM-DD HH:MM:SS.mmm'` 这种格式

在 SQL 中，获取当前时间可以有以下两个方法：

- `GETDATE()` 函数：返回当前的日期和时间，格式为 `'YYYY-MM-DD HH:MM:SS.mmm'`
- `CURRENT_TIMESTAMP` 关键字：返回当前的日期和时间，格式同样为 `'YYYY-MM-DD HH:MM:SS.mmm'`



```sql
%%sql
SELECT
    GETDATE() AS CurrentDateTime1,
    CURRENT_TIMESTAMP AS CurrentDateTime2
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
      <th>CurrentDateTime1</th>
      <th>CurrentDateTime2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2026-03-09 12:57:54.963</td>
      <td>2026-03-09 12:57:54.963</td>
    </tr>
  </tbody>
</table>
</div>



### (2) 日期时间的部分提取

日期时间的部分提取，指的是从一个日期时间类型的字段中提取出年、月、日、小时、分钟、秒等等这些部分来：

- 在 Azure SQL Database 中，我们使用 `DATEPART(part, date)` 函数来提取日期时间的部分，返回的都是整数形式

- 除此之外，还有一个 `DATENAME(part, date)` 函数也可以用来提取日期时间的部分，返回的都是字符串形式

- 这两个函数中，`part` 参数用来指定要提取的部分，常见的提取部分有：

| part | 等价缩写         | 描述        | 举例                                          | 备注                            |
|-----|--------------|-----------|---------------------------------------------|-------------------------------|
| `YEAR` | `yy` 或 `yyyy` | 提取年份      | `2024-12-31 10:12:30.567` 的年份部分是 `2024`     |                               |
| `QUARTER` | `qq` 或 `q`   | 提取季度      | `2024-12-31 10:12:30.567` 的季度部分是 `4`        |                               |
| `MONTH` | `mm` 或 `m`   | 提取月份      | `2024-12-31 10:12:30.567` 的月份部分是 `12`       |                               |
| `DAY` | `dd` 或 `d`   | 提取日       | `2024-12-31 10:12:30.567` 的日部分是 `31`        |                               |
| `DAYOFYEAR` | `dy` 或 `y`   | 提取一年中的第几天 | `2024-12-31 10:12:30.567` 的年份中的第几天部分是 `366` |                               |                    |
| `WEEK` | `wk` 或 `ww`  | 提取一年中的第几周 | `2024-12-31 10:12:30.567` 的年份中的第几周部分是 `1` | 国际惯例，一年中最后一周如果跨年了，那么它属于下一年第一周 |
| `WEEKDAY` |              | 提取星期几     | `2024-12-31` 是周二，但是函数会返回 `3`           | SQL Server 默认：`Sunday = 1`    |
| `HOUR` | `hh`         | 提取小时      | `2024-12-31 10:12:30.567` 的小时部分是 `10`  |                               |
| `MINUTE` | `mi` 或 `n`   | 提取分钟      | `2024-12-31 10:12:30.567` 的分钟部分是 `12`  |                               |
| `SECOND` | `ss` 或 `s`   | 提取秒       | `2024-12-31 10:12:30.567` 的秒部分是 `30`   |                               |
| `MILLISECOND` |     `ms`     |  提取毫秒     | `2024-12-31 10:12:30.567` 的毫秒部分是 `567` |                               |


我们在 `Invoice` 表中的 `InvoiceDate` 字段上提取日期时间的部分：

- 首先，我们来使用 `DATEPART` 函数来提取日期时间的部分，返回整数形式


```sql
%%sql
SELECT
    InvoiceId,
    InvoiceDate,
    DATEPART(YEAR, InvoiceDate) AS InvoiceYear, -- 提取年份
    DATEPART(MONTH, InvoiceDate) AS InvoiceMonth, -- 提取月份
    DATEPART(QUARTER, InvoiceDate) AS InvoiceQuarter, -- 提取季度
    DATEPART(WEEK, InvoiceDate) AS InvoiceWeek, -- 提取一年中的第几周
    DATEPART(WEEKDAY, InvoiceDate) AS InvoiceWeekday, -- 提取星期几
    DATEPART(DAY, InvoiceDate) AS InvoiceDay, -- 提取日
    DATEPART(HOUR, InvoiceDate) AS InvoiceHour, -- 提取小时
    DATEPART(MINUTE, InvoiceDate) AS InvoiceMinute, -- 提取分钟
    DATEPART(SECOND, InvoiceDate) AS InvoiceSecond, -- 提取秒
    DATEPART(MILLISECOND, InvoiceDate) AS InvoiceMillisecond -- 提取毫秒
FROM Invoice
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
      <th>InvoiceDate</th>
      <th>InvoiceYear</th>
      <th>InvoiceMonth</th>
      <th>InvoiceQuarter</th>
      <th>InvoiceWeek</th>
      <th>InvoiceWeekday</th>
      <th>InvoiceDay</th>
      <th>InvoiceHour</th>
      <th>InvoiceMinute</th>
      <th>InvoiceSecond</th>
      <th>InvoiceMillisecond</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>6</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2021-01-02 00:00:00.000</td>
      <td>2021</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>7</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2021-01-03 00:00:00.000</td>
      <td>2021</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2021-01-06 00:00:00.000</td>
      <td>2021</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>2021-01-11 00:00:00.000</td>
      <td>2021</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
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
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>407</th>
      <td>408</td>
      <td>2025-12-05 00:00:00.000</td>
      <td>2025</td>
      <td>12</td>
      <td>4</td>
      <td>49</td>
      <td>6</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>408</th>
      <td>409</td>
      <td>2025-12-06 00:00:00.000</td>
      <td>2025</td>
      <td>12</td>
      <td>4</td>
      <td>49</td>
      <td>7</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>409</th>
      <td>410</td>
      <td>2025-12-09 00:00:00.000</td>
      <td>2025</td>
      <td>12</td>
      <td>4</td>
      <td>50</td>
      <td>3</td>
      <td>9</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>410</th>
      <td>411</td>
      <td>2025-12-14 00:00:00.000</td>
      <td>2025</td>
      <td>12</td>
      <td>4</td>
      <td>51</td>
      <td>1</td>
      <td>14</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>411</th>
      <td>412</td>
      <td>2025-12-22 00:00:00.000</td>
      <td>2025</td>
      <td>12</td>
      <td>4</td>
      <td>52</td>
      <td>2</td>
      <td>22</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>412 rows × 12 columns</p>
</div>



- 接着，我们再来使用 `DATENAME` 函数来提取日期时间的部分，返回字符串形式


```sql
%%sql
SELECT
    InvoiceId,
    InvoiceDate,
    DATENAME(YEAR, InvoiceDate) AS InvoiceYear, -- 提取年份
    DATENAME(MONTH, InvoiceDate) AS InvoiceMonth, -- 提取月份
    DATENAME(QUARTER, InvoiceDate) AS InvoiceQuarter, -- 提取季度
    DATENAME(WEEK, InvoiceDate) AS InvoiceWeek, -- 提取一年中的第几周
    DATENAME(WEEKDAY, InvoiceDate) AS InvoiceWeekday, -- 提取星期几
    DATENAME(DAY, InvoiceDate) AS InvoiceDay, -- 提取日
    DATENAME(HOUR, InvoiceDate) AS InvoiceHour, -- 提取小时
    DATENAME(MINUTE, InvoiceDate) AS InvoiceMinute, -- 提取分钟
    DATENAME(SECOND, InvoiceDate) AS InvoiceSecond, -- 提取秒
    DATENAME(MILLISECOND, InvoiceDate) AS InvoiceMillisecond -- 提取毫秒
FROM Invoice
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
      <th>InvoiceDate</th>
      <th>InvoiceYear</th>
      <th>InvoiceMonth</th>
      <th>InvoiceQuarter</th>
      <th>InvoiceWeek</th>
      <th>InvoiceWeekday</th>
      <th>InvoiceDay</th>
      <th>InvoiceHour</th>
      <th>InvoiceMinute</th>
      <th>InvoiceSecond</th>
      <th>InvoiceMillisecond</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021</td>
      <td>January</td>
      <td>1</td>
      <td>1</td>
      <td>Friday</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2021-01-02 00:00:00.000</td>
      <td>2021</td>
      <td>January</td>
      <td>1</td>
      <td>1</td>
      <td>Saturday</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2021-01-03 00:00:00.000</td>
      <td>2021</td>
      <td>January</td>
      <td>1</td>
      <td>2</td>
      <td>Sunday</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2021-01-06 00:00:00.000</td>
      <td>2021</td>
      <td>January</td>
      <td>1</td>
      <td>2</td>
      <td>Wednesday</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>2021-01-11 00:00:00.000</td>
      <td>2021</td>
      <td>January</td>
      <td>1</td>
      <td>3</td>
      <td>Monday</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
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
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>407</th>
      <td>408</td>
      <td>2025-12-05 00:00:00.000</td>
      <td>2025</td>
      <td>December</td>
      <td>4</td>
      <td>49</td>
      <td>Friday</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>408</th>
      <td>409</td>
      <td>2025-12-06 00:00:00.000</td>
      <td>2025</td>
      <td>December</td>
      <td>4</td>
      <td>49</td>
      <td>Saturday</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>409</th>
      <td>410</td>
      <td>2025-12-09 00:00:00.000</td>
      <td>2025</td>
      <td>December</td>
      <td>4</td>
      <td>50</td>
      <td>Tuesday</td>
      <td>9</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>410</th>
      <td>411</td>
      <td>2025-12-14 00:00:00.000</td>
      <td>2025</td>
      <td>December</td>
      <td>4</td>
      <td>51</td>
      <td>Sunday</td>
      <td>14</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>411</th>
      <td>412</td>
      <td>2025-12-22 00:00:00.000</td>
      <td>2025</td>
      <td>December</td>
      <td>4</td>
      <td>52</td>
      <td>Monday</td>
      <td>22</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>412 rows × 12 columns</p>
</div>



### (3) 日期时间的组合

上面我们介绍了，可以将日期时间的部分提取出来，那么我们也可以根据部分来组合成一个新的日期时间。

在 Azure SQL Database 中，我们可以以下两个函数，将整数形式的日期时间部分组合成一个新的日期时间：

- `DATETIMEFROMPARTS(year, month, day, hour, minute, second, millisecond)` 来构成一个新的日期时间
- `DATEFROMPARTS(year, month, day)` 来构成一个新的日期，这个函数会将小时、分钟、秒和毫秒都设置为 0


这两个函数的一个常用情景就是重构日期时间，例如我们有一个日期时间 `2024-12-31 10:12:30.567`

- 我们如果想把它具体到日，那么我们就可以使用 `DATEFROMPARTS(DATEPART(YEAR, date), DATEPART(MONTH, date), DATEPART(DAY, date))` 来重构这个日期时间，这样就得到了 `2024-12-31 00:00:00.000` 这个日期时间
- 我们如果想把它具体到月，那么我们就可以使用 `DATEFROMPARTS(DATEPART(YEAR, date), DATEPART(MONTH, date), 1)` 来重构这个日期时间，这样就得到了 `2024-12-01 00:00:00.000` 这个日期时间

我们来在 `Invoice` 表中的 `InvoiceDate` 字段上使用 `DATETIMEFROMPARTS` 函数来进行日期时间的组合：


```sql
%%sql
SELECT
    InvoiceId,
    InvoiceDate,
    DATEFROMPARTS(DATEPART(YEAR, InvoiceDate), DATEPART(MONTH, InvoiceDate), DATEPART(DAY, InvoiceDate)) AS ReconstructedToDay, -- 重构到日
    DATEFROMPARTS(DATEPART(YEAR, InvoiceDate), DATEPART(MONTH, InvoiceDate), 1) AS ReconstructedToMonth -- 重构到月
FROM Invoice
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
      <th>InvoiceDate</th>
      <th>ReconstructedToDay</th>
      <th>ReconstructedToMonth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-01</td>
      <td>2021-01-01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2021-01-02 00:00:00.000</td>
      <td>2021-01-02</td>
      <td>2021-01-01</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2021-01-03 00:00:00.000</td>
      <td>2021-01-03</td>
      <td>2021-01-01</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2021-01-06 00:00:00.000</td>
      <td>2021-01-06</td>
      <td>2021-01-01</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>2021-01-11 00:00:00.000</td>
      <td>2021-01-11</td>
      <td>2021-01-01</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>407</th>
      <td>408</td>
      <td>2025-12-05 00:00:00.000</td>
      <td>2025-12-05</td>
      <td>2025-12-01</td>
    </tr>
    <tr>
      <th>408</th>
      <td>409</td>
      <td>2025-12-06 00:00:00.000</td>
      <td>2025-12-06</td>
      <td>2025-12-01</td>
    </tr>
    <tr>
      <th>409</th>
      <td>410</td>
      <td>2025-12-09 00:00:00.000</td>
      <td>2025-12-09</td>
      <td>2025-12-01</td>
    </tr>
    <tr>
      <th>410</th>
      <td>411</td>
      <td>2025-12-14 00:00:00.000</td>
      <td>2025-12-14</td>
      <td>2025-12-01</td>
    </tr>
    <tr>
      <th>411</th>
      <td>412</td>
      <td>2025-12-22 00:00:00.000</td>
      <td>2025-12-22</td>
      <td>2025-12-01</td>
    </tr>
  </tbody>
</table>
<p>412 rows × 4 columns</p>
</div>



### (4) 日期时间的颗粒度截断

上面我们提到，`DATEFROMPARTS` 和 `GETDATE` 这两个函数的一个常用情景就是重构日期时间，但是这种重构的方式太麻烦了，我们接下来介绍一个简单直白的方式来进行日期时间的重构，就是颗粒度截断。

日期时间的颗粒度截断，指的是将一个日期时间具体到某个颗粒度上进行截断，例如具体到年、月、日、小时等等：

- 它和日期时间的部分提取不同，例如 `2024-12-31 10:12:30.567` 这个日期时间：

    - 如果我们按照日的颗粒度进行截断，那么它的结果是 `2024-12-31 00:00:00.000` 它依然是一个日期时间类型的值
    - 如果我们提取日的部分，那么它的结果是 `31`

- 其实本质上来讲，就是在找一个日期时间的起始时间点

    - 例如 `2024-12-31 10:12:30.567` 这个日期时间，如果我们按照月的颗粒度进行截断，那么它的结果是 `2024-12-01 00:00:00.000`
    - 这个日期时间就是 `2024-12-31 10:12:30.567` 这个日期时间所在的月份的起始时间点

在 Azure SQL Database 中，我们可以使用 `DATETRUNC` 函数来进行日期时间的颗粒度截断，语法是 `DATETRUNC(part, date)`

- 这个函数返回的结果依然是一个日期时间类型的值
- 这个函数中 `part` 参数用来指定要截断的颗粒度，常见的颗粒度有：

| part | 等价缩写         | 描述        | 举例                                                            | 备注                   |
|-----|--------------|-----------|---------------------------------------------------------------|----------------------|
| `YEAR` | `yy` 或 `yyyy` | 按年截断      | `2024-12-31 10:12:30.567` 按年截断的结果是 `2024-01-01 00:00:00.000`  |                      |
| `QUARTER` | `qq` 或 `q`   | 按季度截断      | `2024-12-31 10:12:30.567` 按季度截断的结果是 `2024-10-01 00:00:00.000` |                      |
| `MONTH` | `mm` 或 `m`   | 按月截断      | `2024-12-31 10:12:30.567` 按月截断的结果是 `2024-12-01 00:00:00.000`  |                      |
| `WEEK` | `wk` 或 `ww`  | 按周截断      | `2024-12-31 10:12:30.567` 按周截断的结果是 `2024-12-29 00:00:00.000`  | SQL SERVER 中一周的起始是周日 |
| `DAY` | `dd` 或 `d`   | 按日截断       | `2024-12-31 10:12:30.567` 按日截断的结果是 `2024-12-31 00:00:00.000`  |                      |
| `HOUR` | `hh`         | 按小时截断      | `2024-12-31 10:12:30.567` 按小时截断的结果是 `2024-12-31 10:00:00.000` |                      |
| `MINUTE` | `mi` 或 `n`   | 按分钟截断      | `2024-12-31 10:12:30.567` 按分钟截断的结果是 `2024-12-31 10:12:00.000` |                      |
| `SECOND` | `ss` 或 `s`   | 按秒截断       | `2024-12-31 10:12:30.567` 按秒截断的结果是 `2024-12-31 10:12:30.000`  |                      |
| `MILLISECOND` |     `ms`     |  按毫秒截断     | `2024-12-31 10:12:30.567` 按毫秒截断的结果是 `2024-12-31 10:12:30.567` |                      |

我们接下来，在 `Invoice` 表中的 `InvoiceDate` 字段上使用 `DATETRUNC` 函数来进行日期时间的颗粒度截断：


```sql
%%sql
SELECT
    InvoiceId,
    InvoiceDate,
    DATETRUNC(YEAR, InvoiceDate) AS TruncatedToYear, -- 按年截断
    DATETRUNC(QUARTER, InvoiceDate) AS TruncatedToQuarter, -- 按季度截断
    DATETRUNC(MONTH, InvoiceDate) AS TruncatedToMonth, -- 按月截断
    DATETRUNC(WEEK, InvoiceDate) AS TruncatedToWeek, -- 按周截断
    DATETRUNC(DAY, InvoiceDate) AS TruncatedToDay, -- 按日截断
    DATETRUNC(HOUR, InvoiceDate) AS TruncatedToHour, -- 按小时截断
    DATETRUNC(MINUTE, InvoiceDate) AS TruncatedToMinute, -- 按分钟截断
    DATETRUNC(SECOND, InvoiceDate) AS TruncatedToSecond, -- 按秒截断
    DATETRUNC(MILLISECOND, InvoiceDate) AS TruncatedToMillisecond -- 按毫秒截断
FROM Invoice
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
      <th>InvoiceDate</th>
      <th>TruncatedToYear</th>
      <th>TruncatedToQuarter</th>
      <th>TruncatedToMonth</th>
      <th>TruncatedToWeek</th>
      <th>TruncatedToDay</th>
      <th>TruncatedToHour</th>
      <th>TruncatedToMinute</th>
      <th>TruncatedToSecond</th>
      <th>TruncatedToMillisecond</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2020-12-27 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2021-01-02 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2020-12-27 00:00:00.000</td>
      <td>2021-01-02 00:00:00.000</td>
      <td>2021-01-02 00:00:00.000</td>
      <td>2021-01-02 00:00:00.000</td>
      <td>2021-01-02 00:00:00.000</td>
      <td>2021-01-02 00:00:00.000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2021-01-03 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-03 00:00:00.000</td>
      <td>2021-01-03 00:00:00.000</td>
      <td>2021-01-03 00:00:00.000</td>
      <td>2021-01-03 00:00:00.000</td>
      <td>2021-01-03 00:00:00.000</td>
      <td>2021-01-03 00:00:00.000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2021-01-06 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-03 00:00:00.000</td>
      <td>2021-01-06 00:00:00.000</td>
      <td>2021-01-06 00:00:00.000</td>
      <td>2021-01-06 00:00:00.000</td>
      <td>2021-01-06 00:00:00.000</td>
      <td>2021-01-06 00:00:00.000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>2021-01-11 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-10 00:00:00.000</td>
      <td>2021-01-11 00:00:00.000</td>
      <td>2021-01-11 00:00:00.000</td>
      <td>2021-01-11 00:00:00.000</td>
      <td>2021-01-11 00:00:00.000</td>
      <td>2021-01-11 00:00:00.000</td>
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
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>407</th>
      <td>408</td>
      <td>2025-12-05 00:00:00.000</td>
      <td>2025-01-01 00:00:00.000</td>
      <td>2025-10-01 00:00:00.000</td>
      <td>2025-12-01 00:00:00.000</td>
      <td>2025-11-30 00:00:00.000</td>
      <td>2025-12-05 00:00:00.000</td>
      <td>2025-12-05 00:00:00.000</td>
      <td>2025-12-05 00:00:00.000</td>
      <td>2025-12-05 00:00:00.000</td>
      <td>2025-12-05 00:00:00.000</td>
    </tr>
    <tr>
      <th>408</th>
      <td>409</td>
      <td>2025-12-06 00:00:00.000</td>
      <td>2025-01-01 00:00:00.000</td>
      <td>2025-10-01 00:00:00.000</td>
      <td>2025-12-01 00:00:00.000</td>
      <td>2025-11-30 00:00:00.000</td>
      <td>2025-12-06 00:00:00.000</td>
      <td>2025-12-06 00:00:00.000</td>
      <td>2025-12-06 00:00:00.000</td>
      <td>2025-12-06 00:00:00.000</td>
      <td>2025-12-06 00:00:00.000</td>
    </tr>
    <tr>
      <th>409</th>
      <td>410</td>
      <td>2025-12-09 00:00:00.000</td>
      <td>2025-01-01 00:00:00.000</td>
      <td>2025-10-01 00:00:00.000</td>
      <td>2025-12-01 00:00:00.000</td>
      <td>2025-12-07 00:00:00.000</td>
      <td>2025-12-09 00:00:00.000</td>
      <td>2025-12-09 00:00:00.000</td>
      <td>2025-12-09 00:00:00.000</td>
      <td>2025-12-09 00:00:00.000</td>
      <td>2025-12-09 00:00:00.000</td>
    </tr>
    <tr>
      <th>410</th>
      <td>411</td>
      <td>2025-12-14 00:00:00.000</td>
      <td>2025-01-01 00:00:00.000</td>
      <td>2025-10-01 00:00:00.000</td>
      <td>2025-12-01 00:00:00.000</td>
      <td>2025-12-14 00:00:00.000</td>
      <td>2025-12-14 00:00:00.000</td>
      <td>2025-12-14 00:00:00.000</td>
      <td>2025-12-14 00:00:00.000</td>
      <td>2025-12-14 00:00:00.000</td>
      <td>2025-12-14 00:00:00.000</td>
    </tr>
    <tr>
      <th>411</th>
      <td>412</td>
      <td>2025-12-22 00:00:00.000</td>
      <td>2025-01-01 00:00:00.000</td>
      <td>2025-10-01 00:00:00.000</td>
      <td>2025-12-01 00:00:00.000</td>
      <td>2025-12-21 00:00:00.000</td>
      <td>2025-12-22 00:00:00.000</td>
      <td>2025-12-22 00:00:00.000</td>
      <td>2025-12-22 00:00:00.000</td>
      <td>2025-12-22 00:00:00.000</td>
      <td>2025-12-22 00:00:00.000</td>
    </tr>
  </tbody>
</table>
<p>412 rows × 11 columns</p>
</div>



### (5) 日期时间的加减运算

在 SQL 中，我们可以使用 `DATEADD(part, number, date)` 函数来对日期时间进行加减运算：

- 举一个具体的例子，假设我们有一个日期时间 `2024-12-31 10:12:30.567`：

    - 我们想要在这个日期时间的基础上加上 1 年，那么我们就可以使用 `DATEADD(YEAR, 1, '2024-12-31 10:12:30.567')` 来实现这个功能，这个函数会返回 `2025-12-31 10:12:30.567`
    - 如果在这个日期时间的基础上减去 2 个月，那么我们就可以使用 `DATEADD(MONTH, -2, '2024-12-31 10:12:30.567')` 来实现这个功能，这个函数会返回 `2024-10-31 10:12:30.567`

- 这个函数中 `part` 参数用来指定要加减的部分，常见的部分有：

| part | 等价缩写         | 描述        | 举例                                                            | 备注                   |
|-----|--------------|-----------|---------------------------------------------------------------|----------------------|
| `YEAR` | `yy` 或 `yyyy` | 按年加减      | `DATEADD(YEAR, 1, '2024-12-31 10:12:30.567')` 的结果是 `2025-12-31 10:12:30.567`  |                      |
| `QUARTER` | `qq` 或 `q`   | 按季度加减      | `DATEADD(QUARTER, -1, '2024-12-31 10:12:30.567')` 的结果是 `2024-09-30 10:12:30.567` |                      |
| `MONTH` | `mm` 或 `m`   | 按月加减      | `DATEADD(MONTH, 2, '2024-12-31 10:12:30.567')` 的结果是 `2025-02-28 10:12:30.567`  |                      |
| `WEEK` | `wk` 或 `ww`  | 按周加减      | `DATEADD(WEEK, -1, '2024-12-31 10:12:30.567')` 的结果是 `2024-12-24 10:12:30.567`  |  |
| `DAY` | `dd` 或 `d`   | 按日加减       | `DATEADD(DAY, 3, '2024-12-31 10:12:30.567')` 的结果是 `2025-01-03 10:12:30.567`  |                      |
| `HOUR` | `hh`         | 按小时加减      | `DATEADD(HOUR, -5, '2024-12-31 10:12:30.567')` 的结果是 `2024-12-31 05:12:30.567` |                      |
| `MINUTE` | `mi` 或 `n`   | 按分钟加减      | `DATEADD(MINUTE, 15, '2024-12-31 10:12:30.567') 的结果是 `2024-12-31 10:27:30.567` | |                      |
| `SECOND` | `ss` 或 `s`   | 按秒加减       | `DATEADD(SECOND, -30, '2024-12-31 10:12:30.567')` 的结果是 `2024-12-31 10:12:00.567`  |                      |
| `MILLISECOND` |     `ms`     |  按毫秒加减     | `DATEADD(MILLISECOND, 500, '2024-12-31 10:12:30.567')` 的结果是 `2024-12-31 10:12:31.067` |                      |

我们在 `Invoice` 表中的 `InvoiceDate` 字段上使用 `DATEADD` 函数来进行日期时间的加减运算：


```sql
%%sql
SELECT
    InvoiceId,
    InvoiceDate,
    DATEADD(YEAR, 1, InvoiceDate) AS NextYear, -- 在发票日期的基础上加上 1 年
    DATEADD(QUARTER, -1, InvoiceDate) AS PreviousQuarter, -- 在发票日期的基础上减去 1 个季度
    DATEADD(MONTH, 2, InvoiceDate) AS TwoMonthsLater, -- 在发票日期的基础上加上 2 个月
    DATEADD(WEEK, -1, InvoiceDate) AS OneWeekEarlier, -- 在发票日期的基础上减去 1 周
    DATEADD(DAY, 3, InvoiceDate) AS ThreeDaysLater, -- 在发票日期的基础上加上 3 天
    DATEADD(HOUR, -5, InvoiceDate) AS FiveHoursEarlier, -- 在发票日期的基础上减去 5 小时
    DATEADD(MINUTE, 15, InvoiceDate) AS FifteenMinutesLater, -- 在发票日期的基础上加上 15 分钟
    DATEADD(SECOND, -30, InvoiceDate) AS ThirtySecondsEarlier, -- 在发票日期的基础上减去 30 秒
    DATEADD(MILLISECOND, 500, InvoiceDate) AS FiveHundredMillisecondsLater -- 在发票日期的基础上加上 500 毫秒
FROM Invoice
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
      <th>InvoiceDate</th>
      <th>NextYear</th>
      <th>PreviousQuarter</th>
      <th>TwoMonthsLater</th>
      <th>OneWeekEarlier</th>
      <th>ThreeDaysLater</th>
      <th>FiveHoursEarlier</th>
      <th>FifteenMinutesLater</th>
      <th>ThirtySecondsEarlier</th>
      <th>FiveHundredMillisecondsLater</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2022-01-01 00:00:00.000</td>
      <td>2020-10-01 00:00:00.000</td>
      <td>2021-03-01 00:00:00.000</td>
      <td>2020-12-25 00:00:00.000</td>
      <td>2021-01-04 00:00:00.000</td>
      <td>2020-12-31 19:00:00.000</td>
      <td>2021-01-01 00:15:00.000</td>
      <td>2020-12-31 23:59:30.000</td>
      <td>2021-01-01 00:00:00.500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2021-01-02 00:00:00.000</td>
      <td>2022-01-02 00:00:00.000</td>
      <td>2020-10-02 00:00:00.000</td>
      <td>2021-03-02 00:00:00.000</td>
      <td>2020-12-26 00:00:00.000</td>
      <td>2021-01-05 00:00:00.000</td>
      <td>2021-01-01 19:00:00.000</td>
      <td>2021-01-02 00:15:00.000</td>
      <td>2021-01-01 23:59:30.000</td>
      <td>2021-01-02 00:00:00.500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2021-01-03 00:00:00.000</td>
      <td>2022-01-03 00:00:00.000</td>
      <td>2020-10-03 00:00:00.000</td>
      <td>2021-03-03 00:00:00.000</td>
      <td>2020-12-27 00:00:00.000</td>
      <td>2021-01-06 00:00:00.000</td>
      <td>2021-01-02 19:00:00.000</td>
      <td>2021-01-03 00:15:00.000</td>
      <td>2021-01-02 23:59:30.000</td>
      <td>2021-01-03 00:00:00.500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2021-01-06 00:00:00.000</td>
      <td>2022-01-06 00:00:00.000</td>
      <td>2020-10-06 00:00:00.000</td>
      <td>2021-03-06 00:00:00.000</td>
      <td>2020-12-30 00:00:00.000</td>
      <td>2021-01-09 00:00:00.000</td>
      <td>2021-01-05 19:00:00.000</td>
      <td>2021-01-06 00:15:00.000</td>
      <td>2021-01-05 23:59:30.000</td>
      <td>2021-01-06 00:00:00.500</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>2021-01-11 00:00:00.000</td>
      <td>2022-01-11 00:00:00.000</td>
      <td>2020-10-11 00:00:00.000</td>
      <td>2021-03-11 00:00:00.000</td>
      <td>2021-01-04 00:00:00.000</td>
      <td>2021-01-14 00:00:00.000</td>
      <td>2021-01-10 19:00:00.000</td>
      <td>2021-01-11 00:15:00.000</td>
      <td>2021-01-10 23:59:30.000</td>
      <td>2021-01-11 00:00:00.500</td>
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
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>407</th>
      <td>408</td>
      <td>2025-12-05 00:00:00.000</td>
      <td>2026-12-05 00:00:00.000</td>
      <td>2025-09-05 00:00:00.000</td>
      <td>2026-02-05 00:00:00.000</td>
      <td>2025-11-28 00:00:00.000</td>
      <td>2025-12-08 00:00:00.000</td>
      <td>2025-12-04 19:00:00.000</td>
      <td>2025-12-05 00:15:00.000</td>
      <td>2025-12-04 23:59:30.000</td>
      <td>2025-12-05 00:00:00.500</td>
    </tr>
    <tr>
      <th>408</th>
      <td>409</td>
      <td>2025-12-06 00:00:00.000</td>
      <td>2026-12-06 00:00:00.000</td>
      <td>2025-09-06 00:00:00.000</td>
      <td>2026-02-06 00:00:00.000</td>
      <td>2025-11-29 00:00:00.000</td>
      <td>2025-12-09 00:00:00.000</td>
      <td>2025-12-05 19:00:00.000</td>
      <td>2025-12-06 00:15:00.000</td>
      <td>2025-12-05 23:59:30.000</td>
      <td>2025-12-06 00:00:00.500</td>
    </tr>
    <tr>
      <th>409</th>
      <td>410</td>
      <td>2025-12-09 00:00:00.000</td>
      <td>2026-12-09 00:00:00.000</td>
      <td>2025-09-09 00:00:00.000</td>
      <td>2026-02-09 00:00:00.000</td>
      <td>2025-12-02 00:00:00.000</td>
      <td>2025-12-12 00:00:00.000</td>
      <td>2025-12-08 19:00:00.000</td>
      <td>2025-12-09 00:15:00.000</td>
      <td>2025-12-08 23:59:30.000</td>
      <td>2025-12-09 00:00:00.500</td>
    </tr>
    <tr>
      <th>410</th>
      <td>411</td>
      <td>2025-12-14 00:00:00.000</td>
      <td>2026-12-14 00:00:00.000</td>
      <td>2025-09-14 00:00:00.000</td>
      <td>2026-02-14 00:00:00.000</td>
      <td>2025-12-07 00:00:00.000</td>
      <td>2025-12-17 00:00:00.000</td>
      <td>2025-12-13 19:00:00.000</td>
      <td>2025-12-14 00:15:00.000</td>
      <td>2025-12-13 23:59:30.000</td>
      <td>2025-12-14 00:00:00.500</td>
    </tr>
    <tr>
      <th>411</th>
      <td>412</td>
      <td>2025-12-22 00:00:00.000</td>
      <td>2026-12-22 00:00:00.000</td>
      <td>2025-09-22 00:00:00.000</td>
      <td>2026-02-22 00:00:00.000</td>
      <td>2025-12-15 00:00:00.000</td>
      <td>2025-12-25 00:00:00.000</td>
      <td>2025-12-21 19:00:00.000</td>
      <td>2025-12-22 00:15:00.000</td>
      <td>2025-12-21 23:59:30.000</td>
      <td>2025-12-22 00:00:00.500</td>
    </tr>
  </tbody>
</table>
<p>412 rows × 11 columns</p>
</div>



### (6) 日期时间的差值计算

在 SQL 中，我们还可以使用 `DATEDIFF(part, start_date, end_date)` 函数来计算两个日期时间之间的差值：

- 这个函数会返回一个整数，表示 `start_date` 和 `end_date` 之间相差的 `part` 的数量
- 例如，假设我们有两个日期时间 `2024-12-31 10:12:30.567` 和 `2025-01-15 15:30:45.123`：

    - 如果我们想要计算这两个日期时间之间相差的天数，那么我们就可以使用 `DATEDIFF(DAY, '2024-12-31 10:12:30.567', '2025-01-15 15:30:45.123')` 来实现这个功能，这个函数会返回 `15`
    - 如果我们想要计算这两个日期时间之间相差的小时数，那么我们就可以使用 `DATEDIFF(HOUR, '2024-12-31 10:12:30.567', '2025-01-15 15:30:45.123')` 来实现这个功能，这个函数会返回 `375`

- 这个函数中 `part` 参数用来指定要计算差值的部分，常见的部分有：

| part | 等价缩写         | 描述        | 举例                                                            | 备注                   |
|-----|--------------|-----------|---------------------------------------------------------------|----------------------|
| `YEAR` | `yy` 或 `yyyy` | 按年计算差值      | `DATEDIFF(YEAR, '2024-12-31 10:12:30.567', '2025-01-15 15:30:45.123') 的结果是 `1`  |                      |
| `QUARTER` | `qq` 或 `q`   | 按季度计算差值      | `DATEDIFF(QUARTER, '2024-12-31 10:12:30.567', '2025-01-15 15:30:45.123')` 的结果是 `1` |                      |
| `MONTH` | `mm` 或 `m`   | 按月计算差值      | `DATEDIFF(MONTH, '2024-12-31 10:12:30.567', '2025-01-15 15:30:45.123')` 的结果是 `1`  |                      |
| `WEEK` | `wk` 或 `ww`  | 按周计算差值      | `DATEDIFF(WEEK, '2024-12-31 10:12:30.567', '2025-01-15 15:30:45.123')` 的结果 是 `2`  |  |
| `DAY` | `dd` 或 `d`   | 按日计算差值       | `DATEDIFF(DAY, '2024-12-31 10:12:30.567', '2025-01-15 15:30:45.123')` 的结果是 `15`  |                      |
| `HOUR` | `hh`         | 按小时计算差值      | `DATEDIFF(HOUR, '2024-12-31 10:12:30.567', '2025-01-15 15:30:45.123')` 的结果是 `375` |                      |
| `MINUTE` | `mi` 或 `n`   | 按分钟计算差值      | `DATEDIFF(MINUTE, '2024-12-31 10:12:30.567', '2025-01-15 15:30:45.123')` 的结果是 `22530` |                      |
| `SECOND` | `ss` 或 `s`   | 按秒计算差值       | `DATEDIFF(SECOND, '2024-12-31 10:12:30.567', '2025-01-15 15:30:45.123')` 的结果是 `1351800`  |                      |
| `MILLISECOND` |     `ms`     |   按毫秒计算差值     | `DATEDIFF(MILLISECOND, '2024-12-31 10:12:30.567', '2025-01-15 15:30:45.123')` 的结果是 `1351800567` |                      |

这里要注意一点：

- 首先，`DATEDIFF` 函数计算差值的时候，是先提取两个日期时间的 `part` 部分，然后再计算这两个部分之间的差值，例如：

    - 如果我们使用 `DATEDIFF(YEAR, '2024-12-31 10:12:30.567', '2025-01-15 15:30:45.123')` 来计算这两个日期时间之间相差的年数，那么它会先提取出这两个日期时间的年份部分，分别是 `2024` 和 `2025`，然后再计算这两个年份之间的差值，结果就是 `1`
    - 如果我们使用 `DATEDIFF(MONTH, '2024-12-31 10:12:30.567', '2025-01-15 15:30:45.123')` 来计算这两个日期时间之间相差的月数，那么它会先提取出这两个日期时间的月份部分，分别是 `12` 和 `1`，然后再计算这两个月份之间的差值，结果也是 `1`

- 其次，如果想算某个日期时间与当前时间之间的差值，那么我们就可以在 `DATEDIFF` 函数中直接使用 `GETDATE()` 来获取当前时间

我们来在 `Invoice` 表中的 `InvoiceDate` 字段上使用 `DATEDIFF` 函数来计算发票日期与当前日期之间的差值：


```sql
%%sql
SELECT
    InvoiceId,
    InvoiceDate,
    DATEDIFF(YEAR, InvoiceDate, GETDATE()) AS YearsSinceInvoice, -- 计算发票日期与当前日期之间相差的年数
    DATEDIFF(MONTH, InvoiceDate, GETDATE()) AS MonthsSinceInvoice, -- 计算发票日期与当前日期之间相差的月数
    DATEDIFF(DAY, InvoiceDate, GETDATE()) AS DaysSinceInvoice, -- 计算发票日期与当前日期之间相差的天数
    DATEDIFF(HOUR, InvoiceDate, GETDATE()) AS HoursSinceInvoice, -- 计算发票日期与当前日期之间相差的小时数
    DATEDIFF(MINUTE, InvoiceDate, GETDATE()) AS MinutesSinceInvoice, -- 计算发票日期与当前日期之间相差的分钟数
    DATEDIFF(SECOND, InvoiceDate, GETDATE()) AS SecondsSinceInvoice -- 计算发票日期与当前日期之间相差的秒数
FROM Invoice
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
      <th>InvoiceDate</th>
      <th>YearsSinceInvoice</th>
      <th>MonthsSinceInvoice</th>
      <th>DaysSinceInvoice</th>
      <th>HoursSinceInvoice</th>
      <th>MinutesSinceInvoice</th>
      <th>SecondsSinceInvoice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>5</td>
      <td>62</td>
      <td>1893</td>
      <td>45444</td>
      <td>2726697</td>
      <td>163601878</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2021-01-02 00:00:00.000</td>
      <td>5</td>
      <td>62</td>
      <td>1892</td>
      <td>45420</td>
      <td>2725257</td>
      <td>163515478</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2021-01-03 00:00:00.000</td>
      <td>5</td>
      <td>62</td>
      <td>1891</td>
      <td>45396</td>
      <td>2723817</td>
      <td>163429078</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2021-01-06 00:00:00.000</td>
      <td>5</td>
      <td>62</td>
      <td>1888</td>
      <td>45324</td>
      <td>2719497</td>
      <td>163169878</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>2021-01-11 00:00:00.000</td>
      <td>5</td>
      <td>62</td>
      <td>1883</td>
      <td>45204</td>
      <td>2712297</td>
      <td>162737878</td>
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
    </tr>
    <tr>
      <th>407</th>
      <td>408</td>
      <td>2025-12-05 00:00:00.000</td>
      <td>1</td>
      <td>3</td>
      <td>94</td>
      <td>2268</td>
      <td>136137</td>
      <td>8168278</td>
    </tr>
    <tr>
      <th>408</th>
      <td>409</td>
      <td>2025-12-06 00:00:00.000</td>
      <td>1</td>
      <td>3</td>
      <td>93</td>
      <td>2244</td>
      <td>134697</td>
      <td>8081878</td>
    </tr>
    <tr>
      <th>409</th>
      <td>410</td>
      <td>2025-12-09 00:00:00.000</td>
      <td>1</td>
      <td>3</td>
      <td>90</td>
      <td>2172</td>
      <td>130377</td>
      <td>7822678</td>
    </tr>
    <tr>
      <th>410</th>
      <td>411</td>
      <td>2025-12-14 00:00:00.000</td>
      <td>1</td>
      <td>3</td>
      <td>85</td>
      <td>2052</td>
      <td>123177</td>
      <td>7390678</td>
    </tr>
    <tr>
      <th>411</th>
      <td>412</td>
      <td>2025-12-22 00:00:00.000</td>
      <td>1</td>
      <td>3</td>
      <td>77</td>
      <td>1860</td>
      <td>111657</td>
      <td>6699478</td>
    </tr>
  </tbody>
</table>
<p>412 rows × 8 columns</p>
</div>



### (7) 日期时间的格式化

时间日期的格式化是指将一个日期时间类型的值转换成一个特定格式的字符串：

- 例如，我们有一个日期时间 `2024-12-31 10:12:30.567`，我们想要将它格式化成以下几种不同的字符串格式：

    - 如果我们想要将它格式化成 `'YYYY-MM-DD'` 的格式，那么我们就可以得到 `2024-12-31`
    - 如果我们想要将它格式化成 `'MM/DD/YYYY'` 的格式，那么我们就可以得到 `12/31/2024`
    - 如果我们想要将它格式化成 `'DD MMM YYYY'` 的格式，那么我们就可以得到 `31 Dec 2024`

- 在 Azure SQL Database 中，我们可以使用 `FORMAT(date, format_string)` 函数来进行日期时间的格式化

- 在 `format_string` 参数中，我们可以使用以下的一些格式化符号来指定我们想要的日期时间格式，我们拿 `2024-12-31 10:12:30.567` 这个日期时间来举例说明这些格式化符号的含义：

| 符号 | 含义     | 举例 | 备注 |
|-----|--------|------|------|
| `yyyy` | 四位数的年份 | `2024` | |
| `yy` | 两位数的年份 | `24` | |
| `MM` | 两位数的月份 | `12` | |
| `MMM` | 月份缩写   | `Dec` | |
| `MMMM` | 月份全称   | `December` | |
| `dd` | 两位数的日期 | `31` | |
| `ddd` | 星期缩写   | `Tue` | |
| `dddd` | 星期全称   | `Tuesday` | |
| `HH` | 两位数的小时（24 小时制） | `10` | |
| `hh` | 两位数的小时（12 小时制） |  `10` | |
| `mm` | 两位数的分钟 | `12` | |
| `ss` | 两位数的秒   | `30` | |
| `fff` | 三位数的毫秒 | `567` | |

我们在 `Invoice` 表中的 `InvoiceDate` 字段上使用 `FORMAT` 函数来进行日期时间的格式化：


```sql
%%sql
SELECT
    InvoiceId,
    InvoiceDate,
    FORMAT(InvoiceDate, 'yyyy-MM-dd') AS FormattedDate1, -- 将发票日期格式化成 'YYYY-MM-DD' 的格式
    FORMAT(InvoiceDate, 'MM/dd/yyyy') AS FormattedDate2, -- 将发票日期格式化成 'MM/DD/YYYY' 的格式
    FORMAT(InvoiceDate, 'dd MMM yyyy') AS FormattedDate3 -- 将发票日期格式化成 'DD MMM YYYY' 的格式
FROM Invoice
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
      <th>InvoiceDate</th>
      <th>FormattedDate1</th>
      <th>FormattedDate2</th>
      <th>FormattedDate3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2021-01-01 00:00:00.000</td>
      <td>2021-01-01</td>
      <td>01/01/2021</td>
      <td>01 Jan 2021</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2021-01-02 00:00:00.000</td>
      <td>2021-01-02</td>
      <td>01/02/2021</td>
      <td>02 Jan 2021</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2021-01-03 00:00:00.000</td>
      <td>2021-01-03</td>
      <td>01/03/2021</td>
      <td>03 Jan 2021</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2021-01-06 00:00:00.000</td>
      <td>2021-01-06</td>
      <td>01/06/2021</td>
      <td>06 Jan 2021</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>2021-01-11 00:00:00.000</td>
      <td>2021-01-11</td>
      <td>01/11/2021</td>
      <td>11 Jan 2021</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>407</th>
      <td>408</td>
      <td>2025-12-05 00:00:00.000</td>
      <td>2025-12-05</td>
      <td>12/05/2025</td>
      <td>05 Dec 2025</td>
    </tr>
    <tr>
      <th>408</th>
      <td>409</td>
      <td>2025-12-06 00:00:00.000</td>
      <td>2025-12-06</td>
      <td>12/06/2025</td>
      <td>06 Dec 2025</td>
    </tr>
    <tr>
      <th>409</th>
      <td>410</td>
      <td>2025-12-09 00:00:00.000</td>
      <td>2025-12-09</td>
      <td>12/09/2025</td>
      <td>09 Dec 2025</td>
    </tr>
    <tr>
      <th>410</th>
      <td>411</td>
      <td>2025-12-14 00:00:00.000</td>
      <td>2025-12-14</td>
      <td>12/14/2025</td>
      <td>14 Dec 2025</td>
    </tr>
    <tr>
      <th>411</th>
      <td>412</td>
      <td>2025-12-22 00:00:00.000</td>
      <td>2025-12-22</td>
      <td>12/22/2025</td>
      <td>22 Dec 2025</td>
    </tr>
  </tbody>
</table>
<p>412 rows × 5 columns</p>
</div>



### (8) 日期时间操作小结

到目前为止，我们已经介绍了 SQL 中的日期时间类型数据的各种操作，我们列个表做个总结：

| 操作类型 | 函数名称 | 描述 |
|---------|---------|------|
| 获取当前日期时间 | `GETDATE()` | 获取当前的日期和时间，格式为 `'YYYY-MM-DD HH:MM:SS.mmm'` |
| 获取当前日期时间 | `CURRENT_TIMESTAMP` | 获取当前的日期和时间，格式同样为 `'YYYY-MM-DD HH:MM:SS.mmm'` |
| 日期时间的部分提取 | `DATEPART(part, date)` | 从一个日期时间类型的字段中提取出年、月、日、小时、分钟、秒等等这些部分来，返回整数形式 |
| 日期时间的部分提取 | `DATENAME(part, date)` | 从一个日期时间类型的字段中提取出年、月、日、小时、分钟、秒等等这些部分来，返回字符串形式 |
| 日期时间的组合 | `DATEFROMPARTS(year, month, day)` | 将整数形式的日期时间部分组合成一个新的日期，这个函数会将小时、分钟、秒和毫秒 都设置为 0 |
| 日期时间的组合 | `DATETIMEFROMPARTS(year, month, day, hour, minute, second, millisecond)` | 将整数形式的日期时间部分组合成一个新的日期时间 |
| 日期时间的颗粒度截断 | `DATETRUNC(part, date)` | 将一个日期时间具体到某个颗粒度上进行截断，例如具体到年、月、日、小时等等 |
| 日期时间的加减运算 | `DATEADD(part, number, date)` | 对日期时间进行加减运算 |
| 日期时间的差值计算 | `DATEDIFF(part, start_date, end_date)` | 计算两个日期时间之间的差值 |
| 日期时间的格式化 | `FORMAT(date, format_string)` | 将一个日期时间类型的值转换成一个特定格式的字符串 |
