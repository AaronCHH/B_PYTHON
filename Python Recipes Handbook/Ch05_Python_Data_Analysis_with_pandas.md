
# Chapter 5: Python Data Analysis with pandas
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 5: Python Data Analysis with pandas](#chapter-5-python-data-analysis-with-pandas)
  * [5-1. Working with 1D Data](#5-1-working-with-1d-data)
  * [5-2. Working with 2D Data](#5-2-working-with-2d-data)
  * [5-3. Working with 3D Data](#5-3-working-with-3d-data)
  * [5-4. Importing Data from CSV Files](#5-4-importing-data-from-csv-files)
  * [5-5. Saving to a CSV File](#5-5-saving-to-a-csv-file)
  * [5-6. Importing from Spreadsheets](#5-6-importing-from-spreadsheets)
  * [5-7. Saving to a Spreadsheet](#5-7-saving-to-a-spreadsheet)
  * [5-8. Getting the Head and Tail](#5-8-getting-the-head-and-tail)
  * [5-9. Summarizing Data](#5-9-summarizing-data)
  * [5-10. Sorting Data](#5-10-sorting-data)
  * [5-11. Applying Functions Row- or Column-Wise](#5-11-applying-functions-row-or-column-wise)
  * [5-12. Applying Functions Element-Wise](#5-12-applying-functions-element-wise)
  * [5-13. Iterating Over Data](#5-13-iterating-over-data)

<!-- tocstop -->


## 5-1. Working with 1D Data

* Problem
* Solution
* How It Works


```python
import pandas as pd
data = [1,2,3,4]
data_pd = pd.Series(data)
```


```python
>>> data_pd.dtype
dtype('int64')
>>> import numpy as np
>>> data_pd2 = pd.Series(data, dtype=np.float64)
>>> data_pd2.dtype
dtype('float64')
```


```python
2 * data_pd
```




    0    2
    1    4
    2    6
    3    8
    dtype: int64




```python
data_pd[2]
```




    3




```python
data_pd[3] = 9
```

## 5-2. Working with 2D Data
* Problem
* Solution
* How It Works


```python
d1 = {'one' : [1,2,3,4], 'two' : [9,8,7,6]}
df1 = pd.DataFrame(d1)
df1
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1['one']
```




    0    1
    1    2
    2    3
    3    4
    Name: one, dtype: int64




```python
df1['one'][2]
```




    3




```python
df1.loc[1]
```




    one    2
    two    8
    Name: 1, dtype: int64




```python
df1.loc[1][1]
```




    8



## 5-3. Working with 3D Data
* Problem
* Solution
* How It Works


```python
import numpy as np
```


```python
data_dict = {'item1' : pd.DataFrame(np.random.randn(4, 3)), 'item2' :pd.DataFrame(np.random.randn(4, 2))}
data_panel = pd.Panel(data_dict)
```


```python
data_panel['item2']
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-1.161885</td>
      <td>-0.537938</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.671292</td>
      <td>2.432737</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.244829</td>
      <td>-0.633335</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.170161</td>
      <td>-0.637829</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## 5-4. Importing Data from CSV Files
* Problem
* Solution
* How It Works


```python
 csv_data = pd.read_csv('data_file.csv')
```

## 5-5. Saving to a CSV File
* Problem
* Solution
* How It Works


```python
series_data.to_csv('export_file.csv')
```


```python
data2.to_csv('data_file.csv', header=False, index=False)
```

## 5-6. Importing from Spreadsheets
* Problem
* Solution
* How It Works


```python
data_frame1 = pd.read_excel('data_file.xsl', sheetname='Sheet1')
```


```python
excel_data = pd.ExcelFile('data_file.xsl')
```

## 5-7. Saving to a Spreadsheet
* Problem
* Solution
* How It Works


```python
df.to_excel('output_file.xsl', sheet='Sheet1')
```

## 5-8. Getting the Head and Tail
* Problem
* Solution
* How It Works


```python
data_series = pd.Series(np.random.randn(1000))
data_series.head(2)
```




    0   -0.271723
    1   -1.097757
    dtype: float64




```python
data_series.tail(2)
```




    998    1.242268
    999    0.162675
    dtype: float64



## 5-9. Summarizing Data
* Problem
* Solution
* How It Works


```python
data_series.describe()
```




    count    1000.000000
    mean       -0.010750
    std         1.014484
    min        -3.555131
    25%        -0.680081
    50%        -0.030919
    75%         0.651722
    max         2.912694
    dtype: float64




```python
data_series.std() ** 2
```




    1.0291775507060255




```python
data_series.var()
```




    1.0291775507060257



## 5-10. Sorting Data
* Problem
* Solution
* How It Works


```python
df = pd.DataFrame({'one' : [1,2,3], 'two' : [4,5,6], 'three' : [7,8,9]}, index=['b','c','a'])
```


```python
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>three</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>b</th>
      <td>1</td>
      <td>7</td>
      <td>4</td>
    </tr>
    <tr>
      <th>c</th>
      <td>2</td>
      <td>8</td>
      <td>5</td>
    </tr>
    <tr>
      <th>a</th>
      <td>3</td>
      <td>9</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_index()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>three</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>3</td>
      <td>9</td>
      <td>6</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1</td>
      <td>7</td>
      <td>4</td>
    </tr>
    <tr>
      <th>c</th>
      <td>2</td>
      <td>8</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_index(axis=1, ascending=False)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>two</th>
      <th>three</th>
      <th>one</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>b</th>
      <td>4</td>
      <td>7</td>
      <td>1</td>
    </tr>
    <tr>
      <th>c</th>
      <td>5</td>
      <td>8</td>
      <td>2</td>
    </tr>
    <tr>
      <th>a</th>
      <td>6</td>
      <td>9</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_values(by='two', ascending=False)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>three</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>3</td>
      <td>9</td>
      <td>6</td>
    </tr>
    <tr>
      <th>c</th>
      <td>2</td>
      <td>8</td>
      <td>5</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1</td>
      <td>7</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



## 5-11. Applying Functions Row- or Column-Wise
* Problem
* Solution
* How It Works


```python
df = pd.DataFrame({'one' : [1,2,3], 'two' : [4,5,6], 'three' : [7,8,9]}, index=['b','c','a'])
```


```python
df.apply(np.mean)
```




    one      2.0
    three    8.0
    two      5.0
    dtype: float64




```python
df.apply(np.mean, axis=1)
```




    b    4.0
    c    5.0
    a    6.0
    dtype: float64




```python
df.apply(lambda x: 2*x, axis=1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>three</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>b</th>
      <td>2</td>
      <td>14</td>
      <td>8</td>
    </tr>
    <tr>
      <th>c</th>
      <td>4</td>
      <td>16</td>
      <td>10</td>
    </tr>
    <tr>
      <th>a</th>
      <td>6</td>
      <td>18</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



## 5-12. Applying Functions Element-Wise
* Problem
* Solution
* How It Works


```python
df = pd.DataFrame({'one' : [1,2,3], 'two' : [4,5,6], 'three' : [7,8,9]}, index=['b','c','a'])
```


```python
df.applymap(lambda x: x*x)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>three</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>b</th>
      <td>1</td>
      <td>49</td>
      <td>16</td>
    </tr>
    <tr>
      <th>c</th>
      <td>4</td>
      <td>64</td>
      <td>25</td>
    </tr>
    <tr>
      <th>a</th>
      <td>9</td>
      <td>81</td>
      <td>36</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['two'].map(lambda x: 2*x)
```




    b     8
    c    10
    a    12
    Name: two, dtype: int64



## 5-13. Iterating Over Data
* Problem
* Solution
* How It Works


```python
df = pd.DataFrame({'one' : [1,2,3], 'two' : [4,5,6], 'three' : [7,8,9]}, index=['b','c','a'])
for col in df:
    print(df[col].mean())
```

    2.0
    8.0
    5.0



```python
for row_index,row in df.iterrows():
    print(row_index)
    print(row)
```
