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
      <th>Title</th>
      <th>ArtistId</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>...And Justice For All</td>
      <td>50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[1997] Black Light Syndrome</td>
      <td>136</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20th Century Masters - The Millennium Collecti...</td>
      <td>179</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A Copland Celebration, Vol. I</td>
      <td>230</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A Matter of Life and Death</td>
      <td>90</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>342</th>
      <td>War</td>
      <td>150</td>
    </tr>
    <tr>
      <th>343</th>
      <td>Warner 25 Anos</td>
      <td>6</td>
    </tr>
    <tr>
      <th>344</th>
      <td>Weill: The Seven Deadly Sins</td>
      <td>264</td>
    </tr>
    <tr>
      <th>345</th>
      <td>Worlds</td>
      <td>202</td>
    </tr>
    <tr>
      <th>346</th>
      <td>Zooropa</td>
      <td>150</td>
    </tr>
  </tbody>
</table>
<p>347 rows × 2 columns</p>
</div>



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
      <th>UnitPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Love In An Elevator</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Love, Hate, Love</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Let Me Love You Baby</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>My Love</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>4</th>
      <td>The Girl I Love She Got Long Black Wavy Hair</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>109</th>
      <td>Love Comes</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Arms Around Your Love</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>111</th>
      <td>Love Is a Losing Game</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>112</th>
      <td>I Heard Love Is Blind</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>113</th>
      <td>(There Is) No Greater Love (Teo Licks)</td>
      <td>0.99</td>
    </tr>
  </tbody>
</table>
<p>114 rows × 2 columns</p>
</div>



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
      <th>Title</th>
      <th>ArtistId</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Zooropa</td>
      <td>150</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Worlds</td>
      <td>202</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Weill: The Seven Deadly Sins</td>
      <td>264</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Warner 25 Anos</td>
      <td>6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>War</td>
      <td>150</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>342</th>
      <td>A Matter of Life and Death</td>
      <td>90</td>
    </tr>
    <tr>
      <th>343</th>
      <td>A Copland Celebration, Vol. I</td>
      <td>230</td>
    </tr>
    <tr>
      <th>344</th>
      <td>20th Century Masters - The Millennium Collecti...</td>
      <td>179</td>
    </tr>
    <tr>
      <th>345</th>
      <td>[1997] Black Light Syndrome</td>
      <td>136</td>
    </tr>
    <tr>
      <th>346</th>
      <td>...And Justice For All</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
<p>347 rows × 2 columns</p>
</div>



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
      <th>UnitPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Love In An Elevator</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Love, Hate, Love</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Let Me Love You Baby</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>My Love</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>4</th>
      <td>The Girl I Love She Got Long Black Wavy Hair</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>109</th>
      <td>Love Comes</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Arms Around Your Love</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>111</th>
      <td>Love Is a Losing Game</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>112</th>
      <td>I Heard Love Is Blind</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>113</th>
      <td>(There Is) No Greater Love (Teo Licks)</td>
      <td>0.99</td>
    </tr>
  </tbody>
</table>
<p>114 rows × 2 columns</p>
</div>



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
      <th>UnitPrice</th>
      <th>Milliseconds</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Love And Marriage</td>
      <td>0.99</td>
      <td>89730</td>
    </tr>
    <tr>
      <th>1</th>
      <td>I Heard Love Is Blind</td>
      <td>0.99</td>
      <td>129666</td>
    </tr>
    <tr>
      <th>2</th>
      <td>What Now My Love</td>
      <td>0.99</td>
      <td>149995</td>
    </tr>
    <tr>
      <th>3</th>
      <td>When I Had Your Love</td>
      <td>0.99</td>
      <td>152424</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Love Is a Losing Game</td>
      <td>0.99</td>
      <td>154386</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>109</th>
      <td>Old Love</td>
      <td>0.99</td>
      <td>472920</td>
    </tr>
    <tr>
      <th>110</th>
      <td>The Thin Line Between Love &amp; Hate</td>
      <td>0.99</td>
      <td>506801</td>
    </tr>
    <tr>
      <th>111</th>
      <td>Jesus Of Suburbia / City Of The Damned / I Don...</td>
      <td>0.99</td>
      <td>548336</td>
    </tr>
    <tr>
      <th>112</th>
      <td>Whole Lotta Love (Medley)</td>
      <td>0.99</td>
      <td>825103</td>
    </tr>
    <tr>
      <th>113</th>
      <td>Whole Lotta Love</td>
      <td>0.99</td>
      <td>863895</td>
    </tr>
  </tbody>
