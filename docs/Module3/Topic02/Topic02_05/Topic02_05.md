# Topic 2.5 - Pandas 中的排序与聚合运算

本节开始前，我们先导入 Pandas 库：


```python
import pandas as pd
```

## 1. 数据排序

### (1) 基本排序方法

在 Pandas 中，可以使用 `sort_values()` 方法对 DataFrame 进行排序，当中可以强调以下参数：

- `by`：指定排序的列名，可以是单个列名或多个列名组成的列表
- `ascending`：指定排序的顺序，默认为 `True`（升序），如果设置为 `False` 则为降序，应该与 `by` 参数中的排序依据的列一一对应
- `inplace`：指定是否在原 DataFrame 上进行排序，默认为 `False` 就是返回一个新的 DataFrame，设置为 `True` 则会修改原 DataFrame 而不返回新的 DataFrame

我们先来看一个简单的例子，就是之前的学生成绩数据表：


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



- 在这个表中，我们想将所有数据按照 "数学成绩" 这一列进行降序排序，可以使用以下代码实现：


```python
df1.sort_values(by="math", ascending=False, inplace=True)
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
      <th>28</th>
      <td>Cathy Phillips</td>
      <td>2</td>
      <td>Female</td>
      <td>22</td>
      <td>76</td>
      <td>74</td>
      <td>75</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Ethan Henderson</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>75</td>
      <td>73</td>
      <td>74</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Isla Stewart</td>
      <td>2</td>
      <td>Female</td>
      <td>19</td>
      <td>74</td>
      <td>72</td>
      <td>73</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Will Nelson</td>
      <td>2</td>
      <td>Male</td>
      <td>18</td>
      <td>75</td>
      <td>72</td>
      <td>74</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Karen Lee</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>73</td>
      <td>70</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
<p>91 rows × 7 columns</p>
</div>



- 如果我们想按照多个列进行排序，比如先按 "语文成绩" 降序排序，再按 "数学成绩" 升序排序，这里的逻辑是，先按照语文成绩降序排序，如果语文成绩相同，再按照数学成绩升序排序，对应的代码是：


```python
df1.sort_values(by=["chinese", "math"], ascending=[False, True], inplace=True)
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
      <th>22</th>
      <td>Will Nelson</td>
      <td>2</td>
      <td>Male</td>
      <td>18</td>
      <td>75</td>
      <td>72</td>
      <td>74</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Ethan Henderson</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>75</td>
      <td>73</td>
      <td>74</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Isla Stewart</td>
      <td>2</td>
      <td>Female</td>
      <td>19</td>
      <td>74</td>
      <td>72</td>
      <td>73</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Karen Lee</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>73</td>
      <td>70</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
<p>91 rows × 7 columns</p>
</div>



### (2) 排序后重排行号

在上面的例子中，大家应该注意到，排序后 DataFrame 的行号是乱的，因为排序只是改变了数据的顺序，但并没有改变行号

- 如果我们想在排序后重新设置行号，可以使用 `reset_index()` 方法
- 这里我们通常会设置 `drop=True` 参数来丢弃原有的行号列，否则原来的行号会成为一个新的列被保留下来


