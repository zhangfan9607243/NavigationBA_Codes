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



```
|      | TrackId | UnitPrice | SqrtUnitPrice | LogUnitPrice | ExpUnitPrice | RoundedUnitPrice | CeilingUnitPrice | FloorUnitPrice |
|:-----|:--------|:----------|:--------------|:-------------|:-------------|:-----------------|:-----------------|:---------------|
| 0    | 1       | 0.99      | 0.994987      | -0.01005     | 2.691234     | 1.0              | 1                | 0              |
| 1    | 2       | 0.99      | 0.994987      | -0.01005     | 2.691234     | 1.0              | 1                | 0              |
| 2    | 3       | 0.99      | 0.994987      | -0.01005     | 2.691234     | 1.0              | 1                | 0              |
| 3    | 4       | 0.99      | 0.994987      | -0.01005     | 2.691234     | 1.0              | 1                | 0              |
| 4    | 5       | 0.99      | 0.994987      | -0.01005     | 2.691234     | 1.0              | 1                | 0              |
| 5    | 6       | 0.99      | 0.994987      | -0.01005     | 2.691234     | 1.0              | 1                | 0              |
| ...  | ...     | ...       | ...           | ...          | ...          | ...              | ...              | ...            |
| 3498 | 3499    | 0.99      | 0.994987      | -0.01005     | 2.691234     | 1.0              | 1                | 0              |
| 3499 | 3500    | 0.99      | 0.994987      | -0.01005     | 2.691234     | 1.0              | 1                | 0              |
| 3500 | 3501    | 0.99      | 0.994987      | -0.01005     | 2.691234     | 1.0              | 1                | 0              |
| 3501 | 3502    | 0.99      | 0.994987      | -0.01005     | 2.691234     | 1.0              | 1                | 0              |
| 3502 | 3503    | 0.99      | 0.994987      | -0.01005     | 2.691234     | 1.0              | 1                | 0              |
```


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

```
|      | TrackId | UnitPrice | PriceLevel |
|:-----|:--------|:----------|:-----------|
| 0    | 1       | 0.99      | Cheap      |
| 1    | 2       | 0.99      | Cheap      |
| 2    | 3       | 0.99      | Cheap      |
| 3    | 4       | 0.99      | Cheap      |
| 4    | 5       | 0.99      | Cheap      |
| 5    | 6       | 0.99      | Cheap      |
| ...  | ...     | ...       | ...        |
| 3499 | 3500    | 0.99      | Cheap      |
| 3500 | 3501    | 0.99      | Cheap      |
| 3501 | 3502    | 0.99      | Cheap      |
| 3502 | 3503    | 0.99      | Cheap      |
```


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



```
|     | InvoiceId | BillingCountry | IsEnglishSpeakingCountry |
|:----|:----------|:---------------|:-------------------------|
| 0   | 1         | Germany        | 0                        |
| 1   | 2         | Norway         | 0                        |
| 2   | 3         | Belgium        | 0                        |
| 3   | 4         | Canada         | 1                        |
| 4   | 5         | USA            | 1                        |
| 5   | 6         | Germany        | 0                        |
| ... | ...       | ...            | ...                      |
| 407 | 408       | USA            | 1                        |
| 408 | 409       | Canada         | 1                        |
| 409 | 410       | Portugal       | 0                        |
| 410 | 411       | Finland        | 0                        |
| 411 | 412       | India          | 0                        |
```



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



```
|      | TrackId | Milliseconds | TrackType |
|:-----|:--------|:-------------|:----------|
| 0    | 1       | 343719       | Long      |
| 1    | 2       | 342562       | Long      |
| 2    | 3       | 230619       | Medium    |
| 3    | 4       | 252051       | Medium    |
| 4    | 5       | 375418       | Long      |
| 5    | 6       | 205662       | Medium    |
| ...  | ...     | ...          | ...       |
| 3498 | 3499    | 286741       | Medium    |
| 3499 | 3500    | 139200       | Short     |
| 3500 | 3501    | 66639        | Short     |
| 3501 | 3502    | 221331       | Medium    |
| 3502 | 3503    | 206005       | Medium    |
```



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



```
|    | FirstName | LastName  | FirstNameLength | LastNameLength |
|:---|:----------|:----------|:----------------|:---------------|
| 0  | Andrew    | Adams     | 6               | 5              |
| 1  | Nancy     | Edwards   | 5               | 7              |
| 2  | Jane      | Peacock   | 4               | 7              |
| 3  | Margaret  | Park      | 8               | 4              |
| 4  | Steve     | Johnson   | 5               | 7              |
| 5  | Michael   | Mitchell  | 7               | 8              |
| 6  | Robert    | King      | 6               | 4              |
| 7  | Laura     | Callahan  | 5               | 8              |
```



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



```
|     | InvoiceId | BillingPostalCode | PostalCodePrefix |
|:----|:----------|:------------------|:-----------------|
| 0   | 1         | 70174             | 701              |
| 1   | 2         | 0171              | 017              |
| 2   | 3         | 1000              | 100              |
| 3   | 4         | T6G 2C7           | T6G              |
| 4   | 5         | 2113              | 211              |
| 5   | 6         | 60316             | 603              |
| ... | ...       | ...               | ...              |
| 407 | 408       | 53703             | 537              |
| 408 | 409       | M6J 1V1           | M6J              |
| 409 | 410       | NaN               | NaN              |
| 410 | 411       | 00530             | 005              |
| 411 | 412       | 110017            | 110              |
```



- 查询 `Customer` 表中的 `Company` 字段，并提取出公司名称的后 4 个字符作为新的字段 `CompanySuffix`：


```sql
%%sql
SELECT
    CustomerId,
    Company,
    RIGHT(Company, 4) AS CompanySuffix
FROM Customer
```



