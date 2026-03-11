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



```
|    | AlbumId | Title                                 | ArtistId |
|:---|:--------|:--------------------------------------|:---------|
| 0  | 1       | For Those About To Rock We Salute You | 1        |
| 1  | 4       | Let There Be Rock                     | 1        |
```



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



```
|     | TrackId | Name                                   | UnitPrice |
|:----|:--------|:---------------------------------------|:----------|
| 0   | 2819    | Battlestar Galactica: The Story So Far | 1.99      |
| 1   | 2820    | Occupation / Precipice                 | 1.99      |
| 2   | 2821    | Exodus, Pt. 1                          | 1.99      |
| 3   | 2822    | Exodus, Pt. 2                          | 1.99      |
| 4   | 2823    | Collaborators                          | 1.99      |
| 5   | 2824    | Torn                                   | 1.99      |
| ... | ...     | ...                                    | ...       |
| 208 | 3362    | There's No Place Like Home, Pt. 1      | 1.99      |
| 209 | 3363    | There's No Place Like Home, Pt. 2      | 1.99      |
| 210 | 3364    | There's No Place Like Home, Pt. 3      | 1.99      |
| 211 | 3428    | Branch Closing                         | 1.99      |
| 212 | 3429    | The Return                             | 1.99      |
```



- 查询 `Invoice` 表中所有 `BillingCountry` 列的值等于 `Brazil` 的行，只展示 `CustomerId` 与 `InvoiceDate` 两列：


```sql
%%sql
SELECT
    CustomerId,
    InvoiceDate
FROM Invoice
WHERE BillingCountry = 'Brazil'
```



```
|     | CustomerId | InvoiceDate             |
|:----|:-----------|:------------------------|
| 0   | 10         | 2021-04-09 00:00:00.000 |
| 1   | 12         | 2021-05-23 00:00:00.000 |
| 2   | 13         | 2021-06-05 00:00:00.000 |
| 3   | 11         | 2021-09-06 00:00:00.000 |
| 4   | 13         | 2021-09-07 00:00:00.000 |
| 5   | 11         | 2021-10-17 00:00:00.000 |
| ... | ...        | ...                     |
| 30  | 10         | 2025-07-02 00:00:00.000 |
| 31  | 12         | 2025-07-03 00:00:00.000 |
| 32  | 1          | 2025-08-07 00:00:00.000 |
| 33  | 10         | 2025-08-12 00:00:00.000 |
| 34  | 12         | 2025-10-05 00:00:00.000 |
```



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



```
|    | TrackId | Name                   | AlbumId | MediaTypeId | GenreId | Composer | Milliseconds | Bytes      | UnitPrice |
|:---|:--------|:-----------------------|:--------|:------------|:--------|:---------|:-------------|:-----------|:----------|
| 0  | 2820    | Occupation / Precipice | 227     | 3           | 19      | NaN      | 5286953      | 1054423946 | 1.99      |
| 1  | 3224    | Through a Looking Glass| 229     | 3           | 21      | NaN      | 5088838      | 1059546140 | 1.99      |
```



- 查询 `Invoice` 表中 `BillingCountry` 列的值等于 `Brazil` 或者 `Austria` 的行：


```sql
%%sql
SELECT *
FROM Invoice
WHERE BillingCountry = 'Brazil'
OR BillingCountry = 'Austria'
```



