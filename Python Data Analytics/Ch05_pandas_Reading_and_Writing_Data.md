
# Chapter 5: pandas: Reading and Writing Data
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 5: pandas: Reading and Writing Data](#chapter-5-pandas-reading-and-writing-data)
  * [5.1 I/O API Tools](#51-io-api-tools)
  * [5.2 CSV and Textual Files](#52-csv-and-textual-files)
  * [5.3 Reading Data in CSV or Text Files](#53-reading-data-in-csv-or-text-files)
    * [Using RegExp for Parsing TXT Files](#using-regexp-for-parsing-txt-files)
    * [Reading TXT Files into Parts or Partially](#reading-txt-files-into-parts-or-partially)
    * [Writing Data in CSV](#writing-data-in-csv)
  * [5.4 Reading and Writing HTML Files](#54-reading-and-writing-html-files)
    * [Writing Data in HTML](#writing-data-in-html)
    * [Reading Data from an HTML File](#reading-data-from-an-html-file)
  * [5.5 Reading Data from XML](#55-reading-data-from-xml)
  * [5.6 Reading and Writing Data on Microsoft Excel Files](#56-reading-and-writing-data-on-microsoft-excel-files)
  * [5.7 JSON Data](#57-json-data)
  * [5.8 The Format HDF5](#58-the-format-hdf5)
  * [5.9 Pickle—Python Object Serialization](#59-picklepython-object-serialization)
    * [Serialize a Python Object with cPickle](#serialize-a-python-object-with-cpickle)
    * [Pickling with pandas](#pickling-with-pandas)
  * [5.10 Interacting with Databases](#510-interacting-with-databases)
    * [Loading and Writing Data with SQLite3](#loading-and-writing-data-with-sqlite3)
    * [Loading and Writing Data with PostgreSQL](#loading-and-writing-data-with-postgresql)
  * [5.11 Reading and Writing Data with a NoSQL Database: MongoDB](#511-reading-and-writing-data-with-a-nosql-database-mongodb)
  * [5.12 Conclusions](#512-conclusions)

<!-- tocstop -->



```python
import numpy as np
import pandas as pd
```

## 5.1 I/O API Tools

| Readers        | Writers      |
|---|---|
| read_csv       | to_csv       |
| read_excel     | to_excel     |
| read_hdf       | to_hdf       |
| read_sql       | to_sql       |
| read_json      | to_json      |
| read_html      | to_html      |
| read_stata     | to_stata     |
| read_clipboard | to_clipboard |
| read_pickle    | to_pickle |
| read_msgpack   | to_msgpack (experimental) |
| read_gbq       | to_gbq (experimental) |

## 5.2 CSV and Textual Files

* read_csv
* read_table
* to_csv


```python
import pandas as pd
csvframe = pd.read_csv('data/myCSV_01.csv')
csvframe
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>white</th>
      <th>red</th>
      <th>blue</th>
      <th>green</th>
      <th>animal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5</td>
      <td>2</td>
      <td>3</td>
      <td>cat</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>7</td>
      <td>8</td>
      <td>5</td>
      <td>dog</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>3</td>
      <td>6</td>
      <td>7</td>
      <td>horse</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>2</td>
      <td>8</td>
      <td>3</td>
      <td>duck</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>1</td>
      <td>mouse</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_table('data/ch05_01.csv',sep=',')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>white</th>
      <th>red</th>
      <th>blue</th>
      <th>green</th>
      <th>animal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5</td>
      <td>2</td>
      <td>3</td>
      <td>cat</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>7</td>
      <td>8</td>
      <td>5</td>
      <td>dog</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>3</td>
      <td>6</td>
      <td>7</td>
      <td>horse</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>2</td>
      <td>8</td>
      <td>3</td>
      <td>duck</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>1</td>
      <td>mouse</td>
    </tr>
  </tbody>
</table>
</div>



## 5.3 Reading Data in CSV or Text Files


```python
import pandas as pd
```


```python
csvframe = pd.read_csv('data/myCSV_01.csv')
csvframe
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>white</th>
      <th>red</th>
      <th>blue</th>
      <th>green</th>
      <th>animal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5</td>
      <td>2</td>
      <td>3</td>
      <td>cat</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>7</td>
      <td>8</td>
      <td>5</td>
      <td>dog</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>3</td>
      <td>6</td>
      <td>7</td>
      <td>horse</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>2</td>
      <td>8</td>
      <td>3</td>
      <td>duck</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>1</td>
      <td>mouse</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_table('data/ch05_01.csv',sep=',')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>white</th>
      <th>red</th>
      <th>blue</th>
      <th>green</th>
      <th>animal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5</td>
      <td>2</td>
      <td>3</td>
      <td>cat</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>7</td>
      <td>8</td>
      <td>5</td>
      <td>dog</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>3</td>
      <td>6</td>
      <td>7</td>
      <td>horse</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>2</td>
      <td>8</td>
      <td>3</td>
      <td>duck</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>1</td>
      <td>mouse</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_csv('data/ch05_02.csv')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>5</th>
      <th>2</th>
      <th>3</th>
      <th>cat</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>7</td>
      <td>8</td>
      <td>5</td>
      <td>dog</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>6</td>
      <td>7</td>
      <td>horse</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2</td>
      <td>8</td>
      <td>3</td>
      <td>duck</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>1</td>
      <td>mouse</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_csv('data/ch05_02.csv', header=None)
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
      <td>1</td>
      <td>5</td>
      <td>2</td>
      <td>3</td>
      <td>cat</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>7</td>
      <td>8</td>
      <td>5</td>
      <td>dog</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>3</td>
      <td>6</td>
      <td>7</td>
      <td>horse</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>2</td>
      <td>8</td>
      <td>3</td>
      <td>duck</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>1</td>
      <td>mouse</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_csv('data/ch05_02.csv', names=['white','red','blue','green','animal'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>white</th>
      <th>red</th>
      <th>blue</th>
      <th>green</th>
      <th>animal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5</td>
      <td>2</td>
      <td>3</td>
      <td>cat</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>7</td>
      <td>8</td>
      <td>5</td>
      <td>dog</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>3</td>
      <td>6</td>
      <td>7</td>
      <td>horse</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>2</td>
      <td>8</td>
      <td>3</td>
      <td>duck</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>1</td>
      <td>mouse</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_csv('data/ch05_03.csv', index_col=['color','status'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>item1</th>
      <th>item2</th>
      <th>item3</th>
    </tr>
    <tr>
      <th>color</th>
      <th>status</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">black</th>
      <th>up</th>
      <td>3</td>
      <td>4</td>
      <td>6</td>
    </tr>
    <tr>
      <th>down</th>
      <td>2</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">white</th>
      <th>up</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>down</th>
      <td>3</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>left</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">red</th>
      <th>up</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>down</th>
      <td>1</td>
      <td>1</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



### Using RegExp for Parsing TXT Files

| symbol | meanning |
|---|---|
| .         | single character, except newline |
| \d        | digit |
| \D        | non-digit character |
| \s        | whitespace character |
| \S        | non-whitespace character |
| \n        | new line character |
| \t        | tab character |
| \uxxxx    | unicode character specified by the hexadecimal number xxxx |


```python
pd.read_table('data/ch05_04.txt',sep='\s*')
```

    C:\Anaconda36\lib\site-packages\ipykernel\__main__.py:1: ParserWarning: Falling back to the 'python' engine because the 'c' engine does not support regex separators (separators > 1 char and different from '\s+' are interpreted as regex); you can avoid this warning by specifying engine='python'.
      if __name__ == '__main__':
    C:\Anaconda36\lib\site-packages\pandas\io\parsers.py:1961: FutureWarning: split() requires a non-empty pattern match.
      yield pat.split(line.strip())
    C:\Anaconda36\lib\site-packages\pandas\io\parsers.py:1963: FutureWarning: split() requires a non-empty pattern match.
      yield pat.split(line.strip())





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>white</th>
      <th>red</th>
      <th>blue</th>
      <th>green</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>7</td>
      <td>8</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>3</td>
      <td>6</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_table('data/ch05_05.txt',sep='\D*',header=None)
```

    C:\Anaconda36\lib\site-packages\ipykernel\__main__.py:1: ParserWarning: Falling back to the 'python' engine because the 'c' engine does not support regex separators (separators > 1 char and different from '\s+' are interpreted as regex); you can avoid this warning by specifying engine='python'.
      if __name__ == '__main__':
    C:\Anaconda36\lib\site-packages\pandas\io\parsers.py:1961: FutureWarning: split() requires a non-empty pattern match.
      yield pat.split(line.strip())
    C:\Anaconda36\lib\site-packages\pandas\io\parsers.py:1963: FutureWarning: split() requires a non-empty pattern match.
      yield pat.split(line.strip())





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
      <td>0</td>
      <td>123</td>
      <td>122</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>124</td>
      <td>321</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>125</td>
      <td>333</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_table('data/ch05_06.txt',sep=',',skiprows=[0,1,3,6])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>white</th>
      <th>red</th>
      <th>blue</th>
      <th>green</th>
      <th>animal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5</td>
      <td>2</td>
      <td>3</td>
      <td>cat</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>7</td>
      <td>8</td>
      <td>5</td>
      <td>dog</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>3</td>
      <td>6</td>
      <td>7</td>
      <td>horse</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>2</td>
      <td>8</td>
      <td>3</td>
      <td>duck</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>4</td>
      <td>2</td>
      <td>1</td>
      <td>mouse</td>
    </tr>
  </tbody>
</table>
</div>



### Reading TXT Files into Parts or Partially


```python
pd.read_csv('data/ch05_02.csv',skiprows=[2],nrows=3,header=None)
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
      <td>1</td>
      <td>5</td>
      <td>2</td>
      <td>3</td>
      <td>cat</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>7</td>
      <td>8</td>
      <td>5</td>
      <td>dog</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2</td>
      <td>8</td>
      <td>3</td>
      <td>duck</td>
    </tr>
  </tbody>
</table>
</div>




```python
out = pd.Series()
i = 0
pieces = pd.read_csv('data/ch05_01.csv',chunksize=3)

for piece in pieces:
    out.set_value(i,piece['white'].sum())
    i = i + 1
    print(i)
```

    1
    2


### Writing Data in CSV


```python
data = {'color' : ['blue','green','yellow','red','white'],
        'object' : ['ball','pen','pencil','paper','mug'],
        'price' : [1.2,1.0,0.6,0.9,1.7]}
```


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
frame2.to_csv('ch05_07.csv')
```


```python
frame2.to_csv('ch05_07b.csv', index=False, header=False)
```


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




```python
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




```python
frame3.to_csv('ch05_08.csv')
```


```python
frame3.to_csv('ch05_09.csv', na_rep ='NaN')
```

## 5.4 Reading and Writing HTML Files

### Writing Data in HTML

* read_html()
* to_html()


```python
conda install html5lib
```


```python
frame = pd.DataFrame(np.arange(4).reshape(2,2))
```


```python
print(frame.to_html())
```

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
          <th>0</th>
          <td>0</td>
          <td>1</td>
        </tr>
        <tr>
          <th>1</th>
          <td>2</td>
          <td>3</td>
        </tr>
      </tbody>
    </table>



```python
frame = pd.DataFrame( np.random.random((4,4)),
                     index = ['white','black','red','blue'],
                     columns = ['up','down','right','left'])
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>up</th>
      <th>down</th>
      <th>right</th>
      <th>left</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>white</th>
      <td>0.788961</td>
      <td>0.577580</td>
      <td>0.499871</td>
      <td>0.205716</td>
    </tr>
    <tr>
      <th>black</th>
      <td>0.346140</td>
      <td>0.194116</td>
      <td>0.277512</td>
      <td>0.094746</td>
    </tr>
    <tr>
      <th>red</th>
      <td>0.277262</td>
      <td>0.262186</td>
      <td>0.883444</td>
      <td>0.419923</td>
    </tr>
    <tr>
      <th>blue</th>
      <td>0.076713</td>
      <td>0.926889</td>
      <td>0.919097</td>
      <td>0.790951</td>
    </tr>
  </tbody>
</table>
</div>




```python
s = ['<HTML>']
s.append('<HEAD><TITLE>My DataFrame</TITLE></HEAD>')
s.append('<BODY>')
s.append(frame.to_html())
s.append('</BODY></HTML>')
html = ''.join(s)
```


```python
html_file = open('myFrame.html','w')
html_file.write(html)
html_file.close()
```

### Reading Data from an HTML File


```python
web_frames = pd.read_html('myFrame.html')
web_frames[0]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>up</th>
      <th>down</th>
      <th>right</th>
      <th>left</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>white</td>
      <td>0.788961</td>
      <td>0.577580</td>
      <td>0.499871</td>
      <td>0.205716</td>
    </tr>
    <tr>
      <th>1</th>
      <td>black</td>
      <td>0.346140</td>
      <td>0.194116</td>
      <td>0.277512</td>
      <td>0.094746</td>
    </tr>
    <tr>
      <th>2</th>
      <td>red</td>
      <td>0.277262</td>
      <td>0.262186</td>
      <td>0.883444</td>
      <td>0.419923</td>
    </tr>
    <tr>
      <th>3</th>
      <td>blue</td>
      <td>0.076713</td>
      <td>0.926889</td>
      <td>0.919097</td>
      <td>0.790951</td>
    </tr>
  </tbody>
</table>
</div>




```python
ranking = pd.read_html('http://www.meccanismocomplesso.org/en/meccanismo-complesso-sito-2/classifica-punteggio/')
```


```python
ranking[0]
```

## 5.5 Reading Data from XML

http://lxml.de/index.html


```python
# %load data/books.xml
<?xml version="1.0"?>
<Catalog>
  <Book id="ISBN9872122367564">
  <Author>272103_1_EnRoss, Mark</Author>
    <Title>XML Cookbook</Title>
    <Genre>Computer</Genre>
    <Price>23.56</Price>
    <PublishDate>2014-22-01</PublishDate>
  </Book>
  <Book id="ISBN9872122367564">
    <Author>272103_1_EnBracket, Barbara</Author>
    <Title>XML for Dummies</Title>
    <Genre>Computer</Genre>
    <Price>35.95</Price>
    <PublishDate>2014-12-16</PublishDate>
  </Book>
</Catalog>
```


```python
from lxml import objectify
```


```python
xml = objectify.parse('data/books.xml')
xml
```




    <lxml.etree._ElementTree at 0xe6e622f688>




```python
root = xml.getroot()
```


```python
root.Book.Author
```




    '272103_1_EnRoss, Mark'




```python
root.Book.PublishDate
```




    '2014-22-01'




```python
root.getchildren()
```




    [<Element Book at 0xe6e6276f08>, <Element Book at 0xe6e6276b08>]




```python
[child.tag for child in root.Book.getchildren()]
```




    ['Author', 'Title', 'Genre', 'Price', 'PublishDate']




```python
[child.text for child in root.Book.getchildren()]
```




    ['272103_1_EnRoss, Mark', 'XML Cookbook', 'Computer', '23.56', '2014-22-01']




```python
def etree2df(root):
    column_names = []
    for i in range(0,len(root.getchildren()[0].getchildren())):
        column_names.append(root.getchildren()[0].getchildren()[i].tag)
    xml:frame = pd.DataFrame(columns=column_names)
    for j in range(0, len(root.getchildren())):
        obj = root.getchildren()[j].getchildren()
        texts = []
        for k in range(0, len(column_names)):
            texts.append(obj[k].text)
        row = dict(zip(column_names, texts))
        row_s = pd.Series(row)
        row_s.name = j
        xml:frame = xml:frame.append(row_s)
    return xml:frame
```


      File "<ipython-input-75-110bab389c61>", line 14
        xml:frame = xml:frame.append(row_s)
                       ^
    SyntaxError: invalid syntax




```python
etree2df(root)
```

## 5.6 Reading and Writing Data on Microsoft Excel Files

* to_excel()
* read_excel()


```python
import xlrd
```


```python
pd.read_excel('data/data.xls')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>white</th>
      <th>read</th>
      <th>green</th>
      <th>black</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>12</td>
      <td>23</td>
      <td>17</td>
      <td>18</td>
    </tr>
    <tr>
      <th>b</th>
      <td>22</td>
      <td>16</td>
      <td>19</td>
      <td>18</td>
    </tr>
    <tr>
      <th>c</th>
      <td>14</td>
      <td>23</td>
      <td>22</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_excel('data/data.xls','Sheet2')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>yellow</th>
      <th>purple</th>
      <th>blue</th>
      <th>orange</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>12</td>
      <td>23</td>
      <td>17</td>
      <td>18</td>
    </tr>
    <tr>
      <th>B</th>
      <td>22</td>
      <td>16</td>
      <td>19</td>
      <td>18</td>
    </tr>
    <tr>
      <th>C</th>
      <td>14</td>
      <td>23</td>
      <td>22</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.read_excel('data/data.xls',1)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>yellow</th>
      <th>purple</th>
      <th>blue</th>
      <th>orange</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>12</td>
      <td>23</td>
      <td>17</td>
      <td>18</td>
    </tr>
    <tr>
      <th>B</th>
      <td>22</td>
      <td>16</td>
      <td>19</td>
      <td>18</td>
    </tr>
    <tr>
      <th>C</th>
      <td>14</td>
      <td>23</td>
      <td>22</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame = pd.DataFrame(np.random.random((4,4)),
                     index = ['exp1','exp2','exp3','exp4'],
                     columns = ['Jan2015','Fab2015','Mar2015','Apr2005'])
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Jan2015</th>
      <th>Fab2015</th>
      <th>Mar2015</th>
      <th>Apr2005</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>exp1</th>
      <td>0.509758</td>
      <td>0.473159</td>
      <td>0.381452</td>
      <td>0.755255</td>
    </tr>
    <tr>
      <th>exp2</th>
      <td>0.325269</td>
      <td>0.043197</td>
      <td>0.106240</td>
      <td>0.351238</td>
    </tr>
    <tr>
      <th>exp3</th>
      <td>0.379101</td>
      <td>0.690050</td>
      <td>0.475262</td>
      <td>0.702887</td>
    </tr>
    <tr>
      <th>exp4</th>
      <td>0.418955</td>
      <td>0.652997</td>
      <td>0.991569</td>
      <td>0.595785</td>
    </tr>
  </tbody>
</table>
</div>




```python
frame.to_excel('data/data2.xlsx')
```

## 5.7 JSON Data

http://jsonviewer.stack.hu/


```python
frame = pd.DataFrame(np.arange(16).reshape(4,4),
                     index=['white','black','red','blue'],
                     columns=['up','down','right','left'])
frame.to_json('frame.json')
```


```python
pd.read_json('frame.json')
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
      <th>black</th>
      <td>5</td>
      <td>7</td>
      <td>6</td>
      <td>4</td>
    </tr>
    <tr>
      <th>blue</th>
      <td>13</td>
      <td>15</td>
      <td>14</td>
      <td>12</td>
    </tr>
    <tr>
      <th>red</th>
      <td>9</td>
      <td>11</td>
      <td>10</td>
      <td>8</td>
    </tr>
    <tr>
      <th>white</th>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
from pandas.io.json import json_normalize
```


```python
file = open('data/books.json','r')
text = file.read()
text = json.loads(text)
```


```python
json_normalize(text,'books')
```

## 5.8 The Format HDF5


```python
from pandas.io.pytables import HDFStore
```


```python
frame = pd.DataFrame(np.arange(16).reshape(4,4),
                     index=['white','black','red','blue'],
                     columns=['up','down','right','left'])
```


```python
store = HDFStore('mydata.h5')
store['obj1'] = frame

```


```python
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
store['obj2'] = frame2
```


```python
store
```




    <class 'pandas.io.pytables.HDFStore'>
    File path: mydata.h5
    /obj1            frame        (shape->[4,4])
    /obj2            frame        (shape->[5,3])




```python
store['obj2']
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



## 5.9 Pickle—Python Object Serialization

### Serialize a Python Object with cPickle


```python
import cPickle as pickle
```


```python
data = { 'color': ['white','red'], 'value': [5, 7]}
```


```python
pickled_data = pickle.dumps(data)
```


```python
nframe = pickle.loads(pickled_data)
nframe
```

### Pickling with pandas


```python
frame = pd.DataFrame(np.arange(16).reshape(4,4), index = ['up','down','left','right'])
frame.to_pickle('frame.pkl')
```


```python
pd.read_pickle('frame.pkl')
```

## 5.10 Interacting with Databases


```python
from sqlalchemy import create_engine
```


```python
engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')
```


```python
engine = create_engine('mysql+mysqldb://scott:tiger@localhost/foo')
```


```python
engine = create_engine('oracle://scott:tiger@127.0.0.1:1521/sidname')
```


```python
engine = create_engine('mssql+pyodbc://mydsn')
```


```python
engine = create_engine('sqlite:///foo.db')
```

### Loading and Writing Data with SQLite3


```python
frame = pd.DataFrame( np.arange(20).reshape(4,5),
                     columns=['white','red','blue','black','green'])
frame
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>white</th>
      <th>red</th>
      <th>blue</th>
      <th>black</th>
      <th>green</th>
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
  </tbody>
</table>
</div>




```python
engine = create_engine('sqlite:///foo.db')
```


```python
frame.to_sql('colors',engine)
```


```python
pd.read_sql('colors',engine)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>white</th>
      <th>red</th>
      <th>blue</th>
      <th>black</th>
      <th>green</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>15</td>
      <td>16</td>
      <td>17</td>
      <td>18</td>
      <td>19</td>
    </tr>
  </tbody>
</table>
</div>




```python
import sqlite3
query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
c REAL, d INTEGER
);"""
con = sqlite3.connect(':memory:')
con.execute(query)
```




    <sqlite3.Cursor at 0xe6e6cea420>




```python
con.commit()
```


```python
data = [('white','up',1,3),
('black','down',2,8),
('green','up',4,4),
('red','down',5,5)]
stmt = "INSERT INTO test VALUES(?,?,?,?)"
con.executemany(stmt, data)
```




    <sqlite3.Cursor at 0xe6e6cea5e0>




```python
con.commit()
```


```python
cursor = con.execute('select * from test')
cursor
```




    <sqlite3.Cursor at 0xe6e6cea570>




```python
rows = cursor.fetchall()
rows
```




    [('white', 'up', 1.0, 3),
     ('black', 'down', 2.0, 8),
     ('green', 'up', 4.0, 4),
     ('red', 'down', 5.0, 5)]




```python
cursor.description
```




    (('a', None, None, None, None, None, None),
     ('b', None, None, None, None, None, None),
     ('c', None, None, None, None, None, None),
     ('d', None, None, None, None, None, None))




```python
pd.DataFrame(rows, columns=zip(*cursor.description)[0])
```

### Loading and Writing Data with PostgreSQL


```python
pd.__version__
```




    '0.19.2'




```python
engine = create_engine('postgresql://postgres:password@localhost:5432/postgres')
```


```python
frame = pd.DataFrame(np.random.random((4,4)),
                     index=['exp1','exp2','exp3','exp4'],
                     columns=['feb','mar','apr','may']);
```


```python
frame.to_sql('dataframe',engine)
```


```python
psql -U postgres
```


```python
pd.read_sql_table('dataframe',engine)
```


```python
pd.read_sql_query('SELECT index,apr,may FROM DATAFRAME WHERE apr > 0.5',engine)
```

## 5.11 Reading and Writing Data with a NoSQL Database: MongoDB


```python
mongod --dbpath C:\MongoDB_data
```


```python
import pymongo
client = MongoClient('localhost',27017)
```


```python
db = client.mydatabase
db
```


```python
client['mydatabase']
```


```python
collection = db.mycollection
```


```python
db['mycollection']
collection
```


```python
frame = pd.DataFrame( np.arange(20).reshape(4,5),
frame
```


```python
import json
```


```python
record = json.loads(frame.T.to_json()).values()
record
```


```python
collection.mydocument.insert(record)
```


```python
cursor = collection['mydocument'].find()
dataframe = (list(cursor))
del dataframe['_id']
dataframe
```

## 5.12 Conclusions


```python

```