```
|     | CustomerId | Company                                          | CompanySuffix |
|:----|:-----------|:-------------------------------------------------|:--------------|
| 0   | 1          | Embraer - Empresa Brasileira de Aeronáutica S.A. | S.A.          |
| 1   | 2          | NaN                                              | NaN           |
| 2   | 3          | NaN                                              | NaN           |
| 3   | 4          | NaN                                              | NaN           |
| 4   | 5          | JetBrains s.r.o.                                 | r.o.          |
| 5   | 6          | NaN                                              | NaN           |
| ... | ...        | ...                                              | ...           |
| 54  | 55         | NaN                                              | NaN           |
| 55  | 56         | NaN                                              | NaN           |
| 56  | 57         | NaN                                              | NaN           |
| 57  | 58         | NaN                                              | NaN           |
| 58  | 59         | NaN                                              | NaN           |
```



- 查询 `Artist` 表中的 `Name` 字段，并提取出名字中的第 2 到第 4 个字符作为新的字段 `NameSubstring`：


```sql
%%sql
SELECT
    ArtistId,
    Name,
    SUBSTRING(Name, 2, 3) AS NameSubstring
FROM Artist
```



```
|     | ArtistId | Name                                                                               | NameSubstring |
|:----|:---------|:-----------------------------------------------------------------------------------|:--------------|
| 0   | 1        | AC/DC                                                                              | C/D           |
| 1   | 2        | Accept                                                                             | cce           |
| 2   | 3        | Aerosmith                                                                          | ero           |
| 3   | 4        | Alanis Morissette                                                                  | lan           |
| 4   | 5        | Alice In Chains                                                                    | lic           |
| 5   | 6        | Antônio Carlos Jobim                                                               | ntô           |
| ... | ...      | ...                                                                                | ...           |
| 270 | 271      | Mela Tenenbaum, Pro Musica Prague & Richard Kapp                                   | ela           |
| 271 | 272      | Emerson String Quartet                                                             | mer           |
| 272 | 273      | C. Monteverdi, Nigel Rogers - Chiaroscuro; London Baroque; London Cornett & Sackbu | . M           |
| 273 | 274      | Nash Ensemble                                                                      | ash           |
| 274 | 275      | Philip Glass Ensemble                                                              | hil           |
```



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



```
|     | CustomerId | Email                     | AtSymbolPosition |
|:----|:-----------|:--------------------------|:-----------------|
| 0   | 1          | luisg@embraer.com.br      | 6                |
| 1   | 2          | leonekohler@surfeu.de     | 12               |
| 2   | 3          | ftremblay@gmail.com       | 10               |
| 3   | 4          | bjorn.hansen@yahoo.no     | 13               |
| 4   | 5          | frantisekw@jetbrains.com  | 11               |
| 5   | 6          | hholy@gmail.com           | 6                |
| ... | ...        | ...                       | ...              |
| 54  | 55         | mark.taylor@yahoo.au      | 12               |
| 55  | 56         | diego.gutierrez@yahoo.ar  | 16               |
| 56  | 57         | luisrojas@yahoo.cl        | 10               |
| 57  | 58         | manoj.pareek@rediff.com   | 13               |
| 58  | 59         | puja\_srivastava@yahoo.in | 16               |
```



- 查询 `Customer` 表中的 `Email` 字段，并查找 "@gmail" 符号在邮箱地址中的位置，作为新的字段 `GmailPosition`：


```sql
%%sql
SELECT
    CustomerId,
    Email,
    CHARINDEX('@gmail', Email) AS GmailPosition
FROM Customer
```



```
|     | CustomerId | Email                     | GmailPosition |
|:----|:-----------|:--------------------------|:--------------|
| 0   | 1          | luisg@embraer.com.br      | 0             |
| 1   | 2          | leonekohler@surfeu.de     | 0             |
| 2   | 3          | ftremblay@gmail.com       | 10            |
| 3   | 4          | bjorn.hansen@yahoo.no     | 0             |
| 4   | 5          | frantisekw@jetbrains.com  | 0             |
| 5   | 6          | hholy@gmail.com           | 6             |
| ... | ...        | ...                       | ...           |
| 54  | 55         | mark.taylor@yahoo.au      | 0             |
| 55  | 56         | diego.gutierrez@yahoo.ar  | 0             |
| 56  | 57         | luisrojas@yahoo.cl        | 0             |
| 57  | 58         | manoj.pareek@rediff.com   | 0             |
| 58  | 59         | puja\_srivastava@yahoo.in | 0             |
```



- 接下来，我们和SUBSTRING 函数结合使用，提取出邮箱地址中的用户名（也就是 "@" 符号前面的部分）：


```sql
%%sql
SELECT
    CustomerId,
    Email,
    SUBSTRING(Email, 1, CHARINDEX('@', Email) - 1) AS Username -- 这里直接函数套用，和 Python 中的函数套用是一样的
FROM Customer
```



```
|     | CustomerId | Email                     | Username         |
|:----|:-----------|:--------------------------|:-----------------|
| 0   | 1          | luisg@embraer.com.br      | luisg            |
| 1   | 2          | leonekohler@surfeu.de     | leonekohler      |
| 2   | 3          | ftremblay@gmail.com       | ftremblay        |
| 3   | 4          | bjorn.hansen@yahoo.no     | bjorn.hansen     |
| 4   | 5          | frantisekw@jetbrains.com  | frantisekw       |
| 5   | 6          | hholy@gmail.com           | hholy            |
| ... | ...        | ...                       | ...              |
| 54  | 55         | mark.taylor@yahoo.au      | mark.taylor      |
| 55  | 56         | diego.gutierrez@yahoo.ar  | diego.gutierrez  |
| 56  | 57         | luisrojas@yahoo.cl        | luisrojas        |
| 57  | 58         | manoj.pareek@rediff.com   | manoj.pareek     |
| 58  | 59         | puja\_srivastava@yahoo.in | puja\_srivastava |
```



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



