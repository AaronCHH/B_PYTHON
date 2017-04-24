
# Chapter 6: Functions
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 6: Functions](#chapter-6-functions)
  * [6-1. Creating Basic Functions](#6-1-creating-basic-functions)
  * [6-2. Using Named Parameters Rather Than Positional Parameters](#6-2-using-named-parameters-rather-than-positional-parameters)
  * [6-3. Using Default Values in Functions](#6-3-using-default-values-in-functions)
  * [6-4. Implementing a Recursive Algorithm](#6-4-implementing-a-recursive-algorithm)
  * [6-5. Using Lambda Functions to Create Temporary Anonymous Functions](#6-5-using-lambda-functions-to-create-temporary-anonymous-functions)
  * [6-6. Generating Specialized Functions](#6-6-generating-specialized-functions)

<!-- tocstop -->



## 6-1. Creating Basic Functions

* Problem
* Solution
* How It Works


```python
def square_of_two():
    ans = 2 * 2
    return ans
```


```python
square_of_two()
```




    4




```python
my_ans = square_of_two()
```


```python
def fact_two():
    a = 2
    ans = a
    while a > 1:
        ans = ans * (a-1)
        a = a - 1
    return ans
```


## 6-2. Using Named Parameters Rather Than Positional Parameters

* Problem
* Solution
* How It Works


```python
def square_num(a):
    return a*a
```


```python
square_num(2)
```




    4




```python
square_num(a=3)
```




    9




```python
def multiplication(a, b, c):
    return a*b*c
```


```python
multiplication(1, 2, 3)
```




    6




```python
multiplication(2, c=3, b=1)
```




    6



## 6-3. Using Default Values in Functions

* Problem
* Solution
* How It Works


```python
def multiplication(a=1,b=2,c=3):
    return a*b*c
```


```python
multiplication()
```




    6




```python
multiplication(5)
```




    30




```python
multiplication(1,1)
```




    3




```python
multiplication(c=1)
```




    2



## 6-4. Implementing a Recursive Algorithm

* Problem
* Solution
* How It Works


```python
def fact(a):
    if a == 1:
        return 1
    else:
        return a * fact(a-1)
fact(5)
```




    120



## 6-5. Using Lambda Functions to Create Temporary Anonymous Functions
* Problem
* Solution
* How It Works


```python
def apply_operator(a, b, f):
    return f(a,b)
```


```python
apply_operator(2, 3, lambda x, y: x*y)
```




    6



## 6-6. Generating Specialized Functions
* Problem
* Solution
* How It Works


```python
def generate_scaler(a):
    return lambda x: a*x
```


```python
doubler = generate_scaler(2)
doubler(3)
```




    6




```python
tripler = generate_scaler(3)
tripler(3)
```




    9
