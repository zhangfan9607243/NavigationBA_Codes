# Topic 2.1 - SELECT 与 FROM 语句

## 1. SELECT 与 FROM 语句的基本语法

### (1) SELECT 与 FROM 语句的基础查询

在之前我们提到过：

- SQL 是查询关系型数据库的，而关系型数据库就可以理解为表格数据
- 在表格中最基础的查询，就是查询**哪个表的哪个列**，这就是 SQL 中的 `SELECT` 和 `FROM` 语句

`SELECT` 与 `FROM` 的基本语法如下：

- 在一个表中查询某一列：

```sql
SELECT
    列名
FROM 表名
```

- 在一个表中查询多列（注意查询多列要用逗号隔开，最后一个列名后面不加逗号）：

```sql
SELECT 列名1, 列名2, ...
FROM 表名
```

- 在一个表中查询所有列：

```sql
SELECT *
FROM 表名
```



在 Chinook 数据库中，我们来在 `Album` 表中进行查询：

- 查询 `Album` 表中的 `Title` 列：


```sql
%%sql
SELECT Title
FROM Album
```



```
|     | Title                                                          |
|:----|:---------------------------------------------------------------|
| 0   | For Those About To Rock We Salute You                          |
| 1   | Balls to the Wall                                              |
| 2   | Restless and Wild                                              |
| 3   | Let There Be Rock                                              |
| 4   | Big Ones                                                       |
| 5   | Jagged Little Pill                                             |
| ... | ...                                                            |
| 342 | Respighi:Pines of Rome                                         |
| 343 | Schubert: The Late String Quartets & String Quintet \(3 CD's\) |
| 344 | Monteverdi: L'Orfeo                                            |
| 345 | Mozart: Chamber Music                                          |
| 346 | Koyaanisqatsi \(Soundtrack from the Motion Picture\)           |
```



- 查询 `Album` 表中的 `Title` 和 `ArtistId` 列：


```sql
%%sql
SELECT Title, ArtistId
FROM Album
```



```
|     | Title                                                          | ArtistId |
|:----|:---------------------------------------------------------------|:---------|
| 0   | For Those About To Rock We Salute You                          | 1        |
| 1   | Balls to the Wall                                              | 2        |
| 2   | Restless and Wild                                              | 2        |
| 3   | Let There Be Rock                                              | 1        |
| 4   | Big Ones                                                       | 3        |
| 5   | Jagged Little Pill                                             | 4        |
| ... | ...                                                            | ...      |
| 342 | Respighi:Pines of Rome                                         | 226      |
| 343 | Schubert: The Late String Quartets & String Quintet \(3 CD's\) | 272      |
| 344 | Monteverdi: L'Orfeo                                            | 273      |
| 345 | Mozart: Chamber Music                                          | 274      |
| 346 | Koyaanisqatsi \(Soundtrack from the Motion Picture\)           | 275      |
```



- 查询 `Album` 表中的所有列：


```sql
%%sql
SELECT *
FROM Album
```



```
|     | AlbumId | Title                                                          | ArtistId |
|:----|:--------|:---------------------------------------------------------------|:---------|
| 0   | 1       | For Those About To Rock We Salute You                          | 1        |
| 1   | 2       | Balls to the Wall                                              | 2        |
| 2   | 3       | Restless and Wild                                              | 2        |
| 3   | 4       | Let There Be Rock                                              | 1        |
| 4   | 5       | Big Ones                                                       | 3        |
| 5   | 6       | Jagged Little Pill                                             | 4        |
| ... | ...     | ...                                                            | ...      |
| 342 | 343     | Respighi:Pines of Rome                                         | 226      |
| 343 | 344     | Schubert: The Late String Quartets & String Quintet \(3 CD's\) | 272      |
| 344 | 345     | Monteverdi: L'Orfeo                                            | 273      |
| 345 | 346     | Mozart: Chamber Music                                          | 274      |
| 346 | 347     | Koyaanisqatsi \(Soundtrack from the Motion Picture\)           | 275      |
```



SQL 不像 Python 一样：