```python
df1.sort_values(by="english", ascending=True, inplace=True)
df1.reset_index(drop=True, inplace=True)
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
      <td>Isla Stewart</td>
      <td>2</td>
      <td>Female</td>
      <td>19</td>
      <td>74</td>
      <td>72</td>
      <td>73</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ethan Henderson</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>75</td>
      <td>73</td>
      <td>74</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Will Nelson</td>
      <td>2</td>
      <td>Male</td>
      <td>18</td>
      <td>75</td>
      <td>72</td>
      <td>74</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Emma Wilson</td>
      <td>2</td>
      <td>Female</td>
      <td>19</td>
      <td>76</td>
      <td>78</td>
      <td>74</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Karen Lee</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>73</td>
      <td>70</td>
      <td>75</td>
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
      <td>Charlie Brown</td>
      <td>3</td>
      <td>Male</td>
      <td>18</td>
      <td>92</td>
      <td>90</td>
      <td>94</td>
    </tr>
    <tr>
      <th>87</th>
      <td>Wendy Wood</td>
      <td>1</td>
      <td>Female</td>
      <td>22</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>88</th>
      <td>Brian Turner</td>
      <td>1</td>
      <td>Male</td>
      <td>18</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>89</th>
      <td>Ursula Griffin</td>
      <td>3</td>
      <td>Female</td>
      <td>21</td>
      <td>93</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th>90</th>
      <td>Leo Walker</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>95</td>
      <td>94</td>
      <td>96</td>
    </tr>
  </tbody>
</table>
<p>91 rows × 7 columns</p>
</div>



### (3) Pandas 中的 `inplace` 参数

在大多数 Pandas 方法中，都会有一个 `inplace` 参数，这个参数的作用是决定操作是直接在原 DataFrame 上进行修改，还是返回一个新的 DataFrame

- 如果 `inplace=True`，那么操作会直接修改原 DataFrame，不会返回新的 DataFrame
- 如果 `inplace=False`（默认值），那么操作会返回一个新的 DataFrame

这个操作，大家其实之前是体会过的，我们介绍列表操作时，就提到过类似的概念：

- 比如 `list.sort()` 方法就是直接在原列表上进行排序
- 而 `sorted(list)` 函数则是返回一个新的排序后的列表

我们来体会一下 `inplace` 参数的作用：

- 首先我们在排序中设置一个 `inplace=True`，这个操作会直接在原 DataFrame 上进行修改：


```python
df2 = pd.read_csv("../data/students.csv")
df2
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
df2.sort_values(by="math", ascending=False, inplace=True)
df2
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
      <th>28</th>
      <td>Cathy Phillips</td>
      <td>2</td>
      <td>Female</td>
      <td>22</td>
      <td>76</td>
      <td>74</td>
      <td>75</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Ethan Henderson</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>75</td>
      <td>73</td>
      <td>74</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Isla Stewart</td>
      <td>2</td>
      <td>Female</td>
      <td>19</td>
      <td>74</td>
      <td>72</td>
      <td>73</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Will Nelson</td>
      <td>2</td>
      <td>Male</td>
      <td>18</td>
      <td>75</td>
      <td>72</td>
      <td>74</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Karen Lee</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>73</td>
      <td>70</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
<p>91 rows × 7 columns</p>
</div>



- 接下来，我们再来看看如果设置 `inplace=False`，这个操作会将排序结果返回为一个新的 DataFrame，而不会修改原 DataFrame：


```python
df3 = pd.read_csv("../data/students.csv")
df3
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
df3_new = df3.sort_values(by="chinese", ascending=False, inplace=False)

display(df3_new)
display(df3)
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
      <th>22</th>
      <td>Will Nelson</td>
      <td>2</td>
      <td>Male</td>
      <td>18</td>
      <td>75</td>
      <td>72</td>
      <td>74</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Ethan Henderson</td>
      <td>3</td>
      <td>Male</td>
      <td>21</td>
      <td>75</td>
      <td>73</td>
      <td>74</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Isla Stewart</td>
      <td>2</td>
      <td>Female</td>
      <td>19</td>
      <td>74</td>
      <td>72</td>
      <td>73</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Karen Lee</td>
      <td>2</td>
      <td>Female</td>
      <td>20</td>
      <td>73</td>
      <td>70</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
<p>91 rows × 7 columns</p>
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


## 2. 数据聚合运算

### (1) 数据的截面聚合

#### (a) 截面聚合方法

上一节我们讲过一些基本的统计计算，比如 `mean()`、`sum()`、`max()`、`min()` 等方法，这些方法都是对整个列进行计算的

- 而有时，我们并不想对整列进行计算，而是想根据某些条件对数据进行分组，然后对每个组进行聚合计算
- 例如在我们的学生成绩表中，我们想计算每个班级的数学成绩平均分，一班、二班、三班分别来算

这时我们就要用到 Pandas 的 `groupby()` 方法：

- 这个方法接收一个或多个列名作为分组依据，然后返回一个 `GroupBy` 对象
- 之后，我们可以对这个对象调用聚合方法，比如 `mean()` 来计算每个组的平均值

我们在学生成绩表上来应用一下 `groupby()` 方法：

- 首先，我们按照班级求数学成绩的平均分，或者三科的平均分：


```python
df4 = pd.read_csv("../data/students.csv")
df4
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
df4.groupby("class")["math"].mean()
```




    class
    1    84.645161
    2    83.166667
    3    83.633333
    Name: math, dtype: float64




```python
df4.groupby("class")[["math", "chinese", "english"]].mean()
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
      <th>math</th>
      <th>chinese</th>
      <th>english</th>
    </tr>
    <tr>
      <th>class</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>84.645161</td>
      <td>85.612903</td>
      <td>86.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>83.166667</td>
      <td>83.766667</td>
      <td>83.966667</td>
    </tr>
    <tr>
      <th>3</th>
      <td>83.633333</td>
      <td>84.500000</td>
      <td>84.700000</td>
    </tr>
  </tbody>
