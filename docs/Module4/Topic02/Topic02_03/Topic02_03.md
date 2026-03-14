# Topic 2.3 - ORDER BY 语句数据排序与 TOP 结果限制

## 1. SQL 中的排序查询

### (1) 基础的排序查询

在 SQL 中，我们可以使用 `ORDER BY` 语句来对查询结果进行排序，`ORDER BY` 语句的基本语法如下：

```sql
SELECT ...
FROM 表名
WHERE 条件
ORDER BY 列名
```

排序依据的列：

- 如果是数字类型的列，那么排序会按照数值大小进行排序
- 如果是字符串类型的列，那么排序会按照字母顺序进行排序，默认是按照 ASCII 码进行排序（字符 -> 数字 -> 大写字母 -> 小写字母）

我们来看以下几个例子：

- 在 `Album` 表中查询 `Title` 列和 `ArtistId` 列，并且按照 `Title` 列的值进行排序：


```sql
%%sql
SELECT
    Title,
    ArtistId
FROM Album
ORDER BY Title
```



```
|     | Title                                                                   | ArtistId |
|:----|:------------------------------------------------------------------------|:---------|
| 0   | ...And Justice For All                                                  | 50       |
| 1   | \[1997\] Black Light Syndrome                                           | 136      |
| 2   | 20th Century Masters - The Millennium Collection: The Best of Scorpions | 179      |
| 3   | A Copland Celebration, Vol. I                                           | 230      |
| 4   | A Matter of Life and Death                                              | 90       |
| 5   | A Real Dead One                                                         | 90       |
| ... | ...                                                                     | ...      |
| 342 | War                                                                     | 150      |
| 343 | Warner 25 Anos                                                          | 6        |
| 344 | Weill: The Seven Deadly Sins                                            | 264      |
| 345 | Worlds                                                                  | 202      |
| 346 | Zooropa                                                                 | 150      |
```



- 在 `Track` 表中查询 `Name` 列和 `UnitPrice` 列，筛选 `Name` 中带 'Love' 或 'love' 的行，并且按照 `UnitPrice` 列的值进行排序：


```sql
%%sql
SELECT
    Name,
    UnitPrice
FROM Track
WHERE Name LIKE '%Love%' OR Name LIKE '%love%'
ORDER BY UnitPrice
```



```
|     | Name                                         | UnitPrice |
|:----|:---------------------------------------------|:----------|
| 0   | Love In An Elevator                          | 0.99      |
| 1   | Love, Hate, Love                             | 0.99      |
| 2   | Let Me Love You Baby                         | 0.99      |
| 3   | My Love                                      | 0.99      |
| 4   | The Girl I Love She Got Long Black Wavy Hair | 0.99      |
| 5   | Whole Lotta Love                             | 0.99      |
| ... | ...                                          | ...       |
| 109 | Love Comes                                   | 0.99      |
| 110 | Arms Around Your Love                        | 0.99      |
| 111 | Love Is a Losing Game                        | 0.99      |
| 112 | I Heard Love Is Blind                        | 0.99      |
| 113 | \(There Is\) No Greater Love \(Teo Licks\)   | 0.99      |
```



### (2) 指定排序方式

在 SQL 中，`ORDER BY` 语句默认是按照升序（从小到大）进行排序的

- 如果我们想要按照降序（从大到小）进行排序，可以在 `ORDER BY` 语句中使用 `DESC` 关键字来指定排序方式
- 而且，如果想要强调按照升序（从小到大）进行排序，也可以在 `ORDER BY` 语句中使用 `ASC` 关键字来指定排序方式，虽然默认就是升序，但这样写可以让语义更清晰

我们把上面的例子改一下，全部按照降序进行排序：

- 在 `Album` 表中查询 `Title` 列和 `ArtistId` 列，并且按照 `Title` 列的值进行降序排序：


```sql
%%sql
SELECT
    Title,
    ArtistId
FROM Album
ORDER BY Title DESC
```