- 大家知道 Python 有一个官方推荐的代码风格指南叫做 PEP 8
- SQL 并没有一个官方推荐的代码风格，只有一些民间或业界的代码风格指南，例如 [SQL Style Guide](https://www.sqlstyle.guide/)，而且严格遵守这些代码风格指南的程序员也不多，所以在 SQL 中我们经常会看到各种各样的代码风格
- 因此，我们本门课在写SQL的时候，会使用一种大部分人认可的简单清晰的代码风格，例如：

    - SQL 关键字（例如 `SELECT`、`FROM`）使用大写字母（也就是说关键字小写也行，大家可以自己尝试一下，但是数据库中的表名列名必须严格遵守大小写）
    - `SELECT` 中每一列单独占一行，并且列名和 `SELECT` 之间有一个缩进
    - `FROM` 与 `SELECT` 在同一缩进级别
    - 等等，我们在后续讲更多知识点的时候会继续介绍一些 SQL 的代码风格

根据我们上面介绍的 SQL 代码风格，我们来重新写一下上面三个查询：

- 查询 `Album` 表中的 `Title` 列：

```sql
SELECT
    Title
FROM Album
```

- 查询 `Album` 表中的 `Title` 和 `ArtistId` 列：

```sql
SELECT
    Title,
    ArtistId
FROM Album
```

- 查询 `Album` 表中的所有列：

```sql
SELECT
    *
FROM Album
```

### (2) SELECT 与 FROM 中为列和表起别名

在 SQL 中，我们可以使用 `AS` 为列和表起别名，这样在查询结果中显示的列名和表名就会是我们指定的别名，而不是原来的列名和表名。

- 为列起别名和为表起别名的语法如下

```sql
SELECT 列名1 AS 列别名1, 列名2 AS 列别名2, ...
FROM 表名 AS 表别名
```

- 在 SQL 中，还有一种写法，就是 `AS` 可以省略掉，直接写成：

```sql
SELECT 列名1 列别名1, 列名2 列别名2, ...
FROM 表名 表别名
```

- 但是大家要注意，虽然 `AS` 可以省略掉，但是一般业界的习惯还是加上 `AS`，这样代码更清晰易读

在 Chinook 数据库中，我们来在 `Album` 表中进行查询，并且为表名和列名起别名：

- 查询 `Album` 表中的 `Title` 列，并且为 `Title` 列起别名为 `Album_Title`，为 `Album` 表起别名为 `A`：


```sql
%%sql
SELECT
    Title AS Album_Title
FROM Album AS A
```



```
|     | Album\_Title                                                   |
|:----|:---------------------------------------------------------------|
| 0   | For Those About To Rock We Salute You                          |
| 1   | Balls to the Wall                                              |
| 2   | Restless and Wild                                              |
| 3   | Let There Be Rock                                              |
| 4   | Big Ones                                                       |
| 5   | Jagged Little Pill                                             |
| ... | ...                                                            |
| 342 | Respighi:Pines of Rome                                         |
| 343 | Schubert: The Late String Quartets & String Quintet \(3 CD's\) |
| 344 | Monteverdi: L'Orfeo                                            |
| 345 | Mozart: Chamber Music                                          |
| 346 | Koyaanisqatsi \(Soundtrack from the Motion Picture\)           |
```



- 查询 `Album` 表中的 `Title` 和 `ArtistId` 列，并且为 `Title` 列起别名为 `Album_Title`，为 `ArtistId` 列起别名为 `Artist_ID`，为 `Album` 表起别名为 `A`：


```sql
%%sql
SELECT
    Title AS Album_Title,
    ArtistId AS Artist_ID
FROM Album AS A
```



```
|     | Album\_Title                                                   | Artist\_ID |
|:----|:---------------------------------------------------------------|:-----------|
| 0   | For Those About To Rock We Salute You                          | 1          |
| 1   | Balls to the Wall                                              | 2          |
| 2   | Restless and Wild                                              | 2          |
| 3   | Let There Be Rock                                              | 1          |
| 4   | Big Ones                                                       | 3          |
| 5   | Jagged Little Pill                                             | 4          |
| ... | ...                                                            | ...        |
| 342 | Respighi:Pines of Rome                                         | 226        |
| 343 | Schubert: The Late String Quartets & String Quintet \(3 CD's\) | 272        |
| 344 | Monteverdi: L'Orfeo                                            | 273        |
| 345 | Mozart: Chamber Music                                          | 274        |
| 346 | Koyaanisqatsi \(Soundtrack from the Motion Picture\)           | 275        |
```



## 2. 去重查询

### (1) 去重查询的概念

在 SQL 中，去重查询是指在查询结果中去掉重复的行，也就是说在查询结果中只保留不同的行。

这里，同学们可能会有一个疑问：

- 关系型数据库的一个重要特征就是表格中的每一行都是唯一的，也就是说在一个表中是不会有完全重复的行的，那么为什么还需要去重查询呢？
- 那是因为一个表中，当我们把所有列都查询出来的时候，每一行的确是唯一的
- 但是当我们只查询表中的某一列或者某几列的时候，就有可能会有重复的结果，因为不同的行在这些列上的值可能是相同的

我们来看以下这个例子：

- 假设我们有以下这张客户信息表：

<div style="text-align: center;">
    <img src="../截屏2026-03-09 15.02.39.png" width="400">
</div>

- 在这张表中，当我们把 `Customer ID`、`City`、`Country` 这三列都查询出来的时候，每一行都是唯一的
- 但是如果我们只查询 `City` 这一列的时候，就会有重复的结果：

<div style="text-align: center;">
    <img src="../截屏2026-03-09 15.06.25.png" width="100">
</div>

- 对 `City` 列进行去重查询之后，就只保留了不同的城市：

<div style="text-align: center;">
    <img src="../截屏2026-03-09 15.06.45.png" width="100">
</div>

- 同样，如果我们查询 `Country` 列的时候，也会有重复的结果：

<div style="text-align: center;">
    <img src="../截屏2026-03-09 15.10.00.png" width="100">
</div>

- 对 `Country` 列进行去重查询之后，就只保留了不同的国家：

<div style="text-align: center;">
    <img src="../截屏2026-03-09 15.10.05.png" width="100">
</div>

当然，去重查询也可以对多列进行去重查询：

- 当我们查询 `City` 和 `Country` 两列的时候，就会有重复的结果：

<div style="text-align: center;">
    <img src="../截屏2026-03-09 15.12.32.png" width="200">
</div>

- 对 `City` 和 `Country` 两列进行去重查询：

<div style="text-align: center;">
    <img src="../截屏2026-03-09 15.12.37.png" width="200">
</div>

当然，如果我们选择查询两列或多列，那么这两列或多列要去重的话就得同时去重，否则就会出现无法匹配的情况：

- 例如我们决定查询 `City` 和 `Country` 两列，并且只对 `Country` 列进行去重查询，那么就会出现以下这种情况：

<div style="text-align: center;">
    <img src="../截屏2026-03-09 15.18.11.png" width="300">
</div>

- 这种情况下，`City` 查询出 6 行，但是 `Country` 只查询出 2 行，这样就无法匹配了，这个在 SQL 中是不允许的
- 因此，在 SQL 中，如果我们查询多列，那么这些列要么都去重，要么都不去重，不能只对其中的某一列进行去重查询

### (2) SQL 中的去重查询
在 SQL 中，我们可以在 `SELECT` 关键字后面加上 `DISTINCT` 关键字来进行去重查询，也就是说在查询结果中去掉重复的行。

我们在 `Chinnok` 中来看这样一个例子：

- 我们先来看一个会有重复结果的查询：在销售表中查询 `CustomerId` 列：


```sql
%%sql
SELECT
    CustomerId
FROM Invoice
```



```
|     | CustomerId |
|:----|:-----------|
| 0   | 1          |
| 1   | 1          |
| 2   | 1          |
| 3   | 1          |
| 4   | 1          |
| 5   | 1          |
| ... | ...        |
| 407 | 59         |
| 408 | 59         |
| 409 | 59         |
| 410 | 59         |
| 411 | 59         |
```



- 可以看到，在 `Invoice` 表中，`CustomerId` 列有很多重复的值，因为每一条数据其实就是对应一个订单，而一个客户可能会有多个订单，所以在 `CustomerId` 列中就会有重复的值
- 因此，如果我们想要查询 `Invoice` 表中有多少不同的客户，那么我们就可以使用 `DISTINCT` 关键字来进行去重查询：


```sql
%%sql
SELECT DISTINCT
    CustomerId
FROM Invoice
```



```
|     | CustomerId |
|:----|:-----------|
| 0   | 1          |
| 1   | 2          |
| 2   | 3          |
| 3   | 4          |
| 4   | 5          |
| 5   | 6          |
| ... | ...        |
| 54  | 55         |
| 55  | 56         |
| 56  | 57         |
| 57  | 58         |
| 58  | 59         |
```



- 此时，我们就得到了 `Invoice` 表中所有不同的客户的 `CustomerId`，就不存在重复值了

当然，我们还可以对多列进行去重查询：

- 例如查询 `Invoice` 表中每个顾客的账单国家：


```sql
%%sql
SELECT DISTINCT
    CustomerId,
    BillingCountry
FROM Invoice
```



```
|     | CustomerId | BillingCountry |
|:----|:-----------|:---------------|
| 0   | 1          | Brazil         |
| 1   | 2          | Germany        |
| 2   | 3          | Canada         |
| 3   | 4          | Norway         |
| 4   | 5          | Czech Republic |
| 5   | 6          | Czech Republic |
| ... | ...        | ...            |
| 54  | 55         | Australia      |
| 55  | 56         | Argentina      |
| 56  | 57         | Chile          |
| 57  | 58         | India          |
| 58  | 59         | India          |
```



- 再比如，查询 `Invoice` 表中每个顾客的账单国家和账单邮编：


```sql
%%sql
SELECT DISTINCT
    CustomerId,
    BillingCountry,
    BillingPostalCode
FROM Invoice
```



```
|     | CustomerId | BillingCountry | BillingPostalCode |
|:----|:-----------|:---------------|:------------------|
| 0   | 1          | Brazil         | 12227-000         |
| 1   | 2          | Germany        | 70174             |
| 2   | 3          | Canada         | H2G 1A7           |
| 3   | 4          | Norway         | 0171              |
| 4   | 5          | Czech Republic | 14700             |
| 5   | 6          | Czech Republic | 14300             |
| ... | ...        | ...            | ...               |
| 54  | 55         | Australia      | 2010              |
| 55  | 56         | Argentina      | 1106              |
| 56  | 57         | Chile          | NaN               |
| 57  | 58         | India          | 110017            |
| 58  | 59         | India          | 560001            |
```



## 3. SQL 中的注释

和 Python 一样，SQL 中也可以添加单行注释和多行注释：

- 单行注释：使用 `--` 来表示单行注释，`--` 后面的内容都会被视为注释，直到行尾结束
- 多行注释：使用 `/*` 和 `*/` 来表示多行注释，`/*` 和 `*/` 之间的内容都会被视为注释，可以跨越多行

我们来看一下在 SQL 中添加注释的例子：


```sql
%%sql
/*
以下是一个查询 Album 表中 Title 和 ArtistId 列的 SQL 查询语句
其中：
- SELECT 关键字用于指定要查询的列，这里我们查询 Title 和 ArtistId
- FROM 关键字用于指定要查询的表，这里我们查询 Album 表
*/
SELECT
    Title, -- 专辑标题
    ArtistId -- 歌手ID
-- 从 Album 表中查询
FROM Album
```

```
|     | Title                                                          | ArtistId |
|:----|:---------------------------------------------------------------|:---------|
| 0   | For Those About To Rock We Salute You                          | 1        |
| 1   | Balls to the Wall                                              | 2        |
| 2   | Restless and Wild                                              | 2        |
| 3   | Let There Be Rock                                              | 1        |
| 4   | Big Ones                                                       | 3        |
| 5   | Jagged Little Pill                                             | 4        |
| ... | ...                                                            | ...      |
| 342 | Respighi:Pines of Rome                                         | 226      |
| 343 | Schubert: The Late String Quartets & String Quintet \(3 CD's\) | 272      |
| 344 | Monteverdi: L'Orfeo                                            | 273      |
| 345 | Mozart: Chamber Music                                          | 274      |
| 346 | Koyaanisqatsi \(Soundtrack from the Motion Picture\)           | 275      |
```


## 4. SELECT 语句中的特殊操作

### (1) SELECT 语句中的计算

在 SQL 中，SELECT 语句中不仅可以提取表中列的原始数据，还可以对这些数据进行各种计算，计算的结果会作为查询结果的一部分返回。

比方说，我们可以在 `SELECT` 语句中对数值列进行加减乘除等各种计算：

- 加法符号：`+`
- 减法符号：`-`
- 乘法符号：`*`
- 除法符号：`/`
- 乘方符号：`^`（有些数据库使用 `POWER` 函数来进行乘方运算，例如 `POWER(2, 3)` 表示 2 的 3 次方，等同于 `2 ^ 3`）

并且注意，这些运算符号的优先级和大家在 Python 中学到的数学运算符的优先级是一样的，强调优先级可以使用括号 `()` 来改变运算的顺序。

我们在 `Chinnok` 数据库中来看一些例子：

- 例如，我们可以在 `Track` 表中将 `UnitPrice` 列中的价格增加 10%：


```sql
%%sql
SELECT
    TrackId,
    UnitPrice,
    UnitPrice * 1.1 AS NewPrice -- 新价格
FROM Track
```



```
|     | Title                                                          | ArtistId |
|:----|:---------------------------------------------------------------|:---------|
| 0   | For Those About To Rock We Salute You                          | 1        |
| 1   | Balls to the Wall                                              | 2        |
| 2   | Restless and Wild                                              | 2        |
| 3   | Let There Be Rock                                              | 1        |
| 4   | Big Ones                                                       | 3        |
| 5   | Jagged Little Pill                                             | 4        |
| ... | ...                                                            | ...      |
| 342 | Respighi:Pines of Rome                                         | 226      |
| 343 | Schubert: The Late String Quartets & String Quintet \(3 CD's\) | 272      |
| 344 | Monteverdi: L'Orfeo                                            | 273      |
| 345 | Mozart: Chamber Music                                          | 274      |
| 346 | Koyaanisqatsi \(Soundtrack from the Motion Picture\)           | 275      |
```



- 例如，我们要在销售表中计算每笔订单中每首歌的总价：


```sql
%%sql
SELECT
    InvoiceId,
    TrackId,
    UnitPrice * Quantity AS TotalPrice -- 总价
FROM InvoiceLine
```



```
|      | InvoiceId | TrackId | TotalPrice |
|:-----|:----------|:--------|:-----------|
| 0    | 1         | 2       | 0.99       |
| 1    | 1         | 4       | 0.99       |
| 2    | 2         | 6       | 0.99       |
| 3    | 2         | 8       | 0.99       |
| 4    | 2         | 10      | 0.99       |
| 5    | 2         | 12      | 0.99       |
| ...  | ...       | ...     | ...        |
| 2235 | 411       | 3136    | 0.99       |
| 2236 | 411       | 3145    | 0.99       |
| 2237 | 411       | 3154    | 0.99       |
| 2238 | 411       | 3163    | 0.99       |
| 2239 | 412       | 3177    | 1.99       |
```



- 例如，我们算一下每首歌一秒钟的价格（虽然现实意义不大，但是不妨碍我们可以这样计算）：


```sql
%%sql
SELECT
    TrackId,
    UnitPrice / Milliseconds * 1000 AS PricePerSecond
FROM Track
```



```
|      | TrackId | PricePerSecond |
|:-----|:--------|:---------------|
| 0    | 1       | 0.002880       |
| 1    | 2       | 0.002890       |
| 2    | 3       | 0.004293       |
| 3    | 4       | 0.003928       |
| 4    | 5       | 0.002637       |
| 5    | 6       | 0.004814       |
| ...  | ...     | ...            |
| 3498 | 3499    | 0.003453       |
| 3499 | 3500    | 0.007112       |
| 3500 | 3501    | 0.014856       |
| 3501 | 3502    | 0.004473       |
| 3502 | 3503    | 0.004806       |
```



通过上面的例子，我们可以看出列计算的一些特点：

- 首先，我们使用 `UnitPrice` 与 `Quantity` 来计算每首歌的总价，但是 `UnitPrice` 和 `Quantity` 这两列并不需要在 `SELECT` 语句中单独查询出来，也就是说，不查询 `UnitPrice` 和 `Quantity` 列也可以对其进行计算
- 其次，就是计算得到的结果是一个新列，可以使用 `AS` 来为计算得到的结果列起一个别名，这样在查询结果中显示的列名就是我们指定的别名了
- 最后，我们在 `SELECT` 语句中进行的计算是不会改变数据库中原有的数据的，也就是说我们在 `SELECT` 语句中进行的计算只是临时的计算，查询结果中显示的是计算得到的结果，但是数据库中的原有数据并没有被修改

这里要注意一个细节：

- 我们如果有多步计算，可能会想先将第一步计算的结果存储为临时列，然后再在第二步计算中使用这个临时列来进行计算
- 但是在 Azure SQL Database 中，这种操作是不支持的，也就是说我们不能在 `SELECT` 语句中先计算一个临时列，然后再在后续的计算中使用这个临时列来进行计算
- 也就是说，`SELECT` 语句中出现的列名，必须是**表中已经存在的列名**
- 大家以后接触其他数据库类型也许会支持这种操作，但是本门课我们使用 Azure SQL Database 来进行教学，这个功能在 Azure SQL Database 中是不可用的，解决办法是用子查询或 CTE 来实现多步计算的功能，我们后面会讲到
- 例如以下这个查询，我们先算每首歌一秒钟的价格，然后再算每首歌一分钟的价格：


```sql
%%sql
SELECT
    TrackId,
    UnitPrice / Milliseconds * 1000 AS PricePerSecond,
    PricePerSecond * 60 AS PricePerMinute
FROM Track
```


    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    Cell In[15], line 1
    ----> 1 raise Exception(__import__('base64').b64decode('W1MwMDAxXVsyMDddIOihjCA0OiBJbnZhbGlkIGNvbHVtbiBuYW1lICdQcmljZVBlclNlY29uZCcu').decode('utf-8'))


    Exception: [S0001][207] 行 4: Invalid column name 'PricePerSecond'.


- 而正确的做法是直接使用计算每秒价格的表达式来计算每分钟的价格，而不是使用 `PricePerSecond` 这个临时列来进行计算：


```sql
%%sql
SELECT
    TrackId,
    UnitPrice / Milliseconds * 1000 AS PricePerSecond,
    UnitPrice / Milliseconds * 1000 * 60 AS PricePerMinute
FROM Track
```



```
|      | TrackId | PricePerSecond |
|:-----|:--------|:---------------|
| 0    | 1       | 0.002880       |
| 1    | 2       | 0.002890       |
| 2    | 3       | 0.004293       |
| 3    | 4       | 0.003928       |
| 4    | 5       | 0.002637       |
| 5    | 6       | 0.004814       |
| ...  | ...     | ...            |
| 3498 | 3499    | 0.003453       |
| 3499 | 3500    | 0.007112       |
| 3500 | 3501    | 0.014856       |
| 3501 | 3502    | 0.004473       |
| 3502 | 3503    | 0.004806       |
```



上面我们简单了解了使用运算符进行计算，更多高级的计算我们将在后续章节中介绍。

### (2) SQL 中选取特定数值

SQL 有个神奇功能：

- 就是它可以只写 `SELECT` 语句中的数值，而不写 `FROM` 语句中的表名
- 这么做的话，SQL 就会返回一个只有一行一列的结果，这个结果就是我们在 `SELECT` 语句中写的数值
- 相当于把 SQL 当做一个计算器来使用了，这个功能主要在测试 SQL 语法或者进行一些简单的计算的时候会用到

我们来看一下这个功能的例子：


```sql
%%sql
SELECT
    1 + 2 AS Number
```



```
|     | Number |
|:----|:-------|
| 0   | 3      |
```


如果我们既有 `SELECT` 又有 `FROM`，但是我们在 `SELECT` 语句中不写列名，而是直接写数值，那么 SQL 也是可以执行的：

- 比方说 `SELECT 1 + 2 AS Number FROM Album` 这个查询语句也是可以执行的
- 它的效果是，查询出来的所有行，`Number` 列的值都是 `1 + 2` 的计算结果，也就是 `3`
- 而且这个查询结果中的行数和 `Album` 表中的行数是一样的
- 这么做乍一看意义不明，但是我们后面学到一些高级 SQL 操作的时候，大家就可以感受到这个功能的作用了

我们来看一下这个功能的例子：


```sql
%%sql
SELECT
    *,
    1 + 2 AS Number
FROM Album
```



```
|     | AlbumId | Title                                                          | ArtistId | Number |
|:----|:--------|:---------------------------------------------------------------|:---------|:-------|
| 0   | 1       | For Those About To Rock We Salute You                          | 1        | 3      |
| 1   | 2       | Balls to the Wall                                              | 2        | 3      |
| 2   | 3       | Restless and Wild                                              | 2        | 3      |
| 3   | 4       | Let There Be Rock                                              | 1        | 3      |
| 4   | 5       | Big Ones                                                       | 3        | 3      |
| 5   | 6       | Jagged Little Pill                                             | 4        | 3      |
| ... | ...     | ...                                                            | ...      | ...    |
| 342 | 343     | Respighi:Pines of Rome                                         | 226      | 3      |
| 343 | 344     | Schubert: The Late String Quartets & String Quintet \(3 CD's\) | 272      | 3      |
| 344 | 345     | Monteverdi: L'Orfeo                                            | 273      | 3      |
| 345 | 346     | Mozart: Chamber Music                                          | 274      | 3      |
| 346 | 347     | Koyaanisqatsi \(Soundtrack from the Motion Picture\)           | 275      | 3      |
```


