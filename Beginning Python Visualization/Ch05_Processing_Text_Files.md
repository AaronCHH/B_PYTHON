
# Chapter 5: Processing Text Files
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 5: Processing Text Files](#chapter-5-processing-text-files)
  * [5.1 Text Is Everywhere](#51-text-is-everywhere)
  * [5.2 Text and Strings](#52-text-and-strings)
    * [5.2.1 Splitting Text](#521-splitting-text)
    * [5.2.2 Joining Strings](#522-joining-strings)
    * [5.2.3 Converting Strings to Numbers](#523-converting-strings-to-numbers)
    * [5.2.4 Find and Replace](#524-find-and-replace)
    * [5.2.5 Stripping Strings](#525-stripping-strings)
    * [5.2.6 String Formatting](#526-string-formatting)
    * [5.2.7 String Conditionals](#527-string-conditionals)
    * [5.2.8 More on Strings](#528-more-on-strings)
  * [5.3 Files](#53-files)
    * [5.3.1 Opening a File](#531-opening-a-file)
    * [5.3.2 Closing a File](#532-closing-a-file)
    * [5.3.3 Writing Text](#533-writing-text)
    * [5.3.4 Reading Text](#534-reading-text)
  * [5.4 Working with Text Files](#54-working-with-text-files)
    * [5.4.1 Example: Character, Word, and Line Count](#541-example-character-word-and-line-count)
    * [5.4.2 Example: head and tail](#542-example-head-and-tail)
    * [5.4.3 Example: Splitting and Combining Files](#543-example-splitting-and-combining-files)
    * [5.4.4 Example: Searching Inside a Text File](#544-example-searching-inside-a-text-file)
    * [5.4.5 Example: Working with Comments](#545-example-working-with-comments)
    * [5.4.6 Example: Extracting Numbers from a Text File](#546-example-extracting-numbers-from-a-text-file)
  * [5.5 CSV Files](#55-csv-files)
    * [5.5.1 The csv Module](#551-the-csv-module)
    * [5.5.2 The csv.reader Object](#552-the-csvreader-object)
    * [5.5.3 The csv.writer Object](#553-the-csvwriter-object)
    * [5.5.4 More CSV Functionality](#554-more-csv-functionality)
    * [5.5.5 DictReader and DictWriter Objects](#555-dictreader-and-dictwriter-objects)
  * [5.6 Date and Time](#56-date-and-time)
    * [5.6.1 Time Module](#561-time-module)
    * [5.6.2 The struct_time Tuple](#562-the-struct_time-tuple)
    * [5.6.3 Parsing and Formatting Date and Time](#563-parsing-and-formatting-date-and-time)
    * [5.6.4 The Epoch: “Linearizing” the Time Base](#564-the-epoch-linearizing-the-time-base)
    * [5.6.5 Additional Time and Date Functions](#565-additional-time-and-date-functions)
  * [5.7 Regular Expressions](#57-regular-expressions)
    * [5.7.1 Regular Expression Patterns](#571-regular-expression-patterns)
    * [5.7.2 Special Sequences](#572-special-sequences)
    * [5.7.3 Alternatives](#573-alternatives)
    * [5.7.4 Ranges](#574-ranges)
    * [5.7.5 When to Use Regular Expressions](#575-when-to-use-regular-expressions)
  * [5.8 Internationalization and Localization](#58-internationalization-and-localization)
    * [5.8.1 Locale](#581-locale)
    * [5.8.2 Unicode Strings](#582-unicode-strings)
  * [5.9 Final Notes and References](#59-final-notes-and-references)

<!-- tocstop -->


## 5.1 Text Is Everywhere
## 5.2 Text and Strings
### 5.2.1 Splitting Text


```python
"split second".split()
```




    ['split', 'second']




```python
grocery_list = """Milk 2
Eggs 12"""
print(grocery_list)
```

    Milk 2
    Eggs 12



```python
grocery_list.split()
```




    ['Milk', '2', 'Eggs', '12']




```python
grocery_list = """Milk 2
Eggs 12"""
grocery_list.split('ilk')
```




    ['M', ' 2\nEggs 12']




```python
grocery_list = """Milk 2
Eggs 12"""
grocery_list.splitlines()
```




    ['Milk 2', 'Eggs 12']




```python
grocery_list.splitlines(True)
```




    ['Milk 2\n', 'Eggs 12']



* Example: Counting the Number of Words and Number of Lines in a String


```python
def word_line_count(s):
    """Returns the number of words and the numbers of lines in a string."""
    return (len(s.split()), len(s.splitlines()))
```


```python
grocery_list = """Milk 2
Eggs 12"""
word_line_count(grocery_list)
```

### 5.2.2 Joining Strings


```python
SOS = ['...', '---', '...']
"".join(SOS)
```

### 5.2.3 Converting Strings to Numbers


```python
float('3.25')
```


```python
int('100')
```


```python
float('split')
```


```python
for item in grocery_list.split():
    try:
        print(int(item))
    except ValueError:
        pass
```

* Example: Base Conversion—Binary, Octal, Decimal, and Hexadecimal


```python
# %load 0053-7-src-Ch05/src/base_conversion.py
# base conversion helper functions
def bin2dec(s):
    return str(int(s, 2))
def oct2dec(s):
    return str(int(s, 8))
def hex2dec(s):
    return str(int(s, 16))

def dec2hex(s):
    return hex(int(s))
def dec2oct(s):
    return oct(int(s))
def dec2bin(s):
    return bin(int(s))

def hex2oct(s):
    return dec2oct(hex2dec(s))
def hex2bin(s):
    return dec2bin(hex2dec(s))

def oct2hex(s):
    return dec2hex(oct2dec(s))
def bin2hex(s):
    return dec2hex(bin2dec(s))

def oct2bin(s):
    return dec2bin(oct2dec(s))
def bin2oct(s):
    return dec2oct(bin2dec(s))

```


```python
hex2dec('0xffff')
```


```python
oct2hex('0o777')
```

* Testing Your Implementation: exec and assert


```python
assert 1 == 2
```


```python
exec("print(1+2)")
```

    3



```python
from base_conversion import *
def testbases():
    """Tests implementation of base conversion functions"""
    v0 = { 'bin':'0b0', 'oct':'0o0', 'dec':'0', 'hex':'0x0' }
    v1 = { 'bin':'0b1111', 'oct':'0o17', 'dec':'15', 'hex':'0xf' }
    for v in [v0, v1]:
        perms = [ (a, b) for b in v for a in v if a != b ]
        for (s1, s2) in perms:
            tc = "assert %s2%s(v['%s']) == v['%s']" % (s1, s2, s1, s2)
            exec(tc)
    print('All tests passed')
```


```python
v = { 'bin':'0', 'oct':'0', 'dec':'0', 'hex':'0x0' }
perms = [ (a, b) for b in v for a in v if a != b ]
from pprint import pprint
pprint(perms)
```

    [('oct', 'bin'),
     ('dec', 'bin'),
     ('hex', 'bin'),
     ('bin', 'oct'),
     ('dec', 'oct'),
     ('hex', 'oct'),
     ('bin', 'dec'),
     ('oct', 'dec'),
     ('hex', 'dec'),
     ('bin', 'hex'),
     ('oct', 'hex'),
     ('dec', 'hex')]


> __perMUtatIONS__
The module itertools provides functions for creating iterators (see https://docs.python.org/3.3/library/itertools.html).
Specifically, itertools provides combinatorics generators, including the generator permutations().
Instead of implementing all the permutations using a list comprehension as shown in the example, it’s possible to use permutations() like this: permutations(['bin', 'hex', 'dec', 'oct'], 2).
Notice that the result is an iterator; to view the entire list, you’ll have to generate an actual list from the iterator: list(permutations(['bin', 'hex', 'dec', 'oct'], 2)).
The value 2 in the function call tells permutations() to return a tuple of size 2.
The module itertools provide additional useful generators (e.g., combinations() for all possible combinations and product(), which is equivalent to a nested loop).




```python
for (s1, s2) in perms:
    tc = "assert %s2%s(v['%s']) == v['%s']" % \
        (s1, s2, s1, s2)
    print(tc)
```

    assert oct2bin(v['oct']) == v['bin']
    assert dec2bin(v['dec']) == v['bin']
    assert hex2bin(v['hex']) == v['bin']
    assert bin2oct(v['bin']) == v['oct']
    assert dec2oct(v['dec']) == v['oct']
    assert hex2oct(v['hex']) == v['oct']
    assert bin2dec(v['bin']) == v['dec']
    assert oct2dec(v['oct']) == v['dec']
    assert hex2dec(v['hex']) == v['dec']
    assert bin2hex(v['bin']) == v['hex']
    assert oct2hex(v['oct']) == v['hex']
    assert dec2hex(v['dec']) == v['hex']


### 5.2.4 Find and Replace


```python
grocery_list = "Milk 2\nEggs 12"
grocery_list.find('2')
```




    5




```python
grocery_list.find('2', 10)
```




    13




```python
grocery_list.find('2', 10, 16)
```




    13




```python
grocery_list = "Milk 2\nEggs 12"
grocery_list.replace('Eggs', 'Organic Eggs')
```




    'Milk 2\nOrganic Eggs 12'




```python
grocery_list = "Milk 2\nEggs 12"
grocery_list.count('2')
```




    2




```python
grocery_list.count('Eggs')
```




    1



### 5.2.5 Stripping Strings


```python
"Hello ".rstrip()
```




    'Hello'




```python
'*-*-* SECTION BREAK *-*-*'.strip('*-')
```




    ' SECTION BREAK '



* Example: Removing Extra Spaces


```python
grocery_list = "Milk 2\nEggs 12"
new_grocery_list = grocery_list.replace(" ", " ")
print(new_grocery_list)
```

    Milk 2
    Eggs 12



```python
grocery_list = "Milk 2\nEggs 12"
for line in grocery_list.splitlines():
    clear_line = [s.strip() for s in line.split()]
    print(" ".join(clear_line))
```

    Milk 2
    Eggs 12


### 5.2.6 String Formatting


```python
" Middle of Town ".upper()
```




    ' MIDDLE OF TOWN '




```python
" Middle of Town ".lower()
```




    ' middle of town '




```python
" Middle of Town ".swapcase()
```




    ' mIDDLE OF tOWN '




```python
"first sentence.\nSecond sentence. Third Sentence".capitalize()
```




    'First sentence.\nsecond sentence. third sentence'




```python
"first sentence.\nSecond sentence. Third Sentence".title()
```




    'First Sentence.\nSecond Sentence. Third Sentence'




```python
" Middle of Town ".center(26, '*')
```




    '***** Middle of Town *****'




```python
"East side".rjust(20)
```




    '           East side'




```python
"West side".ljust(20, '-')
```




    'West side-----------'



### 5.2.7 String Conditionals


```python
"a20.jpg".endswith('jpg')
```




    True




```python
"a20.jpg".endswith('JPG')
```




    False




```python
"a20.JPG".endswith(('jpg', 'JPG'))
```




    True




```python
"a20.jpg".isalnum()
```




    False




```python
"a20.jpg".islower()
```




    True



### 5.2.8 More on Strings

https://docs.python.org/3.3/library/string.html

## 5.3 Files

### 5.3.1 Opening a File

| Mode  | Description                                                                                         |
|-------|-----------------------------------------------------------------------------------------------------|
| r     | Opens a file for reading. This is the default value if mode isn’t specified.                        |
| w     | Opens a file for writing, overwriting an existing file.                                             |
| a     | Opens a file for writing in append mode; all write operations are performed at the end.             |
|       | If the file doesn’t exist, it is created.                                                           |
| x     | Create a new file, and open it for reading.                                                         |
| r+    | Opens a file for reading and updating.                                                              |
|       | If the file doesn’t exist, an exception is raised.                                                  |
| w+    | Creates a new file for writing and updating, overwriting an existing one.                           |
| a+    | Opens a file for reading and writing in append mode. All write operations are performed at the end. |
|       | If the file doesn’t exist, it is created.                                                           |

### 5.3.2 Closing a File


```python
f = open('somefile.txt', 'wt')
f
```


```python
f.close()
type(f)
```

### 5.3.3 Writing Text


```python
grocery_str = "Milk 2\nEggs 12"
f = open('../data/tobuy.txt', 'wt')
f.write(grocery_str)
f.close()
```


```python
grocery_list = ["Milk", "2", "Eggs", "12"]
f = open('../data/tobuylist.txt', 'wt')
f.writelines(grocery_list)
f.close()
```

### 5.3.4 Reading Text

* Reading the Entire File at Once


```python
f = open('../data/tobuy.txt')
text = f.read()
f.close()
print(text)
```


```python
print(open('../data/tobuy.txt').read())
```


```python
open('../data/tobuy.txt').readlines()
```

* Iterating Over the File Object


```python
for i, line in enumerate(open('../data/tobuy.txt')):
    print("%d: %s" % (i, line.rstrip()))
```

* Using a while Loop


```python
f = open('../data/tobuy.txt')
ch = f.read(1)
while ch != 'k' and ch:
    print(ch)
    ch = f.read(1)
```


```python
f.close()
```

## 5.4 Working with Text Files

### 5.4.1 Example: Character, Word, and Line Count


```python
def wc(filename):
    """Returns the number of characters, words and lines in a file.
The result is a tuple of the form (#characters, #words, #lines)."""
    data = open(filename, 'rb').read()
    return (len(data), len(data.split()), len(data.splitlines()))
```


```python
def wc_large(filename):
    """Returns the number of characters, words and lines in a large file.
The result is a tuple of the form (#characters, #words, #lines)."""
    num_chars, num_words, num_lines = 0, 0, 0
    for line in open(filename, encoding='latin-1'):
        num_chars += len(line)
        num_words += len(line.split())
        num_lines += 1
    return (num_chars, num_words, num_lines)
```


```python
wc('../data/45506-8.txt')
```


```python
wc_large('../data/45506-8.txt')
```

### 5.4.2 Example: head and tail


```python
def head(filename, n=10):
    """Prints the first n lines of the file."""
    for line in open(filename, encoding='latin-1').readlines()[:n]:
        print(line.rstrip())
```


```python
def tail(filename, n=10):
    """Returns the last n lines of the file."""
    for line in open(filename, encoding='latin-1').readlines()[-n:]:
        print(line.rstrip())
```


```python
def head_large(filename, n=10):
    """Returns the first n lines of a very large file."""
    for i, line in enumerate(open(filename, encoding='latin-1')):
        print(line.rstrip())
        if i == n-1: break
```

### 5.4.3 Example: Splitting and Combining Files


```python
def splitfile(filename, size=1024**2):
    """Splits a file into n smaller files.
Files are created with a running index."""
    fin, index = open(filename, 'rb'), 0
    data = fin.read(size)
    while data:
        index += 1
        outfilename = filename+'.'+str(index)
        fout = open(outfilename, 'wb')
        fout.write(data)
        fout.close()
        print("Created file %s, size %d" % (outfilename, len(data)))
        data = fin.read(size)
    return

def combinefiles(filename):
    """Combines a previously split file.
Filename extensions are assumed a running index.
Important note: if a file named filename exists it will be overwritten."""
    fout, index = open(filename, 'wb'), 0
    while True:
        index += 1
        try:
            data = open(filename+'.'+str(index), 'rb').read()
            fout.write(data)
        except IOError:
            break
    fout.close()
    print("Created file %s from %d file(s)" % (filename, index-1))
```


```python
splitfile('../data/45506-8.txt', 100000)
```


```python
import os
src = '../data/45506-8.txt.%d'
dest = '../data/tmp/45506-8.txt.%d'
for i in range(1, 4):
    os.renames(src % i, dest % i)
os.listdir('../data/tmp')
```


```python
combinefiles('../data/tmp/45506-8.txt')
```


```python
data1 = open('../data/45506-8.txt', 'rb').read()
data2 = open('../data/tmp/45506-8.txt', 'rb').read()
data1 == data2
```

### 5.4.4 Example: Searching Inside a Text File


```python
def srchfile(filename, substr):
    """Searches for a substring in a file."""
    for index, line in enumerate(open(filename, encoding='latin-1')):
        if line.find(substr) != -1:
            try:
                print("%4d:%s" % (index, line.rstrip()))
            except UnicodeEncodeError:
                print("%4d: ---encoding error---" % index)
```


```python
numlines = 1234
from math import log10
maxdigits = int(log10(numlines))+1
maxdigits
```


```python
def srchfile_ex(filename, substr):
    """Searches for a substring in a file."""
    lines = open(filename, encoding='latin-1').readlines()
    fmt = r'%' + str(int(log10(len(lines)))+1) + r'd:%s'
    for index, line in enumerate(lines):
        if line.find(substr) != -1:
            try:
                print(fmt % (index, line.rstrip()))
            except UnicodeEncodeError:
                print("%d: --- encoding error ---" % index)
```

### 5.4.5 Example: Working with Comments


```python
def srchcomments(filename, substr):
    """Searches inside Python source comments."""
    for index, line in enumerate(open(filename, 'rt')):
        L = line.split('#')
        if len(L) == 2:
            if L[1].find(substr) != -1:
                print("%5d: %s" % (index, line.rstrip()))
```

### 5.4.6 Example: Extracting Numbers from a Text File


```python
def increment_contents(filename):
    """Increments values in a file, creating a new file."""
    data = open(filename).readlines()
    for i, line in enumerate(data):
        for word in line.split():
            try:
                data[i] = line.replace(word, str(int(word)+1))
            except ValueError:
                # uncomment the following if you'd like feedback
                # print(word, " is not a number")
                pass
    open(filename+'.inc', 'wt').writelines(data)
```


```python
def increment_contents_both(filename):
    """Increments values in a file, creating a new file.
    Works with both ints and floats."""
    data = open(filename, 'rt').readlines()
    for i, line in enumerate(data):
        for word in line.split():
            try:
                data[i] = line.replace(word, str(int(word)+1))
            except ValueError:
                try:
                    data[i] = line.replace(word, str(float(word)+1))
                except ValueError:
                    # uncomment the following if you'd like feedback
                    # print(word, "is not a number")
                    pass
    open(filename+'.inc', 'wt').writelines(data)
```

## 5.5 CSV Files

### 5.5.1 The csv Module


```python
L = open('../data/sometext.csv').read().split(',')
from pprint import pprint
pprint(L)
```


```python
f = open('../data/sometext.csv')
for line in csv.reader(f, skipinitialspace=True):
    print(line)
```

### 5.5.2 The csv.reader Object

### 5.5.3 The csv.writer Object


```python
lines = [["1/1/2000", "Some text, and a comma"]]
csv.writer(open('../data/outtext.csv', 'w')).writerows(lines)
```

### 5.5.4 More CSV Functionality


```python
for line in csv.reader(open('../data/sometext.csv'), delimiter='/'):
    print(line)
```


```python
lines = [["1/1/2000", "Some text, and a comma"]]
f = open('../data/outtext.csv', 'w')
csv.writer(f, quotechar='|').writerows(lines)
f.close()
```


```python
lines = [["1/1/2000", "Some text, and a comma"]]
f = open('../data/outtext.csv', 'w')
cw = csv.writer(f, quoting=csv.QUOTE_NONE, escapechar='~')
cw.writerows(lines)
f.close()
```

### 5.5.5 DictReader and DictWriter Objects


```python
import csv
fcsv = open('../data/tobuy.csv')
for row in csv.DictReader(fcsv):
    print("Please buy", row['Count'], row['Item'])
```


```python
header = ['Item', 'Count']
rows = [['Organic Eggs', 5], ['Cucumbers', 12 ]]
fcsv = open('../data/tobuy_more.csv', 'w', newline='')
dict_wr = csv.DictWriter(fcsv, header)
dict_wr.writeheader()
for row in rows:
    dict_wr.writerow(dict(zip(header, row)))
fcsv.close()
```


```python
header = ['Item', 'Count']
rows = [['Organic Eggs', 5], ['Cucumbers', 12]]
for row in rows:
    print(list(zip(header, row)))
```


```python
for row in rows:
    dict_wr.writerow(dict(zip(header, row)))
```

## 5.6 Date and Time

http://gnosis.cx/TPiP

### 5.6.1 Time Module

### 5.6.2 The struct_time Tuple


```python
from time import localtime
localtime()
```




    time.struct_time(tm_year=2017, tm_mon=4, tm_mday=22, tm_hour=21, tm_min=46, tm_sec=21, tm_wday=5, tm_yday=112, tm_isdst=0)




```python
localtime().tm_year
```




    2017




```python
localtime().tm_yday
```




    112



### 5.6.3 Parsing and Formatting Date and Time

| Identifier | Description                                                                            | Values Range                              |
|------------|----------------------------------------------------------------------------------------|-------------------------------|
| %Y         | Year with century as a decimal number                                                  |                               |
| %m         | Month as a decimal number                                                              | 1–12                          |
| %d         | Day of the month as a decimal number                                                   | 1–31                          |
| %H         | Hour as a decimal number                                                               | 0–23                          |
| %M         | Minute as a decimal number                                                             | 0-59                          |
| %S         | Second as a decimal number                                                             | 00-61 (61 for leap seconds)   |
| %w         | Weekday as a decimal number                                                            | 0–6 (where 0 is Sunday)       |
| %j         | Day of the year as a decimal number                                                    | 001-366 (366 for leap years)  |
| %z         | Time zone field. DST doesn’t have an identifier of its own and is part of this field.  |                               |
| %a, %A     | Locale’s weekday name, abbreviated and full                                            |                               |
| %b, %B     | Locale’s month name, abbreviated and full                                              |                               |

https://docs.python.org/3.3/library/time.html.

* Example: Logging Information with a Date and Timestamp


```python
from time import localtime, strftime
strftime("%Y-%m-%dT%H-%M-%S", localtime())
```


```python
from time import asctime
asctime(localtime())
```


```python
from time import strftime, gmtime
strftime('%d-%b-%Y %H:%M:%S', gmtime())
```


```python
from time import strftime, gmtime, sleep
time_str = strftime("%Y-%m-%dT%H-%M-%S", gmtime())
flog = open("../data/LogExample%s.txt" % time_str, 'wt')
for i in range(5):
    sleep(1.7)
    logline = "%s | Some data %d\n" % \
        (strftime('%d-%b-%Y %H:%M:%S', gmtime()), i)
    flog.write(logline)
flog.close()
```

https://docs.python.org/3.3/library/logging.html

* Example: Extracting Date and Time Information from File Contents


```python
from time import strptime
log1 = '06/21/2008 21:57:20: Some text'
time1 = strptime(log1[:19], '%m/%d/%Y %H:%M:%S')
asctime(time1)
```




    'Sat Jun 21 21:57:20 2008'




```python
from time import asctime, strptime
log2 = '2008-10-21\t20:37:26 Some text'
print(log2)
```

    2008-10-21	20:37:26 Some text



```python
time2 = strptime(log2[:19], '%Y-%m-%d\t%H:%M:%S')
asctime(time2)
```




    'Tue Oct 21 20:37:26 2008'



### 5.6.4 The Epoch: “Linearizing” the Time Base


```python
from time import asctime, gmtime
asctime(gmtime(0))
```




    'Thu Jan  1 00:00:00 1970'




```python
vals = ['140055.00', '140156.00']
[float(x[:2])*3600+float(x[2:4])*60+float(x[4:6]) for x in vals]
```




    [50455.0, 50516.0]




```python
_[1]-_[0]
```




    61.0




```python
from time import mktime
[mktime((2000, 0, 0, int(x[:2]), int(x[2:4]), int(x[4:6]), \
         0, 0, 0)) for x in vals]
```




    [943941655.0, 943941716.0]




```python
_[1]-_[0]
```




    61.0



https://docs.python.org/3.3/library/datetime.html

* Example: End-of-Day Report


```python
# end-of-day report
from time import mktime, strptime, ctime
import csv
d = {}
for row in csv.reader(open('../data/SystemALogs.txt')):
    # t is a struct_time tuple
    t = strptime(row[0], '%a %b %d %H:%M:%S %Y')
    # calculate seconds since the epoch
    t_epoch = mktime(t)
    # construct a key and value
    key = (t.tm_year, t.tm_yday)
    val = (t_epoch, row[1])
    try:
        # do we have a more recent entry?
        if d[key][0] < t_epoch:
        d[key] = val
    except KeyError:
        # current date is not in dictionary
        d[key] = val
for epoch, line in d.values():
    print(ctime(epoch), line)
```

* Example: Combining Data from Several Sources Based on the Epoch


```python
from time import mktime, strptime
data = []
data1 = open('../data/SystemBLogs.txt').readlines()
data2 = open('../data/SystemCLogs.txt').readlines()
fmt = '%b %d %H:%M:%S %Y'

for line in data1+data2:
    # t is a struct_time tuple
    t = strptime(line[4:24], fmt)
    # calculate seconds since the epoch
    t_epoch = mktime(t)
    # append data
    data.append([t_epoch, line])

data = [line[1] for line in sorted(data)]
open('../data/SystemsBCLogs.txt', 'wt').writelines(data)
```

### 5.6.5 Additional Time and Date Functions

We’ve covered most of the functionality available in the time module.
For most of your log file processing needs and other time-based processing requirements, the module is comprehensive and complete.
There are additional time- and date-related modules available in Python.
The datetime module (https://docs.python.org/3.3/library/datetime.html) provides functionality that includes operations on dates using a more object-oriented approach.
The calendar module (https://docs.python.org/3.3/library/calendar.html) provides general calendar-related operations.
Refer to the Python standard library for additional information.



## 5.7 Regular Expressions

### 5.7.1 Regular Expression Patterns


```python
import re
re.split(r'a', 'Flatland')
```




    ['Fl', 'tl', 'nd']




```python
re.split(r'txt', '45506-8.txt')
```




    ['45506-8.', '']




```python
re.findall(r'.?a', 'Flatland')
```




    ['la', 'la']




```python
re.findall(r'a.*', 'Flatland')
```




    ['atland']




```python
re.findall(r'^.*a', 'Flatland')
```




    ['Flatla']




```python
re.findall(r'^.*?a', 'Flatland')
```




    ['Fla']




```python
re.findall(r'a.*$', 'Flatland')
```




    ['atland']



* Example: Removing Extra Spaces with Regular Expressions


```python
grocery_list = "Milk 2\nEggs 12"
re.sub(r' +', ' ', grocery_list)
```

### 5.7.2 Special Sequences


```python
grocery_list = "Milk 2\nEggs 12"
re.findall(r'\d+', grocery_list)
```

### 5.7.3 Alternatives


```python
grocery_list = "Milk 2\nEggs 12"
re.sub(r'Milk|Eggs', 'Chocolate', grocery_list)
```

### 5.7.4 Ranges


```python
grocery_list = "Milk 2\nEggs 12"
re.sub('[12]', '0', grocery_list)
```


```python
grocery_list = "Milk 2\nEggs 12"
re.sub('[^0-5]', '*', grocery_list)
```

### 5.7.5 When to Use Regular Expressions

* Example: Words Used Only Once


```python
def nonce(filename):
    """Returns words used only once in a file."""
    data = open(filename, 'rt').read()
    d, result = dict(), []
    for word in re.split('['+punctuation+whitespace+']', data):
        d[word.lower()] = d.get(word.lower(), 0)+1
    for word, occur in d.iteritems():
        if occur == 1:
            result.append(word)
    return result
```

## 5.8 Internationalization and Localization

### 5.8.1 Locale


```python
import locale
locale.setlocale(locale.LC_ALL, 'french')
```




    'French_France.1252'




```python
from time import gmtime, strftime, strptime
fmt = '%d-%B-%Y'
strftime(fmt, localtime())
```




    '22-avril-2017'




```python
strptime(_, fmt)
```




    time.struct_time(tm_year=2017, tm_mon=4, tm_mday=22, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=112, tm_isdst=-1)



https://docs.python.org/3.3/library/locale.html.

### 5.8.2 Unicode Strings

http://www.unicode.org


```python
"X".encode('utf-8')
```




    b'X'




```python
"X".encode('utf-16')
```




    b'\xff\xfeX\x00'



* Working with Unicode


```python
u = 'a string\xa9'
u
```




    'a string©'




```python
open('../data/special1.txt', 'wb').write(u.encode('utf-8'))
```


```python
open('../data/special2.txt', 'w', encoding='utf-8').write(u)
```


```python
u.encode('utf-8')
```




    b'a string\xc2\xa9'




```python
u.encode('utf-16')
```




    b'\xff\xfea\x00 \x00s\x00t\x00r\x00i\x00n\x00g\x00\xa9\x00'




```python
u.encode('utf-16').decode('utf-16')
```




    'a string©'



* Example: The Hebrew Alphabet


```python
letters = [chr(letter) for letter in range(0x5d0, 0x5eb)]
alephbet = ''.join(letters)
open('../data/alephbet.txt', 'w', encoding='utf-8').write(alephbet)
```


```python
letters = [chr(letter) for letter in range(0xc0, 0x100)]
latin = ''.join(letters)
open('../data/latin.txt', 'w', encoding='utf-8').write(latin)
```

* Example: Writing Today’s Date in the Current Locale


```python
import locale
from time import strftime, strptime, localtime
from sys import platform
if platform == 'linux' or platform == 'darwin':
    locale.setlocale(locale.LC_ALL, 'he_IL')
elif platform == 'win32':
    locale.setlocale(locale.LC_ALL, 'Hebrew_Israel')
elif platform == 'cygwin':
    raise Exception('Cygwin not supported')
else:
    print("Untested platform: ", platform)
today = strftime('%B %d, %Y', localtime())
open('../data/today.txt', 'w', encoding='utf-8').write(today)
```

* More on Unicode

* The Unicode Consortium: http://www.unicode.org.
* Wikipedia: http://en.wikipedia.org/wiki/Locale. Be sure to follow the links to topics such as character encoding and Unicode.
* International Components for Unicode: http://www.icu-project.org/.

## 5.9 Final Notes and References