```
|     | InvoiceId | CustomerId | InvoiceDate             | BillingAddress                  | BillingCity         | BillingState | BillingCountry | BillingPostalCode | Total |
|:----|:----------|:-----------|:------------------------|:--------------------------------|:--------------------|:-------------|:---------------|:------------------|:------|
| 0   | 25        | 10         | 2021-04-09 00:00:00.000 | Rua Dr. Falcão Filho, 155       | São Paulo           | SP           | Brazil         | 01007-010         | 8.91  |
| 1   | 34        | 12         | 2021-05-23 00:00:00.000 | Praça Pio X, 119                | Rio de Janeiro      | RJ           | Brazil         | 20040-020         | 0.99  |
| 2   | 35        | 13         | 2021-06-05 00:00:00.000 | Qe 7 Bloco G                    | Brasília            | DF           | Brazil         | 71020-677         | 1.98  |
| 3   | 57        | 11         | 2021-09-06 00:00:00.000 | Av. Paulista, 2022              | São Paulo           | SP           | Brazil         | 01310-200         | 1.98  |
| 4   | 58        | 13         | 2021-09-07 00:00:00.000 | Qe 7 Bloco G                    | Brasília            | DF           | Brazil         | 71020-677         | 3.96  |
| 5   | 68        | 11         | 2021-10-17 00:00:00.000 | Av. Paulista, 2022              | São Paulo           | SP           | Brazil         | 01310-200         | 13.86 |
| ... | ...       | ...        | ...                     | ...                             | ...                 | ...          | ...            | ...               | ...   |
| 37  | 372       | 10         | 2025-07-02 00:00:00.000 | Rua Dr. Falcão Filho, 155       | São Paulo           | SP           | Brazil         | 01007-010         | 1.98  |
| 38  | 373       | 12         | 2025-07-03 00:00:00.000 | Praça Pio X, 119                | Rio de Janeiro      | RJ           | Brazil         | 20040-020         | 3.96  |
| 39  | 382       | 1          | 2025-08-07 00:00:00.000 | Av. Brigadeiro Faria Lima, 2170 | São José dos Campos | SP           | Brazil         | 12227-000         | 8.91  |
| 40  | 383       | 10         | 2025-08-12 00:00:00.000 | Rua Dr. Falcão Filho, 155       | São Paulo           | SP           | Brazil         | 01007-010         | 13.86 |
| 41  | 395       | 12         | 2025-10-05 00:00:00.000 | Praça Pio X, 119                | Rio de Janeiro      | RJ           | Brazil         | 20040-020         | 5.94  |
```



- 查询 `Track` 表中 `UnitPrice` 列的值大于 0.99 且 `Milliseconds` 列的值大于 50000000 的行，或者 `UnitPrice` 列的值小于等于 0.99 且 `Milliseconds` 列的值小于等于 50000000 的行：


```sql
%%sql
SELECT *
FROM Track
WHERE (UnitPrice > 0.99 AND Milliseconds > 5000000)
OR (UnitPrice <= 0.99 AND Milliseconds <= 5000000)
```



```
|      | TrackId | Name                                                                                     | AlbumId | MediaTypeId | GenreId | Composer                                                                     | Milliseconds | Bytes    | UnitPrice |
|:-----|:--------|:-----------------------------------------------------------------------------------------|:--------|:------------|:--------|:-----------------------------------------------------------------------------|:-------------|:---------|:----------|
| 0    | 1       | For Those About To Rock \(We Salute You\)                                                | 1       | 1           | 1       | Angus Young, Malcolm Young, Brian Johnson                                    | 343719       | 11170334 | 0.99      |
| 1    | 2       | Balls to the Wall                                                                        | 2       | 2           | 1       | U. Dirkschneider, W. Hoffmann, H. Frank, P. Baltes, S. Kaufmann, G. Hoffmann | 342562       | 5510424  | 0.99      |
| 2    | 3       | Fast As a Shark                                                                          | 3       | 2           | 1       | F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman                          | 230619       | 3990994  | 0.99      |
| 3    | 4       | Restless and Wild                                                                        | 3       | 2           | 1       | F. Baltes, R.A. Smith-Diesel, S. Kaufman, U. Dirkscneider & W. Hoffman       | 252051       | 4331779  | 0.99      |
| 4    | 5       | Princess of the Dawn                                                                     | 3       | 2           | 1       | Deaffy & R.A. Smith-Diesel                                                   | 375418       | 6290521  | 0.99      |
| 5    | 6       | Put The Finger On You                                                                    | 1       | 1           | 1       | Angus Young, Malcolm Young, Brian Johnson                                    | 205662       | 6713451  | 0.99      |
| ...  | ...     | ...                                                                                      | ...     | ...         | ...     | ...                                                                          | ...          | ...      | ...       |
| 3287 | 3499    | Pini Di Roma \(Pinien Von Rom\) \\ I Pini Della Via Appia                                | 343     | 2           | 24      | NaN                                                                          | 286741       | 4718950  | 0.99      |
| 3288 | 3500    | String Quartet No. 12 in C Minor, D. 703 "Quartettsatz": II. Andante - Allegro assai     | 344     | 2           | 24      | Franz Schubert                                                               | 139200       | 2283131  | 0.99      |
| 3289 | 3501    | L'orfeo, Act 3, Sinfonia \(Orchestra\)                                                   | 345     | 2           | 24      | Claudio Monteverdi                                                           | 66639        | 1189062  | 0.99      |
| 3290 | 3502    | Quintet for Horn, Violin, 2 Violas, and Cello in E Flat Major, K. 407/386c: III. Allegro | 346     | 2           | 24      | Wolfgang Amadeus Mozart                                                      | 221331       | 3665114  | 0.99      |
| 3291 | 3503    | Koyaanisqatsi                                                                            | 347     | 2           | 10      | Philip Glass                                                                 | 206005       | 3305164  | 0.99      |
```



