# Topic 2.1 - Pandas 中的数据结构

Pandas 其实就是一个处理表格的工具，大家可以把它想象成用代码来操作 Excel 表格，那么表格这个东西在 Pandas 中有两种形式：

- DataFrame：二维表格结构，可以理解为 Excel 中的一个工作表
- Series：一维表格结构，可以理解为 Excel 中的一列数据或一行数据

本节我们就来学习这两种数据结构的基本使用方法，首先我们先导入 Pandas 库：


```python
import pandas as pd
```

然后我们先来复习一下，`print()` 和 `display()` 这两个函数的区别：

- `print()`：这是 Python 内置的打印函数，可以将任何对象转换为字符串并输出到控制台，适用于简单的文本输出
- `display()`：这是 Jupyter Notebook 提供的一个函数，用于在 Notebook 环境中显示复杂对象，比如 Pandas 的 DataFrame 和 Series，更加美观和易读

    - 在单元格中输出，如果不加 `display()`，Jupyter 只会显示最后一个表达式的结果
    - 使用 `display()` 可以显示多个结果

- 对于有些文本输出来说，使用 `print()` 和使用 `display()` 的效果基本是一样的，我们就不做区别了

## 1. Pandas 中的 DataFrame

### (1) 创建 DataFrame

#### (a) 从基础数据类型创建 DataFrame

DataFrame 是 Pandas 中最常用的数据结构，其实就是一个有行有列的表格：

- 在 Python 基础课上我们讲到过，使用 Python 自带的组合数据类型也可以表示出二维表格结构，
- 一种是**列表套列表**：


```python
data1 = [
    ["张三", 25, 95],
    ["李四", 36, 88],
    ["王五", 25, 76]
]
```

- 一种是**字典套列表**：


```python
data2 = {
    "姓名": ["张三", "李四", "王五"],
    "年龄": [25, 36, 25],
    "分数": [95, 88, 76]
}
```

这两种数据格式，都是支持一步到位直接转为 Pandas DataFrame 的：

- 使用的方法是 `pd.DataFrame()`，其中 `pd` 是我们导入 Pandas 库时常用的别名
- 注意，列表套列表的方式需要我们额外指定列名，而字典套列表的方式会自动使用字典的键作为列名


```python
data1_df = pd.DataFrame(data1, columns=["姓名", "年龄", "分数"])
data1_df
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
      <th>姓名</th>
      <th>年龄</th>
      <th>分数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>25</td>
      <td>95</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>36</td>
      <td>88</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>25</td>
      <td>76</td>
    </tr>
  </tbody>
</table>
</div>




```python
data2_df = pd.DataFrame(data2)
data2_df
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
      <th>姓名</th>
      <th>年龄</th>
      <th>分数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>25</td>
      <td>95</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>36</td>
      <td>88</td>
    </tr>
    <tr>
      <th>2</th>
      <td>王五</td>
      <td>25</td>
      <td>76</td>
    </tr>
  </tbody>
</table>
</div>



之后，我们可以使用 `type()` 函数来查看变量的数据类型，确认它已经是一个 DataFrame 了：


```python
print(type(data1_df))
print(type(data2_df))
```

    <class 'pandas.core.frame.DataFrame'>
    <class 'pandas.core.frame.DataFrame'>


#### (b) 从文件创建 DataFrame

除了自创数据外，DataFrame 更常见的创建方式是从文件中读取数据，比如 CSV 文件、Excel 文件等。Pandas 提供了多种函数来实现这一点：

- `pd.read_csv(path)`：从 CSV 文件读取数据
- `pd.read_excel(path)`：从 Excel 文件读取数据
- `pd.read_json(path)`：从 JSON 文件读取数据

接下来，我们以 CSV 文件为例，演示如何从文件中创建 DataFrame 并查看类型，我们使用 `data/students.csv` 这个文件：


