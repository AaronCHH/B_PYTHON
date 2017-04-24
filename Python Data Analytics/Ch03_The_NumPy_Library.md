
# Chapter 3: The NumPy Library
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 3: The NumPy Library](#chapter-3-the-numpy-library)
  * [3.1 NumPy: A Little History](#31-numpy-a-little-history)
  * [3.2 The NumPy Installation](#32-the-numpy-installation)
  * [3.3 Ndarray: The Heart of the Library](#33-ndarray-the-heart-of-the-library)
    * [Create an Array](#create-an-array)
    * [Types of Data](#types-of-data)
    * [The dtype Option](#the-dtype-option)
    * [Intrinsic Crea tion of an Array](#intrinsic-crea-tion-of-an-array)
  * [3.4 Basic Operations](#34-basic-operations)
    * [Arit hmetic Operators](#arit-hmetic-operators)
    * [The M atrix Product](#the-m-atrix-product)
    * [Increm ent and Decrement Operators](#increm-ent-and-decrement-operators)
    * [Universal Functions (ufunc)](#universal-functions-ufunc)
    * [Aggregat e Functions](#aggregat-e-functions)
  * [3.5 Indexing, Slicing, and Iterating](#35-indexing-slicing-and-iterating)
    * [Indexing](#indexing)
    * [Slicing](#slicing)
    * [Iterating an Array](#iterating-an-array)
  * [3.6 Conditions and Boolean Arrays](#36-conditions-and-boolean-arrays)
  * [3.7 Shape Manipulation](#37-shape-manipulation)
  * [3.8 Array Manipulation](#38-array-manipulation)
    * [Joining Arrays](#joining-arrays)
    * [Splitting Arrays](#splitting-arrays)
  * [3.9 General Concepts](#39-general-concepts)
    * [Copies or Views of Objects](#copies-or-views-of-objects)
    * [Vectorization](#vectorization)
    * [Broadcasting](#broadcasting)
  * [3.10 Structured Arrays](#310-structured-arrays)
  * [3.11 Reading and Writing Array Data on Files](#311-reading-and-writing-array-data-on-files)
    * [Loading and Saving Data in Binary Files](#loading-and-saving-data-in-binary-files)
    * [Reading File with T abular Data](#reading-file-with-t-abular-data)
  * [3.12 Conclusions](#312-conclusions)

<!-- tocstop -->



## 3.1 NumPy: A Little History

## 3.2 The NumPy Installation

## 3.3 Ndarray: The Heart of the Library
### Create an Array
### Types of Data
### The dtype Option
### Intrinsic Crea tion of an Array

## 3.4 Basic Operations
### Arit hmetic Operators
### The M atrix Product
### Increm ent and Decrement Operators
### Universal Functions (ufunc)
### Aggregat e Functions

## 3.5 Indexing, Slicing, and Iterating
### Indexing
### Slicing
### Iterating an Array

## 3.6 Conditions and Boolean Arrays


```python
import numpy as np
```


```python
A = np.random.random((4, 4))
A
```




    array([[ 0.18403951,  0.62659785,  0.42960882,  0.591795  ],
           [ 0.84792814,  0.42923672,  0.36447613,  0.2709855 ],
           [ 0.56502426,  0.84623738,  0.32567381,  0.56280886],
           [ 0.14692473,  0.44342994,  0.57167931,  0.44109498]])




```python
A < 0.5
```




    array([[ True, False,  True, False],
           [False,  True,  True,  True],
           [False, False,  True, False],
           [ True,  True, False,  True]], dtype=bool)




```python
A[A < 0.5]
```




    array([ 0.18403951,  0.42960882,  0.42923672,  0.36447613,  0.2709855 ,
            0.32567381,  0.14692473,  0.44342994,  0.44109498])



## 3.7 Shape Manipulation


```python
a = np.random.random(12)
a
```




    array([ 0.40003514,  0.20315289,  0.09077042,  0.37640425,  0.02759888,
            0.30887021,  0.57648954,  0.92072317,  0.87853593,  0.09201792,
            0.7080752 ,  0.90900987])




```python
A = a.reshape(3, 4)
A
```




    array([[ 0.40003514,  0.20315289,  0.09077042,  0.37640425],
           [ 0.02759888,  0.30887021,  0.57648954,  0.92072317],
           [ 0.87853593,  0.09201792,  0.7080752 ,  0.90900987]])




```python
a.shape = (3, 4)
a
```




    array([[ 0.40003514,  0.20315289,  0.09077042,  0.37640425],
           [ 0.02759888,  0.30887021,  0.57648954,  0.92072317],
           [ 0.87853593,  0.09201792,  0.7080752 ,  0.90900987]])




```python
a = a.ravel()
a.shape = (12)
a
```




    array([ 0.40003514,  0.20315289,  0.09077042,  0.37640425,  0.02759888,
            0.30887021,  0.57648954,  0.92072317,  0.87853593,  0.09201792,
            0.7080752 ,  0.90900987])




```python
A.transpose()
```




    array([[ 0.40003514,  0.02759888,  0.87853593],
           [ 0.20315289,  0.30887021,  0.09201792],
           [ 0.09077042,  0.57648954,  0.7080752 ],
           [ 0.37640425,  0.92072317,  0.90900987]])



## 3.8 Array Manipulation

### Joining Arrays


```python
A = np.ones((3, 3))
B = np.zeros((3, 3))
np.vstack((A, B))
```




    array([[ 1.,  1.,  1.],
           [ 1.,  1.,  1.],
           [ 1.,  1.,  1.],
           [ 0.,  0.,  0.],
           [ 0.,  0.,  0.],
           [ 0.,  0.,  0.]])




```python
np.hstack((A,B))
```




    array([[ 1.,  1.,  1.,  0.,  0.,  0.],
           [ 1.,  1.,  1.,  0.,  0.,  0.],
           [ 1.,  1.,  1.,  0.,  0.,  0.]])




```python
a = np.array([0, 1, 2])
b = np.array([3, 4, 5])
c = np.array([6, 7, 8])
np.column_stack((a, b, c))
```




    array([[0, 3, 6],
           [1, 4, 7],
           [2, 5, 8]])




```python
np.row_stack((a, b, c))
```




    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])



### Splitting Arrays


```python
A = np.arange(16).reshape((4, 4))
A
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11],
           [12, 13, 14, 15]])




```python
[B,C] = np.hsplit(A, 2)
B
```




    array([[ 0,  1],
           [ 4,  5],
           [ 8,  9],
           [12, 13]])




```python
C
```




    array([[ 2,  3],
           [ 6,  7],
           [10, 11],
           [14, 15]])




```python
[B,C] = np.vsplit(A, 2)
B
```




    array([[0, 1, 2, 3],
           [4, 5, 6, 7]])




```python
C
```




    array([[ 8,  9, 10, 11],
           [12, 13, 14, 15]])




```python
[A1,A2,A3] = np.split(A,[1,3],axis=1)
A1
```




    array([[ 0],
           [ 4],
           [ 8],
           [12]])




```python
A2
```




    array([[ 1,  2],
           [ 5,  6],
           [ 9, 10],
           [13, 14]])




```python
A3
```




    array([[ 3],
           [ 7],
           [11],
           [15]])




```python
[A1,A2,A3] = np.split(A,[1,3],axis=0)
A1
```




    array([[0, 1, 2, 3]])




```python
A2
```




    array([[ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])




```python
A3
```




    array([[12, 13, 14, 15]])



## 3.9 General Concepts

### Copies or Views of Objects


```python
a = np.array([1, 2, 3, 4])
b = a
b
```




    array([1, 2, 3, 4])




```python
a[2] = 0
b
```




    array([1, 2, 0, 4])




```python
c = a[0:2]
c
```




    array([1, 2])




```python
a[0] = 0
c
```




    array([0, 2])




```python
a = np.array([1, 2, 3, 4])
c = a.copy()
c
```




    array([1, 2, 3, 4])




```python
a[0] = 0
c
```




    array([1, 2, 3, 4])



### Vectorization


```python
for (i = 0; i < rows; i++){
    c[i] = a[i]*b[i];
}
```


```python
for( i=0; i < rows; i++){
    for(j=0; j < columns; j++){
        c[i][j] = a[i][j]*b[i][j];
    }
}
```

### Broadcasting


```python
A = np.arange(16).reshape(4, 4)
b = np.arange(4)
A
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11],
           [12, 13, 14, 15]])




```python
b
```




    array([0, 1, 2, 3])




```python
A + b
```




    array([[ 0,  2,  4,  6],
           [ 4,  6,  8, 10],
           [ 8, 10, 12, 14],
           [12, 14, 16, 18]])




```python
m = np.arange(6).reshape(3, 1, 2)
n = np.arange(6).reshape(3, 2, 1)
m
```




    array([[[0, 1]],

           [[2, 3]],

           [[4, 5]]])




```python
n
```




    array([[[0],
            [1]],

           [[2],
            [3]],

           [[4],
            [5]]])




```python
m + n
```




    array([[[ 0,  1],
            [ 1,  2]],

           [[ 4,  5],
            [ 5,  6]],

           [[ 8,  9],
            [ 9, 10]]])



## 3.10 Structured Arrays


```python
structured = np.array([(1, 'First', 0.5, 1+2j),(2, 'Second', 1.3, 2-2j),
                       (3, 'Third', 0.8, 1+3j)],dtype=('i2, a6, f4, c8'))
```


```python
structured
```




    array([(1, b'First',  0.5       ,  1.+2.j),
           (2, b'Second',  1.29999995,  2.-2.j),
           (3, b'Third',  0.80000001,  1.+3.j)],
          dtype=[('f0', '<i2'), ('f1', 'S6'), ('f2', '<f4'), ('f3', '<c8')])




```python
structured = np.array([(1, 'First', 0.5, 1+2j),(2, 'Second', 1.3,2-2j),
                       (3, 'Third', 0.8, 1+3j)],dtype=('int16, a6, float32, complex64'))
structured
```




    array([(1, b'First',  0.5       ,  1.+2.j),
           (2, b'Second',  1.29999995,  2.-2.j),
           (3, b'Third',  0.80000001,  1.+3.j)],
          dtype=[('f0', '<i2'), ('f1', 'S6'), ('f2', '<f4'), ('f3', '<c8')])




```python
structured[1]
```




    (2, b'Second',  1.29999995,  2.-2.j)




```python
structured['f1']
```




    array([b'First', b'Second', b'Third'],
          dtype='|S6')




```python
structured = np.array([(1,'First',0.5,1+2j),(2,'Second',1.3,2-2j),(3,'Third',0.8,1+3j)],
                      dtype=[('id','i2'),('position','a6'),('value','f4'),('complex','c8')])
structured
```




    array([(1, b'First',  0.5       ,  1.+2.j),
           (2, b'Second',  1.29999995,  2.-2.j),
           (3, b'Third',  0.80000001,  1.+3.j)],
          dtype=[('id', '<i2'), ('position', 'S6'), ('value', '<f4'), ('complex', '<c8')])




```python
structured.dtype.names = ('id','order','value','complex')
```


```python
structured['order']
```




    array([b'First', b'Second', b'Third'],
          dtype='|S6')



## 3.11 Reading and Writing Array Data on Files

### Loading and Saving Data in Binary Files


```python
data
```


```python
np.save('saved_data',data)
```


```python
loaded_data = np.load('data/saved_data.npy')
loaded_data
```

### Reading File with T abular Data


```python
import numpy as np
data = np.genfromtxt('data/data.csv', delimiter=',', names=True)
data
```




    array([( 1.,  123.,  1.4,  23.), ( 2.,  110.,  0.5,  18.),
           ( 3.,  164.,  2.1,  19.)],
          dtype=[('id', '<f8'), ('value1', '<f8'), ('value2', '<f8'), ('value3', '<f8')])




```python
data2 = np.genfromtxt('data/data2.csv', delimiter=',', names=True)
data2
```




    array([( 1.,  123.,  1.4,  23.), ( 2.,  110.,  nan,  18.),
           ( 3.,   nan,  2.1,  19.)],
          dtype=[('id', '<f8'), ('value1', '<f8'), ('value2', '<f8'), ('value3', '<f8')])




```python
data2['id']
```




    array([ 1.,  2.,  3.])



## 3.12 Conclusions


```python

```
