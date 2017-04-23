
# Chapter1 Python Basics
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter1 Python Basics](#chapter1-python-basics)
  * [1.1 How to Create a Python Script](#11-how-to-create-a-python-script)
  * [1.2 How to Run a Python Script](#12-how-to-run-a-python-script)
  * [1.3 Useful Tips for Interacting with the Command Line](#13-useful-tips-for-interacting-with-the-command-line)
  * [1.4 Python's Basic Building Blocks](#14-pythons-basic-building-blocks)
    * [1.4.1 Numbers](#141-numbers)
    * [1.4.2 Strings](#142-strings)
      * [split](#split)
      * [join](#join)
      * [strip](#strip)
      * [replace](#replace)
      * [lower, upper, capitalize](#lower-upper-capitalize)
    * [1.4.3 Regular Expressions/Pattern Matching](#143-regular-expressionspattern-matching)
    * [1.4.4 Dates](#144-dates)
    * [1.4.5 Lists](#145-lists)
    * [1.4.6 Tuples](#146-tuples)
    * [1.4.7 Dictionaries](#147-dictionaries)
    * [1.4.8 Control Flow](#148-control-flow)
  * [1.5 Reading a Text File](#15-reading-a-text-file)
    * [1.5.1 建立文字檔](#151-建立文字檔)
    * [1.5.2 將腳本與輸入檔案放在同一個地方](#152-將腳本與輸入檔案放在同一個地方)
    * [1.5.3 現代檔案讀取語法](#153-現代檔案讀取語法)
  * [1.6 Reading Multiple Text Files with glob](#16-reading-multiple-text-files-with-glob)
    * [1.6.1 建立另一個文字檔](#161-建立另一個文字檔)
  * [1.7 Writing to a Text File](#17-writing-to-a-text-file)
    * [1.7.1 在first script.py裡面加入程式](#171-在first-scriptpy裡面加入程式)
    * [1.7.2 寫至一個以逗號分隔值(CSV)的檔案](#172-寫至一個以逗號分隔值csv的檔案)
  * [1.8 print Statements](#18-print-statements)
  * [1.9 Chapter Exercises](#19-chapter-exercises)

<!-- tocstop -->



```python
#!/usr/bin/env python3
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys
import glob
import os
```


```python
4+5
```




    9




```python
print("I'm excited ot learn Python")
```

    I'm excited ot learn Python


## 1.1 How to Create a Python Script


```python
# Print a simple string
print("Output #1: I'm excited to learn Python.")
```

    Output #1: I'm excited to learn Python.


## 1.2 How to Run a Python Script


```python
# Add two numbers together
x = 4
y = 5
z = x + y
print("Output #2: Four plus five equals {0:d}.".format(z))
```

    Output #2: Four plus five equals 9.



```python
# Add two lists together
a = [1, 2, 3, 4]
b = ["first", "second", "third", "fourth"]
c = a + b
print("Output #3: {0}, {1}, {2}".format(a, b, c))
```

    Output #3: [1, 2, 3, 4], ['first', 'second', 'third', 'fourth'], [1, 2, 3, 4, 'first', 'second', 'third', 'fourth']


## 1.3 Useful Tips for Interacting with the Command Line

## 1.4 Python's Basic Building Blocks

### 1.4.1 Numbers


```python
# INTEGERS
x = 9
print("Output #4: {0}".format(x))
print("Output #5: {0}".format(3**4))
print("Output #6: {0}".format(int(8.3)/int(2.7)))
```

    Output #4: 9
    Output #5: 81
    Output #6: 4.0



```python
# FLOATING-POINT NUMBERS
print("Output #7: {0:.3f}".format(8.3/2.7))
y = 2.5*4.8
print("Output #8: {0:.1f}".format(y))
r = 8/float(3)
print("Output #9: {0:.2f}".format(r))
print("Output #10: {0:.4f}".format(8.0/3))
```

    Output #7: 3.074
    Output #8: 12.0
    Output #9: 2.67
    Output #10: 2.6667



```python
# Some mathematical functions available in the math module
print("Output #11: {0:.4f}".format(exp(3)))
print("Output #12: {0:.2f}".format(log(4)))
print("Output #13: {0:.1f}".format(sqrt(81)))
```

    Output #11: 20.0855
    Output #12: 1.39
    Output #13: 9.0


### 1.4.2 Strings


```python
# STRINGS
# A string with single quotes, so include a backslash before the single quote
print("Output #14: {0:s}".format('I\'m enjoying learning Python'))
```

    Output #14: I'm enjoying learning Python



```python
# A one-line string, but if the string is long and running off the page on the right
# you can use a "\" to separate the long string into smaller strings on separate lines
print("Output #15: {0:s}".format("This is a long string.  Without the backslash \
it would run off of the page on the right in the text editor and be very \
difficult to read and edit.  By using the backslash you can split the long \
string into smaller strings on separate lines so that the whole string is easy \
to view in the text editor."))
```

    Output #15: This is a long string.  Without the backslash it would run off of the page on the right in the text editor and be very difficult to read and edit.  By using the backslash you can split the long string into smaller strings on separate lines so that the whole string is easy to view in the text editor.



```python
# Use triple single or double quotes if you want the string to span multiple lines
# and you don't want to use the "\"
print("Output #16: {0:s}".format('''You can use triple single quotes
for multi-line comment strings'''))
```

    Output #16: You can use triple single quotes
    for multi-line comment strings



```python
print("Output #17: {0:s}".format("""You can also use triple double quotations
for multi-line comment strings"""))
```

    Output #17: You can also use triple double quotations
    for multi-line comment strings



```python
# Add two strings together
string1 = "This is a "
string2 = "short string."
sentence = string1 + string2
print("Output #18: {0:s}".format(sentence))
```

    Output #18: This is a short string.



```python
# Repeat a string four times
print("Output #19: {0:s} {1:s}{2:s}".format("She is", "very "*4, "beautiful."))
```

    Output #19: She is very very very very beautiful.



```python
# Determine the number of characters in a string, including spaces and punctuation
m = len(sentence)
print("Output #20: {0:d}".format(m))
```

    Output #20: 23


#### split


```python
# split()
string1 = "My deliverable is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(" ", 2)
print("Output #21: {0}".format(string1_list1))
print("Output #22: FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}"\
      .format(string1_list2[0], string1_list2[1], string1_list2[2]))
```

    Output #21: ['My', 'deliverable', 'is', 'due', 'in', 'May']
    Output #22: FIRST PIECE:My SECOND PIECE:deliverable THIRD PIECE:is due in May



```python
string2 = "Your,deliverable,is,due,in,June"
string2_list = string2.split(',')
print("Output #23: {0}".format(string2_list))
print("Output #24: {0} {1} {2}".format(string2_list[1], string2_list[5], string2_list[-1]))
```

    Output #23: ['Your', 'deliverable', 'is', 'due', 'in', 'June']
    Output #24: deliverable June June


#### join


```python
# join()
print("Output #25: {0}".format(','.join(string2_list)))
```

    Output #25: Your,deliverable,is,due,in,June


#### strip


```python
# strip()
string3 = "   Remove unwanted characters from this string\t\t    \n"
print("Output #26: string3: {0:s}".format(string3))
string3_lstrip = string3.lstrip()
print("Output #27: lstrip: {0:s}".format(string3_lstrip))
string3_rstrip = string3.rstrip()
print("Output #28: rstrip: {0:s}".format(string3_rstrip))
string3_strip = string3.strip()
print("Output #29: strip: {0:s}".format(string3_strip))
```

    Output #26: string3:    Remove unwanted characters from this string

    Output #27: lstrip: Remove unwanted characters from this string

    Output #28: rstrip:    Remove unwanted characters from this string
    Output #29: strip: Remove unwanted characters from this string



```python
string4 = "$$Here's another string that has unwanted characters.__---++"
print("Output #30: {0:s}".format(string4))
string4 = "$$The unwanted characters have been removed.__---++"
string4_strip = string4.strip('$_-+')
print("Output #31: {0:s}".format(string4_strip))
```

    Output #30: $$Here's another string that has unwanted characters.__---++
    Output #31: The unwanted characters have been removed.


#### replace


```python
# replace()
string5 = "Let's replace the spaces in this sentence with other characters."
string5_replace = string5.replace(" ", "!@!")
print("Output #32 (with !@!): {0:s}".format(string5_replace))
string5_replace = string5.replace(" ", ",")
print("Output #33 (with commas): {0:s}".format(string5_replace))
```

    Output #32 (with !@!): Let's!@!replace!@!the!@!spaces!@!in!@!this!@!sentence!@!with!@!other!@!characters.
    Output #33 (with commas): Let's,replace,the,spaces,in,this,sentence,with,other,characters.


#### lower, upper, capitalize


```python
# lower(), upper(), capitalize()
string6 = "Here's WHAT Happens WHEN You Use lower."
print("Output #34: {0:s}".format(string6.lower()))
```

    Output #34: here's what happens when you use lower.



```python
string7 = "Here's what Happens when You Use UPPER."
print("Output #35: {0:s}".format(string7.upper()))
```

    Output #35: HERE'S WHAT HAPPENS WHEN YOU USE UPPER.



```python
string8 = "here's WHAT Happens WHEN you use Capitalize."
print("Output #36: {0:s}".format(string8.capitalize()))
string8_list = string8.split()
print("Output #37 (on each word):")
for word in string8_list:
    print("{0:s}".format(word.capitalize()))
```

    Output #36: Here's what happens when you use capitalize.
    Output #37 (on each word):
    Here's
    What
    Happens
    When
    You
    Use
    Capitalize.


### 1.4.3 Regular Expressions/Pattern Matching


```python
# REGULAR EXPRESSIONS / PATTERN MATCHING
# Count the number of times a pattern appears in a string
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"The", re.I)
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1
print("Output #38: {0:d}".format(count))
```

    Output #38: 2



```python
# Print the pattern each time it is found in the string
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>The)", re.I)
print("Output #39:")
for word in string_list:
    if pattern.search(word):
        print("{:s}".format(pattern.search(word).group('match_word')))
```

    Output #39:
    The
    the



```python
# Substitute the letter "a" for the word "the" in the string
string = "The quick brown fox jumps over the lazy dog."
string_to_find = r"The"
pattern = re.compile(string_to_find, re.I)
print("Output #40: {:s}".format(pattern.sub("a", string)))
```

    Output #40: a quick brown fox jumps over a lazy dog.


### 1.4.4 Dates


```python
# DATES
# Print today's date, as well as the year, month, and day elements
today = date.today()
print("Output #41: today: {0!s}".format(today))
print("Output #42: {0!s}".format(today.year))
print("Output #43: {0!s}".format(today.month))
print("Output #44: {0!s}".format(today.day))
current_datetime = datetime.today()
print("Output #45: {0!s}".format(current_datetime))
```

    Output #41: today: 2017-03-29
    Output #42: 2017
    Output #43: 3
    Output #44: 29
    Output #45: 2017-03-29 00:26:19.186130



```python
# Calculate a new date using a timedelta
one_day = timedelta(days=-1)
yesterday = today + one_day
print("Output #46: yesterday: {0!s}".format(yesterday))
eight_hours = timedelta(hours=-8)
print("Output #47: {0!s} {1!s}".format(eight_hours.days, eight_hours.seconds))
```

    Output #46: yesterday: 2017-03-28
    Output #47: -1 57600



```python
# Calculate the amount of time between two dates and grab the first element, the number of days
date_diff = today - yesterday
print("Output #48: {0!s}".format(date_diff))
print("Output #49: {0!s}".format(str(date_diff).split()[0]))
```

    Output #48: 1 day, 0:00:00
    Output #49: 1



```python
# Create a string with a specific format from a date object
print("Output #50: {:s}".format(today.strftime('%m/%d/%Y')))
print("Output #51: {:s}".format(today.strftime('%b %d, %Y')))
print("Output #52: {:s}".format(today.strftime('%Y-%m-%d')))
print("Output #53: {:s}".format(today.strftime('%B %d, %Y')))
```

    Output #50: 03/29/2017
    Output #51: Mar 29, 2017
    Output #52: 2017-03-29
    Output #53: March 29, 2017



```python
# Create a datetime object with a specific format
# from a string representing a date
date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')
```


```python
# Two datetime objects and two date objects
# based on the four strings that have different date formats
print("Output #54: {!s}".format(datetime.strptime(date1, '%m/%d/%Y')))
print("Output #55: {!s}".format(datetime.strptime(date2, '%b %d, %Y')))
```

    Output #54: 2017-03-29 00:00:00
    Output #55: 2017-03-29 00:00:00



```python
# Show the date portion only
print("Output #56: {!s}".format(datetime.date(datetime.strptime\
(date3, '%Y-%m-%d'))))
print("Output #57: {!s}".format(datetime.date(datetime.strptime\
(date4, '%B %d, %Y'))))
```

    Output #56: 2017-03-29
    Output #57: 2017-03-29


### 1.4.5 Lists


```python
# LISTS
# Use square brackets to create a list
# len() counts the number of elements in a list
# max() and min() find the maximum and minimum numbers in numeric lists
# count() counts the number of times a value appears in a list
a_list = [1, 2, 3]
print("Output #58: {}".format(a_list))
print("Output #59: a_list has {} elements.".format(len(a_list)))
print("Output #60: the maximum value in a_list is {}.".format(max(a_list)))
print("Output #61: the minimum value in a_list is {}.".format(min(a_list)))
another_list = ['printer', 5, ['star', 'circle', 9]]
print("Output #62: {}".format(another_list))
print("Output #63: another_list also has {} elements.".format(len(another_list)))
print("Output #64: 5 is in another_list {} time.".format(another_list.count(5)))
```

    Output #58: [1, 2, 3]
    Output #59: a_list has 3 elements.
    Output #60: the maximum value in a_list is 3.
    Output #61: the minimum value in a_list is 1.
    Output #62: ['printer', 5, ['star', 'circle', 9]]
    Output #63: another_list also has 3 elements.
    Output #64: 5 is in another_list 1 time.



```python
# Use list indices to access specific values in a list
# [0] is the first value; [-1] is the last value
print("Output #65: {}".format(a_list[0]))
print("Output #66: {}".format(a_list[1]))
print("Output #67: {}".format(a_list[2]))
print("Output #68: {}".format(a_list[-1]))
print("Output #69: {}".format(a_list[-2]))
print("Output #70: {}".format(a_list[-3]))
print("Output #71: {}".format(another_list[2]))
print("Output #72: {}".format(another_list[-1]))
```

    Output #65: 1
    Output #66: 2
    Output #67: 3
    Output #68: 3
    Output #69: 2
    Output #70: 1
    Output #71: ['star', 'circle', 9]
    Output #72: ['star', 'circle', 9]



```python
# Use list slices to access a subset of list values
# Do not include the starting indice to start from the beginning
# Do not include the ending indice to go all of the way to the end
print("Output #73: {}".format(a_list[0:2]))
print("Output #74: {}".format(another_list[:2]))
print("Output #75: {}".format(a_list[1:3]))
print("Output #76: {}".format(another_list[1:]))
```

    Output #73: [1, 2]
    Output #74: ['printer', 5]
    Output #75: [2, 3]
    Output #76: [5, ['star', 'circle', 9]]



```python
# Use [:] to make a copy of a list
a_new_list = a_list[:]
print("Output #77: {}".format(a_new_list))
```

    Output #77: [1, 2, 3]



```python
# Use + to add two or more lists together
a_longer_list = a_list + another_list    # to add lists together
print("Output #78: {}".format(a_longer_list))
```

    Output #78: [1, 2, 3, 'printer', 5, ['star', 'circle', 9]]



```python
# Use 'in' and 'not in' to check whether specific values are or are not in a list
a = 2 in a_list
print("Output #79: {}".format(a))
if 2 in a_list:
    print("Output #80: 2 is in {}.".format(a_list))
b = 6 not in a_list
print("Output #81: {}".format(b))
if 6 not in a_list:
    print("Output #82: 6is not in {}.".format(a_list))
```

    Output #79: True
    Output #80: 2 is in [1, 2, 3].
    Output #81: True
    Output #82: 6is not in [1, 2, 3].



```python
# Use append() to add additional values to the end of the list
# Use remove() to remove specific values from the list
# Use pop() to remove values from the end of the list
a_list.append(4)
a_list.append(5)
a_list.append(6)
print("Output #83: {}".format(a_list))
a_list.remove(5)
print("Output #84: {}".format(a_list))
a_list.pop()
a_list.pop()
print("Output #85: {}".format(a_list))
```

    Output #83: [1, 2, 3, 4, 5, 6]
    Output #84: [1, 2, 3, 4, 6]
    Output #85: [1, 2, 3]



```python
# Use sort() to sort a list, in-place, meaning it changes the list
# To sort a list without changing the original list, make a copy first
unordered_list = [3, 5, 1, 7, 2, 8, 4, 9, 0, 6]
print("Output #88: {}".format(unordered_list))
list_copy = unordered_list[:]
list_copy.sort()
print("Output #89: {}".format(list_copy))
print("Output #90: {}".format(unordered_list))
```

    Output #88: [3, 5, 1, 7, 2, 8, 4, 9, 0, 6]
    Output #89: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    Output #90: [3, 5, 1, 7, 2, 8, 4, 9, 0, 6]



```python
# Use reverse() to reverse a list, in-place, meaning it changes the list
# To reverse a list without changing the original list, make a copy first
a_list.reverse()
print("Output #86: {}".format(a_list))
a_list_copy = a_list[:]
a_list_copy.reverse()
print("Output #87: {}".format(a_list_copy))
```

    Output #86: [3, 2, 1]
    Output #87: [1, 2, 3]



```python
# Use sorted() to sort a collection of lists by a position in the lists
my_lists = [[1,2,3,4], [4,3,2,1], [2,4,1,3]]
my_lists_sorted_by_index_3 = sorted(my_lists, key=lambda index_value: index_value[3])
print("Output #91: {}".format(my_lists_sorted_by_index_3))
```

    Output #91: [[4, 3, 2, 1], [2, 4, 1, 3], [1, 2, 3, 4]]



```python
# Use itemgetter() to sort a collection of lists by two index positions
my_lists = [[123,2,2,444], [22,6,6,444], [354,4,4,678], [236,5,5,678], \
[578,1,1,290], [461,1,1,290]]
my_lists_sorted_by_index_3_and_0 = sorted(my_lists, key=itemgetter(3,0))
print("Output #92: {}".format(my_lists_sorted_by_index_3_and_0))
```

    Output #92: [[461, 1, 1, 290], [578, 1, 1, 290], [22, 6, 6, 444], [123, 2, 2, 444], [236, 5, 5, 678], [354, 4, 4, 678]]


### 1.4.6 Tuples


```python
# TUPLES
# Use parentheses to create a tuple
my_tuple = ('x', 'y', 'z')
print("Output #93: {}".format(my_tuple))
print("Output #94: my_tuple has {} elements".format(len(my_tuple)))
print("Output #95: {}".format(my_tuple[1]))
longer_tuple = my_tuple + my_tuple
print("Output #96: {}".format(longer_tuple))
```

    Output #93: ('x', 'y', 'z')
    Output #94: my_tuple has 3 elements
    Output #95: y
    Output #96: ('x', 'y', 'z', 'x', 'y', 'z')



```python
# Unpack tuples with the left-hand side of an assignment operator
one, two, three = my_tuple
print("Output #97: {0} {1} {2}".format(one, two, three))
var1 = 'red'
var2 = 'robin'
print("Output #98: {} {}".format(var1, var2))
# Swap values between variables
var1, var2 = var2, var1
print("Output #99: {} {}".format(var1, var2))
```

    Output #97: x y z
    Output #98: red robin
    Output #99: robin red



```python
# Convert tuples to lists and lists to tuples
my_list = [1, 2, 3]
my_tuple = ('x', 'y', 'z')
print("Output #100: {}".format(tuple(my_list)))
print("Output #101: {}".format(list(my_tuple)))
```

    Output #100: (1, 2, 3)
    Output #101: ['x', 'y', 'z']


### 1.4.7 Dictionaries


```python
# DICTIONARIES
# Use curly braces to create a dictionary
# Use a colon between keys and values in each pair
# len() counts the number of key-value pairs in a dictionary
empty_dict = { }
a_dict = {'one':1, 'two':2, 'three':3}
print("Output #102: {}".format(a_dict))
print("Output #103: a_dict has {!s} elements".format(len(a_dict)))
another_dict = {'x':'printer', 'y':5, 'z':['star', 'circle', 9]}
print("Output #104: {}".format(another_dict))
print("Output #105: another_dict also has {!s} elements"\
      .format(len(another_dict)))
```

    Output #102: {'one': 1, 'two': 2, 'three': 3}
    Output #103: a_dict has 3 elements
    Output #104: {'x': 'printer', 'y': 5, 'z': ['star', 'circle', 9]}
    Output #105: another_dict also has 3 elements



```python
# Use keys to access specific values in a dictionary
print("Output #106: {}".format(a_dict['two']))
print("Output #107: {}".format(another_dict['z']))
```

    Output #106: 2
    Output #107: ['star', 'circle', 9]



```python
# Use copy() to make a copy of a dictionary
a_new_dict = a_dict.copy()
print("Output #108: {}".format(a_new_dict))
```

    Output #108: {'one': 1, 'two': 2, 'three': 3}



```python
# Use keys(), values(), and items() to access
# a dictionary's keys, values, and key-value pairs, respectively
print("Output #109: {}".format(a_dict.keys()))
a_dict_keys = a_dict.keys()
print("Output #110: {}".format(a_dict_keys))
print("Output #111: {}".format(a_dict.values()))
print("Output #112: {}".format(a_dict.items()))
```

    Output #109: dict_keys(['one', 'two', 'three'])
    Output #110: dict_keys(['one', 'two', 'three'])
    Output #111: dict_values([1, 2, 3])
    Output #112: dict_items([('one', 1), ('two', 2), ('three', 3)])



```python
# Use in, not in, and get to test
# whether a key is in a dictionary
if 'y' in another_dict:
    print("Output #114: y is a key in another_dict: {}."\
          .format(another_dict.keys()))

if 'c' not in another_dict:
    print("Output #115: c is not a key in another_dict: {}."\
          .format(another_dict.keys()))
```

    Output #114: y is a key in another_dict: dict_keys(['x', 'y', 'z']).
    Output #115: c is not a key in another_dict: dict_keys(['x', 'y', 'z']).



```python
print("Output #116: {!s}".format(a_dict.get('three')))
print("Output #117: {!s}".format(a_dict.get('four')))
print("Output #118: {!s}".format(a_dict.get('four', 'Not in dict')))
```

    Output #116: 3
    Output #117: None
    Output #118: Not in dict



```python
# Use sorted() to sort a dictionary
# To sort a dictionary without changing the original dictionary,
# make a copy first
print("Output #119: " + str(a_dict))
dict_copy = a_dict.copy()
ordered_dict1 = sorted(dict_copy.items(), key=lambda item: item[0])
print("Output #120 (order by keys): {}".format(ordered_dict1))
ordered_dict2 = sorted(dict_copy.items(), key=lambda item: item[1])
print("Output #121 (order by values): {}".format(ordered_dict2))
ordered_dict3 = sorted(dict_copy.items(), key=lambda x: x[1], reverse=True)
print("Output #122 (order by values, descending): {}".format(ordered_dict3))
ordered_dict4 = sorted(dict_copy.items(), key=lambda x: x[1], reverse=False)
print("Output #123 (order by values, ascending): {}".format(ordered_dict4))
```

    Output #119: {'one': 1, 'two': 2, 'three': 3}
    Output #120 (order by keys): [('one', 1), ('three', 3), ('two', 2)]
    Output #121 (order by values): [('one', 1), ('two', 2), ('three', 3)]
    Output #122 (order by values, descending): [('three', 3), ('two', 2), ('one', 1)]
    Output #123 (order by values, ascending): [('one', 1), ('two', 2), ('three', 3)]


### 1.4.8 Control Flow


```python
# CONTROL FLOW
# if-else statement
x = 5
if x > 4 or x != 9:
    print("Output #124: {}".format(x))
else:
    print("Output #125: x is not greater than 4")
```

    Output #124: 5



```python
# if-elif-else statement
if x > 6:
    print("Output #126: x is greater than six")
elif x > 4 and x == 5:
    print("Output #127: {}".format(x*x))
else:
    print("Output #128: x is not greater than 4")

```

    Output #127: 25



```python
# for loop
y = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', \
'Nov', 'Dec']
z = ['Annie', 'Betty', 'Claire', 'Daphne', 'Ellie', 'Franchesca', 'Greta', \
'Holly', 'Isabel', 'Jenny']
```


```python
print("Output #129:")
for month in y:
    print("{!s}".format(month))
```

    Output #129:
    Jan
    Feb
    Mar
    Apr
    May
    Jun
    Jul
    Aug
    Sep
    Oct
    Nov
    Dec



```python
print("Output #130: (index value: name in list)")
for i in range(len(z)):
    print("{0!s}: {1:s}".format(i, z[i]))
```

    Output #130: (index value: name in list)
    0: Annie
    1: Betty
    2: Claire
    3: Daphne
    4: Ellie
    5: Franchesca
    6: Greta
    7: Holly
    8: Isabel
    9: Jenny



```python
print("Output #131: (access elements in y with z's index values)")
for j in range(len(z)):
    if y[j].startswith('J'):
        print("{!s}".format(y[j]))
```

    Output #131: (access elements in y with z's index values)
    Jan
    Jun
    Jul



```python
print("Output #132:")
for key, value in another_dict.items():
    print("{0:s}, {1}".format(key, value))
```

    Output #132:
    x, printer
    y, 5
    z, ['star', 'circle', 9]



```python
# compact for loops
# list, set, and dictionary comprehensions
# Select specific rows using a list comprehension
my_data = [[1,2,3], [4,5,6], [7,8,9]]
rows_to_keep = [row for row in my_data if row[2] > 5]
print("Output #133 (list comprehension): {}".format(rows_to_keep))
```

    Output #133 (list comprehension): [[4, 5, 6], [7, 8, 9]]



```python
# Select a set of unique tuples in a list using a set comprehension
my_data = [(1,2,3), (4,5,6), (7,8,9), (7,8,9)]
set_of_tuples1 = {x for x in my_data}
print("Output #134 (set comprehension): {}".format(set_of_tuples1))
set_of_tuples2 = set(my_data)
print("Output #135 (set function): {}".format(set_of_tuples2))
```

    Output #134 (set comprehension): {(4, 5, 6), (7, 8, 9), (1, 2, 3)}
    Output #135 (set function): {(4, 5, 6), (7, 8, 9), (1, 2, 3)}



```python
# Select specific key-value pairs using a dictionary comprehension
my_dictionary = {'customer1': 7, 'customer2': 9, 'customer3': 11}
my_results = {key : value for key, value in my_dictionary.items() if \
value > 10}
print("Output #136 (dictionary comprehension): {}".format(my_results))
```

    Output #136 (dictionary comprehension): {'customer3': 11}



```python
# while loop
print("Output #137:")
x = 0
while x < 11:
    print("{!s}".format(x))
    x += 1
```

    Output #137:
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10



```python
# FUNCTIONS
# Calculate the mean of a sequence of numeric values
def getMean(numericValues):
    return sum(numericValues)/len(numericValues) if len(numericValues) > 0 \
    else float('nan')
```


```python
my_list = [2, 2, 4, 4, 6, 6, 8, 8]
print("Output #138 (mean): {!s}".format(getMean(my_list)))
```

    Output #138 (mean): 5.0



```python
#import numpy as np
#print np.mean(my_list)
```


```python
# EXCEPTIONS
# Calculate the mean of a sequence of numeric values
def getMean(numericValues):
    return sum(numericValues)/len(numericValues)
```


```python
my_list2 = [ ]
# Short version
try:
    print("Output #139: {}".format(getMean(my_list2)))
except ZeroDivisionError as detail:
    print("Output #139 (Error): {}".format(float('nan')))
    print("Output #139 (Error): {}".format(detail))
```

    Output #139 (Error): nan
    Output #139 (Error): division by zero



```python
# Long version
try:
    result = getMean(my_list2)
except ZeroDivisionError as detail:
    print("Output #140 (Error): {}".format(float('nan')))
    print("Output #140 (Error): {}".format(detail))
else:
    print("Output #140 (The mean is): {}".format(result))
finally:
    print("Output #140 (Finally): The finally block is executed every time")
```

    Output #140 (Error): nan
    Output #140 (Error): division by zero
    Output #140 (Finally): The finally block is executed every time


## 1.5 Reading a Text File


```python
#!/usr/bin/env python3
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys
```

### 1.5.1 建立文字檔

### 1.5.2 將腳本與輸入檔案放在同一個地方

### 1.5.3 現代檔案讀取語法


```python
# READ A FILE
# Read a single text file
input_file = sys.argv[1]

## Read a text file (older method) ##
print("Output #141:")
filereader = open(input_file, 'r', newline='')
for row in filereader:
    print("{}".format(row.strip()))
filereader.close()
```


```python
## Read a text file (newer method) ##
#print("Output #142:")
#with open(input_file, 'r', newline='') as filereader:
#    for row in filereader:
#        print("{}".format(row.strip()))

#print("Output #143:")
# READ MULTIPLE FILES
# Read multiple text files
#inputPath = sys.argv[1]
#for input_file in glob.glob(os.path.join(inputPath,'*.txt')):
#    with open(input_file, 'r', newline='') as filereader:
#       for row in filereader:
#           print("{}".format(row.strip()))
```

## 1.6 Reading Multiple Text Files with glob

### 1.6.1 建立另一個文字檔


```python
#讀取多個文字檔
print("Output #145:")
inputPath = sys.argv[1]
for input_file in glob.glob(os.path.join(inputPath, '*.txt')):
    with open(input_file, 'r', newline='') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))
```

    Output #145:


## 1.7 Writing to a Text File

### 1.7.1 在first script.py裡面加入程式


```python
# WRITE TO A FILE
# Write to a text file
my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
max_index = len(my_letters)
output_file = sys.argv[1]
filewriter = open(output_file, 'w')
for index_value in range(len(my_letters)):
    if index_value < (max_index-1):
        filewriter.write(my_letters[index_value]+'\t')
    else:
        filewriter.write(my_letters[index_value]+'\n')
filewriter.close()
print("Output #144: Output written to file")
```

    Output #144: Output written to file


### 1.7.2 寫至一個以逗號分隔值(CSV)的檔案


```python
# Write to a CSV file
my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
max_index = len(my_numbers)
output_file = sys.argv[1]
filewriter = open(output_file, 'a')
for index_value in range(len(my_numbers)):
    if index_value < (max_index-1):
        filewriter.write(str(my_numbers[index_value])+',')
    else:
        filewriter.write(str(my_numbers[index_value])+'\n')
filewriter.close()
print("Output #145: Output appended to file")
```

    Output #145: Output appended to file


## 1.8 print Statements

## 1.9 Chapter Exercises