```
|     | CustomerId | Email                     | ComPosition |
|:----|:-----------|:--------------------------|:------------|
| 0   | 1          | luisg@embraer.com.br      | 0           |
| 1   | 2          | leonekohler@surfeu.de     | 0           |
| 2   | 3          | ftremblay@gmail.com       | 17          |
| 3   | 4          | bjorn.hansen@yahoo.no     | 0           |
| 4   | 5          | frantisekw@jetbrains.com  | 22          |
| 5   | 6          | hholy@gmail.com           | 13          |
| ... | ...        | ...                       | ...         |
| 54  | 55         | mark.taylor@yahoo.au      | 0           |
| 55  | 56         | diego.gutierrez@yahoo.ar  | 0           |
| 56  | 57         | luisrojas@yahoo.cl        | 0           |
| 57  | 58         | manoj.pareek@rediff.com   | 21          |
| 58  | 59         | puja\_srivastava@yahoo.in | 0           |
```



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



```
|     | CustomerId | Email                     | GmailPosition1 | GmailPosition2 |
|:----|:-----------|:--------------------------|:---------------|:---------------|
| 0   | 1          | luisg@embraer.com.br      | 0              | 0              |
| 1   | 2          | leonekohler@surfeu.de     | 0              | 0              |
| 2   | 3          | ftremblay@gmail.com       | 11             | 11             |
| 3   | 4          | bjorn.hansen@yahoo.no     | 0              | 0              |
| 4   | 5          | frantisekw@jetbrains.com  | 0              | 0              |
| 5   | 6          | hholy@gmail.com           | 7              | 7              |
| ... | ...        | ...                       | ...            | ...            |
| 54  | 55         | mark.taylor@yahoo.au      | 0              | 0              |
| 55  | 56         | diego.gutierrez@yahoo.ar  | 0              | 0              |
| 56  | 57         | luisrojas@yahoo.cl        | 0              | 0              |
| 57  | 58         | manoj.pareek@rediff.com   | 0              | 0              |
| 58  | 59         | puja\_srivastava@yahoo.in | 0              | 0              |
```



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



```
|    | EmployeeID | FullNameV1                        | FullNameV2                        | FullNameV3                        |
|:---|:-----------|:----------------------------------|:----------------------------------|:----------------------------------|
| 0  | 1          | General Manager Andrew Adams      | General Manager Andrew Adams      | General Manager Andrew Adams      |
| 1  | 2          | Sales Manager Nancy Edwards       | Sales Manager Nancy Edwards       | Sales Manager Nancy Edwards       |
| 2  | 3          | Sales Support Agent Jane Peacock  | Sales Support Agent Jane Peacock  | Sales Support Agent Jane Peacock  |
| 3  | 4          | Sales Support Agent Margaret Park | Sales Support Agent Margaret Park | Sales Support Agent Margaret Park |
| 4  | 5          | Sales Support Agent Steve Johnson | Sales Support Agent Steve Johnson | Sales Support Agent Steve Johnson |
| 5  | 6          | IT Manager Michael Mitchell       | IT Manager Michael Mitchell       | IT Manager Michael Mitchell       |
| 6  | 7          | IT Staff Robert King              | IT Staff Robert King              | IT Staff Robert King              |
| 7  | 8          | IT Staff Laura Callahan           | IT Staff Laura Callahan           | IT Staff Laura Callahan           |
```



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



