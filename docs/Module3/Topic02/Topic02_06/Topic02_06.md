# Topic 2.6 - Pandas 中的数据筛选

在本节开始前，我们先导入一下 Pandas 库：


```python
import pandas as pd
```

## 1. 基于条件的数据筛选

在前面的章节中，我们介绍了按行和列的索引进行数据筛选，在实际的数据分析中，更常见的是基于条件进行数据筛选。

### (1) 基于单个条件的筛选

在 Pandas 中，可以使用布尔索引来实现基于单个条件的筛选

- 格式是 `df[条件]`，其中 `条件` 的格式是：`df["列名"]` 后面跟上比较运算符和具体的值，注意这里不能只跟列名
- 例如，在学生成绩表中筛选出数学成绩大于 90 的记录：`df1[df1["math"] > 90]`


```python
df1 = pd.read_csv("../data/students.csv")
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




```python
df1[df1["math"] > 90]
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
      <th>5</th>
      <td>Frank Taylor</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>90</td>
      <td>92</td>
      <td>89</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Ivy Moore</td>
      <td>3</td>
      <td>Female</td>
      <td>22</td>
      <td>91</td>
      <td>93</td>
      <td>90</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Leo Walker</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>95</td>
      <td>94</td>
      <td>96</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Rachel Hill</td>
      <td>3</td>
      <td>Female</td>
      <td>18</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Vera Baker</td>
      <td>1</td>
      <td>Female</td>
      <td>21</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Brian Turner</td>
      <td>1</td>
      <td>Male</td>
      <td>18</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Ella Parker</td>
      <td>1</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Jason Sanchez</td>
      <td>3</td>
      <td>Male</td>
      <td>20</td>
      <td>91</td>
      <td>93</td>
      <td>92</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Ophelia Morgan</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Ryan Howard</td>
      <td>2</td>
      <td>Male</td>
      <td>22</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Wendy Wood</td>
      <td>1</td>
      <td>Female</td>
      <td>22</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Zoe Kelly</td>
      <td>1</td>
      <td>Female</td>
      <td>21</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Daisy Ross</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Julia Long</td>
      <td>2</td>
      <td>Female</td>
      <td>21</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Nina Washington</td>
      <td>3</td>
      <td>Female</td>
      <td>20</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Sara Alexander</td>
      <td>1</td>
      <td>Female</td>
      <td>19</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Ursula Griffin</td>
      <td>3</td>
      <td>Female</td>
      <td>21</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Abby Sullivan</td>
      <td>3</td>
      <td>Female</td>
      <td>18</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Felix Stone</td>
      <td>2</td>
      <td>Male</td>
      <td>18</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Irene Olson</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
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
  </tbody>
</table>
</div>



事实上：

- `df1["math"] > 90` 会创建一个新的 Series，是布尔类型的，表示每一行的数学成绩是否大于 90
- 将这个布尔 Series 再传入 `df1[...]` 中，就会只保留对应为 `True` 的那些行


```python
df1["math"] > 90
```




    0     False
    1     False
    2     False
    3     False
    4     False
          ...  
    86    False
    87    False
    88     True
    89    False
    90    False
    Name: math, Length: 91, dtype: bool



### (2) 基于多个条件的筛选

如果基于多个条件进行筛选，可以使用逻辑运算符将多个条件组合起来：

- Pandas 中的逻辑运算符和 Python 中的有所不同：
  
  - 逻辑与（AND）：`&`
  - 逻辑或（OR）：`|`
  - 逻辑非（NOT）：`~`

- 并且，每个条件都需要用括号括起来

例如：

- 我们想筛选出数学成绩大于 90 且英语成绩大于 85 的记录：


