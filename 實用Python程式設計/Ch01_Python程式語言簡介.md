
# Ch01 Python程式語言簡介
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Ch01 Python程式語言簡介](#ch01-python程式語言簡介)
  * [1.1 Python程式語言是什麼?](#11-python程式語言是什麼)
  * [1.2 Python Shell基本操作](#12-python-shell基本操作)
  * [1.3 Python相關工具及程式套件安裝](#13-python相關工具及程式套件安裝)
  * [1.4 程式套件之導入](#14-程式套件之導入)

<!-- tocstop -->


## 1.1 Python程式語言是什麼?

## 1.2 Python Shell基本操作


```python
## Python Codes for Chapter 1: What is Python Language?

#########

x = 5  # 令 x 的值為 5
x
```




    5




```python
x = 5; y = 5; z = 5
(x + y) * z
```




    50



## 1.3 Python相關工具及程式套件安裝

## 1.4 程式套件之導入


```python
import sys
sys.path # 顯示 import 的搜尋路徑
mypath = "D:\Practical-Python-Programming\Python-Files"
sys.path.append(mypath)  # 附加 import 的搜尋路徑
sys.path
```


```python
import os
os.getcwd() # 顯示目前工作目錄
mywd = "D:\Practical-Python-Programming\Python-Files"
os.chdir(mywd) # 更改工作目錄
os.getcwd() # 再次確認目前工作目錄
```


```python
import numpy

x = numpy.zeros(10)
y = numpy.ones(10)
```


```python
import numpy as np
x = np.zeros(10)
y = np.ones(10)
```


```python
from numpy import *
x = zeros(10)
y = ones(10)
```


```python
import numpy.random

z = numpy.random.normal(0, 1, 10)
```


```python
from numpy import random
z = random.normal(0, 1, 10)
```


```python
from numpy.random import normal

z = normal(0, 1, 10)
```


```python
import matplotlib as mpl
import matplotlib.pyplot as plt

import scipy
import scipy.cluster
import scipy.optimize
from scipy.optimize import fsolve
from scipy.optimize import minimize
from scipy.optimize import minimize_scalar
from scipy.optimize import curve_fit
import scipy.integrate
from scipy.integrate import quad
import scipy.interpolate
from scipy.integrate import quad, trapz
from scipy.integrate import odeint
from scipy.interpolate import interp1d
from scipy.interpolate import UnivariateSpline
import scipy.signal
import scipy.stats as stats
from scipy.stats import norm

#########
```


```python

```