```python
df_students = pd.read_csv("../data/students.csv")
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




```python
type(df_students)
```




    pandas.core.frame.DataFrame



可以看到，当一个 DataFrame 太大的时候，Jupyter Notebook 只会显示前几行和后几行的数据，以节省空间

- 要想展示完整的数据，需要在 Pandas 的配置中进行修改，不过一般情况下我们并不推荐这么做，因为这样会占用过多的屏幕空间，不仅影响阅读体验，电脑还可能会卡
- 修改 Pandas 配置的方法是使用 `pd.set_option()` 函数：

    - `pd.set_option('display.max_rows', None)` 可以设置显示所有行
    - `pd.set_option('display.max_columns', None)` 可以设置显示所有列
    - 这两个代码，只要运行一次就可以应用于整个 Notebook 中的所有 DataFrame 显示，如果想改回来只需把 `None` 换成一个整数，然后再运行一次配置代码即可

当然，Pandas 还提供了只展示头部或尾部数据的方法：

- 这两个方法分别是 `df.head(n)` 和 `df.tail(n)`，其中 `n` 是要展示的行数，默认值是 5


```python
display(df_students.head())
display(df_students.tail())
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
  </tbody>
</table>
</div>



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
</div>



```python
display(df_students.head(3))
display(df_students.tail(2))
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
  </tbody>
</table>
</div>



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
</div>


- 事实上，`head()` 和 `tail()` 方法创造出了一个新的 DataFrame，利用这两个方法还可以进行数据提取和切片操作：


```python
df_students_head = df_students.head(3)
display(df_students_head)
print(type(df_students_head))

df_students_tail = df_students.tail(2)
display(df_students_tail)
print(type(df_students_tail))
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
  </tbody>
</table>
</div>


    <class 'pandas.core.frame.DataFrame'>



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
</div>


    <class 'pandas.core.frame.DataFrame'>


### (2) 查看 DataFrame 的基本信息

创建好 DataFrame 之后，我们通常需要查看它的基本信息，Pandas 提供了多种方法来实现这一点。

首先，关于数据的基本信息可以使用以下方法来查看：

- `df.info()`：查看 DataFrame 的基本信息，包括行数、列数、每列的数据类型和非空值数量


```python
df_students.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 91 entries, 0 to 90
    Data columns (total 7 columns):
     #   Column   Non-Null Count  Dtype 
    ---  ------   --------------  ----- 
     0   name     91 non-null     object
     1   class    91 non-null     int64 
     2   gender   91 non-null     object
     3   age      91 non-null     int64 
     4   chinese  91 non-null     int64 
     5   math     91 non-null     int64 
     6   english  91 non-null     int64 
    dtypes: int64(5), object(2)
    memory usage: 5.1+ KB


- `df.describe()`：查看**数值型**列的统计信息，包括均值、标准差、最小值、最大值和四分位数


```python
df_students.describe()
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
      <th>class</th>
      <th>age</th>
      <th>chinese</th>
      <th>math</th>
      <th>english</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>91.000000</td>
      <td>91.000000</td>
      <td>91.000000</td>
      <td>91.000000</td>
      <td>91.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.989011</td>
      <td>19.934066</td>
      <td>84.637363</td>
      <td>83.824176</td>
      <td>84.901099</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.823198</td>
      <td>1.412659</td>
      <td>5.406820</td>
      <td>6.647628</td>
      <td>6.070063</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>18.000000</td>
      <td>73.000000</td>
      <td>70.000000</td>
      <td>73.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.000000</td>
      <td>19.000000</td>
      <td>80.000000</td>
      <td>78.000000</td>
      <td>80.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2.000000</td>
      <td>20.000000</td>
      <td>85.000000</td>
      <td>83.000000</td>
      <td>84.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>3.000000</td>
      <td>21.000000</td>
      <td>89.000000</td>
      <td>89.000000</td>
      <td>90.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>3.000000</td>
      <td>22.000000</td>
      <td>95.000000</td>
      <td>95.000000</td>
      <td>96.000000</td>
    </tr>
  </tbody>
</table>
</div>



- `df.dtypes`：查看每列的数据类型


```python
df_students.dtypes
```




    name       object
    class       int64
    gender     object
    age         int64
    chinese     int64
    math        int64
    english     int64
    dtype: object



- `df.shape`：查看 DataFrame 的形状（行数和列数）


```python
df_students.shape
```




    (91, 7)



我们在学习过 Python 面向对象后，其实就会知道，DataFrame 本质上是一个类，我们创建的各个 DataFrame 就是这个类的对象：

- `info()` 和 `describe()` 都带括号，说明这两个是 DataFrame 类的方法
- `dtypes` 和 `shape` 没有括号，说明它们是 DataFrame 类的属性

