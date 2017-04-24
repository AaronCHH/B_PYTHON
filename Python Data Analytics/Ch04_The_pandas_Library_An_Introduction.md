
# Chapter 4: The pandas Library—An Introduction
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 4: The pandas Library—An Introduction](#chapter-4-the-pandas-libraryan-introduction)
  * [4.1 pandas: The Python Data Analysis Library](#41-pandas-the-python-data-analysis-library)
  * [4.2 Installation](#42-installation)
    * [Installation from Anaconda](#installation-from-anaconda)
    * [Installation from PyPI](#installation-from-pypi)
    * [Installation on Linux](#installation-on-linux)
    * [Installation from Source](#installation-from-source)
    * [A Module Repository for Windows](#a-module-repository-for-windows)
  * [4.3 Test Your pandas Installation](#43-test-your-pandas-installation)
  * [4.4 Getting Started with pandas](#44-getting-started-with-pandas)
  * [4.5 Introduction to pandas Data Structures](#45-introduction-to-pandas-data-structures)
    * [The Series](#the-series)
    * [The DataFrame](#the-dataframe)
    * [The Index Objects](#the-index-objects)
  * [4.6 Other Functionalities on Indexes](#46-other-functionalities-on-indexes)
    * [Reindexing](#reindexing)
    * [Dropping](#dropping)
    * [Arithmetic and Data Alignment](#arithmetic-and-data-alignment)
  * [4.7 Operations between Data Structures](#47-operations-between-data-structures)
    * [Flexible Arithmetic Methods](#flexible-arithmetic-methods)
    * [Operations between DataFrame and Series](#operations-between-dataframe-and-series)
  * [4.8 Function Application and Mapping](#48-function-application-and-mapping)
    * [Functions by Element](#functions-by-element)
    * [Functions by Row or Column](#functions-by-row-or-column)
    * [Statistics Functions](#statistics-functions)
  * [4.9 Sorting and Ranking](#49-sorting-and-ranking)
  * [4.10 Correlation and Covariance](#410-correlation-and-covariance)
  * [4.11 “Not a Number” Data](#411-not-a-number-data)
    * [Assigning a NaN Value](#assigning-a-nan-value)
    * [Filtering Out NaN Values](#filtering-out-nan-values)
    * [Filling in NaN Occurrences](#filling-in-nan-occurrences)
  * [4.12 Hierarchical Indexing and Leveling](#412-hierarchical-indexing-and-leveling)
    * [Reordering and Sorting Levels](#reordering-and-sorting-levels)
    * [Summary Statistic by Level](#summary-statistic-by-level)
  * [4.13 Conclusions](#413-conclusions)

<!-- tocstop -->



## 4.1 pandas: The Python Data Analysis Library

## 4.2 Installation

### Installation from Anaconda
### Installation from PyPI
### Installation on Linux
### Installation from Source

### A Module Repository for Windows
## 4.3 Test Your pandas Installation
## 4.4 Getting Started with pandas
## 4.5 Introduction to pandas Data Structures

### The Series
* Declaring a Series


```python
import pandas as pd
```


```python
s = pd.Series([12,-4,7,9])
s
```




    0    12
    1    -4
    2     7
    3     9
    dtype: int64




```python
s = pd.Series([12,-4,7,9], index=['a','b','c','d'])
s
```




    a    12
    b    -4
    c     7
    d     9
    dtype: int64




```python
s.values
```




    array([12, -4,  7,  9], dtype=int64)




```python
s.index
```




    Index(['a', 'b', 'c', 'd'], dtype='object')



* Selecting the Internal Elements


```python
s[2]
```




    7




```python
s['b']
```




    -4




```python
s[0:2]
```




    a    12
    b    -4
    dtype: int64




```python
s[['b','c']]
```




    b   -4
    c    7
    dtype: int64



 * Assigning Values to the Elements


```python
s[1] = 0
s
```




    a    12
    b     0
    c     7
    d     9
    dtype: int64




```python
s['b'] = 1
s
```




    a    12
    b     1
    c     7
    d     9
    dtype: int64



* Defining Series from NumPy Arrays and Other Series


```python
import numpy as np
arr = np.array([1,2,3,4])
s3 = pd.Series(arr)
s3
```




    0    1
    1    2
    2    3
    3    4
    dtype: int32




```python
s4 = pd.Series(s)
s4
```




    a    12
    b     1
    c     7
    d     9
    dtype: int64




```python
s3
```




    0    1
    1    2
    2    3
    3    4
    dtype: int32




```python
arr[2] = -2
s3
```




    0    1
    1    2
    2   -2
    3    4
    dtype: int32



 * Filtering Values


```python
s[s > 8]
```




    a    12
    d     9
    dtype: int64



 * Operations and Mathematical Functions


```python
s / 2
```




    a    6.0
    b    0.5
    c    3.5
    d    4.5
    dtype: float64




```python
np.log(s)
```




    a    2.484907
    b    0.000000
    c    1.945910
    d    2.197225
    dtype: float64



 * Evaluating Values


```python
serd = pd.Series([1,0,2,1,2,3], index=['white','white','blue','green','green','yellow'])
serd
```




    white     1
    white     0
    blue      2
    green     1
    green     2
    yellow    3
    dtype: int64




```python
serd.unique()
```




    array([1, 0, 2, 3], dtype=int64)




```python
serd.value_counts()
```




    2    2
    1    2
    3    1
    0    1
    dtype: int64




```python
serd.isin([0,3])
```




    white     False
    white      True
    blue      False
    green     False
    green     False
    yellow     True
    dtype: bool




```python
serd[serd.isin([0,3])]
```




    white     0
    yellow    3
    dtype: int64



 * NaN Values


```python
s2 = pd.Series([5,-3,np.NaN,14])
s2
```




    0     5.0
    1    -3.0
    2     NaN
    3    14.0
    dtype: float64




```python
s2.isnull()
```




    0    False
    1    False
    2     True
    3    False
    dtype: bool




```python
s2.notnull()
```




    0     True
    1     True
    2    False
    3     True
    dtype: bool




```python
s2[s2.notnull()]
```




    0     5.0
    1    -3.0
    3    14.0
    dtype: float64




```python
s2[s2.isnull()]
```




    2   NaN
    dtype: float64



* Series as Dictionaries


```python
mydict = {'red': 2000, 'blue': 1000, 'yellow': 500, 'orange': 1000}
myseries = pd.Series(mydict)
myseries
```




    blue      1000
    orange    1000
    red       2000
    yellow     500
    dtype: int64




```python
colors = ['red','yellow','orange','blue','green']
myseries = pd.Series(mydict, index=colors)
myseries
```




    red       2000.0
    yellow     500.0
    orange    1000.0
    blue      1000.0
    green        NaN
    dtype: float64



* Operations between Series


```python
mydict2 = {'red':400,'yellow':1000,'black':700}
myseries2 = pd.Series(mydict2)
myseries + myseries2
```




    black        NaN
    blue         NaN
    green        NaN
    orange       NaN
    red       2400.0
    yellow    1500.0
    dtype: float64



### The DataFrame

* Defining a DataFrame


```python
data = {'color' : ['blue','green','yellow','red','white'],
        'object' : ['ball','pen','pencil','paper','mug'],
        'price' : [1.2,1.0,0.6,0.9,1.7]}
```


```python
frame = pd.DataFrame(data)
```


```python
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>object</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>blue</td>
      <td>ball</td>
      <td>1.2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>green</td>
      <td>pen</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>yellow</td>
      <td>pencil</td>
      <td>0.6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>red</td>
      <td>paper</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>white</td>
      <td>mug</td>
      <td>1.7</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2 = pd.DataFrame(data, columns=['object','price'])
frame2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>object</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ball</td>
      <td>1.2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pen</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pencil</td>
      <td>0.6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>paper</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>mug</td>
      <td>1.7</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2 = pd.DataFrame(data, index=['one','two','three','four','five'])
frame2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>object</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>one</th>
      <td>blue</td>
      <td>ball</td>
      <td>1.2</td>
    </tr>
    <tr>
      <th>two</th>
      <td>green</td>
      <td>pen</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>three</th>
      <td>yellow</td>
      <td>pencil</td>
      <td>0.6</td>
    </tr>
    <tr>
      <th>four</th>
      <td>red</td>
      <td>paper</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>five</th>
      <td>white</td>
      <td>mug</td>
      <td>1.7</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame3 = pd.DataFrame(np.arange(16).reshape((4,4)),
                      index=['red','blue','yellow','white'],
                      columns=['ball','pen','pencil','paper'])
frame3
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>pen</th>
      <th>pencil</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>blue</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>white</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>



 * Selecting Elements


```python
frame.columns
```




    Index(['color', 'object', 'price'], dtype='object')




```python
frame.index
```




    RangeIndex(start=0, stop=5, step=1)




```python
frame.values
```




    array([['blue', 'ball', 1.2],
           ['green', 'pen', 1.0],
           ['yellow', 'pencil', 0.6],
           ['red', 'paper', 0.9],
           ['white', 'mug', 1.7]], dtype=object)




```python
frame['price']
```




    0    1.2
    1    1.0
    2    0.6
    3    0.9
    4    1.7
    Name: price, dtype: float64




```python
frame.price
```




    0    1.2
    1    1.0
    2    0.6
    3    0.9
    4    1.7
    Name: price, dtype: float64




```python
frame.ix[2]
```




    color     yellow
    object    pencil
    price        0.6
    Name: 2, dtype: object




```python
frame.ix[[2,4]]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>object</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>yellow</td>
      <td>pencil</td>
      <td>0.6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>white</td>
      <td>mug</td>
      <td>1.7</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame[0:1]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>object</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>blue</td>
      <td>ball</td>
      <td>1.2</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame[1:3]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>object</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>green</td>
      <td>pen</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>yellow</td>
      <td>pencil</td>
      <td>0.6</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame['object'][3]
```




    'paper'



 * Assigning Values


```python
frame.index.name = 'id'; frame.columns.name = 'item'
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>item</th>
      <th>color</th>
      <th>object</th>
      <th>price</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>blue</td>
      <td>ball</td>
      <td>1.2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>green</td>
      <td>pen</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>yellow</td>
      <td>pencil</td>
      <td>0.6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>red</td>
      <td>paper</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>white</td>
      <td>mug</td>
      <td>1.7</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame['new'] = 12
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>item</th>
      <th>color</th>
      <th>object</th>
      <th>price</th>
      <th>new</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>blue</td>
      <td>ball</td>
      <td>1.2</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>green</td>
      <td>pen</td>
      <td>1.0</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>yellow</td>
      <td>pencil</td>
      <td>0.6</td>
      <td>12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>red</td>
      <td>paper</td>
      <td>0.9</td>
      <td>12</td>
    </tr>
    <tr>
      <th>4</th>
      <td>white</td>
      <td>mug</td>
      <td>1.7</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame['new'] = [3.0,1.3,2.2,0.8,1.1]
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>item</th>
      <th>color</th>
      <th>object</th>
      <th>price</th>
      <th>new</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>blue</td>
      <td>ball</td>
      <td>1.2</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>green</td>
      <td>pen</td>
      <td>1.0</td>
      <td>1.3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>yellow</td>
      <td>pencil</td>
      <td>0.6</td>
      <td>2.2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>red</td>
      <td>paper</td>
      <td>0.9</td>
      <td>0.8</td>
    </tr>
    <tr>
      <th>4</th>
      <td>white</td>
      <td>mug</td>
      <td>1.7</td>
      <td>1.1</td>
    </tr>
  </tbody>
</table>
</div>




```python
ser = pd.Series(np.arange(5))
ser
```




    0    0
    1    1
    2    2
    3    3
    4    4
    dtype: int32




```python
frame['new'] = ser
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>item</th>
      <th>color</th>
      <th>object</th>
      <th>price</th>
      <th>new</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>blue</td>
      <td>ball</td>
      <td>1.2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>green</td>
      <td>pen</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>yellow</td>
      <td>pencil</td>
      <td>0.6</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>red</td>
      <td>paper</td>
      <td>0.9</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>white</td>
      <td>mug</td>
      <td>1.7</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame['price'][2] = 3.3
```

    C:\Anaconda36\lib\site-packages\ipykernel\__main__.py:1: SettingWithCopyWarning:
    A value is trying to be set on a copy of a slice from a DataFrame

    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      if __name__ == '__main__':


* Membership of a Value


```python
frame.isin([1.0,'pen'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>item</th>
      <th>color</th>
      <th>object</th>
      <th>price</th>
      <th>new</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame[frame.isin([1.0,'pen'])]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>item</th>
      <th>color</th>
      <th>object</th>
      <th>price</th>
      <th>new</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>pen</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



* Deleting a Column


```python
del frame['new']
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>item</th>
      <th>color</th>
      <th>object</th>
      <th>price</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>blue</td>
      <td>ball</td>
      <td>1.2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>green</td>
      <td>pen</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>yellow</td>
      <td>pencil</td>
      <td>3.3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>red</td>
      <td>paper</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>white</td>
      <td>mug</td>
      <td>1.7</td>
    </tr>
  </tbody>
</table>
</div>



 * Filtering


```python
frame[frame < 12]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>item</th>
      <th>color</th>
      <th>object</th>
      <th>price</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>blue</td>
      <td>ball</td>
      <td>1.2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>green</td>
      <td>pen</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>yellow</td>
      <td>pencil</td>
      <td>3.3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>red</td>
      <td>paper</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>white</td>
      <td>mug</td>
      <td>1.7</td>
    </tr>
  </tbody>
</table>
</div>



* DataFrame from Nested dict


```python
nestdict = {'red': { 2012: 22, 2013: 33 },
            'white': { 2011: 13, 2012: 22; 2013: 16},
            'blue': {2011: 17, 2012: 27; 2013: 18}}
```


      File "<ipython-input-64-ac007c6cd817>", line 2
        'white': { 2011: 13, 2012: 22; 2013: 16},
                                     ^
    SyntaxError: invalid syntax




```python
nestdict = {'red':{2012: 22, 2013: 33},
            'white':{2011: 13, 2012: 22, 2013: 16},
            'blue': {2011: 17, 2012: 27, 2013: 18}}
frame2 = pd.DataFrame(nestdict)
frame2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>blue</th>
      <th>red</th>
      <th>white</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>17</td>
      <td>NaN</td>
      <td>13</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>27</td>
      <td>22.0</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>18</td>
      <td>33.0</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>



 * Transposition of a DataFrame


```python
frame2.T
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2011</th>
      <th>2012</th>
      <th>2013</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>blue</th>
      <td>17.0</td>
      <td>27.0</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>red</th>
      <td>NaN</td>
      <td>22.0</td>
      <td>33.0</td>
    </tr>
    <tr>
      <th>white</th>
      <td>13.0</td>
      <td>22.0</td>
      <td>16.0</td>
    </tr>
  </tbody>
</table>
</div>



### The Index Objects


```python
ser = pd.Series([5,0,3,8,4], index=['red','blue','yellow','white','green'])
ser.index
```




    Index(['red', 'blue', 'yellow', 'white', 'green'], dtype='object')



* Methods on Index


```python
ser.idxmin()
```




    'blue'




```python
ser.idxmax()
```




    'white'



* Index with Duplicate Labels


```python
serd = pd.Series(range(6), index=['white','white','blue','green','green','yellow'])
serd
```




    white     0
    white     1
    blue      2
    green     3
    green     4
    yellow    5
    dtype: int32




```python
serd['white']
```




    white    0
    white    1
    dtype: int32




```python
serd.index.is_unique
```




    False




```python
frame.index.is_unique
```




    True



## 4.6 Other Functionalities on Indexes

### Reindexing


```python
ser = pd.Series([2,5,7,4], index=['one','two','three','four'])
ser
```




    one      2
    two      5
    three    7
    four     4
    dtype: int64




```python
ser.reindex(['three','four','five','one'])
```




    three    7.0
    four     4.0
    five     NaN
    one      2.0
    dtype: float64




```python
ser3 = pd.Series([1,5,6,3],index=[0,3,5,6])
```


```python
ser3
```




    0    1
    3    5
    5    6
    6    3
    dtype: int64




```python
ser3.reindex(range(6),method='ffill')
```




    0    1
    1    1
    2    1
    3    5
    4    5
    5    6
    dtype: int64




```python
ser3.reindex(range(6),method='bfill')
```




    0    1
    1    5
    2    5
    3    5
    4    6
    5    6
    dtype: int64




```python
frame.reindex(range(5), method='ffill',columns=['colors','price','new','object'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>item</th>
      <th>colors</th>
      <th>price</th>
      <th>new</th>
      <th>object</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>1.2</td>
      <td>NaN</td>
      <td>ball</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>pen</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>3.3</td>
      <td>NaN</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>0.9</td>
      <td>NaN</td>
      <td>paper</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>1.7</td>
      <td>NaN</td>
      <td>mug</td>
    </tr>
  </tbody>
</table>
</div>



### Dropping


```python
ser = pd.Series(np.arange(4.), index=['red','blue','yellow','white'])
ser
```




    red       0.0
    blue      1.0
    yellow    2.0
    white     3.0
    dtype: float64




```python
ser.drop('yellow')
```




    red      0.0
    blue     1.0
    white    3.0
    dtype: float64




```python
ser.drop(['blue','white'])
```




    red       0.0
    yellow    2.0
    dtype: float64




```python
frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red','blue','yellow','white'],
                     columns=['ball','pen','pencil','paper'])
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>pen</th>
      <th>pencil</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>blue</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>white</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.drop(['blue','yellow'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>pen</th>
      <th>pencil</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>white</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.drop(['pen','pencil'],axis=1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>blue</th>
      <td>4</td>
      <td>7</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>8</td>
      <td>11</td>
    </tr>
    <tr>
      <th>white</th>
      <td>12</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>



### Arithmetic and Data Alignment


```python
s1 = pd.Series([3,2,5,1],['white','yellow','green','blue'])
s2 = pd.Series([1,4,7,2,1],['white','yellow','black','blue','brown'])
```


```python
s1 + s2
```




    black     NaN
    blue      3.0
    brown     NaN
    green     NaN
    white     4.0
    yellow    6.0
    dtype: float64




```python
frame1 = pd.DataFrame(np.arange(16).reshape((4,4)),
                      index=['red','blue','yellow','white'],
                      columns=['ball','pen','pencil','paper'])

frame2 = pd.DataFrame(np.arange(12).reshape((4,3)),
                      index=['blue','green','white','yellow'],
                      columns=['mug','pen','ball'])

frame1
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>pen</th>
      <th>pencil</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>blue</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>white</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame1
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>pen</th>
      <th>pencil</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>blue</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>white</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mug</th>
      <th>pen</th>
      <th>ball</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>blue</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>green</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>white</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>



## 4.7 Operations between Data Structures

### Flexible Arithmetic Methods


```python
frame1.add(frame2)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>mug</th>
      <th>paper</th>
      <th>pen</th>
      <th>pencil</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>blue</th>
      <td>6.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>green</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>red</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>white</th>
      <td>20.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>20.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>19.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>19.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### Operations between DataFrame and Series


```python
frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red','blue','yellow','white'],
                     columns=['ball','pen','pencil','paper'])
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>pen</th>
      <th>pencil</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>blue</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>white</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
ser = pd.Series(np.arange(4), index=['ball','pen','pencil','paper'])
ser
```




    ball      0
    pen       1
    pencil    2
    paper     3
    dtype: int32




```python
frame - ser
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>pen</th>
      <th>pencil</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>blue</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
    </tr>
    <tr>
      <th>white</th>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python
ser['mug'] = 9
ser
```




    ball      0
    pen       1
    pencil    2
    paper     3
    mug       9
    dtype: int64




```python
frame - ser
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>mug</th>
      <th>paper</th>
      <th>pen</th>
      <th>pencil</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>blue</th>
      <td>4</td>
      <td>NaN</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>8</td>
      <td>NaN</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
    </tr>
    <tr>
      <th>white</th>
      <td>12</td>
      <td>NaN</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



## 4.8 Function Application and Mapping
### Functions by Element


```python
frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red','blue','yellow','white'],
                     columns=['ball','pen','pencil','paper'])
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>pen</th>
      <th>pencil</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>blue</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>white</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
np.sqrt(frame)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>pen</th>
      <th>pencil</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>1.414214</td>
      <td>1.732051</td>
    </tr>
    <tr>
      <th>blue</th>
      <td>2.000000</td>
      <td>2.236068</td>
      <td>2.449490</td>
      <td>2.645751</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>2.828427</td>
      <td>3.000000</td>
      <td>3.162278</td>
      <td>3.316625</td>
    </tr>
    <tr>
      <th>white</th>
      <td>3.464102</td>
      <td>3.605551</td>
      <td>3.741657</td>
      <td>3.872983</td>
    </tr>
  </tbody>
</table>
</div>



### Functions by Row or Column


```python
f = lambda x: x.max() - x.min()
```


```python
def f(x):
    return x.max() - x.min()
```


```python
frame.apply(f)
```




    ball      12
    pen       12
    pencil    12
    paper     12
    dtype: int64




```python
frame.apply(f, axis=1)
```




    red       3
    blue      3
    yellow    3
    white     3
    dtype: int64




```python
def f(x):
    return pd.Series([x.min(), x.max()], index=['min','max'])
```


```python
frame.apply(f)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>pen</th>
      <th>pencil</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>min</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>max</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>



### Statistics Functions


```python
frame.sum()
```




    ball      24
    pen       28
    pencil    32
    paper     36
    dtype: int64




```python
frame.mean()
```




    ball      6.0
    pen       7.0
    pencil    8.0
    paper     9.0
    dtype: float64




```python
frame.describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>pen</th>
      <th>pencil</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>6.000000</td>
      <td>7.000000</td>
      <td>8.000000</td>
      <td>9.000000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>5.163978</td>
      <td>5.163978</td>
      <td>5.163978</td>
      <td>5.163978</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>3.000000</td>
      <td>4.000000</td>
      <td>5.000000</td>
      <td>6.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>6.000000</td>
      <td>7.000000</td>
      <td>8.000000</td>
      <td>9.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>9.000000</td>
      <td>10.000000</td>
      <td>11.000000</td>
      <td>12.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>12.000000</td>
      <td>13.000000</td>
      <td>14.000000</td>
      <td>15.000000</td>
    </tr>
  </tbody>
</table>
</div>



## 4.9 Sorting and Ranking


```python
ser = pd.Series([5,0,3,8,4], index=['red','blue','yellow','white','green'])
ser
```




    red       5
    blue      0
    yellow    3
    white     8
    green     4
    dtype: int64




```python
ser.sort_index(ascending=False)
```




    yellow    3
    white     8
    red       5
    green     4
    blue      0
    dtype: int64




```python
frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red','blue','yellow','white'],
                     columns=['ball','pen','pencil','paper'])
frame

```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>pen</th>
      <th>pencil</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>blue</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>white</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.sort_index()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>pen</th>
      <th>pencil</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>blue</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>red</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>white</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.sort_index(axis=1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>paper</th>
      <th>pen</th>
      <th>pencil</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>blue</th>
      <td>4</td>
      <td>7</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>8</td>
      <td>11</td>
      <td>9</td>
      <td>10</td>
    </tr>
    <tr>
      <th>white</th>
      <td>12</td>
      <td>15</td>
      <td>13</td>
      <td>14</td>
    </tr>
  </tbody>
</table>
</div>




```python
ser.order()
```

    C:\Anaconda36\lib\site-packages\ipykernel\__main__.py:1: FutureWarning: order is deprecated, use sort_values(...)
      if __name__ == '__main__':





    blue      0
    yellow    3
    green     4
    red       5
    white     8
    dtype: int64




```python
frame.sort_index(by='pen')
```

    C:\Anaconda36\lib\site-packages\ipykernel\__main__.py:1: FutureWarning: by argument to sort_index is deprecated, pls use .sort_values(by=...)
      if __name__ == '__main__':





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>pen</th>
      <th>pencil</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>blue</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>white</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.sort_index(by=['pen','pencil'])
```

    C:\Anaconda36\lib\site-packages\ipykernel\__main__.py:1: FutureWarning: by argument to sort_index is deprecated, pls use .sort_values(by=...)
      if __name__ == '__main__':





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>pen</th>
      <th>pencil</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>blue</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>white</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
ser.rank()
```




    red       4.0
    blue      1.0
    yellow    2.0
    white     5.0
    green     3.0
    dtype: float64




```python
ser.rank(method='first')
```




    red       4.0
    blue      1.0
    yellow    2.0
    white     5.0
    green     3.0
    dtype: float64




```python
ser.rank(ascending=False)
```




    red       2.0
    blue      5.0
    yellow    4.0
    white     1.0
    green     3.0
    dtype: float64



## 4.10 Correlation and Covariance


```python
seq2 = pd.Series([3,4,3,4,5,4,3,2],['2006','2007','2008','2009','2010','2011','2012','2013'])
seq = pd.Series([1,2,3,4,4,3,2,1],['2006','2007','2008','2009','2010','2011','2012','2013'])
```


```python
seq.corr(seq2)
```




    0.77459666924148352




```python
seq.cov(seq2)
```




    0.8571428571428571




```python
frame2 = pd.DataFrame([[1,4,3,6],[4,5,6,1],[3,3,1,5],[4,1,6,4]],
                   index=['red','blue','yellow','white'],
                   columns=['ball','pen','pencil','paper'])
frame2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>pen</th>
      <th>pencil</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <td>1</td>
      <td>4</td>
      <td>3</td>
      <td>6</td>
    </tr>
    <tr>
      <th>blue</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>1</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>white</th>
      <td>4</td>
      <td>1</td>
      <td>6</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2.corr()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>pen</th>
      <th>pencil</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ball</th>
      <td>1.000000</td>
      <td>-0.276026</td>
      <td>0.577350</td>
      <td>-0.763763</td>
    </tr>
    <tr>
      <th>pen</th>
      <td>-0.276026</td>
      <td>1.000000</td>
      <td>-0.079682</td>
      <td>-0.361403</td>
    </tr>
    <tr>
      <th>pencil</th>
      <td>0.577350</td>
      <td>-0.079682</td>
      <td>1.000000</td>
      <td>-0.692935</td>
    </tr>
    <tr>
      <th>paper</th>
      <td>-0.763763</td>
      <td>-0.361403</td>
      <td>-0.692935</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2.corrwith(ser)
```




    ball     -0.140028
    pen      -0.869657
    pencil    0.080845
    paper     0.595854
    dtype: float64




```python
frame2.corrwith(frame)
```




    ball      0.730297
    pen      -0.831522
    pencil    0.210819
    paper    -0.119523
    dtype: float64



## 4.11 “Not a Number” Data

### Assigning a NaN Value


```python
ser = pd.Series([0,1,2,np.NaN,9], index=['red','blue','yellow','white','green'])
ser
```




    red       0.0
    blue      1.0
    yellow    2.0
    white     NaN
    green     9.0
    dtype: float64




```python
ser['white'] = None
ser
```




    red       0.0
    blue      1.0
    yellow    2.0
    white     NaN
    green     9.0
    dtype: float64



### Filtering Out NaN Values


```python
ser.dropna()
```




    red       0.0
    blue      1.0
    yellow    2.0
    green     9.0
    dtype: float64




```python
ser[ser.notnull()]
```




    red       0.0
    blue      1.0
    yellow    2.0
    green     9.0
    dtype: float64




```python
frame3 = pd.DataFrame([[6,np.nan,6],[np.nan,np.nan,np.nan],[2,np.nan,5]],
                      index = ['blue','green','red'],
                      columns = ['ball','mug','pen'])
```


```python
frame3
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>mug</th>
      <th>pen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>blue</th>
      <td>6.0</td>
      <td>NaN</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>green</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>red</th>
      <td>2.0</td>
      <td>NaN</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame3.dropna(how='all')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>mug</th>
      <th>pen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>blue</th>
      <td>6.0</td>
      <td>NaN</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>red</th>
      <td>2.0</td>
      <td>NaN</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>



### Filling in NaN Occurrences


```python
frame3.fillna(0)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>mug</th>
      <th>pen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>blue</th>
      <td>6.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>green</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>red</th>
      <td>2.0</td>
      <td>0.0</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame3.fillna({'ball':1,'mug':0,'pen':99})
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>mug</th>
      <th>pen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>blue</th>
      <td>6.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>green</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>red</th>
      <td>2.0</td>
      <td>0.0</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>



## 4.12 Hierarchical Indexing and Leveling


```python
mser = pd.Series(np.random.rand(8),
                 index=[['white','white','white','blue','blue','red','red','red'],
                        ['up','down','right','up','down','up','down','left']])
mser
```




    white  up       0.434400
           down     0.942360
           right    0.665148
    blue   up       0.329476
           down     0.580203
    red    up       0.301266
           down     0.043086
           left     0.148905
    dtype: float64




```python
mser.index
```




    MultiIndex(levels=[['blue', 'red', 'white'], ['down', 'left', 'right', 'up']],
               labels=[[2, 2, 2, 0, 0, 1, 1, 1], [3, 0, 2, 3, 0, 3, 0, 1]])




```python
mser['white']
```




    up       0.434400
    down     0.942360
    right    0.665148
    dtype: float64




```python
mser[:,'up']
```




    white    0.434400
    blue     0.329476
    red      0.301266
    dtype: float64




```python
mser['white','up']
```




    0.4344003416809239




```python
mser.unstack()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>down</th>
      <th>left</th>
      <th>right</th>
      <th>up</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>blue</th>
      <td>0.580203</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.329476</td>
    </tr>
    <tr>
      <th>red</th>
      <td>0.043086</td>
      <td>0.148905</td>
      <td>NaN</td>
      <td>0.301266</td>
    </tr>
    <tr>
      <th>white</th>
      <td>0.942360</td>
      <td>NaN</td>
      <td>0.665148</td>
      <td>0.434400</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ball</th>
      <th>pen</th>
      <th>pencil</th>
      <th>paper</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>blue</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>yellow</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>white</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.stack()
```




    red     ball       0
            pen        1
            pencil     2
            paper      3
    blue    ball       4
            pen        5
            pencil     6
            paper      7
    yellow  ball       8
            pen        9
            pencil    10
            paper     11
    white   ball      12
            pen       13
            pencil    14
            paper     15
    dtype: int32




```python
mframe = pd.DataFrame(np.random.randn(16).reshape(4,4),
                      index=[['white','white','red','red'], ['up','down','up','down']],
                      columns=[['pen','pen','paper','paper'],[1,2,1,2]])
mframe
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="2" halign="left">pen</th>
      <th colspan="2" halign="left">paper</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">white</th>
      <th>up</th>
      <td>-0.693579</td>
      <td>-0.374331</td>
      <td>0.382002</td>
      <td>1.539948</td>
    </tr>
    <tr>
      <th>down</th>
      <td>-0.816785</td>
      <td>-1.334461</td>
      <td>0.202928</td>
      <td>0.068978</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">red</th>
      <th>up</th>
      <td>-1.029277</td>
      <td>0.167646</td>
      <td>0.127078</td>
      <td>0.651874</td>
    </tr>
    <tr>
      <th>down</th>
      <td>0.947015</td>
      <td>0.836286</td>
      <td>-1.411437</td>
      <td>-0.901950</td>
    </tr>
  </tbody>
</table>
</div>



### Reordering and Sorting Levels


```python
mframe.columns.names = ['objects','id']
```


```python
mframe.index.names = ['colors','status']
```


```python
mframe
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>objects</th>
      <th colspan="2" halign="left">pen</th>
      <th colspan="2" halign="left">paper</th>
    </tr>
    <tr>
      <th></th>
      <th>id</th>
      <th>1</th>
      <th>2</th>
      <th>1</th>
      <th>2</th>
    </tr>
    <tr>
      <th>colors</th>
      <th>status</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">white</th>
      <th>up</th>
      <td>-0.693579</td>
      <td>-0.374331</td>
      <td>0.382002</td>
      <td>1.539948</td>
    </tr>
    <tr>
      <th>down</th>
      <td>-0.816785</td>
      <td>-1.334461</td>
      <td>0.202928</td>
      <td>0.068978</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">red</th>
      <th>up</th>
      <td>-1.029277</td>
      <td>0.167646</td>
      <td>0.127078</td>
      <td>0.651874</td>
    </tr>
    <tr>
      <th>down</th>
      <td>0.947015</td>
      <td>0.836286</td>
      <td>-1.411437</td>
      <td>-0.901950</td>
    </tr>
  </tbody>
</table>
</div>




```python
mframe.swaplevel('colors','status')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>objects</th>
      <th colspan="2" halign="left">pen</th>
      <th colspan="2" halign="left">paper</th>
    </tr>
    <tr>
      <th></th>
      <th>id</th>
      <th>1</th>
      <th>2</th>
      <th>1</th>
      <th>2</th>
    </tr>
    <tr>
      <th>status</th>
      <th>colors</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>up</th>
      <th>white</th>
      <td>-0.693579</td>
      <td>-0.374331</td>
      <td>0.382002</td>
      <td>1.539948</td>
    </tr>
    <tr>
      <th>down</th>
      <th>white</th>
      <td>-0.816785</td>
      <td>-1.334461</td>
      <td>0.202928</td>
      <td>0.068978</td>
    </tr>
    <tr>
      <th>up</th>
      <th>red</th>
      <td>-1.029277</td>
      <td>0.167646</td>
      <td>0.127078</td>
      <td>0.651874</td>
    </tr>
    <tr>
      <th>down</th>
      <th>red</th>
      <td>0.947015</td>
      <td>0.836286</td>
      <td>-1.411437</td>
      <td>-0.901950</td>
    </tr>
  </tbody>
</table>
</div>




```python
mframe.sortlevel('colors')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>objects</th>
      <th colspan="2" halign="left">pen</th>
      <th colspan="2" halign="left">paper</th>
    </tr>
    <tr>
      <th></th>
      <th>id</th>
      <th>1</th>
      <th>2</th>
      <th>1</th>
      <th>2</th>
    </tr>
    <tr>
      <th>colors</th>
      <th>status</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">red</th>
      <th>down</th>
      <td>0.947015</td>
      <td>0.836286</td>
      <td>-1.411437</td>
      <td>-0.901950</td>
    </tr>
    <tr>
      <th>up</th>
      <td>-1.029277</td>
      <td>0.167646</td>
      <td>0.127078</td>
      <td>0.651874</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">white</th>
      <th>down</th>
      <td>-0.816785</td>
      <td>-1.334461</td>
      <td>0.202928</td>
      <td>0.068978</td>
    </tr>
    <tr>
      <th>up</th>
      <td>-0.693579</td>
      <td>-0.374331</td>
      <td>0.382002</td>
      <td>1.539948</td>
    </tr>
  </tbody>
</table>
</div>



### Summary Statistic by Level


```python
mframe.sum(level='colors')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>objects</th>
      <th colspan="2" halign="left">pen</th>
      <th colspan="2" halign="left">paper</th>
    </tr>
    <tr>
      <th>id</th>
      <th>1</th>
      <th>2</th>
      <th>1</th>
      <th>2</th>
    </tr>
    <tr>
      <th>colors</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>red</th>
      <td>-0.082262</td>
      <td>1.003932</td>
      <td>-1.284359</td>
      <td>-0.250076</td>
    </tr>
    <tr>
      <th>white</th>
      <td>-1.510365</td>
      <td>-1.708792</td>
      <td>0.584930</td>
      <td>1.608926</td>
    </tr>
  </tbody>
</table>
</div>




```python
mframe.sum(level='id', axis=1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>1</th>
      <th>2</th>
    </tr>
    <tr>
      <th>colors</th>
      <th>status</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">white</th>
      <th>up</th>
      <td>-0.311577</td>
      <td>1.165617</td>
    </tr>
    <tr>
      <th>down</th>
      <td>-0.613858</td>
      <td>-1.265483</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">red</th>
      <th>up</th>
      <td>-0.902199</td>
      <td>0.819520</td>
    </tr>
    <tr>
      <th>down</th>
      <td>-0.464422</td>
      <td>-0.065664</td>
    </tr>
  </tbody>
</table>
</div>



## 4.13 Conclusions


```python

```
