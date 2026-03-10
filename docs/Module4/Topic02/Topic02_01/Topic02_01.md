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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>For Those About To Rock We Salute You</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Balls to the Wall</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Restless and Wild</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Let There Be Rock</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Big Ones</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>342</th>
      <td>Respighi:Pines of Rome</td>
    </tr>
    <tr>
      <th>343</th>
      <td>Schubert: The Late String Quartets &amp; String Qu...</td>
    </tr>
    <tr>
      <th>344</th>
      <td>Monteverdi: L'Orfeo</td>
    </tr>
    <tr>
      <th>345</th>
      <td>Mozart: Chamber Music</td>
    </tr>
    <tr>
      <th>346</th>
      <td>Koyaanisqatsi (Soundtrack from the Motion Pict...</td>
    </tr>
  </tbody>
</table>
<p>347 rows × 1 columns</p>
</div>



- 查询 `Album` 表中的 `Title` 和 `ArtistId` 列：


```sql
%%sql
SELECT Title, ArtistId
FROM Album
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
      <td>For Those About To Rock We Salute You</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Balls to the Wall</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Restless and Wild</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Let There Be Rock</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Big Ones</td>
      <td>3</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>342</th>
      <td>Respighi:Pines of Rome</td>
      <td>226</td>
    </tr>
    <tr>
      <th>343</th>
      <td>Schubert: The Late String Quartets &amp; String Qu...</td>
      <td>272</td>
    </tr>
    <tr>
      <th>344</th>
      <td>Monteverdi: L'Orfeo</td>
      <td>273</td>
    </tr>
    <tr>
      <th>345</th>
      <td>Mozart: Chamber Music</td>
      <td>274</td>
    </tr>
    <tr>
      <th>346</th>
      <td>Koyaanisqatsi (Soundtrack from the Motion Pict...</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>347 rows × 2 columns</p>
</div>



- 查询 `Album` 表中的所有列：


```sql
%%sql
SELECT *
FROM Album
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
      <td>2</td>
      <td>Balls to the Wall</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Restless and Wild</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Let There Be Rock</td>
      <td>1</td>
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
      <th>342</th>
      <td>343</td>
      <td>Respighi:Pines of Rome</td>
      <td>226</td>
    </tr>
    <tr>
      <th>343</th>
      <td>344</td>
      <td>Schubert: The Late String Quartets &amp; String Qu...</td>
      <td>272</td>
    </tr>
    <tr>
      <th>344</th>
      <td>345</td>
      <td>Monteverdi: L'Orfeo</td>
      <td>273</td>
    </tr>
    <tr>
      <th>345</th>
      <td>346</td>
      <td>Mozart: Chamber Music</td>
      <td>274</td>
    </tr>
    <tr>
      <th>346</th>
      <td>347</td>
      <td>Koyaanisqatsi (Soundtrack from the Motion Pict...</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>347 rows × 3 columns</p>
</div>



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
      <th>Album_Title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>For Those About To Rock We Salute You</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Balls to the Wall</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Restless and Wild</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Let There Be Rock</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Big Ones</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>342</th>
      <td>Respighi:Pines of Rome</td>
    </tr>
    <tr>
      <th>343</th>
      <td>Schubert: The Late String Quartets &amp; String Qu...</td>
    </tr>
    <tr>
      <th>344</th>
      <td>Monteverdi: L'Orfeo</td>
    </tr>
    <tr>
      <th>345</th>
      <td>Mozart: Chamber Music</td>
    </tr>
    <tr>
      <th>346</th>
      <td>Koyaanisqatsi (Soundtrack from the Motion Pict...</td>
    </tr>
  </tbody>
</table>
<p>347 rows × 1 columns</p>
</div>



- 查询 `Album` 表中的 `Title` 和 `ArtistId` 列，并且为 `Title` 列起别名为 `Album_Title`，为 `ArtistId` 列起别名为 `Artist_ID`，为 `Album` 表起别名为 `A`：


```sql
%%sql
SELECT
    Title AS Album_Title,
    ArtistId AS Artist_ID
FROM Album AS A
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
      <th>Album_Title</th>
      <th>Artist_ID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>For Those About To Rock We Salute You</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Balls to the Wall</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Restless and Wild</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Let There Be Rock</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Big Ones</td>
      <td>3</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>342</th>
      <td>Respighi:Pines of Rome</td>
      <td>226</td>
    </tr>
    <tr>
      <th>343</th>
      <td>Schubert: The Late String Quartets &amp; String Qu...</td>
      <td>272</td>
    </tr>
    <tr>
      <th>344</th>
      <td>Monteverdi: L'Orfeo</td>
      <td>273</td>
    </tr>
    <tr>
      <th>345</th>
      <td>Mozart: Chamber Music</td>
      <td>274</td>
    </tr>
    <tr>
      <th>346</th>
      <td>Koyaanisqatsi (Soundtrack from the Motion Pict...</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>347 rows × 2 columns</p>
</div>



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
    <img src="截屏2026-03-09 15.02.39.png" width="400">
</div>

- 在这张表中，当我们把 `Customer ID`、`City`、`Country` 这三列都查询出来的时候，每一行都是唯一的
- 但是如果我们只查询 `City` 这一列的时候，就会有重复的结果：

<div style="text-align: center;">
    <img src="截屏2026-03-09 15.06.25.png" width="100">
</div>

- 对 `City` 列进行去重查询之后，就只保留了不同的城市：

<div style="text-align: center;">
    <img src="截屏2026-03-09 15.06.45.png" width="100">
</div>

- 同样，如果我们查询 `Country` 列的时候，也会有重复的结果：

<div style="text-align: center;">
    <img src="截屏2026-03-09 15.10.00.png" width="100">
</div>

- 对 `Country` 列进行去重查询之后，就只保留了不同的国家：

<div style="text-align: center;">
    <img src="截屏2026-03-09 15.10.05.png" width="100">
</div>

当然，去重查询也可以对多列进行去重查询：

- 当我们查询 `City` 和 `Country` 两列的时候，就会有重复的结果：

<div style="text-align: center;">
    <img src="截屏2026-03-09 15.12.32.png" width="200">
</div>

- 对 `City` 和 `Country` 两列进行去重查询：

<div style="text-align: center;">
    <img src="截屏2026-03-09 15.12.37.png" width="200">
</div>

当然，如果我们选择查询两列或多列，那么这两列或多列要去重的话就得同时去重，否则就会出现无法匹配的情况：

- 例如我们决定查询 `City` 和 `Country` 两列，并且只对 `Country` 列进行去重查询，那么就会出现以下这种情况：

<div style="text-align: center;">
    <img src="截屏2026-03-09 15.18.11.png" width="300">
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>407</th>
      <td>59</td>
    </tr>
    <tr>
      <th>408</th>
      <td>59</td>
    </tr>
    <tr>
      <th>409</th>
      <td>59</td>
    </tr>
    <tr>
      <th>410</th>
      <td>59</td>
    </tr>
    <tr>
      <th>411</th>
      <td>59</td>
    </tr>
  </tbody>
</table>
<p>412 rows × 1 columns</p>
</div>



- 可以看到，在 `Invoice` 表中，`CustomerId` 列有很多重复的值，因为每一条数据其实就是对应一个订单，而一个客户可能会有多个订单，所以在 `CustomerId` 列中就会有重复的值
- 因此，如果我们想要查询 `Invoice` 表中有多少不同的客户，那么我们就可以使用 `DISTINCT` 关键字来进行去重查询：


```sql
%%sql
SELECT DISTINCT
    CustomerId
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
      <th>CustomerId</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
    </tr>
    <tr>
      <th>28</th>
      <td>29</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
    </tr>
    <tr>
      <th>30</th>
      <td>31</td>
    </tr>
    <tr>
      <th>31</th>
      <td>32</td>
    </tr>
    <tr>
      <th>32</th>
      <td>33</td>
    </tr>
    <tr>
      <th>33</th>
      <td>34</td>
    </tr>
    <tr>
      <th>34</th>
      <td>35</td>
    </tr>
    <tr>
      <th>35</th>
      <td>36</td>
    </tr>
    <tr>
      <th>36</th>
      <td>37</td>
    </tr>
    <tr>
      <th>37</th>
      <td>38</td>
    </tr>
    <tr>
      <th>38</th>
      <td>39</td>
    </tr>
    <tr>
      <th>39</th>
      <td>40</td>
    </tr>
    <tr>
      <th>40</th>
      <td>41</td>
    </tr>
    <tr>
      <th>41</th>
      <td>42</td>
    </tr>
    <tr>
      <th>42</th>
      <td>43</td>
    </tr>
    <tr>
      <th>43</th>
      <td>44</td>
    </tr>
    <tr>
      <th>44</th>
      <td>45</td>
    </tr>
    <tr>
      <th>45</th>
      <td>46</td>
    </tr>
    <tr>
      <th>46</th>
      <td>47</td>
    </tr>
    <tr>
      <th>47</th>
      <td>48</td>
    </tr>
    <tr>
      <th>48</th>
      <td>49</td>
    </tr>
    <tr>
      <th>49</th>
      <td>50</td>
    </tr>
    <tr>
      <th>50</th>
      <td>51</td>
    </tr>
    <tr>
      <th>51</th>
      <td>52</td>
    </tr>
    <tr>
      <th>52</th>
      <td>53</td>
    </tr>
    <tr>
      <th>53</th>
      <td>54</td>
    </tr>
    <tr>
      <th>54</th>
      <td>55</td>
    </tr>
    <tr>
      <th>55</th>
      <td>56</td>
    </tr>
    <tr>
      <th>56</th>
      <td>57</td>
    </tr>
    <tr>
      <th>57</th>
      <td>58</td>
    </tr>
    <tr>
      <th>58</th>
      <td>59</td>
    </tr>
  </tbody>
</table>
</div>



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
      <th>BillingCountry</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Brazil</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Germany</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Norway</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Czech Republic</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Czech Republic</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Austria</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Belgium</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Denmark</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>Brazil</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>Brazil</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>Brazil</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>Brazil</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>USA</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>USA</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>USA</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>USA</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>USA</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>USA</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>USA</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>USA</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24</td>
      <td>USA</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>USA</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26</td>
      <td>USA</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27</td>
      <td>USA</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>USA</td>
    </tr>
    <tr>
      <th>28</th>
      <td>29</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>30</th>
      <td>31</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>31</th>
      <td>32</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>32</th>
      <td>33</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>33</th>
      <td>34</td>
      <td>Portugal</td>
    </tr>
    <tr>
      <th>34</th>
      <td>35</td>
      <td>Portugal</td>
    </tr>
    <tr>
      <th>35</th>
      <td>36</td>
      <td>Germany</td>
    </tr>
    <tr>
      <th>36</th>
      <td>37</td>
      <td>Germany</td>
    </tr>
    <tr>
      <th>37</th>
      <td>38</td>
      <td>Germany</td>
    </tr>
    <tr>
      <th>38</th>
      <td>39</td>
      <td>France</td>
    </tr>
    <tr>
      <th>39</th>
      <td>40</td>
      <td>France</td>
    </tr>
    <tr>
      <th>40</th>
      <td>41</td>
      <td>France</td>
    </tr>
    <tr>
      <th>41</th>
      <td>42</td>
      <td>France</td>
    </tr>
    <tr>
      <th>42</th>
      <td>43</td>
      <td>France</td>
    </tr>
    <tr>
      <th>43</th>
      <td>44</td>
      <td>Finland</td>
    </tr>
    <tr>
      <th>44</th>
      <td>45</td>
      <td>Hungary</td>
    </tr>
    <tr>
      <th>45</th>
      <td>46</td>
      <td>Ireland</td>
    </tr>
    <tr>
      <th>46</th>
      <td>47</td>
      <td>Italy</td>
    </tr>
    <tr>
      <th>47</th>
      <td>48</td>
      <td>Netherlands</td>
    </tr>
    <tr>
      <th>48</th>
      <td>49</td>
      <td>Poland</td>
    </tr>
    <tr>
      <th>49</th>
      <td>50</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>50</th>
      <td>51</td>
      <td>Sweden</td>
    </tr>
    <tr>
      <th>51</th>
      <td>52</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>52</th>
      <td>53</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>53</th>
      <td>54</td>
      <td>United Kingdom</td>
    </tr>
    <tr>
      <th>54</th>
      <td>55</td>
      <td>Australia</td>
    </tr>
    <tr>
      <th>55</th>
      <td>56</td>
      <td>Argentina</td>
    </tr>
    <tr>
      <th>56</th>
      <td>57</td>
      <td>Chile</td>
    </tr>
    <tr>
      <th>57</th>
      <td>58</td>
      <td>India</td>
    </tr>
    <tr>
      <th>58</th>
      <td>59</td>
      <td>India</td>
    </tr>
  </tbody>
</table>
</div>



- 再比如，查询 `Invoice` 表中每个顾客的账单国家和账单邮编：


```sql
%%sql
SELECT DISTINCT
    CustomerId,
    BillingCountry,
    BillingPostalCode
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
      <th>CustomerId</th>
      <th>BillingCountry</th>
      <th>BillingPostalCode</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Brazil</td>
      <td>12227-000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Germany</td>
      <td>70174</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Canada</td>
      <td>H2G 1A7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Norway</td>
      <td>0171</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Czech Republic</td>
      <td>14700</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Czech Republic</td>
      <td>14300</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Austria</td>
      <td>1010</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Belgium</td>
      <td>1000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Denmark</td>
      <td>1720</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>Brazil</td>
      <td>01007-010</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>Brazil</td>
      <td>01310-200</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>Brazil</td>
      <td>20040-020</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>Brazil</td>
      <td>71020-677</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>Canada</td>
      <td>T6G 2C7</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>Canada</td>
      <td>V6C 1G8</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>USA</td>
      <td>94043-1351</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>USA</td>
      <td>98052-8300</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>USA</td>
      <td>10012-2612</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>USA</td>
      <td>95014</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>USA</td>
      <td>94040-111</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>USA</td>
      <td>89503</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>USA</td>
      <td>32801</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>USA</td>
      <td>2113</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24</td>
      <td>USA</td>
      <td>60611</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>USA</td>
      <td>53703</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26</td>
      <td>USA</td>
      <td>76110</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27</td>
      <td>USA</td>
      <td>85719</td>
    </tr>
    <tr>
      <th>27</th>
      <td>28</td>
      <td>USA</td>
      <td>84102</td>
    </tr>
    <tr>
      <th>28</th>
      <td>29</td>
      <td>Canada</td>
      <td>M6J 1V1</td>
    </tr>
    <tr>
      <th>29</th>
      <td>30</td>
      <td>Canada</td>
      <td>K2P 1L7</td>
    </tr>
    <tr>
      <th>30</th>
      <td>31</td>
      <td>Canada</td>
      <td>B3S 1C5</td>
    </tr>
    <tr>
      <th>31</th>
      <td>32</td>
      <td>Canada</td>
      <td>R3L 2B9</td>
    </tr>
    <tr>
      <th>32</th>
      <td>33</td>
      <td>Canada</td>
      <td>X1A 1N6</td>
    </tr>
    <tr>
      <th>33</th>
      <td>34</td>
      <td>Portugal</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>34</th>
      <td>35</td>
      <td>Portugal</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35</th>
      <td>36</td>
      <td>Germany</td>
      <td>10789</td>
    </tr>
    <tr>
      <th>36</th>
      <td>37</td>
      <td>Germany</td>
      <td>60316</td>
    </tr>
    <tr>
      <th>37</th>
      <td>38</td>
      <td>Germany</td>
      <td>10779</td>
    </tr>
    <tr>
      <th>38</th>
      <td>39</td>
      <td>France</td>
      <td>75009</td>
    </tr>
    <tr>
      <th>39</th>
      <td>40</td>
      <td>France</td>
      <td>75002</td>
    </tr>
    <tr>
      <th>40</th>
      <td>41</td>
      <td>France</td>
      <td>69002</td>
    </tr>
    <tr>
      <th>41</th>
      <td>42</td>
      <td>France</td>
      <td>33000</td>
    </tr>
    <tr>
      <th>42</th>
      <td>43</td>
      <td>France</td>
      <td>21000</td>
    </tr>
    <tr>
      <th>43</th>
      <td>44</td>
      <td>Finland</td>
      <td>00530</td>
    </tr>
    <tr>
      <th>44</th>
      <td>45</td>
      <td>Hungary</td>
      <td>H-1073</td>
    </tr>
    <tr>
      <th>45</th>
      <td>46</td>
      <td>Ireland</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>46</th>
      <td>47</td>
      <td>Italy</td>
      <td>00192</td>
    </tr>
    <tr>
      <th>47</th>
      <td>48</td>
      <td>Netherlands</td>
      <td>1016</td>
    </tr>
    <tr>
      <th>48</th>
      <td>49</td>
      <td>Poland</td>
      <td>00-358</td>
    </tr>
    <tr>
      <th>49</th>
      <td>50</td>
      <td>Spain</td>
      <td>28015</td>
    </tr>
    <tr>
      <th>50</th>
      <td>51</td>
      <td>Sweden</td>
      <td>11230</td>
    </tr>
    <tr>
      <th>51</th>
      <td>52</td>
      <td>United Kingdom</td>
      <td>N1 5LH</td>
    </tr>
    <tr>
      <th>52</th>
      <td>53</td>
      <td>United Kingdom</td>
      <td>SW1V 3EN</td>
    </tr>
    <tr>
      <th>53</th>
      <td>54</td>
      <td>United Kingdom</td>
      <td>EH4 1HH</td>
    </tr>
    <tr>
      <th>54</th>
      <td>55</td>
      <td>Australia</td>
      <td>2010</td>
    </tr>
    <tr>
      <th>55</th>
      <td>56</td>
      <td>Argentina</td>
      <td>1106</td>
    </tr>
    <tr>
      <th>56</th>
      <td>57</td>
      <td>Chile</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>57</th>
      <td>58</td>
      <td>India</td>
      <td>110017</td>
    </tr>
    <tr>
      <th>58</th>
      <td>59</td>
      <td>India</td>
      <td>560001</td>
    </tr>
  </tbody>
</table>
</div>



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
      <td>For Those About To Rock We Salute You</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Balls to the Wall</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Restless and Wild</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Let There Be Rock</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Big Ones</td>
      <td>3</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>342</th>
      <td>Respighi:Pines of Rome</td>
      <td>226</td>
    </tr>
    <tr>
      <th>343</th>
      <td>Schubert: The Late String Quartets &amp; String Qu...</td>
      <td>272</td>
    </tr>
    <tr>
      <th>344</th>
      <td>Monteverdi: L'Orfeo</td>
      <td>273</td>
    </tr>
    <tr>
      <th>345</th>
      <td>Mozart: Chamber Music</td>
      <td>274</td>
    </tr>
    <tr>
      <th>346</th>
      <td>Koyaanisqatsi (Soundtrack from the Motion Pict...</td>
      <td>275</td>
    </tr>
  </tbody>
</table>
<p>347 rows × 2 columns</p>
</div>



## 4. SELECT 语句中的数据运算

### (1) SELECT 语句中的数值计算

在 SQL 中，我们可以在 `SELECT` 语句中对数值列进行加减乘除等各种计算：

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
      <th>NewPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0.99</td>
      <td>1.089</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>0.99</td>
      <td>1.089</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>0.99</td>
      <td>1.089</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>0.99</td>
      <td>1.089</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0.99</td>
      <td>1.089</td>
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
      <td>1.089</td>
    </tr>
    <tr>
      <th>3499</th>
      <td>3500</td>
      <td>0.99</td>
      <td>1.089</td>
    </tr>
    <tr>
      <th>3500</th>
      <td>3501</td>
      <td>0.99</td>
      <td>1.089</td>
    </tr>
    <tr>
      <th>3501</th>
      <td>3502</td>
      <td>0.99</td>
      <td>1.089</td>
    </tr>
    <tr>
      <th>3502</th>
      <td>3503</td>
      <td>0.99</td>
      <td>1.089</td>
    </tr>
  </tbody>
</table>
<p>3503 rows × 3 columns</p>
</div>



- 例如，我们要在销售表中计算每笔订单中每首歌的总价：


```sql
%%sql
SELECT
    InvoiceId,
    TrackId,
    UnitPrice * Quantity AS TotalPrice -- 总价
FROM InvoiceLine
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
      <th>TrackId</th>
      <th>TotalPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>4</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>6</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>8</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>10</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2235</th>
      <td>411</td>
      <td>3136</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>2236</th>
      <td>411</td>
      <td>3145</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>2237</th>
      <td>411</td>
      <td>3154</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>2238</th>
      <td>411</td>
      <td>3163</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>2239</th>
      <td>412</td>
      <td>3177</td>
      <td>1.99</td>
    </tr>
  </tbody>
</table>
<p>2240 rows × 3 columns</p>
</div>



- 例如，我们算一下每首歌一秒钟的价格（虽然现实意义不大，但是不妨碍我们可以这样计算）：


```sql
%%sql
SELECT
    TrackId,
    UnitPrice / Milliseconds * 1000 AS PricePerSecond
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
      <th>PricePerSecond</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0.002880</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>0.002890</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>0.004293</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>0.003928</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0.002637</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3498</th>
      <td>3499</td>
      <td>0.003453</td>
    </tr>
    <tr>
      <th>3499</th>
      <td>3500</td>
      <td>0.007112</td>
    </tr>
    <tr>
      <th>3500</th>
      <td>3501</td>
      <td>0.014856</td>
    </tr>
    <tr>
      <th>3501</th>
      <td>3502</td>
      <td>0.004473</td>
    </tr>
    <tr>
      <th>3502</th>
      <td>3503</td>
      <td>0.004806</td>
    </tr>
  </tbody>
</table>
<p>3503 rows × 2 columns</p>
</div>



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

    Cell In[33], line 1
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
      <th>PricePerSecond</th>
      <th>PricePerMinute</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0.002880</td>
      <td>0.172816</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>0.002890</td>
      <td>0.173399</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>0.004293</td>
      <td>0.257568</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>0.003928</td>
      <td>0.235667</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0.002637</td>
      <td>0.158224</td>
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
      <td>0.003453</td>
      <td>0.207156</td>
    </tr>
    <tr>
      <th>3499</th>
      <td>3500</td>
      <td>0.007112</td>
      <td>0.426724</td>
    </tr>
    <tr>
      <th>3500</th>
      <td>3501</td>
      <td>0.014856</td>
      <td>0.891370</td>
    </tr>
    <tr>
      <th>3501</th>
      <td>3502</td>
      <td>0.004473</td>
      <td>0.268376</td>
    </tr>
    <tr>
      <th>3502</th>
      <td>3503</td>
      <td>0.004806</td>
      <td>0.288343</td>
    </tr>
  </tbody>
</table>
<p>3503 rows × 3 columns</p>
</div>



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


