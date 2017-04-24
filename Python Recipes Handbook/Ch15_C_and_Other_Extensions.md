
# Chapter 15: C and Other Extensions
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 15: C and Other Extensions](#chapter-15-c-and-other-extensions)
  * [15-1. Compiling Python Code](#15-1-compiling-python-code)
  * [15-2. Using Static Types](#15-2-using-static-types)
  * [15-3. Calling Python from C](#15-3-calling-python-from-c)
  * [15-4. Calling C from Python](#15-4-calling-c-from-python)

<!-- tocstop -->


## 15-1. Compiling Python Code
* Problem
* Solution
* How It Works


```python
pip install --user cython
```


```python
def print_msg():
    print("Hello World")
```


```python
import pyximport
pyximport.install()
import HelloWorld
print_msg()
```


```python
import cython
def my_adder(a, b):
    ret = cython.inline("return a+b")
```

## 15-2. Using Static Types
* Problem
* Solution
* How It Works


```python
def f(x):
    return x**2-42
def integrate_f(a, b, N):
    s = 0
    dx = (b-a)/N
    for I in range(N):
        s += f(a+i*dx)
    return s*dx
```


```python
def f(double x):
    return x**2-42

def integrate_f(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b-a)/N
    for I in range(N):
        s += f(a+i*dx)
    return s*dx
```


```python
cython myfile.pyx
gcc -shared -o myfile.so myfile.c `python3-config --includes`
```

## 15-3. Calling Python from C
* Problem
* Solution
* How It Works


```python
#include "Python.h"
void run_pycode(const char* code) {
    Py_Initialize();
    PyRun_SimpleString(code);
    Py_Finalize();
}
```


```python
#include "Python.h"
Int main() {
    Py_Initialize();
    FILE* file = fopen("./my_script.py", "r");
    PyRun_SimpleFile(file, "./my_script.py");
    Py_Finalize();
}
```

## 15-4. Calling C from Python
* Problem
* Solution
* How It Works


```python
cdef extern from "hello_world.c":
    void print_msg()
```


```python
static void print_msg() {
    printf("Hello World");
}
```