```
|     | Title                                                                   | ArtistId |
|:----|:------------------------------------------------------------------------|:---------|
| 0   | Zooropa                                                                 | 150      |
| 1   | Worlds                                                                  | 202      |
| 2   | Weill: The Seven Deadly Sins                                            | 264      |
| 3   | Warner 25 Anos                                                          | 6        |
| 4   | War                                                                     | 150      |
| 5   | Walking Into Clarksdale                                                 | 115      |
| ... | ...                                                                     | ...      |
| 342 | A Matter of Life and Death                                              | 90       |
| 343 | A Copland Celebration, Vol. I                                           | 230      |
| 344 | 20th Century Masters - The Millennium Collection: The Best of Scorpions | 179      |
| 345 | \[1997\] Black Light Syndrome                                           | 136      |
| 346 | ...And Justice For All                                                  | 50       |
```



- 在 `Track` 表中查询 `Name` 列和 `UnitPrice` 列，筛选 `Name` 中带 'Love' 或 'love' 的行，并且按照 `UnitPrice` 列的值进行降序排序：


```sql
%%sql
SELECT
    Name,
    UnitPrice
FROM Track
WHERE Name LIKE '%Love%' OR Name LIKE '%love%'
ORDER BY UnitPrice DESC
```



```
|     | Name                                         | UnitPrice |
|:----|:---------------------------------------------|:----------|
| 0   | Love In An Elevator                          | 0.99      |
| 1   | Love, Hate, Love                             | 0.99      |
| 2   | Let Me Love You Baby                         | 0.99      |
| 3   | My Love                                      | 0.99      |
| 4   | The Girl I Love She Got Long Black Wavy Hair | 0.99      |
| 5   | Whole Lotta Love                             | 0.99      |
| ... | ...                                          | ...       |
| 109 | Love Comes                                   | 0.99      |
| 110 | Arms Around Your Love                        | 0.99      |
| 111 | Love Is a Losing Game                        | 0.99      |
| 112 | I Heard Love Is Blind                        | 0.99      |
| 113 | \(There Is\) No Greater Love \(Teo Licks\)   | 0.99      |
```



### (3) 多列排序

在 SQL 中，我们还可以在 `ORDER BY` 语句中指定多个列来进行排序：

- 多列排序的语法如下：

```sql
SELECT ...
FROM 表名
WHERE 条件
ORDER BY 列名1 ASC 或 DESC, 列名2 ASC 或 DESC, ...
```

- 当指定多个列进行排序时，SQL 会先按照第一个列进行排序，如果第一个列的值相同，那么就会按照第二个列进行排序，以此类推
- 每个列都可以单独指定排序方式（升序或降序）

我们来看以下例子：

- 在 `Track` 表中查询 `Name` 列、`UnitPrice` 列和 `Milliseconds` 列，筛选 `Name` 中带 'Love' 或 'love' 的行，并且按照 `UnitPrice` 列的值进行降序排序，如果 `UnitPrice` 的值相同，那么就按照 `Milliseconds` 列的值进行升序排序：


```sql
%%sql
SELECT
    Name,
    UnitPrice,
    Milliseconds
FROM Track
WHERE Name LIKE '%Love%' OR Name LIKE '%love%'
ORDER BY UnitPrice DESC, Milliseconds ASC
```



```
|     | Name                                                                                                  | UnitPrice | Milliseconds |
|:----|:------------------------------------------------------------------------------------------------------|:----------|:-------------|
| 0   | Love And Marriage                                                                                     | 0.99      | 89730        |
| 1   | I Heard Love Is Blind                                                                                 | 0.99      | 129666       |
| 2   | What Now My Love                                                                                      | 0.99      | 149995       |
| 3   | When I Had Your Love                                                                                  | 0.99      | 152424       |
| 4   | Love Is a Losing Game                                                                                 | 0.99      | 154386       |
| 5   | Oh, My Love                                                                                           | 0.99      | 159473       |
| ... | ...                                                                                                   | ...       | ...          |
| 109 | Old Love                                                                                              | 0.99      | 472920       |
| 110 | The Thin Line Between Love & Hate                                                                     | 0.99      | 506801       |
| 111 | Jesus Of Suburbia / City Of The Damned / I Don't Care / Dearly Beloved / Tales Of Another Broken Home | 0.99      | 548336       |
| 112 | Whole Lotta Love \(Medley\)                                                                           | 0.99      | 825103       |
| 113 | Whole Lotta Love                                                                                      | 0.99      | 863895       |
```



- 在 `Album` 表中查询 `Title` 列、`ArtistId` 列和 `AlbumId` 列，并且按照 `ArtistId` 列的值进行升序排序，如果 `ArtistId` 的值相同，那么就按照 `AlbumId` 列的值进行降序排序：


