
# Chapter 6: pandas in Depth: Data Manipulation
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 6: pandas in Depth: Data Manipulation](#chapter-6-pandas-in-depth-data-manipulation)
  * [6.1 Data Preparation](#61-data-preparation)
    * [Merging](#merging)
  * [6.2 Concatenating](#62-concatenating)
    * [Combining](#combining)
    * [Pivoting](#pivoting)
    * [Removing](#removing)
  * [6.3 Data Transformation](#63-data-transformation)
    * [Removing Duplicates](#removing-duplicates)
    * [Mapping](#mapping)
  * [6.4 Discretization and Binning](#64-discretization-and-binning)
    * [Detecting and Filtering Outliers](#detecting-and-filtering-outliers)
  * [6.5 Permutation](#65-permutation)
  * [6.6 String Manipulation](#66-string-manipulation)
    * [Built-in Methods for Manipulation of Strings](#built-in-methods-for-manipulation-of-strings)
    * [Regular Expressions](#regular-expressions)
  * [6.7 Data Aggregation](#67-data-aggregation)
    * [GroupBy](#groupby)
    * [A Practical Example](#a-practical-example)
    * [Hierarchical Grouping](#hierarchical-grouping)
  * [6.8 Group Iteration](#68-group-iteration)
    * [Chain of Transformations](#chain-of-transformations)
    * [Functions on Groups](#functions-on-groups)
  * [6.9 Advanced Data Aggregation](#69-advanced-data-aggregation)
  * [6.10 Conclusions](#610-conclusions)

<!-- tocstop -->


## 6.1 Data Preparation

### Merging


```python
import numpy as np
import pandas as pd
```


```python
frame1 = pd.DataFrame( {'id':['ball','pencil','pen','mug','ashtray'],
                        'price': [12.33,11.44,33.21,13.23,33.62]})
frame1
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ball</td>
      <td>12.33</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pencil</td>
      <td>11.44</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pen</td>
      <td>33.21</td>
    </tr>
    <tr>
      <th>3</th>
      <td>mug</td>
      <td>13.23</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ashtray</td>
      <td>33.62</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2 = pd.DataFrame( {'id':['pencil','pencil','ball','pen'],
'color': ['white','red','red','black']})
frame2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>white</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>1</th>
      <td>red</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>2</th>
      <td>red</td>
      <td>ball</td>
    </tr>
    <tr>
      <th>3</th>
      <td>black</td>
      <td>pen</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(frame1,frame2)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>price</th>
      <th>color</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ball</td>
      <td>12.33</td>
      <td>red</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pencil</td>
      <td>11.44</td>
      <td>white</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pencil</td>
      <td>11.44</td>
      <td>red</td>
    </tr>
    <tr>
      <th>3</th>
      <td>pen</td>
      <td>33.21</td>
      <td>black</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame1 = pd.DataFrame( {'id':['ball','pencil','pen','mug','ashtray'],
                        'color': ['white','red','red','black','green'],
                        'brand': ['OMG','ABC','ABC','POD','POD']})
frame1
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>brand</th>
      <th>color</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>OMG</td>
      <td>white</td>
      <td>ball</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ABC</td>
      <td>red</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ABC</td>
      <td>red</td>
      <td>pen</td>
    </tr>
    <tr>
      <th>3</th>
      <td>POD</td>
      <td>black</td>
      <td>mug</td>
    </tr>
    <tr>
      <th>4</th>
      <td>POD</td>
      <td>green</td>
      <td>ashtray</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2 = pd.DataFrame( {'id':['pencil','pencil','ball','pen'],
                        'brand': ['OMG','POD','ABC','POD']})
frame2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>brand</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>OMG</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>1</th>
      <td>POD</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ABC</td>
      <td>ball</td>
    </tr>
    <tr>
      <th>3</th>
      <td>POD</td>
      <td>pen</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(frame1,frame2)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>brand</th>
      <th>color</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
pd.merge(frame1,frame2,on='id')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>brand_x</th>
      <th>color</th>
      <th>id</th>
      <th>brand_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>OMG</td>
      <td>white</td>
      <td>ball</td>
      <td>ABC</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ABC</td>
      <td>red</td>
      <td>pencil</td>
      <td>OMG</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ABC</td>
      <td>red</td>
      <td>pencil</td>
      <td>POD</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ABC</td>
      <td>red</td>
      <td>pen</td>
      <td>POD</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(frame1,frame2,on='brand')
frame2.columns = ['brand','sid']
frame2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>brand</th>
      <th>sid</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>OMG</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>1</th>
      <td>POD</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ABC</td>
      <td>ball</td>
    </tr>
    <tr>
      <th>3</th>
      <td>POD</td>
      <td>pen</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(frame1, frame2, left_on='id', right_on='sid')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>brand_x</th>
      <th>color</th>
      <th>id</th>
      <th>brand_y</th>
      <th>sid</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>OMG</td>
      <td>white</td>
      <td>ball</td>
      <td>ABC</td>
      <td>ball</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ABC</td>
      <td>red</td>
      <td>pencil</td>
      <td>OMG</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ABC</td>
      <td>red</td>
      <td>pencil</td>
      <td>POD</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ABC</td>
      <td>red</td>
      <td>pen</td>
      <td>POD</td>
      <td>pen</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame2.columns = ['brand','id']
```


```python
pd.merge(frame1,frame2,on='id')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>brand_x</th>
      <th>color</th>
      <th>id</th>
      <th>brand_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>OMG</td>
      <td>white</td>
      <td>ball</td>
      <td>ABC</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ABC</td>
      <td>red</td>
      <td>pencil</td>
      <td>OMG</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ABC</td>
      <td>red</td>
      <td>pencil</td>
      <td>POD</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ABC</td>
      <td>red</td>
      <td>pen</td>
      <td>POD</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(frame1,frame2,on='id',how='outer')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>brand_x</th>
      <th>color</th>
      <th>id</th>
      <th>brand_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>OMG</td>
      <td>white</td>
      <td>ball</td>
      <td>ABC</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ABC</td>
      <td>red</td>
      <td>pencil</td>
      <td>OMG</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ABC</td>
      <td>red</td>
      <td>pencil</td>
      <td>POD</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ABC</td>
      <td>red</td>
      <td>pen</td>
      <td>POD</td>
    </tr>
    <tr>
      <th>4</th>
      <td>POD</td>
      <td>black</td>
      <td>mug</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>POD</td>
      <td>green</td>
      <td>ashtray</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(frame1,frame2,on='id',how='left')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>brand_x</th>
      <th>color</th>
      <th>id</th>
      <th>brand_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>OMG</td>
      <td>white</td>
      <td>ball</td>
      <td>ABC</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ABC</td>
      <td>red</td>
      <td>pencil</td>
      <td>OMG</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ABC</td>
      <td>red</td>
      <td>pencil</td>
      <td>POD</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ABC</td>
      <td>red</td>
      <td>pen</td>
      <td>POD</td>
    </tr>
    <tr>
      <th>4</th>
      <td>POD</td>
      <td>black</td>
      <td>mug</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>POD</td>
      <td>green</td>
      <td>ashtray</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(frame1,frame2,on=['id','brand'],how='outer')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>brand</th>
      <th>color</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>OMG</td>
      <td>white</td>
      <td>ball</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ABC</td>
      <td>red</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ABC</td>
      <td>red</td>
      <td>pen</td>
    </tr>
    <tr>
      <th>3</th>
      <td>POD</td>
      <td>black</td>
      <td>mug</td>
    </tr>
    <tr>
      <th>4</th>
      <td>POD</td>
      <td>green</td>
      <td>ashtray</td>
    </tr>
    <tr>
      <th>5</th>
      <td>OMG</td>
      <td>NaN</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>6</th>
      <td>POD</td>
      <td>NaN</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>7</th>
      <td>ABC</td>
      <td>NaN</td>
      <td>ball</td>
    </tr>
    <tr>
      <th>8</th>
      <td>POD</td>
      <td>NaN</td>
      <td>pen</td>
    </tr>
  </tbody>
</table>
</div>



* Merging on Index


```python
pd.merge(frame1,frame2,right_index=True, left_index=True)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>brand_x</th>
      <th>color</th>
      <th>id_x</th>
      <th>brand_y</th>
      <th>id_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>OMG</td>
      <td>white</td>
      <td>ball</td>
      <td>OMG</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ABC</td>
      <td>red</td>
      <td>pencil</td>
      <td>POD</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ABC</td>
      <td>red</td>
      <td>pen</td>
      <td>ABC</td>
      <td>ball</td>
    </tr>
    <tr>
      <th>3</th>
      <td>POD</td>
      <td>black</td>
      <td>mug</td>
      <td>POD</td>
      <td>pen</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame1.join(frame2)
```


```python
frame2.columns = ['brand2','id2']
frame1.join(frame2)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>brand</th>
      <th>color</th>
      <th>id</th>
      <th>brand2</th>
      <th>id2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>OMG</td>
      <td>white</td>
      <td>ball</td>
      <td>OMG</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ABC</td>
      <td>red</td>
      <td>pencil</td>
      <td>POD</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ABC</td>
      <td>red</td>
      <td>pen</td>
      <td>ABC</td>
      <td>ball</td>
    </tr>
    <tr>
      <th>3</th>
      <td>POD</td>
      <td>black</td>
      <td>mug</td>
      <td>POD</td>
      <td>pen</td>
    </tr>
    <tr>
      <th>4</th>
      <td>POD</td>
      <td>green</td>
      <td>ashtray</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## 6.2 Concatenating


```python
array1 = np.array([[0, 1, 2],[3, 4, 5],[6, 7, 8]])
```


```python
array2 = np.arange(9).reshape((3,3))+6
array2
```




    array([[ 6,  7,  8],
           [ 9, 10, 11],
           [12, 13, 14]])




```python
np.concatenate([array1,array2],axis=1)
```




    array([[ 0,  1,  2,  6,  7,  8],
           [ 3,  4,  5,  9, 10, 11],
           [ 6,  7,  8, 12, 13, 14]])




```python
np.concatenate([array1,array2],axis=0)
```




    array([[ 0,  1,  2],
           [ 3,  4,  5],
           [ 6,  7,  8],
           [ 6,  7,  8],
           [ 9, 10, 11],
           [12, 13, 14]])




```python
ser1 = pd.Series(np.random.rand(4), index=[1,2,3,4])
ser1
```




    1    0.910493
    2    0.298214
    3    0.318329
    4    0.884459
    dtype: float64




```python
ser2 = pd.Series(np.random.rand(4), index=[5,6,7,8])
ser2
```




    5    0.895608
    6    0.423411
    7    0.103493
    8    0.696658
    dtype: float64




```python
pd.concat([ser1,ser2])
```




    1    0.910493
    2    0.298214
    3    0.318329
    4    0.884459
    5    0.895608
    6    0.423411
    7    0.103493
    8    0.696658
    dtype: float64




```python
pd.concat([ser1,ser2],axis=1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0.910493</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.298214</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.318329</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.884459</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>0.895608</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>0.423411</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>0.103493</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
      <td>0.696658</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([ser1,ser2],axis=1,join='inner')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
pd.concat([ser1,ser2], keys=[1,2])
```




    1  1    0.910493
       2    0.298214
       3    0.318329
       4    0.884459
    2  5    0.895608
       6    0.423411
       7    0.103493
       8    0.696658
    dtype: float64




```python
pd.concat([ser1,ser2], axis=1, keys=[1,2])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0.910493</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.298214</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.318329</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.884459</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>0.895608</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>0.423411</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>0.103493</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
      <td>0.696658</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame1 = pd.DataFrame(np.random.rand(9).reshape(3,3), index=[1,2,3], columns=['A','B','C'])
frame2 = pd.DataFrame(np.random.rand(9).reshape(3,3), index=[4,5,6], columns=['A','B','C'])
pd.concat([frame1, frame2])
```




<div>
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
      <th>1</th>
      <td>0.475940</td>
      <td>0.447771</td>
      <td>0.372670</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.349441</td>
      <td>0.831730</td>
      <td>0.577195</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.559221</td>
      <td>0.541314</td>
      <td>0.877827</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.248061</td>
      <td>0.890715</td>
      <td>0.259952</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.687247</td>
      <td>0.995097</td>
      <td>0.988769</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.513229</td>
      <td>0.056054</td>
      <td>0.886335</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([frame1, frame2], axis=1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0.475940</td>
      <td>0.447771</td>
      <td>0.372670</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.349441</td>
      <td>0.831730</td>
      <td>0.577195</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.559221</td>
      <td>0.541314</td>
      <td>0.877827</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.248061</td>
      <td>0.890715</td>
      <td>0.259952</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.687247</td>
      <td>0.995097</td>
      <td>0.988769</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.513229</td>
      <td>0.056054</td>
      <td>0.886335</td>
    </tr>
  </tbody>
</table>
</div>



### Combining


```python
ser1 = pd.Series(np.random.rand(5),index=[1,2,3,4,5])
ser1
```




    1    0.891562
    2    0.632302
    3    0.881810
    4    0.278750
    5    0.729209
    dtype: float64




```python
ser2 = pd.Series(np.random.rand(4),index=[2,4,5,6])
ser2
```




    2    0.920502
    4    0.723257
    5    0.138429
    6    0.628079
    dtype: float64




```python
ser1.combine_first(ser2)
```




    1    0.891562
    2    0.632302
    3    0.881810
    4    0.278750
    5    0.729209
    6    0.628079
    dtype: float64




```python
ser2.combine_first(ser1)
```




    1    0.891562
    2    0.920502
    3    0.881810
    4    0.723257
    5    0.138429
    6    0.628079
    dtype: float64




```python
ser1[:3].combine_first(ser2[:3])
```

### Pivoting

* Pivoting with Hierarchical Indexing


```python
frame1 = pd.DataFrame(np.arange(9).reshape(3,3),
                      index=['white','black','red'],
                      columns=['ball','pen','pencil'])
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>white</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>black</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>red</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame1.stack()
```




    white  ball      0
           pen       1
           pencil    2
    black  ball      3
           pen       4
           pencil    5
    red    ball      6
           pen       7
           pencil    8
    dtype: int32




```python
ser5.unstack()
```


```python
ser5.unstack(0)
```

* Pivoting from “Long” to “Wide” Format


```python
longframe = pd.DataFrame({ 'color':['white','white','white',
                                    'red','red','red',
                                    'black','black','black'],
                          'item':['ball','pen','mug',
                                  'ball','pen','mug',
                                  'ball','pen','mug'],
                          'value': np.random.rand(9)})
longframe
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>item</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>white</td>
      <td>ball</td>
      <td>0.692423</td>
    </tr>
    <tr>
      <th>1</th>
      <td>white</td>
      <td>pen</td>
      <td>0.122552</td>
    </tr>
    <tr>
      <th>2</th>
      <td>white</td>
      <td>mug</td>
      <td>0.685354</td>
    </tr>
    <tr>
      <th>3</th>
      <td>red</td>
      <td>ball</td>
      <td>0.013963</td>
    </tr>
    <tr>
      <th>4</th>
      <td>red</td>
      <td>pen</td>
      <td>0.544619</td>
    </tr>
    <tr>
      <th>5</th>
      <td>red</td>
      <td>mug</td>
      <td>0.897542</td>
    </tr>
    <tr>
      <th>6</th>
      <td>black</td>
      <td>ball</td>
      <td>0.859759</td>
    </tr>
    <tr>
      <th>7</th>
      <td>black</td>
      <td>pen</td>
      <td>0.009580</td>
    </tr>
    <tr>
      <th>8</th>
      <td>black</td>
      <td>mug</td>
      <td>0.702358</td>
    </tr>
  </tbody>
</table>
</div>



### Removing


```python
wideframe = longframe.pivot('color','item')
wideframe
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">value</th>
    </tr>
    <tr>
      <th>item</th>
      <th>ball</th>
      <th>mug</th>
      <th>pen</th>
    </tr>
    <tr>
      <th>color</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>black</th>
      <td>0.859759</td>
      <td>0.702358</td>
      <td>0.009580</td>
    </tr>
    <tr>
      <th>red</th>
      <td>0.013963</td>
      <td>0.897542</td>
      <td>0.544619</td>
    </tr>
    <tr>
      <th>white</th>
      <td>0.692423</td>
      <td>0.685354</td>
      <td>0.122552</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame1 = pd.DataFrame(np.arange(9).reshape(3,3),
                      index=['white','black','red'],
                      columns=['ball','pen','pencil'])
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>white</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>black</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>red</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
del frame1['ball']
frame1
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pen</th>
      <th>pencil</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>white</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>black</th>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>red</th>
      <td>7</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame1.drop('white')
```

## 6.3 Data Transformation

### Removing Duplicates


```python
dframe = pd.DataFrame({ 'color': ['white','white','red','red','white'],
                       'value': [2,1,3,3,2]})
dframe
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>white</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>white</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>red</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>red</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>white</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
dframe.duplicated()
```




    0    False
    1    False
    2    False
    3     True
    4     True
    dtype: bool




```python
dframe[dframe.duplicated()]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>red</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>white</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
dframe[dframe.duplicated()]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>red</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>white</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



### Mapping


```python
map = {
    'label1' : 'value1,
    'label2' : 'value2,
    ...
}
```

* replace(): replaces values
* map(): creates a new column
* rename(): replaces the index values

* Replacing Values via Mapping


```python
frame = pd.DataFrame({ 'item':['ball','mug','pen','pencil','ashtray'],
                      'color':['white','rosso','verde','black','yellow'],
                      'price':[5.56,4.20,1.30,0.56,2.75]})
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>item</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>white</td>
      <td>ball</td>
      <td>5.56</td>
    </tr>
    <tr>
      <th>1</th>
      <td>rosso</td>
      <td>mug</td>
      <td>4.20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>verde</td>
      <td>pen</td>
      <td>1.30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>black</td>
      <td>pencil</td>
      <td>0.56</td>
    </tr>
    <tr>
      <th>4</th>
      <td>yellow</td>
      <td>ashtray</td>
      <td>2.75</td>
    </tr>
  </tbody>
</table>
</div>




```python
newcolors = {
    'rosso': 'red',
    'verde': 'green'
}
```


```python
frame.replace(newcolors)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>item</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>white</td>
      <td>ball</td>
      <td>5.56</td>
    </tr>
    <tr>
      <th>1</th>
      <td>red</td>
      <td>mug</td>
      <td>4.20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>green</td>
      <td>pen</td>
      <td>1.30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>black</td>
      <td>pencil</td>
      <td>0.56</td>
    </tr>
    <tr>
      <th>4</th>
      <td>yellow</td>
      <td>ashtray</td>
      <td>2.75</td>
    </tr>
  </tbody>
</table>
</div>




```python
ser = pd.Series([1,3,np.nan,4,6,np.nan,3])
ser
```




    0    1.0
    1    3.0
    2    NaN
    3    4.0
    4    6.0
    5    NaN
    6    3.0
    dtype: float64




```python
ser.replace(np.nan,0)
```




    0    1.0
    1    3.0
    2    0.0
    3    4.0
    4    6.0
    5    0.0
    6    3.0
    dtype: float64



* Adding Values via Mapping


```python
frame = pd.DataFrame({ 'item':['ball','mug','pen','pencil','ashtray'],
                      'color':['white','red','green','black','yellow']})
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>item</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>white</td>
      <td>ball</td>
    </tr>
    <tr>
      <th>1</th>
      <td>red</td>
      <td>mug</td>
    </tr>
    <tr>
      <th>2</th>
      <td>green</td>
      <td>pen</td>
    </tr>
    <tr>
      <th>3</th>
      <td>black</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>4</th>
      <td>yellow</td>
      <td>ashtray</td>
    </tr>
  </tbody>
</table>
</div>




```python
price = {
    'ball' : 5.56,
    'mug' : 4.20,
    'bottle' : 1.30,
    'scissors' : 3.41,
    'pen' : 1.30,
    'pencil' : 0.56,
    'ashtray' : 2.75
}
```


```python
frame['price'] = frame['item'].map(prices)
frame
```

* Rename the Indexes of the Axes


```python
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>item</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>white</td>
      <td>ball</td>
    </tr>
    <tr>
      <th>1</th>
      <td>red</td>
      <td>mug</td>
    </tr>
    <tr>
      <th>2</th>
      <td>green</td>
      <td>pen</td>
    </tr>
    <tr>
      <th>3</th>
      <td>black</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>4</th>
      <td>yellow</td>
      <td>ashtray</td>
    </tr>
  </tbody>
</table>
</div>




```python
reindex = {
    0: 'first',
    1: 'second',
    2: 'third',
    3: 'fourth',
    4: 'fifth'}
frame.rename(reindex)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>item</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>first</th>
      <td>white</td>
      <td>ball</td>
    </tr>
    <tr>
      <th>second</th>
      <td>red</td>
      <td>mug</td>
    </tr>
    <tr>
      <th>third</th>
      <td>green</td>
      <td>pen</td>
    </tr>
    <tr>
      <th>fourth</th>
      <td>black</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>fifth</th>
      <td>yellow</td>
      <td>ashtray</td>
    </tr>
  </tbody>
</table>
</div>




```python
recolumn = {
    'item':'object',
    'price': 'value'}
frame.rename(index=reindex, columns=recolumn)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>object</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>first</th>
      <td>white</td>
      <td>ball</td>
    </tr>
    <tr>
      <th>second</th>
      <td>red</td>
      <td>mug</td>
    </tr>
    <tr>
      <th>third</th>
      <td>green</td>
      <td>pen</td>
    </tr>
    <tr>
      <th>fourth</th>
      <td>black</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>fifth</th>
      <td>yellow</td>
      <td>ashtray</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.rename(index={1:'first'}, columns={'item':'object'})
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>object</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>white</td>
      <td>ball</td>
    </tr>
    <tr>
      <th>first</th>
      <td>red</td>
      <td>mug</td>
    </tr>
    <tr>
      <th>2</th>
      <td>green</td>
      <td>pen</td>
    </tr>
    <tr>
      <th>3</th>
      <td>black</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>4</th>
      <td>yellow</td>
      <td>ashtray</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.rename(columns={'item':'object'}, inplace=True)
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>object</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>white</td>
      <td>ball</td>
    </tr>
    <tr>
      <th>1</th>
      <td>red</td>
      <td>mug</td>
    </tr>
    <tr>
      <th>2</th>
      <td>green</td>
      <td>pen</td>
    </tr>
    <tr>
      <th>3</th>
      <td>black</td>
      <td>pencil</td>
    </tr>
    <tr>
      <th>4</th>
      <td>yellow</td>
      <td>ashtray</td>
    </tr>
  </tbody>
</table>
</div>



## 6.4 Discretization and Binning


```python
results = [12,34,67,55,28,90,99,12,3,56,74,44,87,23,49,89,87]
```


```python
bins = [0,25,50,75,100]
```


```python
cat = pd.cut(results, bins)
cat
```




    [(0, 25], (25, 50], (50, 75], (50, 75], (25, 50], ..., (75, 100], (0, 25], (25, 50], (75, 100], (75, 100]]
    Length: 17
    Categories (4, object): [(0, 25] < (25, 50] < (50, 75] < (75, 100]]




```python
cat.levels
```


```python
cat.labels
```

    C:\Anaconda36\lib\site-packages\ipykernel\__main__.py:1: FutureWarning: 'labels' is deprecated. Use 'codes' instead
      if __name__ == '__main__':





    array([0, 1, 2, 2, 1, 3, 3, 0, 0, 2, 2, 1, 3, 0, 1, 3, 3], dtype=int8)




```python
pd.value_counts(cat)
```




    (75, 100]    5
    (50, 75]     4
    (25, 50]     4
    (0, 25]      4
    dtype: int64




```python
bin_names = ['unlikely','less likely','likely','highly likely']
```


```python
pd.cut(results, bins, labels=bin_names)
```




    [unlikely, less likely, likely, likely, less likely, ..., highly likely, unlikely, less likely, highly likely, highly likely]
    Length: 17
    Categories (4, object): [unlikely < less likely < likely < highly likely]




```python
 pd.cut(results, 5)
```




    [(2.904, 22.2], (22.2, 41.4], (60.6, 79.8], (41.4, 60.6], (22.2, 41.4], ..., (79.8, 99], (22.2, 41.4], (41.4, 60.6], (79.8, 99], (79.8, 99]]
    Length: 17
    Categories (5, object): [(2.904, 22.2] < (22.2, 41.4] < (41.4, 60.6] < (60.6, 79.8] < (79.8, 99]]




```python
quintiles = pd.qcut(results, 5)
quintiles
```




    [[3, 24], (24, 46], (62.6, 87], (46, 62.6], (24, 46], ..., (62.6, 87], [3, 24], (46, 62.6], (87, 99], (62.6, 87]]
    Length: 17
    Categories (5, object): [[3, 24] < (24, 46] < (46, 62.6] < (62.6, 87] < (87, 99]]




```python
 pd.value_counts(quintiles)
```




    (62.6, 87]    4
    [3, 24]       4
    (87, 99]      3
    (46, 62.6]    3
    (24, 46]      3
    dtype: int64



### Detecting and Filtering Outliers


```python
randframe = pd.DataFrame(np.random.randn(1000,3))
```


```python
randframe.describe()
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
      <th>count</th>
      <td>1000.000000</td>
      <td>1000.000000</td>
      <td>1000.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>-0.021353</td>
      <td>0.034104</td>
      <td>0.041467</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.012940</td>
      <td>1.006746</td>
      <td>1.015152</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-3.250735</td>
      <td>-3.426949</td>
      <td>-3.768719</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.692757</td>
      <td>-0.672788</td>
      <td>-0.661038</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>-0.006635</td>
      <td>0.036966</td>
      <td>0.071840</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.661155</td>
      <td>0.723325</td>
      <td>0.696483</td>
    </tr>
    <tr>
      <th>max</th>
      <td>3.205903</td>
      <td>3.432151</td>
      <td>3.725687</td>
    </tr>
  </tbody>
</table>
</div>




```python
randframe.std()
```




    0    1.012940
    1    1.006746
    2    1.015152
    dtype: float64




```python
randframe[(np.abs(randframe) > (3*randframe.std())).any(1)]
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
      <th>9</th>
      <td>-1.043426</td>
      <td>1.531990</td>
      <td>3.080348</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.077319</td>
      <td>-1.846109</td>
      <td>3.046813</td>
    </tr>
    <tr>
      <th>51</th>
      <td>3.205903</td>
      <td>0.054044</td>
      <td>1.437197</td>
    </tr>
    <tr>
      <th>157</th>
      <td>-0.914126</td>
      <td>0.982495</td>
      <td>-3.476512</td>
    </tr>
    <tr>
      <th>182</th>
      <td>0.723537</td>
      <td>-3.426949</td>
      <td>-1.413697</td>
    </tr>
    <tr>
      <th>210</th>
      <td>-1.613691</td>
      <td>3.432151</td>
      <td>-0.725403</td>
    </tr>
    <tr>
      <th>541</th>
      <td>0.729019</td>
      <td>-1.153548</td>
      <td>3.725687</td>
    </tr>
    <tr>
      <th>546</th>
      <td>-3.250735</td>
      <td>-0.128765</td>
      <td>0.662599</td>
    </tr>
    <tr>
      <th>604</th>
      <td>-0.326745</td>
      <td>3.104579</td>
      <td>0.962763</td>
    </tr>
    <tr>
      <th>745</th>
      <td>1.336574</td>
      <td>3.082801</td>
      <td>0.920802</td>
    </tr>
    <tr>
      <th>844</th>
      <td>-2.092100</td>
      <td>-0.497475</td>
      <td>-3.768719</td>
    </tr>
    <tr>
      <th>900</th>
      <td>3.083482</td>
      <td>0.350981</td>
      <td>-0.092085</td>
    </tr>
    <tr>
      <th>906</th>
      <td>-0.539917</td>
      <td>3.182339</td>
      <td>-0.962901</td>
    </tr>
  </tbody>
</table>
</div>



## 6.5 Permutation


```python
nframe = pd.DataFrame(np.arange(25).reshape(5,5))
nframe
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>16</td>
      <td>17</td>
      <td>18</td>
      <td>19</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20</td>
      <td>21</td>
      <td>22</td>
      <td>23</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_order = np.random.permutation(5)
new_order
```




    array([3, 2, 1, 0, 4])




```python
nframe.take(new_order)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>16</td>
      <td>17</td>
      <td>18</td>
      <td>19</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20</td>
      <td>21</td>
      <td>22</td>
      <td>23</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_order = [3,4,2]
nframe.take(new_order)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>16</td>
      <td>17</td>
      <td>18</td>
      <td>19</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20</td>
      <td>21</td>
      <td>22</td>
      <td>23</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
    </tr>
  </tbody>
</table>
</div>



* Random Sampling


```python
sample = np.random.randint(0, len(nframe), size=3)
sample
```




    array([3, 0, 3])




```python
nframe.take(sample)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>16</td>
      <td>17</td>
      <td>18</td>
      <td>19</td>
    </tr>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>16</td>
      <td>17</td>
      <td>18</td>
      <td>19</td>
    </tr>
  </tbody>
</table>
</div>



## 6.6 String Manipulation

### Built-in Methods for Manipulation of Strings


```python
text = '16 Bolton Avenue , Boston'
text.split(',')
```




    ['16 Bolton Avenue ', ' Boston']




```python
tokens = [s.strip() for s in text.split(',')]
tokens
```




    ['16 Bolton Avenue', 'Boston']




```python
address, city = [s.strip() for s in text.split(',')]
address
```




    '16 Bolton Avenue'




```python
city
```




    'Boston'




```python
address + ',' + city
```




    '16 Bolton Avenue,Boston'




```python
strings = ['A+','A','A-','B','BB','BBB','C+']
```


```python
';'.join(strings)
```




    'A+;A;A-;B;BB;BBB;C+'




```python
'Boston' in text
```




    True




```python
text.index('Boston')
```




    19




```python
text.find('Boston')
```




    19




```python
text.index('New York')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-100-e44f5210d36c> in <module>()
    ----> 1 text.index('New York')


    ValueError: substring not found



```python
text.find('New York')
```




    -1




```python
text.count('e')
```




    2




```python
text.count('Avenue')
```




    1




```python
text.replace('Avenue','Street')
```




    '16 Bolton Street , Boston'




```python
text.replace('1','')
```




    '6 Bolton Avenue , Boston'



### Regular Expressions

* pattern matching
* substitution
* splitting


```python
import re
```


```python
text = "This is an\t odd \n text!"
```


```python
re.split('\s+', text)
```




    ['This', 'is', 'an', 'odd', 'text!']




```python
regex = re.compile('\s+')
```


```python
regex.split(text)
```




    ['This', 'is', 'an', 'odd', 'text!']




```python
text = 'This is my address: 16 Bolton Avenue, Boston'
re.findall('A\w+',text)
```




    ['Avenue']




```python
re.findall('[A,a]\w+',text)
```




    ['address', 'Avenue']




```python
re.search('[A,a]\w+',text)
```




    <_sre.SRE_Match object; span=(11, 18), match='address'>




```python
search = re.search('[A,a]\w+',text)
search.start()
```




    11




```python
search.end()
```




    18




```python
text[search.start():search.end()]
```




    'address'




```python
re.match('[A,a]\w+',text)
```


```python
re.match('T\w+',text)
```




    <_sre.SRE_Match object; span=(0, 4), match='This'>




```python
match = re.match('T\w+',text)
```


```python
text[match.start():match.end()]
```




    'This'



## 6.7 Data Aggregation

### GroupBy


```python

```

### A Practical Example


```python
frame = pd.DataFrame({ 'color': ['white','red','green','red','green'],
                      'object': ['pen','pencil','pencil','ashtray','pen'],
                      'price1' : [5.56,4.20,1.30,0.56,2.75],
                      'price2' : [4.75,4.12,1.60,0.75,3.15]})
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>object</th>
      <th>price1</th>
      <th>price2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>white</td>
      <td>pen</td>
      <td>5.56</td>
      <td>4.75</td>
    </tr>
    <tr>
      <th>1</th>
      <td>red</td>
      <td>pencil</td>
      <td>4.20</td>
      <td>4.12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>green</td>
      <td>pencil</td>
      <td>1.30</td>
      <td>1.60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>red</td>
      <td>ashtray</td>
      <td>0.56</td>
      <td>0.75</td>
    </tr>
    <tr>
      <th>4</th>
      <td>green</td>
      <td>pen</td>
      <td>2.75</td>
      <td>3.15</td>
    </tr>
  </tbody>
</table>
</div>




```python
group = frame['price1'].groupby(frame['color'])
group
```




    <pandas.core.groupby.SeriesGroupBy object at 0x000000A9E3AC4EF0>




```python
group.groups
```




    {'green': Int64Index([2, 4], dtype='int64'),
     'red': Int64Index([1, 3], dtype='int64'),
     'white': Int64Index([0], dtype='int64')}




```python
group.mean()
```




    color
    green    2.025
    red      2.380
    white    5.560
    Name: price1, dtype: float64




```python
group.sum()
```




    color
    green    4.05
    red      4.76
    white    5.56
    Name: price1, dtype: float64



### Hierarchical Grouping


```python
ggroup = frame['price1'].groupby([frame['color'],frame['object']])
ggroup.groups
```




    {('green', 'pen'): Int64Index([4], dtype='int64'),
     ('green', 'pencil'): Int64Index([2], dtype='int64'),
     ('red', 'ashtray'): Int64Index([3], dtype='int64'),
     ('red', 'pencil'): Int64Index([1], dtype='int64'),
     ('white', 'pen'): Int64Index([0], dtype='int64')}




```python
ggroup.sum()
```




    color  object
    green  pen        2.75
           pencil     1.30
    red    ashtray    0.56
           pencil     4.20
    white  pen        5.56
    Name: price1, dtype: float64




```python
frame[['price1','price2']].groupby(frame['color']).mean()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price1</th>
      <th>price2</th>
    </tr>
    <tr>
      <th>color</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>green</th>
      <td>2.025</td>
      <td>2.375</td>
    </tr>
    <tr>
      <th>red</th>
      <td>2.380</td>
      <td>2.435</td>
    </tr>
    <tr>
      <th>white</th>
      <td>5.560</td>
      <td>4.750</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.groupby(frame['color']).mean()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price1</th>
      <th>price2</th>
    </tr>
    <tr>
      <th>color</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>green</th>
      <td>2.025</td>
      <td>2.375</td>
    </tr>
    <tr>
      <th>red</th>
      <td>2.380</td>
      <td>2.435</td>
    </tr>
    <tr>
      <th>white</th>
      <td>5.560</td>
      <td>4.750</td>
    </tr>
  </tbody>
</table>
</div>



## 6.8 Group Iteration


```python
for name, group in frame.groupby('color'):
    print (name)
    print (group)
```

    green
       color  object  price1  price2
    2  green  pencil    1.30    1.60
    4  green     pen    2.75    3.15
    red
      color   object  price1  price2
    1   red   pencil    4.20    4.12
    3   red  ashtray    0.56    0.75
    white
       color object  price1  price2
    0  white    pen    5.56    4.75


### Chain of Transformations


```python
result1 = frame['price1'].groupby(frame['color']).mean()
type(result1)
```




    pandas.core.series.Series




```python
result2 = frame.groupby(frame['color']).mean()
type(result2)
```




    pandas.core.frame.DataFrame




```python
frame['price1'].groupby(frame['color']).mean()
frame.groupby(frame['color'])['price1'].mean()
```




    color
    green    2.025
    red      2.380
    white    5.560
    Name: price1, dtype: float64




```python
(frame.groupby(frame['color']).mean())['price1']
```




    color
    green    2.025
    red      2.380
    white    5.560
    Name: price1, dtype: float64




```python
means = frame.groupby('color').mean().add_prefix('mean_')
means
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mean_price1</th>
      <th>mean_price2</th>
    </tr>
    <tr>
      <th>color</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>green</th>
      <td>2.025</td>
      <td>2.375</td>
    </tr>
    <tr>
      <th>red</th>
      <td>2.380</td>
      <td>2.435</td>
    </tr>
    <tr>
      <th>white</th>
      <td>5.560</td>
      <td>4.750</td>
    </tr>
  </tbody>
</table>
</div>



### Functions on Groups


```python
group = frame.groupby('color')
group['price1'].quantile(0.6)
```




    color
    green    2.170
    red      2.744
    white    5.560
    Name: price1, dtype: float64




```python
def range(series):
    return series.max() - series.min()
group['price1'].agg(range)
```




    color
    green    1.45
    red      3.64
    white    0.00
    Name: price1, dtype: float64




```python
group.agg(range)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price1</th>
      <th>price2</th>
    </tr>
    <tr>
      <th>color</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>green</th>
      <td>1.45</td>
      <td>1.55</td>
    </tr>
    <tr>
      <th>red</th>
      <td>3.64</td>
      <td>3.37</td>
    </tr>
    <tr>
      <th>white</th>
      <td>0.00</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
group['price1'].agg(['mean','std',range])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mean</th>
      <th>std</th>
      <th>range</th>
    </tr>
    <tr>
      <th>color</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>green</th>
      <td>2.025</td>
      <td>1.025305</td>
      <td>1.45</td>
    </tr>
    <tr>
      <th>red</th>
      <td>2.380</td>
      <td>2.573869</td>
      <td>3.64</td>
    </tr>
    <tr>
      <th>white</th>
      <td>5.560</td>
      <td>NaN</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>
</div>



## 6.9 Advanced Data Aggregation


```python
frame = pd.DataFrame({ 'color':['white','red','green','red','green'],
                      'price1':[5.56,4.20,1.30,0.56,2.75],
                      'price2':[4.75,4.12,1.60,0.75,3.15]})
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>price1</th>
      <th>price2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>white</td>
      <td>5.56</td>
      <td>4.75</td>
    </tr>
    <tr>
      <th>1</th>
      <td>red</td>
      <td>4.20</td>
      <td>4.12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>green</td>
      <td>1.30</td>
      <td>1.60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>red</td>
      <td>0.56</td>
      <td>0.75</td>
    </tr>
    <tr>
      <th>4</th>
      <td>green</td>
      <td>2.75</td>
      <td>3.15</td>
    </tr>
  </tbody>
</table>
</div>




```python
sums = frame.groupby('color').sum().add_prefix('tot_')
sums
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tot_price1</th>
      <th>tot_price2</th>
    </tr>
    <tr>
      <th>color</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>green</th>
      <td>4.05</td>
      <td>4.75</td>
    </tr>
    <tr>
      <th>red</th>
      <td>4.76</td>
      <td>4.87</td>
    </tr>
    <tr>
      <th>white</th>
      <td>5.56</td>
      <td>4.75</td>
    </tr>
  </tbody>
</table>
</div>




```python
merge(frame,sums,left_on='color',right_index=True)
```


```python
frame.groupby('color').transform(np.sum).add_prefix('tot_')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tot_price1</th>
      <th>tot_price2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.56</td>
      <td>4.75</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.76</td>
      <td>4.87</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.05</td>
      <td>4.75</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.76</td>
      <td>4.87</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4.05</td>
      <td>4.75</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame = DataFrame( { 'color':['white','black','white','white','black','black'],
                    'status':['up','up','down','down','down','up'],
                    'value1':[12.33,14.55,22.34,27.84,23.40,18.33],
                    'value2':[11.23,31.80,29.99,31.18,18.25,22.44]})
frame
```


```python
frame.groupby(['color','status']).apply( lambda x: x.max())
```


```python
frame.rename(index=reindex, columns=recolumn)
```


```python
temp = date_range('1/1/2015', periods=10, freq= 'H')
temp
```


```python
timeseries = Series(np.random.rand(10), index=temp)
timeseries
```


```python
timetable = DataFrame( {'date': temp, 'value1' : np.random.rand(10),
                        'value2' : np.random.rand(10)})
timetable
```


```python
timetable['cat'] = ['up','down','left','left','up','up','down','right','right','up']
timetable
```

## 6.10 Conclusions


```python

```