除此之外，我们还可以查看 DataFrame 的行名和列名：

- 在 DataFrame 中，列名叫做 `columns`，行名叫做 `index`

    - `df.columns`：查看列名列表，列名就叫做 `columns`
    - `df.index`：查看行名列表，行名就叫做 `index`


```python
display(df_students.columns)
display(df_students.index)
```


    Index(['name', 'class', 'gender', 'age', 'chinese', 'math', 'english'], dtype='object')



    RangeIndex(start=0, stop=91, step=1)


- 可以看到，`columns` 和 `index` 返回的结果都是一个特殊的 Pandas 对象：

    - 这个对象类型叫做 `Index`，它是 Pandas 用来表示行名和列名的专用数据结构，有些不直观
    - 要想把它们转换成普通的列表，可以使用 `tolist()` 方法：


```python
display(df_students.columns.tolist())
display(df_students.index.tolist())
```


    ['name', 'class', 'gender', 'age', 'chinese', 'math', 'english']



    [0,
     1,
     2,
     3,
     4,
     5,
     6,
     7,
     8,
     9,
     10,
     11,
     12,
     13,
     14,
     15,
     16,
     17,
     18,
     19,
     20,
     21,
     22,
     23,
     24,
     25,
     26,
     27,
     28,
     29,
     30,
     31,
     32,
     33,
     34,
     35,
     36,
     37,
     38,
     39,
     40,
     41,
     42,
     43,
     44,
     45,
     46,
     47,
     48,
     49,
     50,
     51,
     52,
     53,
     54,
     55,
     56,
     57,
     58,
     59,
     60,
     61,
     62,
     63,
     64,
     65,
     66,
     67,
     68,
     69,
     70,
     71,
     72,
     73,
     74,
     75,
     76,
     77,
     78,
     79,
     80,
     81,
     82,
     83,
     84,
     85,
     86,
     87,
     88,
     89,
     90]


## 2. Pandas 中的 Series

### (1) 创建 Series

Series 是 Pandas 中的一种一维数据结构，可以理解为只有一列或一行的表格。

#### (a) 从基础数据类型创建 Series

Series 的创建方式和 DataFrame 类似，也可以从基础数据类型中创建，使用的方法是 `pd.Series()`：

- 一种方法是从**列表**创建 Series，这时如果不指定索引，则默认索引是从 0 开始的整数序列：


```python
sr1 = pd.Series([10, 20, 30, 40])
display(sr1)
print(type(sr1))
```


    0    10
    1    20
    2    30
    3    40
    dtype: int64


    <class 'pandas.core.series.Series'>



```python
sr2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
display(sr2)
print(type(sr2))
```


    a    10
    b    20
    c    30
    d    40
    dtype: int64


    <class 'pandas.core.series.Series'>


- 另一种方法是从**字典**创建 Series，这时会自动使用字典的键作为索引：


```python
sr3 = pd.Series({'a': 10, 'b': 20, 'c': 30, 'd': 40})
display(sr3)
print(type(sr3))
```


    a    10
    b    20
    c    30
    d    40
    dtype: int64


    <class 'pandas.core.series.Series'>


#### (b) 将 DataFrame 的某一列或某一行转换为 Series

如果将 DataFrame 的某一列或某一行提取出来，那么得到的结果就是一个 Series：

- 提取某一列可以使用 `df['列名']` 或 `df.列名` 的方式：

    - 注意第一种方式必须使用引号括起来
    - 提取某一列出来之后，默认使用原始的行名作为索引


```python
data3_df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})
display(data3_df)
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
      <td>4</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>5</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>6</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



```python
col_A_v1 = data3_df['A']
display(col_A_v1)
print(type(col_A_v1))

col_A_v2 = data3_df.A
display(col_A_v2)
print(type(col_A_v2))
```


    0    1
    1    2
    2    3
    Name: A, dtype: int64


    <class 'pandas.core.series.Series'>



    0    1
    1    2
    2    3
    Name: A, dtype: int64


    <class 'pandas.core.series.Series'>


- 提取某一行可以使用 `df.loc[行名]` 或 `df.iloc[行号]` 的方式：

    - `loc` 是基于行名进行提取，`iloc` 是基于行号也，就是顺序进行提取，这两者的区别我们在下一节课中会详细讲解
    - 将行提取出来之后，默认使用原始的列名作为索引


```python
row0_v1 = data3_df.loc[0]
display(row0_v1)
print(type(row0_v1))

