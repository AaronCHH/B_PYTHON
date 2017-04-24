
# Chapter 11: Numerics and Numpy
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 11: Numerics and Numpy](#chapter-11-numerics-and-numpy)
  * [11-1. Creating Arrays](#11-1-creating-arrays)
  * [11-2. Copying an Array](#11-2-copying-an-array)
  * [11-3. Accessing Array Data](#11-3-accessing-array-data)
  * [11-4. Manipulating a Matrix](#11-4-manipulating-a-matrix)
  * [11-5. Calculating Fast Fourier Transforms](#11-5-calculating-fast-fourier-transforms)
  * [11-6. Loading File Data into an Array](#11-6-loading-file-data-into-an-array)
  * [11-7. Saving Arrays](#11-7-saving-arrays)
  * [11-8. Generating Random Numbers](#11-8-generating-random-numbers)
  * [11-9. Calculating Basic Statistics](#11-9-calculating-basic-statistics)
  * [11-10. Computing Histograms](#11-10-computing-histograms)

<!-- tocstop -->


## 11-1. Creating Arrays
* Problem
* Solution
* How It Works


```python
import numpy as np
list1 = [1, 2, 3.0, 4]
```


```python
array1 = np.array(list1)
array1
```




    array([ 1.,  2.,  3.,  4.])




```python
complex1 = np.array(list1, dtype=complex)
complex1
```




    array([ 1.+0.j,  2.+0.j,  3.+0.j,  4.+0.j])




```python
matrix1 = np.array([[1, 2], [3, 4]])
matrix1
```




    array([[1, 2],
           [3, 4]])




```python
empty1 = np.empty([2, 2], dtype=int)
empty1
```




    array([[0, 0],
           [0, 0]])




```python
zero1 = np.zeros((2, 3), dtype=float)
zero1
```




    array([[ 0.,  0.,  0.],
           [ 0.,  0.,  0.]])




```python
ones1 = np.ones((3, 2), dtype=int)
ones1
```




    array([[1, 1],
           [1, 1],
           [1, 1]])



## 11-2. Copying an Array
* Problem
* Solution
* How It Works


```python
a = np.ones((6,), dtype=int)
a
```




    array([1, 1, 1, 1, 1, 1])




```python
b = a
```


```python
view1 = ones1.view()
# Do these variables point to the same object?
view1 is ones1
```




    False




```python
view1.base is ones1
```




    True




```python
view1.shape = 2,3
ones1
```




    array([[1, 1],
           [1, 1],
           [1, 1]])




```python
view1
```




    array([[1, 1, 1],
           [1, 1, 1]])




```python
copy1 = a.copy()
a is copy1
```




    False




```python
a is copy1.base
```




    False



## 11-3. Accessing Array Data
* Problem
* Solution
* How It Works


```python
a[1] = 2
a
```




    array([1, 2, 1, 1, 1, 1])




```python
a[1:3]
```




    array([2, 1])




```python
ones1[1, 1] = 2
ones1
```




    array([[1, 1],
           [1, 2],
           [1, 1]])




```python
ones1[1, : ]
```




    array([1, 2])



## 11-4. Manipulating a Matrix
* Problem
* Solution
* How It Works


```python
a = np.array([[1.0, 2.0], [3.0, 4.0]])
np.linalg.inv(a)
```




    array([[-2. ,  1. ],
           [ 1.5, -0.5]])




```python
np.linalg.norm(a)
```




    5.4772255750516612




```python
a.trace()
```




    5.0




```python
a.transpose()
```




    array([[ 1.,  3.],
           [ 2.,  4.]])



## 11-5. Calculating Fast Fourier Transforms
* Problem
* Solution
* How It Works


```python
# a is a 1-dimensional array
np.fft.fft(a)
# b is a 2-dimensional array
np.fft.fft2(b)
# c is a 3-dimensional array
np.fft.fftn(c)
```


```python
np.fft.fft(c, axis=1)
```

## 11-6. Loading File Data into an Array
* Problem
* Solution
* How It Works


```python
txt1 = np.loadtxt('mydata.txt')
```


```python
txt2 = np.loadtxt('mydata.txt', delimiter=',')
```


```python
data = np.load('mydata.npy')
```

## 11-7. Saving Arrays
* Problem
* Solution
* How It Works


```python
np.save('mydata.npy', data)
```


```python
np.savetxt('mydata.csv', data, delimiter=',')
```

## 11-8. Generating Random Numbers
* Problem
* Solution
* How It Works


```python
rand1 = np.random.geometric(p=0.5)
```


```python
np.random.seed(42)
```


```python
rand2 = np.random.random()
```

## 11-9. Calculating Basic Statistics
* Problem
* Solution
* How It Works


```python
a = np.array([1, 2, 3, 4, 5])
np.mean(a)
```


```python
np.median(a)
```


```python
np.var(a)
```


```python
np.std(a)
```

## 11-10. Computing Histograms
* Problem
* Solution
* How It Works


```python
b = np.array([1,2,1,2,3,1,2,3,3,2,1])
np.histogram(b)
```




    (array([4, 0, 0, 0, 0, 4, 0, 0, 0, 3], dtype=int64),
     array([ 1. ,  1.2,  1.4,  1.6,  1.8,  2. ,  2.2,  2.4,  2.6,  2.8,  3. ]))




```python
np.histogram(b, 3)
```




    (array([4, 4, 3], dtype=int64),
     array([ 1.        ,  1.66666667,  2.33333333,  3.        ]))