</table>
<p>114 rows × 3 columns</p>
</div>



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
      <th>Title</th>
      <th>ArtistId</th>
      <th>AlbumId</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Let There Be Rock</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>For Those About To Rock We Salute You</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Restless and Wild</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Balls to the Wall</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Big Ones</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>342</th>
      <td>Locatelli: Concertos for Violin, Strings and C...</td>
      <td>271</td>
      <td>342</td>
    </tr>
    <tr>
      <th>343</th>
      <td>Schubert: The Late String Quartets &amp; String Qu...</td>
      <td>272</td>
      <td>344</td>
    </tr>
    <tr>
      <th>344</th>
      <td>Monteverdi: L'Orfeo</td>
      <td>273</td>
      <td>345</td>
    </tr>
    <tr>
      <th>345</th>
      <td>Mozart: Chamber Music</td>
      <td>274</td>
      <td>346</td>
    </tr>
    <tr>
      <th>346</th>
      <td>Koyaanisqatsi (Soundtrack from the Motion Pict...</td>
      <td>275</td>
      <td>347</td>
    </tr>
  </tbody>
</table>
<p>347 rows × 3 columns</p>
</div>



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
    <tr>
      <th>2</th>
      <td>3244</td>
      <td>Greetings from Earth, Pt. 1</td>
      <td>253</td>
      <td>3</td>
      <td>20</td>
      <td>NaN</td>
      <td>2960293</td>
      <td>536824558</td>
      <td>1.99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3242</td>
      <td>The Man With Nine Lives</td>
      <td>253</td>
      <td>3</td>
      <td>20</td>
      <td>NaN</td>
      <td>2956998</td>
      <td>577829804</td>
      <td>1.99</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3227</td>
      <td>Battlestar Galactica, Pt. 2</td>
      <td>253</td>
      <td>3</td>
      <td>20</td>
      <td>NaN</td>
      <td>2956081</td>
      <td>521387924</td>
      <td>1.99</td>
    </tr>
  </tbody>
</table>
</div>



- 查询 `Album` 表，按 `ArtistId` 列的值进行升序排序，如果 `ArtistId` 的值相同，那么就按照 `AlbumId` 列的值进行降序排序，最后只返回前 10 行数据：


```sql
%%sql
SELECT TOP 10 *
FROM Album
ORDER BY ArtistId ASC, AlbumId DESC
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
      <td>4</td>
      <td>Let There Be Rock</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>For Those About To Rock We Salute You</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Restless and Wild</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>Balls to the Wall</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Big Ones</td>
      <td>3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Jagged Little Pill</td>
      <td>4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Facelift</td>
      <td>5</td>
    </tr>
    <tr>
      <th>7</th>
      <td>34</td>
      <td>Chill: Brazil (Disc 2)</td>
      <td>6</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>Warner 25 Anos</td>
      <td>6</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>Plays Metallica By Four Cellos</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>



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
    <tr>
      <th>2</th>
      <td>3244</td>
      <td>Greetings from Earth, Pt. 1</td>
      <td>253</td>
      <td>3</td>
      <td>20</td>
      <td>NaN</td>
      <td>2960293</td>
      <td>536824558</td>
      <td>1.99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3242</td>
      <td>The Man With Nine Lives</td>
      <td>253</td>
      <td>3</td>
      <td>20</td>
      <td>NaN</td>
      <td>2956998</td>
      <td>577829804</td>
      <td>1.99</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3227</td>
      <td>Battlestar Galactica, Pt. 2</td>
      <td>253</td>
      <td>3</td>
      <td>20</td>
      <td>NaN</td>
      <td>2956081</td>
      <td>521387924</td>
      <td>1.99</td>
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
      <th>696</th>
      <td>493</td>
      <td>Love Is Blind</td>
      <td>40</td>
      <td>1</td>
      <td>1</td>
      <td>David Coverdale/Earl Slick</td>
      <td>344999</td>
      <td>11409720</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>697</th>
      <td>1383</td>
      <td>Stranger in a Strange Land</td>
      <td>111</td>
      <td>1</td>
      <td>3</td>
      <td>Adrian Smith</td>
      <td>344502</td>
      <td>8270899</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>698</th>
      <td>558</td>
      <td>Viradouro</td>
      <td>45</td>
      <td>1</td>
      <td>7</td>
      <td>Dadinho/Gilbreto Gomes/Gustavo/P.C. Portugal/R...</td>
      <td>344320</td>
      <td>11484362</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>699</th>
      <td>2102</td>
      <td>Mr. Crowley</td>
      <td>174</td>
      <td>1</td>
      <td>3</td>
      <td>O. Osbourne, R. Daisley, R. Rhoads</td>
      <td>344241</td>
      <td>11184130</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>700</th>
      <td>60</td>
      <td>Confusion</td>
      <td>7</td>
      <td>1</td>
      <td>1</td>
      <td>Jerry Cantrell, Michael Starr, Layne Staley</td>
      <td>344163</td>
      <td>11183647</td>
      <td>0.99</td>
    </tr>
  </tbody>
</table>
<p>701 rows × 9 columns</p>
</div>



- 查询 `Album` 表，按 `ArtistId` 列的值进行升序排序，如果 `ArtistId` 的值相同，那么就按照 `AlbumId` 列的值进行降序排序，最后只返回前 50% 的数据：


```sql
%%sql
SELECT TOP 50 PERCENT *
FROM Album
ORDER BY ArtistId ASC, AlbumId DESC
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
      <td>4</td>
      <td>Let There Be Rock</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>For Those About To Rock We Salute You</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Restless and Wild</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>Balls to the Wall</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Big Ones</td>
      <td>3</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>169</th>
      <td>162</td>
      <td>Motley Crue Greatest Hits</td>
      <td>109</td>
    </tr>
    <tr>
      <th>170</th>
      <td>164</td>
      <td>Nevermind</td>
      <td>110</td>
    </tr>
    <tr>
      <th>171</th>
      <td>163</td>
      <td>From The Muddy Banks Of The Wishkah [Live]</td>
      <td>110</td>
    </tr>
    <tr>
      <th>172</th>
      <td>165</td>
      <td>Compositores</td>
      <td>111</td>
    </tr>
    <tr>
      <th>173</th>
      <td>166</td>
      <td>Olodum</td>
      <td>112</td>
    </tr>
  </tbody>
</table>
<p>174 rows × 3 columns</p>
</div>



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
  </tbody>
</table>
</div>



这里我们注意一点：

- 一般的 SQL 数据库，数据在数据库中的存储的顺序是很玄幻的，可能是按照数据插入的顺序存储的，也可能是按照某个索引的顺序存储的，也可能是按照某个物理存储结构的顺序存储的
- 这些都是数据库内部实现细节，我们无法确定数据在数据库中的存储顺序
- 因此，如果我们在 SQL 查询中没有使用 `ORDER BY` 语句来指定排序方式，那么查询结果的行顺序就是随机的
- 也就是说每次执行这个查询语句，返回的前 5 行数据可能都是不一样的，这就是为什么我们说没有 `ORDER BY` 语句时，查询结果是随机的前 `n` 行数据