```python
df1[(df1["math"] > 90) & (df1["english"] >= 85)]
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
      <th>5</th>
      <td>Frank Taylor</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>90</td>
      <td>92</td>
      <td>89</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Ivy Moore</td>
      <td>3</td>
      <td>Female</td>
      <td>22</td>
      <td>91</td>
      <td>93</td>
      <td>90</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Leo Walker</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>95</td>
      <td>94</td>
      <td>96</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Rachel Hill</td>
      <td>3</td>
      <td>Female</td>
      <td>18</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Vera Baker</td>
      <td>1</td>
      <td>Female</td>
      <td>21</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Brian Turner</td>
      <td>1</td>
      <td>Male</td>
      <td>18</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Ella Parker</td>
      <td>1</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Jason Sanchez</td>
      <td>3</td>
      <td>Male</td>
      <td>20</td>
      <td>91</td>
      <td>93</td>
      <td>92</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Ophelia Morgan</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Ryan Howard</td>
      <td>2</td>
      <td>Male</td>
      <td>22</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Wendy Wood</td>
      <td>1</td>
      <td>Female</td>
      <td>22</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Zoe Kelly</td>
      <td>1</td>
      <td>Female</td>
      <td>21</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Daisy Ross</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Julia Long</td>
      <td>2</td>
      <td>Female</td>
      <td>21</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Nina Washington</td>
      <td>3</td>
      <td>Female</td>
      <td>20</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Sara Alexander</td>
      <td>1</td>
      <td>Female</td>
      <td>19</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Ursula Griffin</td>
      <td>3</td>
      <td>Female</td>
      <td>21</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Abby Sullivan</td>
      <td>3</td>
      <td>Female</td>
      <td>18</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Felix Stone</td>
      <td>2</td>
      <td>Male</td>
      <td>18</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Irene Olson</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
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
  </tbody>
</table>
</div>



- 数学成绩大于 90 且英语和语文至少一个大于 70 的记录：


```python
df1[(df1["math"] > 90) & ( (df1["english"] >= 70) | (df1["chinese"] >= 70) )]
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
      <th>5</th>
      <td>Frank Taylor</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>90</td>
      <td>92</td>
      <td>89</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Ivy Moore</td>
      <td>3</td>
      <td>Female</td>
      <td>22</td>
      <td>91</td>
      <td>93</td>
      <td>90</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Leo Walker</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>95</td>
      <td>94</td>
      <td>96</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Rachel Hill</td>
      <td>3</td>
      <td>Female</td>
      <td>18</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Vera Baker</td>
      <td>1</td>
      <td>Female</td>
      <td>21</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Brian Turner</td>
      <td>1</td>
      <td>Male</td>
      <td>18</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Ella Parker</td>
      <td>1</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Jason Sanchez</td>
      <td>3</td>
      <td>Male</td>
      <td>20</td>
      <td>91</td>
      <td>93</td>
      <td>92</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Ophelia Morgan</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Ryan Howard</td>
      <td>2</td>
      <td>Male</td>
      <td>22</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Wendy Wood</td>
      <td>1</td>
      <td>Female</td>
      <td>22</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Zoe Kelly</td>
      <td>1</td>
      <td>Female</td>
      <td>21</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Daisy Ross</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Julia Long</td>
      <td>2</td>
      <td>Female</td>
      <td>21</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Nina Washington</td>
      <td>3</td>
      <td>Female</td>
      <td>20</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Sara Alexander</td>
      <td>1</td>
      <td>Female</td>
      <td>19</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Ursula Griffin</td>
      <td>3</td>
      <td>Female</td>
      <td>21</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Abby Sullivan</td>
      <td>3</td>
      <td>Female</td>
      <td>18</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Felix Stone</td>
      <td>2</td>
      <td>Male</td>
      <td>18</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Irene Olson</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
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
  </tbody>
</table>
</div>



### (3) 高级筛选方法

除了常见的数值判断之外，Pandas 还支持一些更高级的筛选方法：

- 范围筛选：使用 `between()` 方法筛选在某个范围内的值，例如筛选数学成绩在 80 到 90之 间的记录（包括边界值 80 和 90）：


