
# Chapter 8: Metaprogramming
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 8: Metaprogramming](#chapter-8-metaprogramming)
  * [8-1. Using a Function Decorator to Wrap Existing Code](#8-1-using-a-function-decorator-to-wrap-existing-code)
  * [8-2. Writing a Function Decorator to Wrap Existing Code](#8-2-writing-a-function-decorator-to-wrap-existing-code)
  * [8-3. Unwrapping a Decorated Function](#8-3-unwrapping-a-decorated-function)
  * [8-4. Using a Metaclass to Change the Construction of a Class](#8-4-using-a-metaclass-to-change-the-construction-of-a-class)
  * [8-5. Writing a Metaclass](#8-5-writing-a-metaclass)
  * [8-6. Using Signatures to Change the Parameters a Function Accepts](#8-6-using-signatures-to-change-the-parameters-a-function-accepts)

<!-- tocstop -->



## 8-1. Using a Function Decorator to Wrap Existing Code
* Problem
* Solution
* How It Works


```python
from line_profile import *
@profile
def my_adder(x, y):
    return x + y
```


```python
from line_profiler import *
def my_adder(x, y):
    return x + y

my_adder = profile(my_adder)
```


```python
from line_profiler import *
def my_adder(x, y):
    return x + y

my_adder = profile(my_adder)
```

## 8-2. Writing a Function Decorator to Wrap Existing Code
* Problem
* Solution
* How It Works


```python
from functools import wraps
def function_name(func):
    message = func.__qualname__
    @wraps(func)
    def wrapper((*args, **kwargs)):
        print(message)
        return func(*args, **kwargs)
    return wrapper
```


```python
@function_name
def adder(x,y):
    return x+y
```

## 8-3. Unwrapping a Decorated Function
* Problem
* Solution
* How It Works


```python
>>> adder(2,3)
adder
5
>>> adder.__wrapper__(2,3)
5
```

## 8-4. Using a Metaclass to Change the Construction of a Class
* Problem
* Solution
* How It Works


```python
class my_counter(metaclass=Singleton):
    pass
```


```python
class my_counter():
    __metaclass__ = Singleton
    pass
```

## 8-5. Writing a Metaclass
* Problem
* Solution
* How It Works


```python
class CannotInit(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Cannot instantiate")
```


```python
class MySingleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)
    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance
```

## 8-6. Using Signatures to Change the Parameters a Function Accepts
* Problem
* Solution
* How It Works


```python
>>> from inspect import Signature, Parameter
>>> params = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
... Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
... Parameter('z', Parameter.KEYWORD_ONLY, default=None)]
>>> my_sig = Signature(params)
>>> print(my_sig)
(x, y=42, *, z=None)
```


```python
def my_func(*args, **kwargs):
    bound_values = my_sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)
```
