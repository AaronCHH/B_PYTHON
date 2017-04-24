
# Chapter 1: Strings and Texts
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 1: Strings and Texts](#chapter-1-strings-and-texts)
  * [1-1. Concatenating Strings](#1-1-concatenating-strings)
  * [1-2. Comparing Strings](#1-2-comparing-strings)
  * [1-3. Searching for a Substring](#1-3-searching-for-a-substring)
  * [1-4. Getting a Substring](#1-4-getting-a-substring)
  * [1-5. Replacing Text Matches](#1-5-replacing-text-matches)
  * [1-6. Reversing a String](#1-6-reversing-a-string)
  * [1-7. Trimming White Space](#1-7-trimming-white-space)
  * [1-8. Changing Case](#1-8-changing-case)
  * [1-9. Converting to Numbers](#1-9-converting-to-numbers)
  * [1-10. Iterating Over the Characters of a String](#1-10-iterating-over-the-characters-of-a-string)
  * [1-11. Statistics on Texts](#1-11-statistics-on-texts)
  * [1-12. Encoding Unicode](#1-12-encoding-unicode)
  * [1-13. Translation](#1-13-translation)

<!-- tocstop -->


## 1-1. Concatenating Strings
* Problem
* Solution
* How It Works


```python
new_str = "hello " + "world"
print(new_str)
```

    hello world



```python
new_str = "Hello" * 3
print(new_str)
```

    HelloHelloHello



```python
New_str = "Count = " + str(42)
print(New_str)
```

    Count = 42


## 1-2. Comparing Strings
* Problem
* Solution
* How It Works


```python
str1 = "Hello"
str2 = "World"
if str1 == str2:
    print("The strings are equal")
else:
    print("The strings are not equal")
```

    The strings are not equal


## 1-3. Searching for a Substring
* Problem
* Solution
* How It Works


```python
>>> Str1 = 'This is a string'
>>> 'is' in Str1
True
>>> 'me' in Str1
False
```


```python
>>> Str1.find('is')
2
>>> Str1.find('me')
-1
```


```python
>>> Str1.find('is', 3)
5
```

## 1-4. Getting a Substring
* Problem
* Solution
* How It Works


```python
>>> Str2 = 'One two three'
>>> Str2[0:2]
On
>>> Str2[:2]
On
>>> Str2[8:]
three
```

## 1-5. Replacing Text Matches
* Problem
* Solution
* How It Works


```python
str1 = "Here are a string"
corrected_str1 = str1[:5] + "is" + str1[7:]
print(corrected_str1)
```

    Here ise a string



```python
corrected_str1 = str1.replace("are", "is", 1)
```

## 1-6. Reversing a String
* Problem
* Solution
* How It Works


```python
>>> str1 = "Hello World"
>>> str2 = str1[::-1]
>>> print(str2)
dlrow olleH
```

## 1-7. Trimming White Space
* Problem
* Solution
* How It Works


```python
>>> str1 = "Space"
>>> str2 = str1.strip()
>>> print(str2)
Space
```

## 1-8. Changing Case
* Problem
* Solution
* How It Works


```python
>>> str1 = "Hello World"
>>> print(str1.lower())
hello world
>>> print(str1.upper())
HELLO WORLD
```

## 1-9. Converting to Numbers
* Problem
* Solution
* How It Works


```python
>>> hex1 = int("ae", 16)
>>> hex1
```

## 1-10. Iterating Over the Characters of a String
* Problem
* Solution
* How It Works


```python
str1 = "0123456789"
for i in range(10):
    print(str1[i], " and ")
```

    0  and
    1  and
    2  and
    3  and
    4  and
    5  and
    6  and
    7  and
    8  and
    9  and



```python
for i in str1:
    print(i, " and ")
```

    0  and
    1  and
    2  and
    3  and
    4  and
    5  and
    6  and
    7  and
    8  and
    9  and


## 1-11. Statistics on Texts
* Problem
* Solution
* How It Works


```python
>>> str1 = "Hello world"
>>> len(str1)
11
>>> min(str1)
' '
>>> max(str1)
'w'
>>> str1.count('o')
2
```

## 1-12. Encoding Unicode
* Problem
* Solution
* How It Works


```python
>>> ustr1 = unicode("Hello")
>>> ustr2 = u’Hello’
>>> ustr1 == ustr2
True
```


```python
ustr1.encode("utf-8")
```

## 1-13. Translation
* Problem
* Solution
* How It Works


```python
>>> str1 = "Hello world"
>>> translate_table = str1.maketrans("abcd", "efgh")
>>> str1.translate(translate_table)
Hello worlh
```


```python
>>> str1.translate(str.maketrans({'l':None,'W':None}))
Heo ord
```