- 查询 `Invoice` 表中 `BillingCountry` 列的值不等于 `Brazil` 的行：


```sql
%%sql
SELECT *
FROM Invoice
WHERE NOT (BillingCountry = 'Brazil')
```



```
|     | InvoiceId | CustomerId | InvoiceDate             | BillingAddress                           | BillingCity | BillingState | BillingCountry | BillingPostalCode | Total |
|:----|:----------|:-----------|:------------------------|:-----------------------------------------|:------------|:-------------|:---------------|:------------------|:------|
| 0   | 1         | 2          | 2021-01-01 00:00:00.000 | Theodor-Heuss-Straße 34                  | Stuttgart   | NaN          | Germany        | 70174             | 1.98  |
| 1   | 2         | 4          | 2021-01-02 00:00:00.000 | Ullevålsveien 14                         | Oslo        | NaN          | Norway         | 0171              | 3.96  |
| 2   | 3         | 8          | 2021-01-03 00:00:00.000 | Grétrystraat 63                          | Brussels    | NaN          | Belgium        | 1000              | 5.94  |
| 3   | 4         | 14         | 2021-01-06 00:00:00.000 | 8210 111 ST NW                           | Edmonton    | AB           | Canada         | T6G 2C7           | 8.91  |
| 4   | 5         | 23         | 2021-01-11 00:00:00.000 | 69 Salem Street                          | Boston      | MA           | USA            | 2113              | 13.86 |
| 5   | 6         | 37         | 2021-01-19 00:00:00.000 | Berger Straße 10                         | Frankfurt   | NaN          | Germany        | 60316             | 0.99  |
| ... | ...       | ...        | ...                     | ...                                      | ...         | ...          | ...            | ...               | ...   |
| 372 | 408       | 25         | 2025-12-05 00:00:00.000 | 319 N. Frances Street                    | Madison     | WI           | USA            | 53703             | 3.96  |
| 373 | 409       | 29         | 2025-12-06 00:00:00.000 | 796 Dundas Street West                   | Toronto     | ON           | Canada         | M6J 1V1           | 5.94  |
| 374 | 410       | 35         | 2025-12-09 00:00:00.000 | Rua dos Campeões Europeus de Viena, 4350 | Porto       | NaN          | Portugal       | NaN               | 8.91  |
| 375 | 411       | 44         | 2025-12-14 00:00:00.000 | Porthaninkatu 9                          | Helsinki    | NaN          | Finland        | 00530             | 13.86 |
| 376 | 412       | 58         | 2025-12-22 00:00:00.000 | 12,Community Centre                      | Delhi       | NaN          | India          | 110017            | 1.99  |
```



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


对于这一问题，一个可行的解决方式是：