```
|     | CustomerId | Email                     | UpperEmail                | LowerEmail                | LeftTrimmedEmail          | RightTrimmedEmail         | TrimmedEmail              | ReplacedEmail                  | ReplicatedEmail                                    | ReversedEmail             |
|:----|:-----------|:--------------------------|:--------------------------|:--------------------------|:--------------------------|:--------------------------|:--------------------------|:-------------------------------|:---------------------------------------------------|:--------------------------|
| 0   | 1          | luisg@embraer.com.br      | LUISG@EMBRAER.COM.BR      | luisg@embraer.com.br      | luisg@embraer.com.br      | luisg@embraer.com.br      | luisg@embraer.com.br      | luisg\[at\]embraer.com.br      | luisg@embraer.com.brluisg@embraer.com.br           | rb.moc.rearbme@gsiul      |
| 1   | 2          | leonekohler@surfeu.de     | LEONEKOHLER@SURFEU.DE     | leonekohler@surfeu.de     | leonekohler@surfeu.de     | leonekohler@surfeu.de     | leonekohler@surfeu.de     | leonekohler\[at\]surfeu.de     | leonekohler@surfeu.deleonekohler@surfeu.de         | ed.uefrus@relhokenoel     |
| 2   | 3          | ftremblay@gmail.com       | FTREMBLAY@GMAIL.COM       | ftremblay@gmail.com       | ftremblay@gmail.com       | ftremblay@gmail.com       | ftremblay@gmail.com       | ftremblay\[at\]gmail.com       | ftremblay@gmail.comftremblay@gmail.com             | moc.liamg@yalbmertf       |
| 3   | 4          | bjorn.hansen@yahoo.no     | BJORN.HANSEN@YAHOO.NO     | bjorn.hansen@yahoo.no     | bjorn.hansen@yahoo.no     | bjorn.hansen@yahoo.no     | bjorn.hansen@yahoo.no     | bjorn.hansen\[at\]yahoo.no     | bjorn.hansen@yahoo.nobjorn.hansen@yahoo.no         | on.oohay@nesnah.nrojb     |
| 4   | 5          | frantisekw@jetbrains.com  | FRANTISEKW@JETBRAINS.COM  | frantisekw@jetbrains.com  | frantisekw@jetbrains.com  | frantisekw@jetbrains.com  | frantisekw@jetbrains.com  | frantisekw\[at\]jetbrains.com  | frantisekw@jetbrains.comfrantisekw@jetbrains.com   | moc.sniarbtej@wkesitnarf  |
| 5   | 6          | hholy@gmail.com           | HHOLY@GMAIL.COM           | hholy@gmail.com           | hholy@gmail.com           | hholy@gmail.com           | hholy@gmail.com           | hholy\[at\]gmail.com           | hholy@gmail.comhholy@gmail.com                     | moc.liamg@ylohh           |
| ... | ...        | ...                       | ...                       | ...                       | ...                       | ...                       | ...                       | ...                            | ...                                                | ...                       |
| 54  | 55         | mark.taylor@yahoo.au      | MARK.TAYLOR@YAHOO.AU      | mark.taylor@yahoo.au      | mark.taylor@yahoo.au      | mark.taylor@yahoo.au      | mark.taylor@yahoo.au      | mark.taylor\[at\]yahoo.au      | mark.taylor@yahoo.aumark.taylor@yahoo.au           | ua.oohay@rolyat.kram      |
| 55  | 56         | diego.gutierrez@yahoo.ar  | DIEGO.GUTIERREZ@YAHOO.AR  | diego.gutierrez@yahoo.ar  | diego.gutierrez@yahoo.ar  | diego.gutierrez@yahoo.ar  | diego.gutierrez@yahoo.ar  | diego.gutierrez\[at\]yahoo.ar  | diego.gutierrez@yahoo.ardiego.gutierrez@yahoo.ar   | ra.oohay@zerreitug.ogeid  |
| 56  | 57         | luisrojas@yahoo.cl        | LUISROJAS@YAHOO.CL        | luisrojas@yahoo.cl        | luisrojas@yahoo.cl        | luisrojas@yahoo.cl        | luisrojas@yahoo.cl        | luisrojas\[at\]yahoo.cl        | luisrojas@yahoo.clluisrojas@yahoo.cl               | lc.oohay@sajorsiul        |
| 57  | 58         | manoj.pareek@rediff.com   | MANOJ.PAREEK@REDIFF.COM   | manoj.pareek@rediff.com   | manoj.pareek@rediff.com   | manoj.pareek@rediff.com   | manoj.pareek@rediff.com   | manoj.pareek\[at\]rediff.com   | manoj.pareek@rediff.commanoj.pareek@rediff.com     | moc.ffider@keerap.jonam   |
| 58  | 59         | puja\_srivastava@yahoo.in | PUJA\_SRIVASTAVA@YAHOO.IN | puja\_srivastava@yahoo.in | puja\_srivastava@yahoo.in | puja\_srivastava@yahoo.in | puja\_srivastava@yahoo.in | puja\_srivastava\[at\]yahoo.in | puja\_srivastava@yahoo.inpuja\_srivastava@yahoo.in | ni.oohay@avatsavirs\_ajup |
```



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



```
|     | CurrentDateTime1         | CurrentDateTime2        |
|:----|:-------------------------|:------------------------|
| 0   | 2026-03-11 03:07:30.820  | 2026-03-11 03:07:30.820 |
```



### (2) 日期时间的部分提取

日期时间的部分提取，指的是从一个日期时间类型的字段中提取出年、月、日、小时、分钟、秒等等这些部分来：

- 在 Azure SQL Database 中，我们使用 `DATEPART(part, date)` 函数来提取日期时间的部分，返回的都是整数形式

- 除此之外，还有一个 `DATENAME(part, date)` 函数也可以用来提取日期时间的部分，返回的都是字符串形式

- 这两个函数中，`part` 参数用来指定要提取的部分，常见的提取部分有：

| part           | 等价缩写             | 描述            | 举例                                          | 备注                            |
|----------------|------------------|---------------|---------------------------------------------|-------------------------------|
| `YEAR`         | `yy` 或 `yyyy`    | 提取年份          | `2024-12-31 10:12:30.567` 的年份部分是 `2024`     |                               |
| `QUARTER`      | `qq` 或 `q`       | 提取季度          | `2024-12-31 10:12:30.567` 的季度部分是 `4`        |                               |
| `MONTH`        | `mm` 或 `m`       | 提取月份          | `2024-12-31 10:12:30.567` 的月份部分是 `12`       |                               |
| `DAY`          | `dd` 或 `d`       | 提取日           | `2024-12-31 10:12:30.567` 的日部分是 `31`        |                               |
| `DAYOFYEAR`    | `dy` 或 `y`       | 提取一年中的第几天     | `2024-12-31 10:12:30.567` 的年份中的第几天部分是 `366` |                               |                    |
| `WEEK`         | `wk` 或 `ww`      | 提取一年中的第几周     | `2024-12-31 10:12:30.567` 的年份中的第几周部分是 `1`   | 国际惯例，一年中最后一周如果跨年了，那么它属于下一年第一周 |
| `WEEKDAY`      |                  | 提取星期几         | `2024-12-31` 是周二，但是函数会返回 `3`                | SQL Server 默认：`Sunday = 1`    |
| `HOUR`         | `hh`             | 提取小时          | `2024-12-31 10:12:30.567` 的小时部分是 `10`       |                               |
| `MINUTE`       | `mi` 或 `n`       | 提取分钟          | `2024-12-31 10:12:30.567` 的分钟部分是 `12`       |                               |
| `SECOND`       | `ss` 或 `s`       | 提取秒           | `2024-12-31 10:12:30.567` 的秒部分是 `30`        |                               |
| `MILLISECOND`  | `ms`             | 提取毫秒          | `2024-12-31 10:12:30.567` 的毫秒部分是 `567`      |                               |


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



