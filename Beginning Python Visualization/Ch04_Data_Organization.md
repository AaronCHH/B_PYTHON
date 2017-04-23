
# Chapter 4: Data Organization
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 4: Data Organization](#chapter-4-data-organization)
  * [4.1 Organizing Chaos](#41-organizing-chaos)
  * [4.2 File Name Conventions](#42-file-name-conventions)
    * [4.2.1 Date and Time in a File Name](#421-date-and-time-in-a-file-name)
    * [4.2.2 Useful File Name Titles](#422-useful-file-name-titles)
    * [4.2.3 File Name Extensions](#423-file-name-extensions)
    * [4.2.4 File Name Convention Recap](#424-file-name-convention-recap)
    * [4.2.5 Other Schemes](#425-other-schemes)
  * [4.3 File Formats](#43-file-formats)
    * [4.3.1 CSV File Format](#431-csv-file-format)
    * [4.3.2 Binary Files](#432-binary-files)
    * [4.3.3 Readme Files](#433-readme-files)
    * [4.3.4 INI Files](#434-ini-files)
    * [4.3.5 XML and Other Formats](#435-xml-and-other-formats)
  * [4.4 Locating Data Files](#44-locating-data-files)
    * [4.4.1 Organization into Directories](#441-organization-into-directories)
    * [4.4.2 Searching for Files](#442-searching-for-files)
    * [4.4.3 Indexing](#443-indexing)
    * [4.4.4 Catalogs](#444-catalogs)
    * [Files vs. a Database](#files-vs-a-database)
  * [4.5 Final Notes and References](#45-final-notes-and-references)

<!-- tocstop -->


## 4.1 Organizing Chaos

## 4.2 File Name Conventions

### 4.2.1 Date and Time in a File Name


```python
a_date = "2014-05-05-22-17-14"
a_date.split('-')
```




    ['2014', '05', '05', '22', '17', '14']




```python
int("2014-05-05-22-17-14".split('-')[1])
```




    5




```python
from time import strptime
strptime("2014-04-12T09-29-22", "%Y-%m-%dT%H-%M-%S")
```




    time.struct_time(tm_year=2014, tm_mon=4, tm_mday=12, tm_hour=9, tm_min=29, tm_sec=22, tm_wday=5, tm_yday=102, tm_isdst=-1)



### 4.2.2 Useful File Name Titles


```python

```

### 4.2.3 File Name Extensions

| Description        | Precision              | Extension                             |
|--------------------|------------------------|---------------------------------------|
| Signed integers    | 8, 16, 32, 64          | .i08, .i16, .i32, .i64 (respectively) |
| Unsigned integers  | 8, 16, 32, 64          | .u08, .u16, .u32, .u64 (respectively) |
| Floating point     | 32 (single precision)  | .f32                                  |
|                    | 64 (double precision)  | .f64                                  |

### 4.2.4 File Name Convention Recap

| Placeholder | Description                                                                               |
|-------------|-------------------------------------------------------------------------------------------|
| Title       | A descriptive title of your choice.                                                       |
| YYYY        | Year the file was created.                                                                |
| mm          | Month the file was created. In the case of January, mm is 01.                             |
| dd          | Day the file was created. In the case of the 7th, dd is 07.                               |
| HH          | Hours in 24-hour notation. 11 p.m. would be represented as 23. Values are from 00 to 23.  |
| MM          | Minutes. 5 minutes past the hour is 05.                                                   |
| SS          | Seconds. 7 seconds past the minute is 07.                                                 |
| ext         | An extension describing the file format, three characters long (if possible).             |

* Example: Automating File Name Creation


```python
# %load 0053-7-src-Ch04/src/unique.py
from time import localtime
# a script to create unique filenames based on title,
# date and time stamp and an extension
datetime_stamp  = '%4d-%02d-%02dT%02d-%02d-%02d' % localtime()[:6]
title = 'SysALogs'
ext = 'csv'
print('Unique filename: %s-%s.%s' % (title, datetime_stamp, ext))
```

    Unique filename: SysALogs-2017-04-22T20-57-31.csv



```python
localtime()
```




    time.struct_time(tm_year=2017, tm_mon=4, tm_mday=22, tm_hour=20, tm_min=57, tm_sec=47, tm_wday=5, tm_yday=112, tm_isdst=0)




```python
localtime()[:6]
```




    (2017, 4, 22, 20, 57, 51)



### 4.2.5 Other Schemes

* Example: Running Index


```python
# a script to create unique filenames using a running index
from os.path import exists
index_stamp = 1
max_index = 999 # maximum number of files
title = '../data/SysALogs'
ext = 'txt'

while index_stamp <= max_index:
    unique_filename = '%s-%03d.%s' % (title, index_stamp, ext)
    if exists(unique_filename):
        index_stamp += 1
        continue
    f = open(unique_filename, 'wt')
    f.write("Data")
    f.close()
    break

# report status
if index_stamp > max_index:
    print("Could not create a unique filename")
else:
    print("Created a unique file: ", unique_filename)
```

## 4.3 File Formats

### 4.3.1 CSV File Format

* Example: Stock Price Charts


```python
# %load 0053-7-src-Ch04/src/stock_charts.py
from pylab import *
import csv
from time import gmtime, mktime

# modify the following to point to your data file
filepath = '../data/charts.xls'

# read the entire CSV file and store it in an array of lists
# use tab ('\t') as a delimiter
data=[]
for row in csv.reader(open(filepath), delimiter='\t'):
    data.append(row)

# split the data to header and values
header = data[0]
values = array(data[2:])

# the first column is date information in a string format
# we transform it to a day of year format
# notice that this will not work over year boundary (need to add 365)
yearday = zeros(len(values[:, 0]))
for i, day in enumerate(values[:, 0]):
    market_close_time = (int(day[6:]), int(day[:2]), int(day[3:5]), \
        16, 0, 0, 0, 0, 0)
    yearday[i] = gmtime(mktime(market_close_time)).tm_yday

# plot the data
for i in range(1, 5):
    plot(yearday, values[:, i], label=header[i], linewidth=3)

# annotate the start and end dates
text(yearday[0], values[0, 1], values[0, 0], ha='center')
text(yearday[-1], values[-1, 1], values[-1 ,0], ha='center')

grid()
legend(loc='best')
ylabel('Stock price [USD]')
xlabel('Days from start of the year '+values[0, 0][6:])
title('NASDAQ-100 (IXNDX) Stock price, period %s-%s' % \
    (values[-1, 0], values[0, 0]))
savefig('../images/stock_price.png', dpi=150)
```

* Example: Automatically Reading Yahoo! Financial Data


```python
# %load 0053-7-src-Ch04/src/yahoo_data.py
from pylab import *
from matplotlib.finance import *

# stock name and period
stock_name  = '^NDX'
t_start     = datetime.datetime(2014, 1, 1)
t_end       = datetime.datetime(2014, 1, 31)
year_start  = datetime.datetime(2014, 1, 1)

# retrieve and parse stock data
data    = fetch_historical_yahoo(stock_name, t_start, t_end)
y       = array(parse_yahoo_historical(data))

# dates might not be trade days, so update values
# to show actual dates retrieved
t_start = num2date(y[0, 0])
t_end   = num2date(y[-1, -0])

# normalize the x-axis to show values from the start of year
y[:, 0] = y[:, 0]-date2num(year_start)+1

# plot a candlestick graph
figure()
candlestick(gca(), y)

# annotate the graph with additional text
start_str   = "%d-%02d-%02d" % (t_start.year, t_start.month, t_start.day)
end_str     = "%d-%02d-%02d" % (t_end.year, t_end.month, t_end.day)
title('Stock: %s, period %s to %s' % (stock_name, start_str, end_str))
xlabel('Days from start of the year %d' % t_start.year)
ylabel('%s Stock price [USD]' % stock_name)
text(y[0, 0], y[0, 1], start_str)
text(y[-1, 0], y[-1, 1], end_str)
grid()
savefig('../images/%s_candlestick_yahoo-%s-%s.png' % \
    (stock_name, start_str, end_str), dpi=150)
```

* Example: Creating a CSV File

* CSV Limitations

* What to Store

* When to Use CSV

### 4.3.2 Binary Files

* An Array of Values

* Example: Reading and Writing an Array of Binary Values


```python
from array import *
```


```python
from array import *
a = array('h') # array of signed numbers, of zero size
a
```




    array('h')




```python
b = array('L', [1000, 2000, 3000]) # array of three unsigned numbers
b
```




    array('L', [1000, 2000, 3000])




```python
c = array('d', range(10)) # array of floating-points, from 0 to 9 including
c
```




    array('d', [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])



| Data Type  | Data Meaning and Minimum Size in bytes                    |
|------------|-----------------------------------------------------------|
| 'b'        | Signed integer, 1 byte                                    |
| 'B'        | Unsigned integer, 1 byte                                  |
| 'u'        | Unicode character, 2 bytes or 4 bytes, platform dependent |
| 'h'        | Signed integer, 2 bytes                                   |
| 'H'        | Unsigned integer, 2 bytes                                 |
| 'i'        | Signed integer, 2 bytes                                   |
| 'I'        | Unsigned integer, 2 bytes                                 |
| 'l'        | Signed integer, 4 bytes                                   |
| 'L'        | Unsigned integer, 4 bytes                                 |
| 'q'        | Signed integer, 8 bytes                                   |
| 'Q'        | Unsigned integer, 8 bytes                                 |
| 'f'        | Floating-point value, 4 bytes                             |
| 'd'        | Floating-point value, 8 bytes                             |


```python
a = array('L')
a.itemsize
```




    4




```python
f = open('b.u32', 'wb')
b.tofile(f)
f.close()
```


```python
d = array('L')
f = open('../data/b.u32', 'rb')
d.fromfile(f, 3)
f.close()
d == b
```

* An Array of Structs


```python
struct some_binary_file_format
{
    long epoch;
    float fTemperature;
    float fPressure;
};
```

* Example: Reading and Writing an Array of Structs


```python
import struct
```


```python
L = [ [ 10, 1.0, 2.0], [20, 0.125, 0.25] ]
```


```python
filename = '../data/structs.bin'
```


```python
format = 'Lff'
fout = open(filename, 'wb')
```


```python
for row in L:
    data = struct.pack(format, row[0], row[1], row[2])
    num = fout.write(data)
fout.close()
```


```python
struct_size = struct.calcsize(format)
```


```python
fin = open(filename, 'rb')
data = fin.read(struct_size)
data
```


```python
while data:
    values = struct.unpack(format, data)
    print(values)
    data = fin.read(struct_size)

```


```python
fin.close()
```


```python
data = open(filename, 'rb').read()
len(data)
```


```python
'Lff'*5
```


```python
print(struct.unpack(format*int(len(data)/struct_size), data))
```

* Header Files

### 4.3.3 Readme Files

### 4.3.4 INI Files

* Example: Reading and Writing INI Files


```python
# creating an INI (config) file
import configparser
options = configparser.ConfigParser()
options['User Options'] = {}
options['User Options']['all_data'] = 'Y'
options['User Options']['graph'] = '1'
options['Plot'] = {}
options['Plot']['grid'] = 'Y'
f = open('../data/options.ini', 'w')
options.write(f)
f.close()
```


```python
# read an INI (config) file
import configparser
read_opts = configparser.ConfigParser()
read_opts.read('../data/options.ini')

# print parameters and values
for section in read_opts.sections():
    print("[%s]" % section)
    for param in read_opts.items(section):
        print(param)
```

### 4.3.5 XML and Other Formats

https://docs.python.org/3.3/library/xml.html

## 4.4 Locating Data Files

### 4.4.1 Organization into Directories

### 4.4.2 Searching for Files

* Example: Storing Directory Contents in an Array


```python
import os
def get_all_files(srchpath):
    """Get the names of all the files in a directory, recursively,
    including path, name and size."""
    allfiles = []
    for root, dirs, files in os.walk(srchpath):
        for file in files:
            try:
                pathname = os.path.join(root, file)
                filesize = os.path.getsize(pathname)
                allfiles.append([file, pathname, filesize])
            except FileNotFoundError:
                pass
    return allfiles
```

### 4.4.3 Indexing

* Example: Searching for Duplicate Files


```python
def find_dupes_1(thefiles):
    """Searches for file duplicates, method 1."""
    result1 = []
    mydict1 = {}
    for filename, pathname, filesize in thefiles:
        if filename in mydict1:
            [dup_file, dup_size] = mydict1[filename]
        if dup_size==filesize:
            result1.append(pathname+filename)
        else:
            mydict1[filename] = [pathname,filesize]
    return result1
```


```python
def find_dupes_2(thefiles):
    """Searches for file duplicates, method 2."""
    result2 = []
    mydict2 = {}
    for filename, pathname, filesize in thefiles:
        for k, v in mydict2.items():
            if v[0]==filename and v[1]==filesize:
                result2.append(pathname+filename)
            else:
                mydict2[pathname] = [filename, filesize]
    return result2
```


```python
def find_dupes_3(thefiles):
    """Searches for file duplicates, method 3."""
    result3 = []
    mydict3 = {}
    for filename, pathname, filesize in thefiles:
        if mydict3.get(filename):
            for [dup_file, dup_size] in mydict3[filename]:
                if dup_size==filesize:
                    result3.append(pathname+filename)
            mydict3[filename].append([pathname, filesize])
        else:
            mydict3[filename] = [[pathname, filesize]]
    return result3
```


```python
srchpath = 'c:/Python33'
allfiles = get_all_files(srchpath)
t = []
from time import clock as clk
t.append(clk()); res1 = find_dupes_1(allfiles); t.append(clk())
t.append(clk()); res2 = find_dupes_2(allfiles); t.append(clk())
t.append(clk()); res3 = find_dupes_3(allfiles); t.append(clk())
len(allfiles) # number of data files processed
```


```python
print("method 1: %5.5f; method 2: %5.5f; method 3: %5.5f" % \
      (t[1]-t[0], t[3]-t[2], t[5]-t[4]))
```


```python
len(res1), len(res2), len(res3)
```


```python
if open(file1,'rb').read() == open(file2,'rb').read():
    print('identical files')
```

### 4.4.4 Catalogs

* Example: Creating a Clean Catalog File


```python
import os, csv

# rename the following to a directory of your choosing
srchpath = '../src'

# the CSV header
catalog = [['Filename', 'pathname', 'size']]

# walk directory tree
for root, dirs, files in os.walk(srchpath):
    for file in files:
        # process only .py files
        if file.lower().endswith('py'):
            pathname = os.path.join(root, file)
            filesize = os.path.getsize(pathname)
            catalog.append([ file, pathname, filesize])

# create the clean catalog
f = open('../data/clean_catalog.csv', 'w', newline='')
csv.writer(f).writerows(catalog)
f.close()
```

### Files vs. a Database

## 4.5 Final Notes and References

“Numeric representation of Dates and Time, The ISO solution to a long-standing source of confusion,” http://www.iso.org/iso/support/faqs/faqs_widely_used_standards/widely_used_standards_other/date_and_time_format.htm.