- 将带有原字段的表达式直接放在 `WHERE` 语句中来进行条件查询
- 例如在上面的例子中，我们可以把计算字段 `TotalPrice` 的计算式 `UnitPrice * Quantity` 直接放在 `WHERE` 语句中：

```sql
%%sql
SELECT
    InvoiceId,
    UnitPrice * Quantity AS TotalPrice
FROM InvoiceLine
WHERE UnitPrice * Quantity > 1.00
```

```
|     | InvoiceId | TotalPrice |
|:----|:----------|:-----------|
| 0   | 87        | 1.99       |
| 1   | 88        | 1.99       |
| 2   | 88        | 1.99       |
| 3   | 88        | 1.99       |
| 4   | 88        | 1.99       |
| 5   | 88        | 1.99       |
| ... | ...       | ...        |
| 106 | 404       | 1.99       |
| 107 | 404       | 1.99       |
| 108 | 404       | 1.99       |
| 109 | 404       | 1.99       |
| 110 | 412       | 1.99       |
```

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



```
|    | ArtistId | Name                                                                                  |
|:---|:---------|:--------------------------------------------------------------------------------------|
| 0  | 170      | Jack Johnson                                                                          |
| 1  | 218      | Orchestre Révolutionnaire et Romantique & John Eliot Gardiner                         |
| 2  | 222      | Academy of St. Martin in the Fields, John Birch, Sir Neville Marriner & Sylvia McNair |
| 3  | 263      | Equale Brass Ensemble, John Eliot Gardiner & Munich Monteverdi Orchestra and Choir    |
```



- 查询 `Artist` 表中 `Name` 是 4 个字符长度的行：


```sql
%%sql
SELECT *
FROM Artist
WHERE Name LIKE '____'
```



```
|     | ArtistId | Name   |
|:----|:---------|:-------|
| 0   | 52       | Kiss   |
| 1   | 128      | Rush   |
| 2   | 149      | Lost   |
| 3   | 151      | UB40   |
| 4   | 189      | Otto   |
| 5   | 196      | Cake   |
```



- 查询 `Track` 表中 `Name` 中带有 `Love` 或 `love` 的行（大小写都可以）：


```sql
%%sql
SELECT *
FROM Track
WHERE Name LIKE '%Love%'
OR Name LIKE '%love%'
```



```
|     | TrackId | Name                                         | AlbumId | MediaTypeId | GenreId | Composer                                                         | Milliseconds | Bytes    | UnitPrice |
|:----|:--------|:---------------------------------------------|:--------|:------------|:--------|:-----------------------------------------------------------------|:-------------|:---------|:----------|
| 0   | 24      | Love In An Elevator                          | 5       | 1           | 1       | Steven Tyler, Joe Perry                                          | 321828       | 10552051 | 0.99      |
| 1   | 56      | Love, Hate, Love                             | 7       | 1           | 1       | Jerry Cantrell, Layne Staley                                     | 387134       | 12575396 | 0.99      |
| 2   | 195     | Let Me Love You Baby                         | 20      | 1           | 6       | Willie Dixon                                                     | 175386       | 5716994  | 0.99      |
| 3   | 335     | My Love                                      | 29      | 1           | 9       | Jauperi/Zeu Góes                                                 | 203493       | 6772813  | 0.99      |
| 4   | 341     | The Girl I Love She Got Long Black Wavy Hair | 30      | 1           | 1       | Jimmy Page/John Bonham/John Estes/John Paul Jones/Robert Plant   | 183327       | 5995686  | 0.99      |
| 5   | 345     | Whole Lotta Love                             | 30      | 1           | 1       | Jimmy Page/John Bonham/John Paul Jones/Robert Plant/Willie Dixon | 373394       | 12258175 | 0.99      |
| ... | ...     | ...                                          | ...     | ...         | ...     | ...                                                              | ...          | ...      | ...       |
| 109 | 3355    | Love Comes                                   | 265     | 5           | 1       | Darius "Take One" Minwalla/Jon Auer/Ken Stringfellow/Matt Harris | 199923       | 3240609  | 0.99      |
| 110 | 3377    | Arms Around Your Love                        | 270     | 2           | 23      | Chris Cornell                                                    | 214016       | 3516224  | 0.99      |
| 111 | 3460    | Love Is a Losing Game                        | 321     | 2           | 14      | NaN                                                              | 154386       | 2509409  | 0.99      |
| 112 | 3470    | I Heard Love Is Blind                        | 322     | 2           | 9       | NaN                                                              | 129666       | 2190831  | 0.99      |
| 113 | 3471    | \(There Is\) No Greater Love \(Teo Licks\)   | 322     | 2           | 9       | Isham Jones & Marty Symes                                        | 167933       | 2773507  | 0.99      |
```



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



