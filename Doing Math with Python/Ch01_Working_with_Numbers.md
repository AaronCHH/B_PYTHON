
# Chapter 1: Working with Numbers
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 1: Working with Numbers](#chapter-1-working-with-numbers)
  * [1.1 Basic Mathematical Operations](#11-basic-mathematical-operations)
  * [1.2 Labels: Attaching Names to Numbers](#12-labels-attaching-names-to-numbers)
  * [1.3 Different Kinds of Numbers](#13-different-kinds-of-numbers)
    * [Working with Fractions](#working-with-fractions)
    * [Complex Numbers](#complex-numbers)
  * [1.4 Getting User Input](#14-getting-user-input)
    * [Handling Exceptions and Invalid Input](#handling-exceptions-and-invalid-input)
    * [Fractions and Complex Numbers as Input](#fractions-and-complex-numbers-as-input)
  * [1.5 Writing Programs That Do the Math for You](#15-writing-programs-that-do-the-math-for-you)
    * [Calculating the Factors of an Integer](#calculating-the-factors-of-an-integer)
    * [Generating Multiplication Tables](#generating-multiplication-tables)
    * [Converting Units of Measurement](#converting-units-of-measurement)
    * [Finding the Roots of a Quadratic Equation](#finding-the-roots-of-a-quadratic-equation)
  * [1.6 What You Learned](#16-what-you-learned)
  * [1.7 Programming Challenges](#17-programming-challenges)
    * [Challenge 1: Even-Odd Vending Machine](#challenge-1-even-odd-vending-machine)
    * [Challenge 2: Enhanced Multiplication Table Generator](#challenge-2-enhanced-multiplication-table-generator)
    * [Challenge 3: Enhanced Unit Converter](#challenge-3-enhanced-unit-converter)
    * [Challenge 4: Fraction Calculator](#challenge-4-fraction-calculator)
    * [Challenge 5: Give Exit Power to the User](#challenge-5-give-exit-power-to-the-user)

<!-- tocstop -->


## 1.1 Basic Mathematical Operations

## 1.2 Labels: Attaching Names to Numbers

## 1.3 Different Kinds of Numbers


```python
type(3)
```




    int




```python
type(3.5)
```




    float




```python
type(3.0)
```




    float




```python
int(3.8)
```




    3




```python
int(3.0)
```




    3



### Working with Fractions


```python
from fractions import Fraction
f = Fraction(3, 4)
f
```




    Fraction(3, 4)




```python
Fraction(3, 4) + 1 + 1.5
```




    3.25




```python
Fraction(3, 4) + 1 + Fraction(1/4)
```




    Fraction(2, 1)



### Complex Numbers


```python
a = 2 + 3j
type(a)
```




    complex




```python
a = complex(2, 3)
a
```




    (2+3j)




```python
b = 3 + 3j
```


```python

```


```python
a + b
```




    (5+6j)




```python
a - b
```




    (-1+0j)




```python
a * b
```




    (-3+15j)




```python
a / b
```




    (0.8333333333333334+0.16666666666666666j)




```python
z = 2 + 3j
```


```python
z.real
```




    2.0




```python
z.imag
```




    3.0




```python
z.conjugate()
```




    (2-3j)




```python
(z.real ** 2 + z.imag ** 2) ** 0.5
```




    3.605551275463989




```python
abs(z)
```




    3.605551275463989



## 1.4 Getting User Input


```python
a = input()
a
```







    ''




```python
s1 = 'a string'
```


```python
s2 = "a string"
```


```python
a = '1'
```


```python
int(a) + 1
```




    2




```python
float(a) + 1
```




    2.0




```python
int('2.0')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-33-1a2e39c94309> in <module>()
    ----> 1 int('2.0')


    ValueError: invalid literal for int() with base 10: '2.0'



```python
a = float(input())
```

    2/4



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-34-7b96a7c8fa9f> in <module>()
    ----> 1 a = float(input())


    ValueError: could not convert string to float: '2/4'


### Handling Exceptions and Invalid Input


```python
try:
    a = float(input('Enter a number: '))
except ValueError:
    print('You entered an invalid number')
```


```python
a = input('Input an integer: ')
```


```python
a = int(input())
```


```python
a + 1
```


```python
a = int(input())
```


```python
1.1.is_integer()
```




    False




```python
1.0.is_integer()
```




    True



### Fractions and Complex Numbers as Input


```python
a = Fraction(input('Enter a fraction: '))
a
```


```python
a = Fraction(input('Enter a fraction: '))
```


```python
try:
    a = Fraction(input('Enter a fraction: '))
except ZeroDivisionError:
    print('Invalid fraction')
```


```python
z = complex(input('Enter a complex number: '))
z
```


```python
z = complex(input('Enter a complex number: '))
```


```python

```

## 1.5 Writing Programs That Do the Math for You

### Calculating the Factors of an Integer


```python
def is_factor(a, b):
    if b % a == 0:
        return True
    else:
        return False
```


```python
is_factor(4, 1024)
```




    True




```python
for i in range(1, 4):
    print(i)
```

    1
    2
    3



```python
for i in range(5):
    print(i)
```

    0
    1
    2
    3
    4



```python
for i in range(1,10,2):
    print(i)
```

    1
    3
    5
    7
    9


### Generating Multiplication Tables

### Converting Units of Measurement

### Finding the Roots of a Quadratic Equation

## 1.6 What You Learned

## 1.7 Programming Challenges

### Challenge 1: Even-Odd Vending Machine

### Challenge 2: Enhanced Multiplication Table Generator

### Challenge 3: Enhanced Unit Converter

### Challenge 4: Fraction Calculator

### Challenge 5: Give Exit Power to the User