```
|     | InvoiceId | InvoiceDate             | InvoiceYear | InvoiceMonth | InvoiceQuarter | InvoiceWeek | InvoiceWeekday | InvoiceDay | InvoiceHour | InvoiceMinute | InvoiceSecond | InvoiceMillisecond |
|:----|:----------|:------------------------|:------------|:-------------|:---------------|:------------|:---------------|:-----------|:------------|:--------------|:--------------|:-------------------|
| 0   | 1         | 2021-01-01 00:00:00.000 | 2021        | 1            | 1              | 1           | 6              | 1          | 0           | 0             | 0             | 0                  |
| 1   | 2         | 2021-01-02 00:00:00.000 | 2021        | 1            | 1              | 1           | 7              | 2          | 0           | 0             | 0             | 0                  |
| 2   | 3         | 2021-01-03 00:00:00.000 | 2021        | 1            | 1              | 2           | 1              | 3          | 0           | 0             | 0             | 0                  |
| 3   | 4         | 2021-01-06 00:00:00.000 | 2021        | 1            | 1              | 2           | 4              | 6          | 0           | 0             | 0             | 0                  |
| 4   | 5         | 2021-01-11 00:00:00.000 | 2021        | 1            | 1              | 3           | 2              | 11         | 0           | 0             | 0             | 0                  |
| 5   | 6         | 2021-01-19 00:00:00.000 | 2021        | 1            | 1              | 4           | 3              | 19         | 0           | 0             | 0             | 0                  |
| ... | ...       | ...                     | ...         | ...          | ...            | ...         | ...            | ...        | ...         | ...           | ...           | ...                |
| 407 | 408       | 2025-12-05 00:00:00.000 | 2025        | 12           | 4              | 49          | 6              | 5          | 0           | 0             | 0             | 0                  |
| 408 | 409       | 2025-12-06 00:00:00.000 | 2025        | 12           | 4              | 49          | 7              | 6          | 0           | 0             | 0             | 0                  |
| 409 | 410       | 2025-12-09 00:00:00.000 | 2025        | 12           | 4              | 50          | 3              | 9          | 0           | 0             | 0             | 0                  |
| 410 | 411       | 2025-12-14 00:00:00.000 | 2025        | 12           | 4              | 51          | 1              | 14         | 0           | 0             | 0             | 0                  |
| 411 | 412       | 2025-12-22 00:00:00.000 | 2025        | 12           | 4              | 52          | 2              | 22         | 0           | 0             | 0             | 0                  |
```


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



```
|     | InvoiceId | InvoiceDate             | InvoiceYear | InvoiceMonth | InvoiceQuarter | InvoiceWeek | InvoiceWeekday | InvoiceDay | InvoiceHour | InvoiceMinute | InvoiceSecond | InvoiceMillisecond |
|:----|:----------|:------------------------|:------------|:-------------|:---------------|:------------|:---------------|:-----------|:------------|:--------------|:--------------|:-------------------|
| 0   | 1         | 2021-01-01 00:00:00.000 | 2021        | January      | 1              | 1           | Friday         | 1          | 0           | 0             | 0             | 0                  |
| 1   | 2         | 2021-01-02 00:00:00.000 | 2021        | January      | 1              | 1           | Saturday       | 2          | 0           | 0             | 0             | 0                  |
| 2   | 3         | 2021-01-03 00:00:00.000 | 2021        | January      | 1              | 2           | Sunday         | 3          | 0           | 0             | 0             | 0                  |
| 3   | 4         | 2021-01-06 00:00:00.000 | 2021        | January      | 1              | 2           | Wednesday      | 6          | 0           | 0             | 0             | 0                  |
| 4   | 5         | 2021-01-11 00:00:00.000 | 2021        | January      | 1              | 3           | Monday         | 11         | 0           | 0             | 0             | 0                  |
| 5   | 6         | 2021-01-19 00:00:00.000 | 2021        | January      | 1              | 4           | Tuesday        | 19         | 0           | 0             | 0             | 0                  |
| ... | ...       | ...                     | ...         | ...     | ...            | ...         | ...            | ...        | ...         | ...           | ...           | ...                |
| 407 | 408       | 2025-12-05 00:00:00.000 | 2025        | December     | 4              | 49          | Friday         | 5          | 0           | 0             | 0             | 0                  |
| 408 | 409       | 2025-12-06 00:00:00.000 | 2025        | December     | 4              | 49          | Saturday       | 6          | 0           | 0             | 0             | 0                  |
| 409 | 410       | 2025-12-09 00:00:00.000 | 2025        | December     | 4              | 50          | Tuesday        | 9          | 0           | 0             | 0             | 0                  |
| 410 | 411       | 2025-12-14 00:00:00.000 | 2025        | December     | 4              | 51          | Sunday         | 14         | 0           | 0             | 0             | 0                  |
| 411 | 412       | 2025-12-22 00:00:00.000 | 2025        | December     | 4              | 52          | Monday         | 22         | 0           | 0             | 0             | 0                  |
```



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



```
|     | InvoiceId | InvoiceDate             | ReconstructedToDay | ReconstructedToMonth |
|:----|:----------|:------------------------|:-------------------|:---------------------|
| 0   | 1         | 2021-01-01 00:00:00.000 | 2021-01-01         | 2021-01-01           |
| 1   | 2         | 2021-01-02 00:00:00.000 | 2021-01-02         | 2021-01-01           |
| 2   | 3         | 2021-01-03 00:00:00.000 | 2021-01-03         | 2021-01-01           |
| 3   | 4         | 2021-01-06 00:00:00.000 | 2021-01-06         | 2021-01-01           |
| 4   | 5         | 2021-01-11 00:00:00.000 | 2021-01-11         | 2021-01-01           |
| 5   | 6         | 2021-01-19 00:00:00.000 | 2021-01-19         | 2021-01-01           |
| ... | ...       | ...                     | ...                | ...                  |
| 407 | 408       | 2025-12-05 00:00:00.000 | 2025-12-05         | 2025-12-01           |
| 408 | 409       | 2025-12-06 00:00:00.000 | 2025-12-06         | 2025-12-01           |
| 409 | 410       | 2025-12-09 00:00:00.000 | 2025-12-09         | 2025-12-01           |
| 410 | 411       | 2025-12-14 00:00:00.000 | 2025-12-14         | 2025-12-01           |
| 411 | 412       | 2025-12-22 00:00:00.000 | 2025-12-22         | 2025-12-01           |
```



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



