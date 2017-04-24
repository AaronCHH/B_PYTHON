
# Chapter 13: Utilities
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 13: Utilities](#chapter-13-utilities)
  * [13-1. Creating a Virtual Environment](#13-1-creating-a-virtual-environment)
  * [13-2. Using the Ipython Shell](#13-2-using-the-ipython-shell)
  * [13-3. Using the Jupyter Environment](#13-3-using-the-jupyter-environment)
  * [13-4. Using xonsh as a Replacement Shell](#13-4-using-xonsh-as-a-replacement-shell)

<!-- tocstop -->



## 13-1. Creating a Virtual Environment
* Problem
* Solution
* How It Works


```python
pip install virtualenv
```


```python
virtualenv project1
```

## 13-2. Using the Ipython Shell
* Problem
* Solution
* How It Works


```python
pip install ipython
```


```python
%timeit x = range(1000000)
```


```python
# Saving a series of commands to a file
%save myfile.py 2-5 10
```


```python
%load myfile.py
```


```python
print("Hello world")
```

> You can also create your own magic functions that can further extend the functionality of IPython .
The main documentation can be found at http://ipython.readthedocs.io/en/stable/index.html.

## 13-3. Using the Jupyter Environment
* Problem
* Solution
* How It Works


```python
pip install jupyter
```

> http://jupyter.readthedocs.io/en/latest/

## 13-4. Using xonsh as a Replacement Shell
* Problem
* Solution
* How It Works


```python
pip install xonsh
```


```python
jbernard@DESKTOP-QPKN2QC ~ <branch-timeout> $ import numpy as np
jbernard@DESKTOP-QPKN2QC ~ <branch-timeout> $ np.random.random()
0.48053753953641054
```

> The main documentation site is located at http://xon.sh/index.html.