```python
df1[df1["math"].between(80, 90)]
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
      <th>6</th>
      <td>Grace Anderson</td>
      <td>1</td>
      <td>Female</td>
      <td>20</td>
      <td>84</td>
      <td>82</td>
      <td>86</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Jack Martin</td>
      <td>1</td>
      <td>Male</td>
      <td>19</td>
      <td>87</td>
      <td>85</td>
      <td>88</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Mia Hall</td>
      <td>1</td>
      <td>Female</td>
      <td>18</td>
      <td>82</td>
      <td>80</td>
      <td>84</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Nathan Young</td>
      <td>2</td>
      <td>Male</td>
      <td>22</td>
      <td>88</td>
      <td>86</td>
      <td>87</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Paul Wright</td>
      <td>1</td>
      <td>Male</td>
      <td>20</td>
      <td>85</td>
      <td>83</td>
      <td>84</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Sam Scott</td>
      <td>1</td>
      <td>Male</td>
      <td>22</td>
      <td>83</td>
      <td>80</td>
      <td>82</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Tina Green</td>
      <td>2</td>
      <td>Female</td>
      <td>19</td>
      <td>86</td>
      <td>88</td>
      <td>85</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Xander Carter</td>
      <td>3</td>
      <td>Male</td>
      <td>22</td>
      <td>89</td>
      <td>88</td>
      <td>90</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Yara Mitchell</td>
      <td>1</td>
      <td>Female</td>
      <td>19</td>
      <td>84</td>
      <td>82</td>
      <td>83</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Zack Perez</td>
      <td>2</td>
      <td>Male</td>
      <td>20</td>
      <td>88</td>
      <td>90</td>
      <td>87</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Amy Roberts</td>
      <td>3</td>
      <td>Female</td>
      <td>21</td>
      <td>81</td>
      <td>80</td>
      <td>82</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Dylan Campbell</td>
      <td>3</td>
      <td>Male</td>
      <td>19</td>
      <td>85</td>
      <td>83</td>
      <td>86</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Gina Edwards</td>
      <td>3</td>
      <td>Female</td>
      <td>18</td>
      <td>82</td>
      <td>80</td>
      <td>81</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Harry Collins</td>
      <td>1</td>
      <td>Male</td>
      <td>22</td>
      <td>87</td>
      <td>85</td>
      <td>88</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Kelly Morris</td>
      <td>1</td>
      <td>Female</td>
      <td>21</td>
      <td>83</td>
      <td>82</td>
      <td>84</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Liam Rogers</td>
      <td>2</td>
      <td>Male</td>
      <td>18</td>
      <td>88</td>
      <td>87</td>
      <td>89</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Noah Cook</td>
      <td>1</td>
      <td>Male</td>
      <td>19</td>
      <td>86</td>
      <td>85</td>
      <td>87</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Queen Foster</td>
      <td>1</td>
      <td>Female</td>
      <td>18</td>
      <td>84</td>
      <td>82</td>
      <td>83</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Tom Cox</td>
      <td>1</td>
      <td>Male</td>
      <td>20</td>
      <td>85</td>
      <td>83</td>
      <td>84</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Uma Diaz</td>
      <td>2</td>
      <td>Female</td>
      <td>21</td>
      <td>89</td>
      <td>88</td>
      <td>90</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Victor Richardson</td>
      <td>3</td>
      <td>Male</td>
      <td>18</td>
      <td>81</td>
      <td>80</td>
      <td>82</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Yusuf Brooks</td>
      <td>3</td>
      <td>Male</td>
      <td>20</td>
      <td>86</td>
      <td>85</td>
      <td>87</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Bella Bennett</td>
      <td>3</td>
      <td>Female</td>
      <td>22</td>
      <td>84</td>
      <td>82</td>
      <td>83</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Chris Barnes</td>
      <td>1</td>
      <td>Male</td>
      <td>19</td>
      <td>88</td>
      <td>87</td>
      <td>89</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Fiona Coleman</td>
      <td>1</td>
      <td>Female</td>
      <td>18</td>
      <td>82</td>
      <td>80</td>
      <td>81</td>
    </tr>
    <tr>
      <th>58</th>
      <td>George Jenkins</td>
      <td>2</td>
      <td>Male</td>
      <td>22</td>
      <td>87</td>
      <td>86</td>
      <td>88</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Ian Powell</td>
      <td>1</td>
      <td>Male</td>
      <td>20</td>
      <td>85</td>
      <td>83</td>
      <td>84</td>
    </tr>
    <tr>
      <th>63</th>
      <td>Laura Hughes</td>
      <td>1</td>
      <td>Female</td>
      <td>22</td>
      <td>89</td>
      <td>88</td>
      <td>90</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Mike Flores</td>
      <td>2</td>
      <td>Male</td>
      <td>19</td>
      <td>83</td>
      <td>82</td>
      <td>84</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Paula Simmons</td>
      <td>2</td>
      <td>Female</td>
      <td>18</td>
      <td>88</td>
      <td>87</td>
      <td>89</td>
    </tr>
    <tr>
      <th>68</th>
      <td>Ray Bryant</td>
      <td>3</td>
      <td>Male</td>
      <td>22</td>
      <td>84</td>
      <td>82</td>
      <td>83</td>
    </tr>
    <tr>
      <th>70</th>
      <td>Tony Russell</td>
      <td>2</td>
      <td>Male</td>
      <td>20</td>
      <td>81</td>
      <td>80</td>
      <td>82</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Whitney Myers</td>
      <td>2</td>
      <td>Female</td>
      <td>22</td>
      <td>86</td>
      <td>85</td>
      <td>87</td>
    </tr>
    <tr>
      <th>74</th>
      <td>Xavier Ford</td>
      <td>3</td>
      <td>Male</td>
      <td>19</td>
      <td>82</td>
      <td>80</td>
      <td>81</td>
    </tr>
    <tr>
      <th>75</th>
      <td>Yvonne Hamilton</td>
      <td>1</td>
      <td>Female</td>
      <td>20</td>
      <td>88</td>
      <td>87</td>
      <td>89</td>
    </tr>
    <tr>
      <th>76</th>
      <td>Zane Graham</td>
      <td>2</td>
      <td>Male</td>
      <td>21</td>
      <td>85</td>
      <td>83</td>
      <td>84</td>
    </tr>
    <tr>
      <th>79</th>
      <td>Clara West</td>
      <td>2</td>
      <td>Female</td>
      <td>19</td>
      <td>84</td>
      <td>82</td>
      <td>83</td>
    </tr>
    <tr>
      <th>80</th>
      <td>Daniel Jordan</td>
      <td>3</td>
      <td>Male</td>
      <td>20</td>
      <td>89</td>
      <td>88</td>
      <td>90</td>
    </tr>
    <tr>
      <th>83</th>
      <td>Gloria Hawkins</td>
      <td>3</td>
      <td>Female</td>
      <td>22</td>
      <td>83</td>
      <td>82</td>
      <td>84</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Howard Dunn</td>
      <td>1</td>
      <td>Male</td>
      <td>19</td>
      <td>86</td>
      <td>85</td>
      <td>87</td>
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
</div>



- 集合筛选：使用 `isin()` 方法筛选某列中值属于指定集合的记录，例如筛选一班和二班的学生记录：


```python
df1[df1["class"].isin([1, 2])]
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
      <th>6</th>
      <td>Grace Anderson</td>
      <td>1</td>
      <td>Female</td>
      <td>20</td>
      <td>84</td>
      <td>82</td>
      <td>86</td>
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
      <th>84</th>
      <td>Howard Dunn</td>
      <td>1</td>
      <td>Male</td>
      <td>19</td>
      <td>86</td>
      <td>85</td>
      <td>87</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Irene Olson</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
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
<p>61 rows × 7 columns</p>
</div>