```
|     | InvoiceId | InvoiceDate             | TruncatedToYear         | TruncatedToQuarter      | TruncatedToMonth        | TruncatedToWeek         | TruncatedToDay          | TruncatedToHour         | TruncatedToMinute       | TruncatedToSecond       | TruncatedToMillisecond  |
|:----|:----------|:------------------------|:------------------------|:------------------------|:------------------------|:------------------------|:------------------------|:------------------------|:------------------------|:------------------------|:------------------------|
| 0   | 1         | 2021-01-01 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-01 00:00:00.000 | 2020-12-27 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-01 00:00:00.000 |
| 1   | 2         | 2021-01-02 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-01 00:00:00.000 | 2020-12-27 00:00:00.000 | 2021-01-02 00:00:00.000 | 2021-01-02 00:00:00.000 | 2021-01-02 00:00:00.000 | 2021-01-02 00:00:00.000 | 2021-01-02 00:00:00.000 |
| 2   | 3         | 2021-01-03 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-03 00:00:00.000 | 2021-01-03 00:00:00.000 | 2021-01-03 00:00:00.000 | 2021-01-03 00:00:00.000 | 2021-01-03 00:00:00.000 | 2021-01-03 00:00:00.000 |
| 3   | 4         | 2021-01-06 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-03 00:00:00.000 | 2021-01-06 00:00:00.000 | 2021-01-06 00:00:00.000 | 2021-01-06 00:00:00.000 | 2021-01-06 00:00:00.000 | 2021-01-06 00:00:00.000 |
| 4   | 5         | 2021-01-11 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-10 00:00:00.000 | 2021-01-11 00:00:00.000 | 2021-01-11 00:00:00.000 | 2021-01-11 00:00:00.000 | 2021-01-11 00:00:00.000 | 2021-01-11 00:00:00.000 |
| 5   | 6         | 2021-01-19 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-01 00:00:00.000 | 2021-01-17 00:00:00.000 | 2021-01-19 00:00:00.000 | 2021-01-19 00:00:00.000 | 2021-01-19 00:00:00.000 | 2021-01-19 00:00:00.000 | 2021-01-19 00:00:00.000 |
| ... | ...       | ...                     | ...                     | ...                     | ...                     | ...                     | ...                     | ...                     | ...                     | ...                     | ...                     |
| 407 | 408       | 2025-12-05 00:00:00.000 | 2025-01-01 00:00:00.000 | 2025-10-01 00:00:00.000 | 2025-12-01 00:00:00.000 | 2025-11-30 00:00:00.000 | 2025-12-05 00:00:00.000 | 2025-12-05 00:00:00.000 | 2025-12-05 00:00:00.000 | 2025-12-05 00:00:00.000 | 2025-12-05 00:00:00.000 |
| 408 | 409       | 2025-12-06 00:00:00.000 | 2025-01-01 00:00:00.000 | 2025-10-01 00:00:00.000 | 2025-12-01 00:00:00.000 | 2025-11-30 00:00:00.000 | 2025-12-06 00:00:00.000 | 2025-12-06 00:00:00.000 | 2025-12-06 00:00:00.000 | 2025-12-06 00:00:00.000 | 2025-12-06 00:00:00.000 |
| 409 | 410       | 2025-12-09 00:00:00.000 | 2025-01-01 00:00:00.000 | 2025-10-01 00:00:00.000 | 2025-12-01 00:00:00.000 | 2025-12-07 00:00:00.000 | 2025-12-09 00:00:00.000 | 2025-12-09 00:00:00.000 | 2025-12-09 00:00:00.000 | 2025-12-09 00:00:00.000 | 2025-12-09 00:00:00.000 |
| 410 | 411       | 2025-12-14 00:00:00.000 | 2025-01-01 00:00:00.000 | 2025-10-01 00:00:00.000 | 2025-12-01 00:00:00.000 | 2025-12-14 00:00:00.000 | 2025-12-14 00:00:00.000 | 2025-12-14 00:00:00.000 | 2025-12-14 00:00:00.000 | 2025-12-14 00:00:00.000 | 2025-12-14 00:00:00.000 |
| 411 | 412       | 2025-12-22 00:00:00.000 | 2025-01-01 00:00:00.000 | 2025-10-01 00:00:00.000 | 2025-12-01 00:00:00.000 | 2025-12-21 00:00:00.000 | 2025-12-22 00:00:00.000 | 2025-12-22 00:00:00.000 | 2025-12-22 00:00:00.000 | 2025-12-22 00:00:00.000 | 2025-12-22 00:00:00.000 |
```



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