```
|      | TrackId | Name                                                                                     | AlbumId | MediaTypeId | GenreId | Composer                                                               | Milliseconds | Bytes   | UnitPrice |
|:-----|:--------|:-----------------------------------------------------------------------------------------|:--------|:------------|:--------|:-----------------------------------------------------------------------|:-------------|:--------|:----------|
| 0    | 3       | Fast As a Shark                                                                          | 3       | 2           | 1       | F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman                    | 230619       | 3990994 | 0.99      |
| 1    | 4       | Restless and Wild                                                                        | 3       | 2           | 1       | F. Baltes, R.A. Smith-Diesel, S. Kaufman, U. Dirkscneider & W. Hoffman | 252051       | 4331779 | 0.99      |
| 2    | 6       | Put The Finger On You                                                                    | 1       | 1           | 1       | Angus Young, Malcolm Young, Brian Johnson                              | 205662       | 6713451 | 0.99      |
| 3    | 7       | Let's Get It Up                                                                          | 1       | 1           | 1       | Angus Young, Malcolm Young, Brian Johnson                              | 233926       | 7636561 | 0.99      |
| 4    | 8       | Inject The Venom                                                                         | 1       | 1           | 1       | Angus Young, Malcolm Young, Brian Johnson                              | 210834       | 6852860 | 0.99      |
| 5    | 9       | Snowballed                                                                               | 1       | 1           | 1       | Angus Young, Malcolm Young, Brian Johnson                              | 203102       | 6599424 | 0.99      |
| ...  | ...     | ...                                                                                      | ...     | ...         | ...     | ...                                                                    | ...          | ...     | ...       |
| 1675 | 3495    | 24 Caprices, Op. 1, No. 24, for Solo Violin, in A Minor                                  | 339     | 2           | 24      | Niccolò Paganini                                                       | 265541       | 4371533 | 0.99      |
| 1676 | 3497    | Erlkonig, D.328                                                                          | 341     | 2           | 24      | NaN                                                                    | 261849       | 4307907 | 0.99      |
| 1677 | 3499    | Pini Di Roma \(Pinien Von Rom\) \\ I Pini Della Via Appia                                | 343     | 2           | 24      | NaN                                                                    | 286741       | 4718950 | 0.99      |
| 1678 | 3502    | Quintet for Horn, Violin, 2 Violas, and Cello in E Flat Major, K. 407/386c: III. Allegro | 346     | 2           | 24      | Wolfgang Amadeus Mozart                                                | 221331       | 3665114 | 0.99      |
| 1679 | 3503    | Koyaanisqatsi                                                                            | 347     | 2           | 10      | Philip Glass                                                           | 206005       | 3305164 | 0.99      |
```



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