</table>
</div>



- 接着，我们还可以既按照班级分组，又按照性别分组，来计算每个班级中男生和女生的数学成绩平均分，或者三科的平均分：


```python
df4.groupby(["class", "gender"])["math"].mean()
```




    class  gender
    1      Female    86.062500
           Male      83.133333
    2      Female    83.714286
           Male      82.687500
    3      Female    83.857143
           Male      83.437500
    Name: math, dtype: float64




```python
df4.groupby(["class", "gender"])[["math", "chinese", "english"]].mean()
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
      <th></th>
      <th>math</th>
      <th>chinese</th>
      <th>english</th>
    </tr>
    <tr>
      <th>class</th>
      <th>gender</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">1</th>
      <th>Female</th>
      <td>86.062500</td>
      <td>86.375000</td>
      <td>87.187500</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>83.133333</td>
      <td>84.800000</td>
      <td>84.733333</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2</th>
      <th>Female</th>
      <td>83.714286</td>
      <td>83.857143</td>
      <td>84.000000</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>82.687500</td>
      <td>83.687500</td>
      <td>83.937500</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">3</th>
      <th>Female</th>
      <td>83.857143</td>
      <td>84.357143</td>
      <td>84.714286</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>83.437500</td>
      <td>84.625000</td>
      <td>84.687500</td>
    </tr>
  </tbody>
</table>
</div>



要注意，本身 `groupby()` 方法并不会改变原 DataFrame，而是返回一个 `GroupBy` 对象：

- 也就是说，只告诉 Pandas 我们要把数据进行聚合，又不说聚在一起做什么，是不会有任何计算发生的
- 只有在之后调用聚合方法时，才会进行实际的计算并返回结果


```python
df4.groupby("class")
```




    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x13f5726d0>



#### (b) 截面聚合后的数据处理

大家可以看到，将数据按类别分组聚合后，返回的结果是一个新的 DataFrame：

- 这个 DataFrame 的格式其实是我们之前提到的 MultiIndex 格式，也就是数据透视表
- 那么要想将这个数据透视表还原成普通的 DataFrame 格式，可以使用 `reset_index()` 方法


```python
df4.groupby(["class", "gender"])[["math", "chinese", "english"]].mean().reset_index()
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
      <th>gender</th>
      <th>math</th>
      <th>chinese</th>
      <th>english</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Female</td>
      <td>86.062500</td>
      <td>86.375000</td>
      <td>87.187500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Male</td>
      <td>83.133333</td>
      <td>84.800000</td>
      <td>84.733333</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Female</td>
      <td>83.714286</td>
      <td>83.857143</td>
      <td>84.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>Male</td>
      <td>82.687500</td>
      <td>83.687500</td>
      <td>83.937500</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>Female</td>
      <td>83.857143</td>
      <td>84.357143</td>
      <td>84.714286</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3</td>
      <td>Male</td>
      <td>83.437500</td>
      <td>84.625000</td>
      <td>84.687500</td>
    </tr>
  </tbody>
</table>
</div>



#### (c) Pandas 中的方法链

在上面的操作中，我们使用了一连串的方法调用：`df4.groupby(...)[...].mean().reset_index()` 

- 这种形式被称为方法链（method chaining），它允许我们将多个方法调用串联在一起，使代码更加简洁和易读
- 当然，有个更好的习惯是，每个方法调用后面都换行，并且使用括号将整个方法链首尾包裹起来（不加括号换行会报错），这样代码会更清晰一些：