- 字符串筛选：

    - `str.contains()` 筛选包含特定子字符串的记录
    - `str.startswith()` 和 `str.endswith()` 分别筛选以特定子字符串开头或结尾的记录


```python
df1[df1["name"].str.contains("A")]
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
      <th>6</th>
      <td>Grace Anderson</td>
      <td>1</td>
      <td>Female</td>
      <td>20</td>
      <td>84</td>
      <td>82</td>
      <td>86</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Ulysses Adams</td>
      <td>3</td>
      <td>Male</td>
      <td>20</td>
      <td>79</td>
      <td>77</td>
      <td>78</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Amy Roberts</td>
      <td>3</td>
      <td>Female</td>
      <td>21</td>
      <td>81</td>
      <td>80</td>
      <td>82</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Aaron Price</td>
      <td>2</td>
      <td>Male</td>
      <td>18</td>
      <td>79</td>
      <td>77</td>
      <td>78</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Sara Alexander</td>
      <td>1</td>
      <td>Female</td>
      <td>19</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Abby Sullivan</td>
      <td>3</td>
      <td>Female</td>
      <td>18</td>
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
  </tbody>
</table>
</div>




```python
df1[df1["name"].str.startswith("A")]
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
      <th>26</th>
      <td>Amy Roberts</td>
      <td>3</td>
      <td>Female</td>
      <td>21</td>
      <td>81</td>
      <td>80</td>
      <td>82</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Aaron Price</td>
      <td>2</td>
      <td>Male</td>
      <td>18</td>
      <td>79</td>
      <td>77</td>
      <td>78</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Abby Sullivan</td>
      <td>3</td>
      <td>Female</td>
      <td>18</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1[df1["name"].str.endswith("Taylor")]
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
      <th>5</th>
      <td>Frank Taylor</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>90</td>
      <td>92</td>
      <td>89</td>
    </tr>
  </tbody>