```sql
%%sql
SELECT
    Title,
    ArtistId,
    AlbumId
FROM Album
ORDER BY ArtistId ASC, AlbumId DESC
```



```
|     | Title                                                          | ArtistId | AlbumId |
|:----|:---------------------------------------------------------------|:---------|:--------|
| 0   | Let There Be Rock                                              | 1        | 4       |
| 1   | For Those About To Rock We Salute You                          | 1        | 1       |
| 2   | Restless and Wild                                              | 2        | 3       |
| 3   | Balls to the Wall                                              | 2        | 2       |
| 4   | Big Ones                                                       | 3        | 5       |
| 5   | Jagged Little Pill                                             | 4        | 6       |
| ... | ...                                                            | ...      | ...     |
| 342 | Locatelli: Concertos for Violin, Strings and Continuo, Vol. 3  | 271      | 342     |
| 343 | Schubert: The Late String Quartets & String Quintet \(3 CD's\) | 272      | 344     |
| 344 | Monteverdi: L'Orfeo                                            | 273      | 345     |
| 345 | Mozart: Chamber Music                                          | 274      | 346     |
| 346 | Koyaanisqatsi \(Soundtrack from the Motion Picture\)           | 275      | 347     |
```


### (4) ORDER BY 语法的注意事项

这里大家注意一下 `ORDER BY` 语句的一个特殊性：

- 之前我们在讲 `WHERE` 语句的时候，提到过 `WHERE` 语句中的列名必须使用原列名
- 而在 `ORDER BY` 语句中，列名可以使用原列名，也可以使用列别名
- 这个是 `ORDER BY` 语句的一个特殊性
- 我们来看以下例子：

```sql
%%sql
SELECT
    Title AS AlbumTitle,
    ArtistId AS ArtistId
FROM Album
ORDER BY AlbumTitle DESC, ArtistId ASC
```

```
|     | AlbumTitle                                                              | ArtistId |
|:----|:------------------------------------------------------------------------|:---------|
| 0   | Zooropa                                                                 | 150      |
| 1   | Worlds                                                                  | 202      |
| 2   | Weill: The Seven Deadly Sins                                            | 264      |
| 3   | Warner 25 Anos                                                          | 6        |
| 4   | War                                                                     | 150      |
| 5   | Walking Into Clarksdale                                                 | 115      |
| ... | ...                                                                     | ...      |
| 342 | A Matter of Life and Death                                              | 90       |
| 343 | A Copland Celebration, Vol. I                                           | 230      |
| 344 | 20th Century Masters - The Millennium Collection: The Best of Scorpions | 179      |
| 345 | \[1997\] Black Light Syndrome                                           | 136      |
| 346 | ...And Justice For All                                                  | 50       |
```


## 2. 头部查询

### (1) 查询前 N 行数据

在 SQL 中，我们还可以用 `TOP` 关键字与 `ORDER BY` 语句结合来进行头部查询：

- `TOP` 关键字的基本语法如下：

```sql
SELECT TOP n ...
FROM 表名
WHERE 条件
ORDER BY 列名1 ASC 或 DESC, 列名2 ASC 或 DESC, ...
```

- 其中，`n` 是一个整数，表示要查询的前 `n` 行数据
- 这个查询结果是按照 `ORDER BY` 语句指定的排序方式进行排序之后的前 `n` 行数据

我们来看以下例子：

- 查询 `Track` 表，按 `Milliseconds` 列的值进行降序排序，最后只返回前 5 行数据：


```sql
%%sql
SELECT TOP 5 *
FROM Track
ORDER BY Milliseconds DESC
```


```
|   | TrackId | Name                        | AlbumId | MediaTypeId | GenreId | Composer | Milliseconds | Bytes      | UnitPrice |
|:--|:--------|:----------------------------|:--------|:------------|:--------|:---------|:-------------|:-----------|:---------|
| 0 | 2820    | Occupation / Precipice      | 227     | 3           | 19      | NaN      | 5286953      | 1054423946 | 1.99     |
| 1 | 3224    | Through a Looking Glass     | 229     | 3           | 21      | NaN      | 5088838      | 1059546140 | 1.99     |
| 2 | 3244    | Greetings from Earth, Pt. 1 | 253     | 3           | 20      | NaN      | 2960293      | 536824558  | 1.99     |
| 3 | 3242    | The Man With Nine Lives     | 253     | 3           | 20      | NaN      | 2956998      | 577829804  | 1.99     |
| 4 | 3227    | Battlestar Galactica, Pt. 2 | 253     | 3           | 20      | NaN      | 2956081      | 521387924  | 1.99     |
```