```python
df4_mean_scores = (
    df4.groupby(["class", "gender"])[["math", "chinese", "english"]]
    .mean()
    .reset_index()
)
df4_mean_scores
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
      <th>gender</th>
      <th>math</th>
      <th>chinese</th>
      <th>english</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Female</td>
      <td>86.062500</td>
      <td>86.375000</td>
      <td>87.187500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Male</td>
      <td>83.133333</td>
      <td>84.800000</td>
      <td>84.733333</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Female</td>
      <td>83.714286</td>
      <td>83.857143</td>
      <td>84.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>Male</td>
      <td>82.687500</td>
      <td>83.687500</td>
      <td>83.937500</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>Female</td>
      <td>83.857143</td>
      <td>84.357143</td>
      <td>84.714286</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3</td>
      <td>Male</td>
      <td>83.437500</td>
      <td>84.625000</td>
      <td>84.687500</td>
    </tr>
  </tbody>
</table>
</div>



### (2) 数据的时间聚合

#### (a) 时间聚合方法

除了按类别分组进行聚合计算外，Pandas 还支持按时间窗口进行聚合计算，使用的是 `resample()` 方法：

- `resample()` 方法适用于时间序列数据，可以按照指定的时间频率对数据进行重采样，然后对每个时间窗口进行聚合计算：

    - `resample(rule="YS")` 表示按年重采样
    - `resample(rule="ME")` 表示按月重采样
    - `resample(rule="W")` 表示按周重采样
    - `resample(rule="D")` 表示按天重采样
    - `resample(rule="H")` 表示按小时重采样
    - `resample(rule="T")` 表示按分钟重采样
    - `resample(rule="S")` 表示按秒重采样

- 当然，`resample()` 方法要求数据本身有一个时间索引（DatetimeIndex），否则无法进行时间重采样
- 这里我们先导入之前见过的销售数据，并且将索引改为 `date` 列，再改为时间格式，再算出一个 `revenue` 列为 `price` 和 `quantity` 的乘积：


```python
df5 = pd.read_excel("../data/sales.xlsx", sheet_name="sales")
df5['date'] = pd.to_datetime(df5['date'])
df5.set_index('date', inplace=True)

df5['revenue'] = df5['price'] * df5['quantity']
df5
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
      <th>product</th>
      <th>price</th>
      <th>quantity</th>
      <th>revenue</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2024-01-01</th>
      <td>Camera</td>
      <td>4599</td>
      <td>6</td>
      <td>27594</td>
    </tr>
    <tr>
      <th>2024-01-01</th>
      <td>Monitor</td>
      <td>1599</td>
      <td>5</td>
      <td>7995</td>
    </tr>
    <tr>
      <th>2024-01-01</th>
      <td>Tablet</td>
      <td>2999</td>
      <td>11</td>
      <td>32989</td>
    </tr>
    <tr>
      <th>2024-01-01</th>
      <td>Phone</td>
      <td>4999</td>
      <td>4</td>
      <td>19996</td>
    </tr>
    <tr>
      <th>2024-01-01</th>
      <td>Laptop</td>
      <td>6999</td>
      <td>10</td>
      <td>69990</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2024-02-29</th>
      <td>Speaker</td>
      <td>899</td>
      <td>11</td>
      <td>9889</td>
    </tr>
    <tr>
      <th>2024-02-29</th>
      <td>Keyboard</td>
      <td>399</td>
      <td>11</td>
      <td>4389</td>
    </tr>
    <tr>
      <th>2024-02-29</th>
      <td>Laptop</td>
      <td>6999</td>
      <td>10</td>
      <td>69990</td>
    </tr>
    <tr>
      <th>2024-02-29</th>
      <td>Keyboard</td>
      <td>399</td>
      <td>14</td>
      <td>5586</td>
    </tr>
    <tr>
      <th>2024-02-29</th>
      <td>Laptop</td>
      <td>6999</td>
      <td>14</td>
      <td>97986</td>
    </tr>
  </tbody>
</table>
<p>333 rows × 4 columns</p>
</div>



之后，我们就可以按时间来计算总销售额了：

- 首先，我们来看按月计算总销售额的例子：


```python
df5.resample(rule="ME")["revenue"].sum()
```




    date
    2024-01-31    4054530
    2024-02-29    4391709
    Freq: ME, Name: revenue, dtype: int64



- 接着，我们来看一个按周计算总销售额的例子：