</table>
</div>



## 2. 基于索引的数据筛选

事实上，我们之前讲过的 `.loc` 方法同样可以用于基于条件的筛选：

- 语法格式是：`df.loc[条件, 列名列表]`，这里的 `条件` 和前面介绍的布尔索引是一样的，需要写成 `df["列名"]` 后面跟上比较运算符和具体的值
- 这样做的好处是，可以同时指定要筛选的列，而不是将所有列都保留下来

我们来看以下例子：

- 筛选出数学成绩大于 90 的学生的姓名和数学成绩：


```python
df1.loc[df1["math"] > 90, ["name", "math"]]
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
      <th>math</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>Frank Taylor</td>
      <td>92</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Ivy Moore</td>
      <td>93</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Leo Walker</td>
      <td>94</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Rachel Hill</td>
      <td>92</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Vera Baker</td>
      <td>94</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Brian Turner</td>
      <td>95</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Ella Parker</td>
      <td>92</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Jason Sanchez</td>
      <td>93</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Ophelia Morgan</td>
      <td>94</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Ryan Howard</td>
      <td>92</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Wendy Wood</td>
      <td>95</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Zoe Kelly</td>
      <td>92</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Daisy Ross</td>
      <td>92</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Julia Long</td>
      <td>94</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Nina Washington</td>
      <td>92</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Sara Alexander</td>
      <td>92</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Ursula Griffin</td>
      <td>95</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Abby Sullivan</td>
      <td>92</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Felix Stone</td>
      <td>94</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Irene Olson</td>
      <td>92</td>
    </tr>
    <tr>
      <th>88</th>
      <td>Lucas Porter</td>
      <td>92</td>
    </tr>
  </tbody>
</table>
</div>



- 筛选出英数学成绩大于 85 且语文成绩大于 80 的学生的姓名、语文、数学、英语成绩：


```python
df1.loc[(df1["english"] > 85) & (df1["chinese"] > 80), ["name", "chinese", "math", "english"]]
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
      <th>chinese</th>
      <th>math</th>
      <th>english</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice Johnson</td>
      <td>85</td>
      <td>88</td>
      <td>90</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie Brown</td>
      <td>92</td>
      <td>90</td>
      <td>94</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David Miller</td>
      <td>88</td>
      <td>85</td>
      <td>87</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Frank Taylor</td>
      <td>90</td>
      <td>92</td>
      <td>89</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Grace Anderson</td>
      <td>84</td>
      <td>82</td>
      <td>86</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Ivy Moore</td>
      <td>91</td>
      <td>93</td>
      <td>90</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Jack Martin</td>
      <td>87</td>
      <td>85</td>
      <td>88</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Leo Walker</td>
      <td>95</td>
      <td>94</td>
      <td>96</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Nathan Young</td>
      <td>88</td>
      <td>86</td>
      <td>87</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Rachel Hill</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Vera Baker</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Xander Carter</td>
      <td>89</td>
      <td>88</td>
      <td>90</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Zack Perez</td>
      <td>88</td>
      <td>90</td>
      <td>87</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Brian Turner</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Dylan Campbell</td>
      <td>85</td>
      <td>83</td>
      <td>86</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Ella Parker</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Harry Collins</td>
      <td>87</td>
      <td>85</td>
      <td>88</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Jason Sanchez</td>
      <td>91</td>
      <td>93</td>
      <td>92</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Liam Rogers</td>
      <td>88</td>
      <td>87</td>
      <td>89</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Noah Cook</td>
      <td>86</td>
      <td>85</td>
      <td>87</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Ophelia Morgan</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Ryan Howard</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Uma Diaz</td>
      <td>89</td>
      <td>88</td>
      <td>90</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Wendy Wood</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Yusuf Brooks</td>
      <td>86</td>
      <td>85</td>
      <td>87</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Zoe Kelly</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Chris Barnes</td>
      <td>88</td>
      <td>87</td>
      <td>89</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Daisy Ross</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>58</th>
      <td>George Jenkins</td>
      <td>87</td>
      <td>86</td>
      <td>88</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Julia Long</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>63</th>
      <td>Laura Hughes</td>
      <td>89</td>
      <td>88</td>
      <td>90</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Nina Washington</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Paula Simmons</td>
      <td>88</td>
      <td>87</td>
      <td>89</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Sara Alexander</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Ursula Griffin</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>73</th>
      <td>Whitney Myers</td>
      <td>86</td>
      <td>85</td>
      <td>87</td>
    </tr>
    <tr>
      <th>75</th>
      <td>Yvonne Hamilton</td>
      <td>88</td>
      <td>87</td>
      <td>89</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Abby Sullivan</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>80</th>
      <td>Daniel Jordan</td>
      <td>89</td>
      <td>88</td>
      <td>90</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Felix Stone</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Howard Dunn</td>
      <td>86</td>
      <td>85</td>
      <td>87</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Irene Olson</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>88</th>
      <td>Lucas Porter</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>90</th>
      <td>Nick Keller</td>
      <td>87</td>
      <td>85</td>
      <td>88</td>
    </tr>
  </tbody>
