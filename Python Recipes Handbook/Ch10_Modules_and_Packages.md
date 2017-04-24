
# Chapter 10: Modules and Packages
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 10: Modules and Packages](#chapter-10-modules-and-packages)
  * [10-1. Importing Modules](#10-1-importing-modules)
  * [10-2. Installing Modules from Source](#10-2-installing-modules-from-source)
  * [10-3. Installing Modules from Pypi](#10-3-installing-modules-from-pypi)
  * [10-4. Upgrading a Module Using pip](#10-4-upgrading-a-module-using-pip)

<!-- tocstop -->


## 10-1. Importing Modules
* Problem
* Solution
* How It Works


```python
import math
```


```python
math.sin(45)
```




    0.8509035245341184




```python
import math as m
m.cos(45)
```




    0.5253219888177297




```python
from math import sin, pi
sin(pi/2)
```




    1.0




```python
from math import *
```

## 10-2. Installing Modules from Source
* Problem
* Solution
* How It Works


```python
python setup.py install
```

## 10-3. Installing Modules from Pypi
* Problem
* Solution
* How It Works


```python
pip install numpy
```


```python
pip install --usernumpy
```

## 10-4. Upgrading a Module Using pip
* Problem
* Solution
* How It Works


```python
pip install --upgrade numpy
```


```python
pip install --upgrade --no-deps numpy
pip install numpy
```