```
|     | InvoiceId | CustomerId | InvoiceDate             | BillingAddress            | BillingCity    | BillingState | BillingCountry | BillingPostalCode | Total |
|:----|:----------|:-----------|:------------------------|:--------------------------|:---------------|:-------------|:---------------|:------------------|:------|
| 0   | 8         | 40         | 2021-02-01 00:00:00.000 | 8, Rue Hanovre            | Paris          | NaN          | France         | 75002             | 1.98  |
| 1   | 9         | 42         | 2021-02-02 00:00:00.000 | 9, Place Louis Barthou    | Bordeaux       | NaN          | France         | 33000             | 3.96  |
| 2   | 19        | 40         | 2021-03-14 00:00:00.000 | 8, Rue Hanovre            | Paris          | NaN          | France         | 75002             | 13.86 |
| 3   | 25        | 10         | 2021-04-09 00:00:00.000 | Rua Dr. Falcão Filho, 155 | São Paulo      | SP           | Brazil         | 01007-010         | 8.91  |
| 4   | 31        | 42         | 2021-05-07 00:00:00.000 | 9, Place Louis Barthou    | Bordeaux       | NaN          | France         | 33000             | 5.94  |
| 5   | 34        | 12         | 2021-05-23 00:00:00.000 | Praça Pio X, 119          | Rio de Janeiro | RJ           | Brazil         | 20040-020         | 0.99  |
| ... | ...       | ...        | ...                     | ...                       | ...            | ...          | ...            | ...               | ...   |
| 72  | 383       | 10         | 2025-08-12 00:00:00.000 | Rua Dr. Falcão Filho, 155 | São Paulo      | SP           | Brazil         | 01007-010         | 13.86 |
| 73  | 389       | 39         | 2025-09-07 00:00:00.000 | 4, Rue Milton             | Paris          | NaN          | France         | 75009             | 8.91  |
| 74  | 395       | 12         | 2025-10-05 00:00:00.000 | Praça Pio X, 119          | Rio de Janeiro | RJ           | Brazil         | 20040-020         | 5.94  |
| 75  | 398       | 41         | 2025-10-21 00:00:00.000 | 11, Place Bellecour       | Lyon           | NaN          | France         | 69002             | 0.99  |
| 76  | 399       | 42         | 2025-11-03 00:00:00.000 | 9, Place Louis Barthou    | Bordeaux       | NaN          | France         | 33000             | 1.98  |
```



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



```
|     | TrackId | Name                                                             | AlbumId | MediaTypeId | GenreId | Composer | Milliseconds | Bytes   | UnitPrice |
|:----|:--------|:-----------------------------------------------------------------|:--------|:------------|:--------|:---------|:-------------|:--------|:----------|
| 0   | 63      | Desafinado                                                       | 8       | 1           | 2       | NaN      | 185338       | 5990473 | 0.99      |
| 1   | 64      | Garota De Ipanema                                                | 8       | 1           | 2       | NaN      | 285048       | 9348428 | 0.99      |
| 2   | 65      | Samba De Uma Nota Só \(One Note Samba\)                          | 8       | 1           | 2       | NaN      | 137273       | 4535401 | 0.99      |
| 3   | 66      | Por Causa De Você                                                | 8       | 1           | 2       | NaN      | 169900       | 5536496 | 0.99      |
| 4   | 67      | Ligia                                                            | 8       | 1           | 2       | NaN      | 251977       | 8226934 | 0.99      |
| 5   | 68      | Fotografia                                                       | 8       | 1           | 2       | NaN      | 129227       | 4198774 | 0.99      |
| ... | ...     | ...                                                              | ...     | ...         | ...     | ...      | ...          | ...     | ...       |
| 972 | 3478    | Slowness                                                         | 323     | 2           | 23      | NaN      | 215386       | 3644793 | 0.99      |
| 973 | 3481    | A Midsummer Night's Dream, Op.61 Incidental Music: No.7 Notturno | 326     | 2           | 24      | NaN      | 387826       | 6497867 | 0.99      |
| 974 | 3496    | Étude 1, In C Major - Preludio \(Presto\) - Liszt                | 340     | 4           | 24      | NaN      | 51780        | 2229617 | 0.99      |
| 975 | 3497    | Erlkonig, D.328                                                  | 341     | 2           | 24      | NaN      | 261849       | 4307907 | 0.99      |
| 976 | 3499    | Pini Di Roma \(Pinien Von Rom\) \\ I Pini Della Via Appia        | 343     | 2           | 24      | NaN      | 286741       | 4718950 | 0.99      |
```