```
|     | InvoiceId | InvoiceDate             | NextYear                | PreviousQuarter         | TwoMonthsLater          | OneWeekEarlier          | ThreeDaysLater          | FiveHoursEarlier        | FifteenMinutesLater     | ThirtySecondsEarlier    | FiveHundredMillisecondsLater |
|:----|:----------|:------------------------|:------------------------|:------------------------|:------------------------|:------------------------|:------------------------|:------------------------|:------------------------|:------------------------|:-----------------------------|
| 0   | 1         | 2021-01-01 00:00:00.000 | 2022-01-01 00:00:00.000 | 2020-10-01 00:00:00.000 | 2021-03-01 00:00:00.000 | 2020-12-25 00:00:00.000 | 2021-01-04 00:00:00.000 | 2020-12-31 19:00:00.000 | 2021-01-01 00:15:00.000 | 2020-12-31 23:59:30.000 | 2021-01-01 00:00:00.500      |
| 1   | 2         | 2021-01-02 00:00:00.000 | 2022-01-02 00:00:00.000 | 2020-10-02 00:00:00.000 | 2021-03-02 00:00:00.000 | 2020-12-26 00:00:00.000 | 2021-01-05 00:00:00.000 | 2021-01-01 19:00:00.000 | 2021-01-02 00:15:00.000 | 2021-01-01 23:59:30.000 | 2021-01-02 00:00:00.500      |
| 2   | 3         | 2021-01-03 00:00:00.000 | 2022-01-03 00:00:00.000 | 2020-10-03 00:00:00.000 | 2021-03-03 00:00:00.000 | 2020-12-27 00:00:00.000 | 2021-01-06 00:00:00.000 | 2021-01-02 19:00:00.000 | 2021-01-03 00:15:00.000 | 2021-01-02 23:59:30.000 | 2021-01-03 00:00:00.500      |
| 3   | 4         | 2021-01-06 00:00:00.000 | 2022-01-06 00:00:00.000 | 2020-10-06 00:00:00.000 | 2021-03-06 00:00:00.000 | 2020-12-30 00:00:00.000 | 2021-01-09 00:00:00.000 | 2021-01-05 19:00:00.000 | 2021-01-06 00:15:00.000 | 2021-01-05 23:59:30.000 | 2021-01-06 00:00:00.500      |
| 4   | 5         | 2021-01-11 00:00:00.000 | 2022-01-11 00:00:00.000 | 2020-10-11 00:00:00.000 | 2021-03-11 00:00:00.000 | 2021-01-04 00:00:00.000 | 2021-01-14 00:00:00.000 | 2021-01-10 19:00:00.000 | 2021-01-11 00:15:00.000 | 2021-01-10 23:59:30.000 | 2021-01-11 00:00:00.500      |
| 5   | 6         | 2021-01-19 00:00:00.000 | 2022-01-19 00:00:00.000 | 2020-10-19 00:00:00.000 | 2021-03-19 00:00:00.000 | 2021-01-12 00:00:00.000 | 2021-01-22 00:00:00.000 | 2021-01-18 19:00:00.000 | 2021-01-19 00:15:00.000 | 2021-01-18 23:59:30.000 | 2021-01-19 00:00:00.500      |
| ... | ...       | ...                     | ...                     | ...                     | ...                     | ...                     | ...                     | ...                     | ...                     | ...                     | ...                          |
| 407 | 408       | 2025-12-05 00:00:00.000 | 2026-12-05 00:00:00.000 | 2025-09-05 00:00:00.000 | 2026-02-05 00:00:00.000 | 2025-11-28 00:00:00.000 | 2025-12-08 00:00:00.000 | 2025-12-04 19:00:00.000 | 2025-12-05 00:15:00.000 | 2025-12-04 23:59:30.000 | 2025-12-05 00:00:00.500      |
| 408 | 409       | 2025-12-06 00:00:00.000 | 2026-12-06 00:00:00.000 | 2025-09-06 00:00:00.000 | 2026-02-06 00:00:00.000 | 2025-11-29 00:00:00.000 | 2025-12-09 00:00:00.000 | 2025-12-05 19:00:00.000 | 2025-12-06 00:15:00.000 | 2025-12-05 23:59:30.000 | 2025-12-06 00:00:00.500      |
| 409 | 410       | 2025-12-09 00:00:00.000 | 2026-12-09 00:00:00.000 | 2025-09-09 00:00:00.000 | 2026-02-09 00:00:00.000 | 2025-12-02 00:00:00.000 | 2025-12-12 00:00:00.000 | 2025-12-08 19:00:00.000 | 2025-12-09 00:15:00.000 | 2025-12-08 23:59:30.000 | 2025-12-09 00:00:00.500      |
| 410 | 411       | 2025-12-14 00:00:00.000 | 2026-12-14 00:00:00.000 | 2025-09-14 00:00:00.000 | 2026-02-14 00:00:00.000 | 2025-12-07 00:00:00.000 | 2025-12-17 00:00:00.000 | 2025-12-13 19:00:00.000 | 2025-12-14 00:15:00.000 | 2025-12-13 23:59:30.000 | 2025-12-14 00:00:00.500      |
| 411 | 412       | 2025-12-22 00:00:00.000 | 2026-12-22 00:00:00.000 | 2025-09-22 00:00:00.000 | 2026-02-22 00:00:00.000 | 2025-12-15 00:00:00.000 | 2025-12-25 00:00:00.000 | 2025-12-21 19:00:00.000 | 2025-12-22 00:15:00.000 | 2025-12-21 23:59:30.000 | 2025-12-22 00:00:00.500      |
```



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



```
|     | InvoiceId | InvoiceDate             | YearsSinceInvoice | MonthsSinceInvoice | DaysSinceInvoice | HoursSinceInvoice | MinutesSinceInvoice | SecondsSinceInvoice |
|:----|:----------|:------------------------|:------------------|:-------------------|:-----------------|:------------------|:--------------------|:--------------------|
| 0   | 1         | 2021-01-01 00:00:00.000 | 5                 | 62                 | 1895             | 45483             | 2728987             | 163739254           |
| 1   | 2         | 2021-01-02 00:00:00.000 | 5                 | 62                 | 1894             | 45459             | 2727547             | 163652854           |
| 2   | 3         | 2021-01-03 00:00:00.000 | 5                 | 62                 | 1893             | 45435             | 2726107             | 163566454           |
| 3   | 4         | 2021-01-06 00:00:00.000 | 5                 | 62                 | 1890             | 45363             | 2721787             | 163307254           |
| 4   | 5         | 2021-01-11 00:00:00.000 | 5                 | 62                 | 1885             | 45243             | 2714587             | 162875254           |
| 5   | 6         | 2021-01-19 00:00:00.000 | 5                 | 62                 | 1877             | 45051             | 2703067             | 162184054           |
| ... | ...       | ...                     | ...               | ...                | ...              | ...               | ...                 | ...                 |
| 408 | 409       | 2025-12-06 00:00:00.000 | 1                 | 3                  | 95               | 2283              | 136987              | 8219254             |
| 409 | 410       | 2025-12-09 00:00:00.000 | 1                 | 3                  | 92               | 2211              | 132667              | 7960054             |
| 410 | 411       | 2025-12-14 00:00:00.000 | 1                 | 3                  | 87               | 2091              | 125467              | 7528054             |
| 411 | 412       | 2025-12-22 00:00:00.000 | 1                 | 3                  | 79               | 1899              | 113947              | 6836854             |
```



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