</table>
</div>



- 筛选出数学成绩大于 90 且语文或英语至少一科成绩大于 85 的学生的姓名、语文、数学、英语成绩：


```python
df1.loc[(df1["math"] > 90) & ( (df1["english"] > 85) | (df1["chinese"] > 85) ), ["name", "chinese", "math", "english"]]
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
      <th>chinese</th>
      <th>math</th>
      <th>english</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>Frank Taylor</td>
      <td>90</td>
      <td>92</td>
      <td>89</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Ivy Moore</td>
      <td>91</td>
      <td>93</td>
      <td>90</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Leo Walker</td>
      <td>95</td>
      <td>94</td>
      <td>96</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Rachel Hill</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Vera Baker</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Brian Turner</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Ella Parker</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Jason Sanchez</td>
      <td>91</td>
      <td>93</td>
      <td>92</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Ophelia Morgan</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Ryan Howard</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Wendy Wood</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Zoe Kelly</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Daisy Ross</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Julia Long</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Nina Washington</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Sara Alexander</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Ursula Griffin</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Abby Sullivan</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Felix Stone</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Irene Olson</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>88</th>
      <td>Lucas Porter</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
  </tbody>
</table>
</div>



## 3. 基于查询的数据筛选

Pandas 还提供了一种更简洁的基于查询的方法 `query()` 来实现数据筛选：

- 语法格式是：`df.query("条件表达式")`，其中 `条件表达式` 是一个字符串，直接写列名和比较运算符
- 大家如果学过 SQL，会发现这种语法和 SQL 的 `WHERE` 子句非常类似

在这个条件表达式中：

- 列名可以直接使用，不需要加引号或方括号
- 逻辑运算符和前面介绍的布尔索引中使用的是一样的：`&` 表示逻辑与，`|` 表示逻辑或，`~` 表示逻辑非
- 条件和条件之间不强制使用括号，括号的使用主要是表明优先级的

我们来看以下例子，和上面的例子其实是对应的：

- 筛选出数学成绩大于 90 的记录：


```python
df1.query("math > 90")
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
      <th>5</th>
      <td>Frank Taylor</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>90</td>
      <td>92</td>
      <td>89</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Ivy Moore</td>
      <td>3</td>
      <td>Female</td>
      <td>22</td>
      <td>91</td>
      <td>93</td>
      <td>90</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Leo Walker</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>95</td>
      <td>94</td>
      <td>96</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Rachel Hill</td>
      <td>3</td>
      <td>Female</td>
      <td>18</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Vera Baker</td>
      <td>1</td>
      <td>Female</td>
      <td>21</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Brian Turner</td>
      <td>1</td>
      <td>Male</td>
      <td>18</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Ella Parker</td>
      <td>1</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Jason Sanchez</td>
      <td>3</td>
      <td>Male</td>
      <td>20</td>
      <td>91</td>
      <td>93</td>
      <td>92</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Ophelia Morgan</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Ryan Howard</td>
      <td>2</td>
      <td>Male</td>
      <td>22</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Wendy Wood</td>
      <td>1</td>
      <td>Female</td>
      <td>22</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Zoe Kelly</td>
      <td>1</td>
      <td>Female</td>
      <td>21</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Daisy Ross</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Julia Long</td>
      <td>2</td>
      <td>Female</td>
      <td>21</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Nina Washington</td>
      <td>3</td>
      <td>Female</td>
      <td>20</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Sara Alexander</td>
      <td>1</td>
      <td>Female</td>
      <td>19</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Ursula Griffin</td>
      <td>3</td>
      <td>Female</td>
      <td>21</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Abby Sullivan</td>
      <td>3</td>
      <td>Female</td>
      <td>18</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Felix Stone</td>
      <td>2</td>
      <td>Male</td>
      <td>18</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Irene Olson</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
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
  </tbody>
