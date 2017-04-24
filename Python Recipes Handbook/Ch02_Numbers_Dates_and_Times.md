
# Chapter 2: Numbers, Dates, and Times
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 2: Numbers, Dates, and Times](#chapter-2-numbers-dates-and-times)
  * [2-1. Creating Integers](#2-1-creating-integers)
  * [2-2. Creating Floating Points](#2-2-creating-floating-points)
  * [2-3. Rounding Floats to Integers](#2-3-rounding-floats-to-integers)
  * [2-4. Formatting Numbers](#2-4-formatting-numbers)
  * [2-5. Working with Arbitrary Precision Numbers](#2-5-working-with-arbitrary-precision-numbers)
  * [2-6. Generating Random Numbers](#2-6-generating-random-numbers)
  * [2-7. Getting the Current Date and Time](#2-7-getting-the-current-date-and-time)
  * [2-8. Calculating Date/Time Differences](#2-8-calculating-datetime-differences)
  * [2-9. Formatting Dates and Times](#2-9-formatting-dates-and-times)
  * [2-10. Reading Dates and Times from a String](#2-10-reading-dates-and-times-from-a-string)

<!-- tocstop -->


## 2-1. Creating Integers
* Problem
* Solution
* How It Works


```python
>>> a = 123456789
>>> a.bit_length()
27
```


```python
>>> b = int('110',2)
>>> b
6
```

## 2-2. Creating Floating Points
* Problem
* Solution
* How It Works


```python
>>> b = 1.
>>> b
1.0
>>> c = 1e2
>>> c
100.0
```

## 2-3. Rounding Floats to Integers
* Problem
* Solution
* How It Works


```python
>>> c = 1234.567
>>> int(c)
1234
```


```python
>>> import math
>>> math.trunc(c)
1234
```


```python
>>> round(c)
1235
```


```python
>>> round(c, 1)
1234.6
```


## 2-4. Formatting Numbers
* Problem
* Solution
* How It Works


```python
[sign][width][.precision][type]
```


```python
>>> format(c)
'1234.567'
>>> format(c, '+.2f')
'+1234.57'
>>> format(.25, '%')
'25.000000%'
```

## 2-5. Working with Arbitrary Precision Numbers
* Problem
* Solution
* How It Works


```python
>>> from decimal import *
>>> getcontext()
Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero,
Overflow])
>>> getcontext().prec = 10
```


```python
>>> a = Decimal(10.5)
>>> a
Decimal('10.5')
>>> 2*a
Decimal('21.0')
```

## 2-6. Generating Random Numbers
* Problem
* Solution
* How It Works


```python
>>> import random
>>> random.seed()
```


```python
>>> random.random()
0.35060766413719124
```


```python
>>> items = [1, 2, 3, 4]
>>> random.choice(items)
3
```

## 2-7. Getting the Current Date and Time
* Problem
* Solution
* How It Works


```python
import datetime
curr_datetime = datetime.datetime.now()
curr_datetime.year
```




    2017




```python
curr_datetime.weekday()
```




    0




```python
>>> import datetime
>>> curr_datetime = datetime.datetime.now()
>>> curr_date = curr_datetime.date()
>>> curr_time = curr_datetime.time()
```


## 2-8. Calculating Date/Time Differences
* Problem
* Solution
* How It Works


```python
>>> time1 = datetime.datetime.now()
>>> time2 = datetime.datetime.now()
>>> timediff = time2 - time1
>>> timediff.days
0
>>> timediff.seconds
7
>>> timediff.total_seconds()
7.532031
```


```python
>>> timediff = datetime.timedelta(days=7)
>>> time1 = datetime.datetime.now()
>>> time1.day
10
>>> time2 = time1 + timediff
>>> time2.day
17
```

## 2-9. Formatting Dates and Times
* Problem
* Solution
* How It Works


```python
>>> time3 = datetime.datetime.now()
>>> time3.strftime("%A %d. %B %Y %I:%M%p")
'Wednesday, 10. February 2016 09:39AM'
```

## 2-10. Reading Dates and Times from a String
* Problem
* Solution
* How It Works


```python
date4 = datetime.datetime(year=1999, month=9, day=21)
date4.weekday()
```




    1




```python
date5 = datetime.datetime.strptime("1999-09-21", "%Y-%m-%d")
date5.weekday()
```




    1




```python

```