```
|      | InvoiceId | InvoiceDate             | FormattedDate1 | FormattedDate2 | FormattedDate3 |
|:-----|:----------|:------------------------|:---------------|:---------------|:---------------|
| 0    | 1         | 2021-01-01 00:00:00.000 | 2021-01-01     | 01/01/2021     | 01 Jan 2021    |
| 1    | 2         | 2021-01-02 00:00:00.000 | 2021-01-02     | 01/02/2021     | 02 Jan 2021    |
| 2    | 3         | 2021-01-03 00:00:00.000 | 2021-01-03     | 01/03/2021     | 03 Jan 2021    |
| 3    | 4         | 2021-01-06 00:00:00.000 | 2021-01-06     | 01/06/2021     | 06 Jan 2021    |
| 4    | 5         | 2021-01-11 00:00:00.000 | 2021-01-11     | 01/11/2021     | 11 Jan 2021    |
| 5    | 6         | 2021-01-19 00:00:00.000 | 2021-01-19     | 01/19/2021     | 19 Jan 2021    |
| ...  | ...       | ...                     | ...            | ...            | ...            |
| 407  | 408       | 2025-12-05 00:00:00.000 | 2025-12-05     | 12/05/2025     | 05 Dec 2025    |
| 408  | 409       | 2025-12-06 00:00:00.000 | 2025-12-06     | 12/06/2025     | 06 Dec 2025    |
| 409  | 410       | 2025-12-09 00:00:00.000 | 2025-12-09     | 12/09/2025     | 09 Dec 2025    |
| 410  | 411       | 2025-12-14 00:00:00.000 | 2025-12-14     | 12/14/2025     | 14 Dec 2025    |
| 411  | 412       | 2025-12-22 00:00:00.000 | 2025-12-22     | 12/22/2025     | 22 Dec 2025    |
```


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

## 5. SQL 中数据类型之间的转换

我们在学习 Python 时，一个重要的知识点便是数据类型之间的转换，这一点在 SQL 中也是可以做到的：

- SQL 中的数据类型之间的转换使用的是 `CAST` 函数，用法是 `CAST(expression AS data_type)`，其中 `expression` 是要转换的数据，`data_type` 是要转换成的数据类型
- 其中 `data_type` 参数是数据类型的关键字：

    - `INT` 表示整数类型
    - `FLOAT` 表示浮点数类型
    - `VARCHAR` 表示字符串类型
    - `DATETIME` 表示日期时间类型

目前，我们学习了三种 SQL 中的数据类型：数值类型、字符串类型和日期时间类型，这三种类型之间的转换场景其实是比较简单的：

- 数值和字符串之间的转换：

    - 基本上只能进行数值类型转换成字符串类型，字符串类型转换成数值类型的场景比较少见
    - 因为很多字符串是无法转换成数值的，例如 `Hello` 这个字符串是无法转换成数值的

- 日期时间与数值之间的转换：

    - 日期时间类型转换成数值类型，大多数需要使用到我们上面介绍的 `DATEPART` 函数，而不是使用 `CAST` 函数来实现
    - 数值类型转换成日期时间类型，也基本上使用我们上面介绍到的 `DATETIMEFROMPARTS` 与 `DATEFROMPARTS` 函数来实现，而不是使用 `CAST` 函数来实现

- 日期时间和字符串之间的转换：
    - 日期时间类型转换成字符串类型，大多数要是哟我们上面学到的 `FORMAT` 函数，而不是使用 `CAST` 函数来实现
    - 字符串类型转换成日期时间类型的场景比较固定，例如数据库中有一个记录时间的列，由于数据采集或处理的原因，这一列在数据库中并不是日期时间类型，而是字符串类型，例如 `'2024-12-31'`，这时候就需要将这个字符串转换成日期时间类型，这时候我们就可以使用 `CAST(column, AS DATETIME)` 来实现这个功能

综上，大家可以看到 `CAST` 函数在 SQL 中使用的场景是比较局限的，主要原因是 SQL 中的数据类型本身就不如 Python 中的数据类型丰富。

我们在 Chinook 数据库中来演示一下 SQL 中的数据类型之间的转换，只看以下数字转为字符串：


```sql
%%sql
SELECT
    EmployeeId,
    CONCAT(FirstName, ' ', LastName, ' ', CAST(DATEDIFF(YEAR, HireDate, GETDATE()) AS VARCHAR), ' Years') AS EmployeeInfo
FROM Employee
```



```
|     | EmployeeId | EmployeeInfo              |
|:----|:-----------|:--------------------------|
| 0   | 1          | Andrew Adams 24 Years     |
| 1   | 2          | Nancy Edwards 24 Years    |
| 2   | 3          | Jane Peacock 24 Years     |
| 3   | 4          | Margaret Park 23 Years    |
| 4   | 5          | Steve Johnson 23 Years    |
| 5   | 6          | Michael Mitchell 23 Years |
| 6   | 7          | Robert King 22 Years      |
| 7   | 8          | Laura Callahan 22 Years   |
```