</table>
</div>



- 筛选出数学成绩大于 90 且英语成绩大于 85 的记录：


```python
df1.query("math > 90 & english > 85")
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
      <th>5</th>
      <td>Frank Taylor</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>90</td>
      <td>92</td>
      <td>89</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Ivy Moore</td>
      <td>3</td>
      <td>Female</td>
      <td>22</td>
      <td>91</td>
      <td>93</td>
      <td>90</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Leo Walker</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>95</td>
      <td>94</td>
      <td>96</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Rachel Hill</td>
      <td>3</td>
      <td>Female</td>
      <td>18</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Vera Baker</td>
      <td>1</td>
      <td>Female</td>
      <td>21</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Brian Turner</td>
      <td>1</td>
      <td>Male</td>
      <td>18</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Ella Parker</td>
      <td>1</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Jason Sanchez</td>
      <td>3</td>
      <td>Male</td>
      <td>20</td>
      <td>91</td>
      <td>93</td>
      <td>92</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Ophelia Morgan</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Ryan Howard</td>
      <td>2</td>
      <td>Male</td>
      <td>22</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Wendy Wood</td>
      <td>1</td>
      <td>Female</td>
      <td>22</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Zoe Kelly</td>
      <td>1</td>
      <td>Female</td>
      <td>21</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Daisy Ross</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Julia Long</td>
      <td>2</td>
      <td>Female</td>
      <td>21</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Nina Washington</td>
      <td>3</td>
      <td>Female</td>
      <td>20</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Sara Alexander</td>
      <td>1</td>
      <td>Female</td>
      <td>19</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Ursula Griffin</td>
      <td>3</td>
      <td>Female</td>
      <td>21</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Abby Sullivan</td>
      <td>3</td>
      <td>Female</td>
      <td>18</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Felix Stone</td>
      <td>2</td>
      <td>Male</td>
      <td>18</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Irene Olson</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
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
  </tbody>
</table>
</div>



- 筛选出数学成绩大于 90 且语文和英语至少一科成绩大于 85 的记录：


```python
df1.query("math > 90 & (english > 85 | chinese > 85)")
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
      <th>5</th>
      <td>Frank Taylor</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>90</td>
      <td>92</td>
      <td>89</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Ivy Moore</td>
      <td>3</td>
      <td>Female</td>
      <td>22</td>
      <td>91</td>
      <td>93</td>
      <td>90</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Leo Walker</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>95</td>
      <td>94</td>
      <td>96</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Rachel Hill</td>
      <td>3</td>
      <td>Female</td>
      <td>18</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Vera Baker</td>
      <td>1</td>
      <td>Female</td>
      <td>21</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Brian Turner</td>
      <td>1</td>
      <td>Male</td>
      <td>18</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Ella Parker</td>
      <td>1</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Jason Sanchez</td>
      <td>3</td>
      <td>Male</td>
      <td>20</td>
      <td>91</td>
      <td>93</td>
      <td>92</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Ophelia Morgan</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Ryan Howard</td>
      <td>2</td>
      <td>Male</td>
      <td>22</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Wendy Wood</td>
      <td>1</td>
      <td>Female</td>
      <td>22</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Zoe Kelly</td>
      <td>1</td>
      <td>Female</td>
      <td>21</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Daisy Ross</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Julia Long</td>
      <td>2</td>
      <td>Female</td>
      <td>21</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Nina Washington</td>
      <td>3</td>
      <td>Female</td>
      <td>20</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Sara Alexander</td>
      <td>1</td>
      <td>Female</td>
      <td>19</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Ursula Griffin</td>
      <td>3</td>
      <td>Female</td>
      <td>21</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Abby Sullivan</td>
      <td>3</td>
      <td>Female</td>
      <td>18</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Felix Stone</td>
      <td>2</td>
      <td>Male</td>
      <td>18</td>
      <td>92</td>
      <td>94</td>
      <td>93</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Irene Olson</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>90</td>
      <td>92</td>
      <td>91</td>
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
  </tbody>