```python
df5.resample(rule="W")["revenue"].sum()
```




    date
    2024-01-07    1004069
    2024-01-14    1006881
    2024-01-21     764904
    2024-01-28     946609
    2024-02-04     836333
    2024-02-11    1248149
    2024-02-18    1085734
    2024-02-25     866033
    2024-03-03     687527
    Freq: W-SUN, Name: revenue, dtype: int64



- 当然，对多列也可以进行时间聚合计算，比如同时计算总销售额和总销量：


```python
df5.resample(rule="ME")[["quantity", "revenue"]].sum()
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
      <th>quantity</th>
      <th>revenue</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2024-01-31</th>
      <td>1770</td>
      <td>4054530</td>
    </tr>
    <tr>
      <th>2024-02-29</th>
      <td>1591</td>
      <td>4391709</td>
    </tr>
  </tbody>
</table>
</div>



#### (b) 时间聚合后的数据处理

在使用 `resample()` 方法进行时间聚合后，返回的结果同样是一个新的 DataFrame：

- 这个新的 DataFrame 也是含有多重索引的，也就是说，是数据透视表格式的
- 如果想将其还原为普通的 DataFrame 格式，同样可以使用 `reset_index()` 方法
- 并且可以使用方法链的形式将这些操作串联起来：


```python
df5_monthly_total = (df5.resample(rule="ME")[["quantity", "revenue"]]
                     .sum()
                     .reset_index()
                     )

df5_monthly_total
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
      <th>date</th>
      <th>quantity</th>
      <th>revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2024-01-31</td>
      <td>1770</td>
      <td>4054530</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2024-02-29</td>
      <td>1591</td>
      <td>4391709</td>
    </tr>
  </tbody>
</table>
</div>



## 3. 数据的窗口运算



### (1) 窗口运算的概念

窗口运算属于一种比较复杂的数据运算了，它常用于时间序列的运算中，我们先来说说它的概念：

- 窗口运算首先会定义一个固定大小的“窗口”，这个窗口会框出数据中的一部分，这部分数据可以进行求和、求平均等操作
- 然后，这个窗口会沿着数据移动，通常是从上到下移动，每次移动一个单位，重新框出一部分数据，再进行相同的计算
- 这样就可以得到一个新的序列，这个序列中的每个值都是对应窗口内数据的计算结果

这么说有些抽象，我们来看一个求移动平均的例子：

- 假设我们有一个时间序列数据，我们想计算 `Close` 这列的 3 天移动平均值：

<div align="center">
    <img src="../截屏2026-01-30 23.29.55.png" width="500"/>
</div>

- 这里我们定义了一个大小为 3 的窗口：

    - 首先框出前 3 天的数据，计算它们的平均值，得到第一个移动平均值
    - 接着，窗口向下移动一天，框出第 2 天到第 4 天的数据，计算它们的平均值，得到第二个移动平均值
    - 依此类推，直到整个数据序列都被处理完毕
    - 由于前两天的数据无法形成完整的 3 天窗口，因此对应的移动平均值为 NaN

### (2) Pandas 中的窗口运算方法

在 Pandas 中，可以使用 `rolling()` 方法来实现窗口运算：

- 当中我们要强调 `window` 参数用来指定窗口的大小，正数是从上到下，
- 并且与 `resample()` 和 `groupby()` 方法类似，`rolling()` 方法后面也需要接一个聚合方法，比如 `mean()` 来计算窗口内数据的平均值，不然的话，`rolling()` 方法本身并不会进行任何计算，只会返回一个滚动窗口对象


```python
df6 = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=7, freq='D'),
    'Security': ['A', 'A', 'A', 'A', 'A', 'A', 'A'],
    'Close': [104, 120, 107, 103, 117, 109, 105]
})

df6
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
      <th>Date</th>
      <th>Security</th>
      <th>Close</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023-01-01</td>
      <td>A</td>
      <td>104</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023-01-02</td>
      <td>A</td>
      <td>120</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023-01-03</td>
      <td>A</td>
      <td>107</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023-01-04</td>
      <td>A</td>
      <td>103</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023-01-05</td>
      <td>A</td>
      <td>117</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2023-01-06</td>
      <td>A</td>
      <td>109</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2023-01-07</td>
      <td>A</td>
      <td>105</td>
    </tr>
  </tbody>
</table>
</div>




```python
df6["Close_Avg_3"] = df6["Close"].rolling(window=3).mean()
df6
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
      <th>Date</th>
      <th>Security</th>
      <th>Close</th>
      <th>Close_Avg_3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023-01-01</td>
      <td>A</td>
      <td>104</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023-01-02</td>
      <td>A</td>
      <td>120</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023-01-03</td>
      <td>A</td>
      <td>107</td>
      <td>110.333333</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023-01-04</td>
      <td>A</td>
      <td>103</td>
      <td>110.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023-01-05</td>
      <td>A</td>
      <td>117</td>
      <td>109.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2023-01-06</td>
      <td>A</td>
      <td>109</td>
      <td>109.666667</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2023-01-07</td>
      <td>A</td>
      <td>105</td>
      <td>110.333333</td>
    </tr>
  </tbody>