row0_v2 = data3_df.iloc[0]
display(row0_v2)
print(type(row0_v2))
```


    A    1
    B    4
    C    7
    Name: 0, dtype: int64


    <class 'pandas.core.series.Series'>



    A    1
    B    4
    C    7
    Name: 0, dtype: int64


    <class 'pandas.core.series.Series'>


### (2) 查看 Series 的基本信息

查看 DataFrame 基本信息的方法，其实也是可以应用到 Series 上的：

- `sr.info()`：查看 Series 的基本信息，包括长度、数据类型和非空值数量


```python
sr4 = pd.Series({'a': 10, 'b': 20, 'c': 30, 'd': 40})
sr4
```




    a    10
    b    20
    c    30
    d    40
    dtype: int64




```python
sr4.info()
```

    <class 'pandas.core.series.Series'>
    Index: 4 entries, a to d
    Series name: None
    Non-Null Count  Dtype
    --------------  -----
    4 non-null      int64
    dtypes: int64(1)
    memory usage: 236.0+ bytes


- `sr.describe()`：查看 Series 的统计信息，包括均值、标准差、最小值、最大值和四分位数


```python
sr4.describe()
```




    count     4.000000
    mean     25.000000
    std      12.909944
    min      10.000000
    25%      17.500000
    50%      25.000000
    75%      32.500000
    max      40.000000
    dtype: float64



- `sr.dtype`：查看 Series 的数据类型


```python
sr4.dtype
```




    dtype('int64')



- `sr.shape`：查看 Series 的形状（长度）


```python
sr4.shape
```




    (4,)



当然，Series 就没有列这一说了，只能使用 `sr.index` 来查看 Series 的索引


```python
sr4.index
```




    Index(['a', 'b', 'c', 'd'], dtype='object')



## 3. DataFrame 和 Series 的区别

DataFrame 是二维表格结构，有行有列，而 Series 是一维表格结构，只有一列或一行

- 但是，DataFrame 中有一种比较特殊的，就是只有一行或者只有一列的 DataFrame
- 这种 DataFrame 在某些方面和 Series 很相似，但它们仍然是不同的数据结构

我们首先来看一个只有一列的 DataFrame，以及一个只有一行的 DataFrame：


```python
df_new_1 = pd.DataFrame({
    'A': [1, 2, 3]
})
display(df_new_1)
print(type(df_new_1))
print(df_new_1.shape)
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
  </tbody>
</table>
</div>


    <class 'pandas.core.frame.DataFrame'>
    (3, 1)



```python
df_new_2 = pd.DataFrame([[1, 2, 3]], columns=['A', 'B', 'C'])
display(df_new_2)
print(type(df_new_2))
print(df_new_2.shape)
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
  </tbody>
</table>
</div>


    <class 'pandas.core.frame.DataFrame'>
    (1, 3)


- 这两种虽然在外观上看起来和 Series 很像，但它们仍然是 DataFrame 类型：
- 它们仍然有两个维度，行和列，只不过行维度为1或者列维度为1

而 Series 则只有一个维度，没有行和列的区别：


```python
sr_new = pd.Series([1, 2, 3])
display(sr_new)
print(type(sr_new))
print(sr_new.shape)
```


    0    1
    1    2
    2    3
    dtype: int64


    <class 'pandas.core.series.Series'>
    (3,)


- 可以发现，Series 只有一个维度，并没有行和列的区分
- 所以，事实上 Series 和 Python 自带的列表是很相似的，Series 多了索引和数据类型的概念

当然，这两者之间是可以相互转换的：

- 可以使用 `df['列名']` 或 `df.loc[行名]` 的方式将 DataFrame 转换为 Series
- 可以使用 `sr.to_frame(name='列名')` 方法将 Series 转换为 DataFrame


```python
df_new_1["A"]
```




    0    1
    1    2
    2    3
    Name: A, dtype: int64




```python
sr_new.to_frame(name='A')
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
  </tbody>
</table>
</div>