</table>
</div>



注意：

- `query()` 方法只能用于筛选行，不能像 `.loc` 那样同时指定要筛选的列
- 但是要想筛选列，直接在 `query()` 之后再使用列索引来筛选即可
- 例如，筛选出数学成绩大于 90 的学生的姓名和数学成绩：


```python
df1.query("math > 90")[["name", "math"]]
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
      <th>math</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>Frank Taylor</td>
      <td>92</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Ivy Moore</td>
      <td>93</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Leo Walker</td>
      <td>94</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Rachel Hill</td>
      <td>92</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Vera Baker</td>
      <td>94</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Brian Turner</td>
      <td>95</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Ella Parker</td>
      <td>92</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Jason Sanchez</td>
      <td>93</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Ophelia Morgan</td>
      <td>94</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Ryan Howard</td>
      <td>92</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Wendy Wood</td>
      <td>95</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Zoe Kelly</td>
      <td>92</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Daisy Ross</td>
      <td>92</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Julia Long</td>
      <td>94</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Nina Washington</td>
      <td>92</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Sara Alexander</td>
      <td>92</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Ursula Griffin</td>
      <td>95</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Abby Sullivan</td>
      <td>92</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Felix Stone</td>
      <td>94</td>
    </tr>
    <tr>
      <th>85</th>
      <td>Irene Olson</td>
      <td>92</td>
    </tr>
    <tr>
      <th>88</th>
      <td>Lucas Porter</td>
      <td>92</td>
    </tr>
  </tbody>
</table>
</div>