</table>
</div>



我们发现，使用 `rolling()` 时，其实并不需要将数据设置为时间索引：

- 只需要保证数据是按时间顺序排列的即可
- 因此，为了保险起见，我们通常会先将数据按时间排序，再进行窗口运算：


```python
df6 = df6.sort_values(by="Date", ascending=True)
df6["Close_Avg_3"] = df6["Close"].rolling(window=3).mean()
df6
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
      <th>Date</th>
      <th>Security</th>
      <th>Close</th>
      <th>Close_Avg_3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023-01-01</td>
      <td>A</td>
      <td>104</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023-01-02</td>
      <td>A</td>
      <td>120</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023-01-03</td>
      <td>A</td>
      <td>107</td>
      <td>110.333333</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023-01-04</td>
      <td>A</td>
      <td>103</td>
      <td>110.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023-01-05</td>
      <td>A</td>
      <td>117</td>
      <td>109.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2023-01-06</td>
      <td>A</td>
      <td>109</td>
      <td>109.666667</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2023-01-07</td>
      <td>A</td>
      <td>105</td>
      <td>110.333333</td>
    </tr>
  </tbody>
</table>
</div>



### (3) Pandas 中实现从下往上的窗口运算

Pandas 中的 `rolling()` 方法默认是从上往下进行窗口运算的，也就是正向滚动窗口。

如果我们想实现从下往上的窗口运算，也就是反向滚动窗口，可以通过以下方法：

- 先将数据翻转过来，使用 `iloc[::-1]` 方法
- 然后对翻转后的数据使用 `rolling()` 方法进行窗口运算
- 最后再将结果翻转回来，恢复原来的顺序，还是使用 `iloc[::-1]` 方法
- 这时候，尾部的数据由于无法形成完整的窗口，结果会是 NaN

例如，我们想计算 `Close` 列的 3 天反向移动平均值，可以使用以下代码实现：


```python
df7 = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=7, freq='D'),
    'Security': ['A', 'A', 'A', 'A', 'A', 'A', 'A'],
    'Close': [104, 120, 107, 103, 117, 109, 105]
})

df7
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
      <th>Date</th>
      <th>Security</th>
      <th>Close</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023-01-01</td>
      <td>A</td>
      <td>104</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023-01-02</td>
      <td>A</td>
      <td>120</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023-01-03</td>
      <td>A</td>
      <td>107</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023-01-04</td>
      <td>A</td>
      <td>103</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023-01-05</td>
      <td>A</td>
      <td>117</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2023-01-06</td>
      <td>A</td>
      <td>109</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2023-01-07</td>
      <td>A</td>
      <td>105</td>
    </tr>
  </tbody>
</table>
</div>




```python
df7["Close_Avg_3_reverse"] = df7["Close"].iloc[::-1].rolling(window=3).mean().iloc[::-1]
df7
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
      <th>Date</th>
      <th>Security</th>
      <th>Close</th>
      <th>Close_Avg_3_reverse</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2023-01-01</td>
      <td>A</td>
      <td>104</td>
      <td>110.333333</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2023-01-02</td>
      <td>A</td>
      <td>120</td>
      <td>110.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2023-01-03</td>
      <td>A</td>
      <td>107</td>
      <td>109.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2023-01-04</td>
      <td>A</td>
      <td>103</td>
      <td>109.666667</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2023-01-05</td>
      <td>A</td>
      <td>117</td>
      <td>110.333333</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2023-01-06</td>
      <td>A</td>
      <td>109</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2023-01-07</td>
      <td>A</td>
      <td>105</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>