- 查询 `Album` 表，按 `ArtistId` 列的值进行升序排序，如果 `ArtistId` 的值相同，那么就按照 `AlbumId` 列的值进行降序排序，最后只返回前 10 行数据：


```sql
%%sql
SELECT TOP 10 *
FROM Album
ORDER BY ArtistId ASC, AlbumId DESC
```



```
|   | AlbumId | Title                                 | ArtistId |
|:--|:--------|:--------------------------------------|:--------|
| 0 | 4       | Let There Be Rock                     | 1       |
| 1 | 1       | For Those About To Rock We Salute You | 1       |
| 2 | 3       | Restless and Wild                     | 2       |
| 3 | 2       | Balls to the Wall                     | 2       |
| 4 | 5       | Big Ones                              | 3       |
| 5 | 6       | Jagged Little Pill                    | 4       |
| 6 | 7       | Facelift                              | 5       |
| 7 | 34      | Chill: Brazil \(Disc 2\)              | 6       |
| 8 | 8       | Warner 25 Anos                        | 6       |
| 9 | 9       | Plays Metallica By Four Cellos        | 7       |
```



### (2) 查询前 N 百分比数据

`Top` 关键字还有一个用法，那就是查询前 `n` 百分比的数据：

- `TOP` 关键字查询前 `n` 百分比数据的基本语法如下：

```sql
SELECT TOP n PERCENT ...
FROM 表名
WHERE 条件
ORDER BY 列名1 ASC 或 DESC, 列名2 ASC 或 DESC, ...
```

- 其中，`n` 是一个整数，表示要查询的前 `n` 百分比的数据
- 这个查询结果是按照 `ORDER BY` 语句指定的排序方式进行序之后的前 `n` 百分比的数据

我们来把上面两个例子改成查询前 `n` 百分比的数据：

- 查询 `Track` 表，按 `Milliseconds` 列的值进行降序排序，最后只返回前 20% 的数据：


```sql
%%sql
SELECT TOP 20 PERCENT *
FROM Track
ORDER BY Milliseconds DESC
```



```
|     | TrackId | Name                        | AlbumId | MediaTypeId | GenreId | Composer                                               | Milliseconds | Bytes      | UnitPrice |
|:----|:--------|:----------------------------|:--------|:------------|:--------|:-------------------------------------------------------|:-------------|:-----------|:----------|
| 0   | 2820    | Occupation / Precipice      | 227     | 3           | 19      | NaN                                                    | 5286953      | 1054423946 | 1.99      |
| 1   | 3224    | Through a Looking Glass     | 229     | 3           | 21      | NaN                                                    | 5088838      | 1059546140 | 1.99      |
| 2   | 3244    | Greetings from Earth, Pt. 1 | 253     | 3           | 20      | NaN                                                    | 2960293      | 536824558  | 1.99      |
| 3   | 3242    | The Man With Nine Lives     | 253     | 3           | 20      | NaN                                                    | 2956998      | 577829804  | 1.99      |
| 4   | 3227    | Battlestar Galactica, Pt. 2 | 253     | 3           | 20      | NaN                                                    | 2956081      | 521387924  | 1.99      |
| 5   | 3226    | Battlestar Galactica, Pt. 1 | 253     | 3           | 20      | NaN                                                    | 2952702      | 541359437  | 1.99      |
| ... | ...     | ...                         | ...     | ...         | ...     | ...                                                    | ...          | ...        | ...       |
| 696 | 493     | Love Is Blind               | 40      | 1           | 1       | David Coverdale/Earl Slick                             | 344999       | 11409720   | 0.99      |
| 697 | 1383    | Stranger in a Strange Land  | 111     | 1           | 3       | Adrian Smith                                           | 344502       | 8270899    | 0.99      |
| 698 | 558     | Viradouro                   | 45      | 1           | 7       | Dadinho/Gilbreto Gomes/Gustavo/P.C. Portugal/R. Mocoto | 344320       | 11484362   | 0.99      |
| 699 | 2102    | Mr. Crowley                 | 174     | 1           | 3       | O. Osbourne, R. Daisley, R. Rhoads                     | 344241       | 11184130   | 0.99      |
| 700 | 60      | Confusion                   | 7       | 1           | 1       | Jerry Cantrell, Michael Starr, Layne Staley            | 344163       | 11183647   | 0.99      |
```



- 查询 `Album` 表，按 `ArtistId` 列的值进行升序排序，如果 `ArtistId` 的值相同，那么就按照 `AlbumId` 列的值进行降序排序，最后只返回前 50% 的数据：


```sql
%%sql
SELECT TOP 50 PERCENT *
FROM Album
ORDER BY ArtistId ASC, AlbumId DESC
```



```
|     | AlbumId | Title                                        | ArtistId |
|:----|:--------|:---------------------------------------------|:---------|
| 0   | 4       | Let There Be Rock                            | 1        |
| 1   | 1       | For Those About To Rock We Salute You        | 1        |
| 2   | 3       | Restless and Wild                            | 2        |
| 3   | 2       | Balls to the Wall                            | 2        |
| 4   | 5       | Big Ones                                     | 3        |
| 5   | 6       | Jagged Little Pill                           | 4        |
| ... | ...     | ...                                          | ...      |
| 169 | 162     | Motley Crue Greatest Hits                    | 109      |
| 170 | 164     | Nevermind                                    | 110      |
| 171 | 163     | From The Muddy Banks Of The Wishkah \[Live\] | 110      |
| 172 | 165     | Compositores                                 | 111      |
| 173 | 166     | Olodum                                       | 112      |
```



### (3) Top N 单独使用

在 SQL 中：如果 我们在 `SELECT` 语句中使用了 `TOP` 关键字，但是没有使用 `ORDER BY` 语句来指定排序方式，那么查询结果就是随机的前 `n` 行数据

- 这种方式最实用的场景就是，当我们尝试一个查询语句，但是又不想要查询结果太多行数据
- 这时候可以先使用 `TOP` 关键字来限制查询结果的行数
- 这样就可以快速地查看查询结果的前几行数据，来判断这个查询语句是否正确，或者查询结果是否符合我们的预期

我们来看以下例子：查询 `Track` 表中 `Name` 列带有 'Love' 或 'love' 的行，并且只返回前 5 行数据：


```sql
%%sql
SELECT TOP 5 *
FROM Track
WHERE Name LIKE '%Love%' OR Name LIKE '%love%'
```



```
|    | TrackId | Name                                         | AlbumId | MediaTypeId | GenreId | Composer                                                       | Milliseconds | Bytes    | UnitPrice |
|:---|:--------|:---------------------------------------------|:--------|:------------|:--------|:---------------------------------------------------------------|:-------------|:---------|:----------|
| 0  | 24      | Love In An Elevator                          | 5       | 1           | 1       | Steven Tyler, Joe Perry                                        | 321828       | 10552051 | 0.99      |
| 1  | 56      | Love, Hate, Love                             | 7       | 1           | 1       | Jerry Cantrell, Layne Staley                                   | 387134       | 12575396 | 0.99      |
| 2  | 195     | Let Me Love You Baby                         | 20      | 1           | 6       | Willie Dixon                                                   | 175386       | 5716994  | 0.99      |
| 3  | 335     | My Love                                      | 29      | 1           | 9       | Jauperi/Zeu Góes                                               | 203493       | 6772813  | 0.99      |
| 4  | 341     | The Girl I Love She Got Long Black Wavy Hair | 30      | 1           | 1       | Jimmy Page/John Bonham/John Estes/John Paul Jones/Robert Plant | 183327       | 5995686  | 0.99      |
```



这里我们注意一点：

- 一般的 SQL 数据库，数据在数据库中的存储的顺序是很玄幻的，可能是按照数据插入的顺序存储的，也可能是按照某个索引的顺序存储的，也可能是按照某个物理存储结构的顺序存储的
- 这些都是数据库内部实现细节，我们无法确定数据在数据库中的存储顺序
- 因此，如果我们在 SQL 查询中没有使用 `ORDER BY` 语句来指定排序方式，那么查询结果的行顺序就是随机的
- 也就是说每次执行这个查询语句，返回的前 5 行数据可能都是不一样的，这就是为什么我们说没有 `ORDER BY` 语句时，查询结果是随机的前 `n` 行数据
