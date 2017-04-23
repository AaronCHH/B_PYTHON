
# Chapter 10: Advanced File Processing
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 10: Advanced File Processing](#chapter-10-advanced-file-processing)
  * [10.1 Binary Files and Random Access](#101-binary-files-and-random-access)
    * [10.1.1 Example: Reading the Nth Field](#1011-example-reading-the-nth-field)
    * [10.1.2 Example: Efficient Tail Implementation](#1012-example-efficient-tail-implementation)
    * [10.1.3 Example: Creating a Fixed Size File](#1013-example-creating-a-fixed-size-file)
    * [10.1.4 Example: Recording Time-Based Binary Data](#1014-example-recording-time-based-binary-data)
  * [10.2 Reading MATLAB Files as NumPy Arrays](#102-reading-matlab-files-as-numpy-arrays)
  * [10.3 Reading Text Files Directly to NumPy Arrays](#103-reading-text-files-directly-to-numpy-arrays)
    * [10.3.1 Example: Reading and Writing Text Files to NumPy Arrays](#1031-example-reading-and-writing-text-files-to-numpy-arrays)
  * [10.4 Object Serialization](#104-object-serialization)
    * [10.4.1 The Pickle Module](#1041-the-pickle-module)
  * [10.5 Command-Line Parameters](#105-command-line-parameters)
    * [10.5.1 argv](#1051-argv)
    * [10.5.2 Example: Creating a Fixed Size File (a Stand-Alone Script)](#1052-example-creating-a-fixed-size-file-a-stand-alone-script)
    * [10.5.3 The optparse Module](#1053-the-optparse-module)
    * [10.5.4 The FileInput Module](#1054-the-fileinput-module)
  * [10.6 File and Directory Manipulation](#106-file-and-directory-manipulation)
    * [10.6.1 Module glob](#1061-module-glob)
    * [10.6.2 Additional os Module Functionality](#1062-additional-os-module-functionality)
    * [10.6.3 Additional os.path Module Functionality](#1063-additional-ospath-module-functionality)
    * [10.6.4 Module shutil](#1064-module-shutil)
  * [10.7 File Compression](#107-file-compression)
    * [10.7.1 Example: A Compressed tar File](#1071-example-a-compressed-tar-file)
  * [10.8 Comparing Files](#108-comparing-files)
    * [10.8.1 Module filecmp](#1081-module-filecmp)
    * [10.8.2 Module difflib](#1082-module-difflib)
  * [10.9 Final Notes and References](#109-final-notes-and-references)

<!-- tocstop -->


## 10.1 Binary Files and Random Access


```python
f = open('data/example.bin', 'wb')
f.tell()
```




    0




```python
f.write(b'0123456789')
f.tell()
```




    10




```python
f.seek(5)
```




    5




```python
f.write(b'0123456789')
f.tell()
```




    15




```python
f.close()
```


```python
open('data/example.bin', 'rb').read()
```




    b'012340123456789'




```python
f = open('data/example.bin', 'rb')
f.seek(-2, 2)
```




    13




```python
print(f.read())
```

    b'89'


### 10.1.1 Example: Reading the Nth Field


```python
import struct
from math import sqrt
from random import randrange
# binary filename
bin_fn = 'data/large_file.bin'
Nfields = 1000 # number of fields
N = 766 # field to retrieve
fmt = 'cdL' # format: byte, float, 4-bytes
fmt_size = struct.calcsize(fmt)
```


```python
# create a random binary file
fout = open(bin_fn, 'wb')
for i in range(Nfields):
    data = struct.pack(fmt, bytes([randrange(32, 128)]), sqrt(float(i)), i)
    fout.write(data)
fout.close()
# read the nth value
fin = open(bin_fn, 'rb')
fin.seek((N-1)*fmt_size)
data = fin.read(fmt_size)
(c, d, l) = struct.unpack(fmt, data)
print("At location %d, I read:" % (fin.tell()/fmt_size), (c, d, l))
```

    At location 766, I read: (b'-', 27.65863337187866, 765)


### 10.1.2 Example: Efficient Tail Implementation


```python
from os.path import getsize
def tail_large(filename, n=10):
    """Returns the last n lines of a very large file."""
    N, data = 1024, b''
    # open the file and retrieve its size
    f = open(filename, 'rb')
    fsize = getsize(filename)

    # seek to the end of file
    f.seek(0, 2)
    for i in range(fsize-N, -N, -N):
        # read the next chunk of data
        f.seek(max(i, 0))
        # store read data, reversed order
        data = f.read(N)+data
        # do we have enough lines?
        if data.count(b'\n') > n:
            break
    # print the last n lines
    lines = data.splitlines()

    for line in lines[-n:]:
        print(line)
```

### 10.1.3 Example: Creating a Fixed Size File


```python
f = open('data/1gb_file.bin', 'wb')
f.seek(2**30-1)
```




    1073741823




```python
f.write(bytes([0]))
```




    1




```python
f.close()
```


```python
from os.path import getsize
getsize('data/1gb_file.bin')
```




    1073741824



### 10.1.4 Example: Recording Time-Based Binary Data


```python
import random, time, array
N = 10
fname = 'data/binary_data.f64'
data = array.array('d')
# create data

for value in range(N):
    time.sleep(random.random())
    data.append(time.time())
    data.append(value)

# store data to file
f = open(fname, 'wb')
data.tofile(f)
f.close()
```


```python
import random, time, array
N = 10
fname = 'data/binary_data.f64'
data = array.array('d')
# read data
f = open(fname, 'rb')
data.fromfile(f, N*2)
f.close()
# display data
L = data.tolist()
for t, val in zip(L[::2], L[1::2]):
    print(time.ctime(t), val)
```

    Sun Apr 23 14:29:35 2017 0.0
    Sun Apr 23 14:29:36 2017 1.0
    Sun Apr 23 14:29:37 2017 2.0
    Sun Apr 23 14:29:37 2017 3.0
    Sun Apr 23 14:29:38 2017 4.0
    Sun Apr 23 14:29:38 2017 5.0
    Sun Apr 23 14:29:39 2017 6.0
    Sun Apr 23 14:29:40 2017 7.0
    Sun Apr 23 14:29:40 2017 8.0
    Sun Apr 23 14:29:41 2017 9.0



```python
L = [1, 'Value', 2, 'Another value', 3, 'Last value']
L[::2] # these are the odd values
```




    [1, 2, 3]




```python
L[1::2] # these are the even values
```




    ['Value', 'Another value', 'Last value']




```python
list(zip(L[::2], L[1::2]))
```




    [(1, 'Value'), (2, 'Another value'), (3, 'Last value')]




```python
for i, s in zip(L[::2], L[1::2]):
    print(i, s)
```

    1 Value
    2 Another value
    3 Last value


## 10.2 Reading MATLAB Files as NumPy Arrays


```python
import numpy as np
from pylab import *
from scipy.io import savemat, loadmat
a = np.arange(10)
savemat('data.mat', {'a': a})
del a
a
```


```python
loadmat('data.mat')
```




    {'__globals__': [],
     '__header__': b'MATLAB 5.0 MAT-file Platform: nt, Created on: Sun Apr 23 14:33:07 2017',
     '__version__': '1.0',
     'a': array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])}




```python
data = loadmat('data.mat')
data['a']
```




    array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])



## 10.3 Reading Text Files Directly to NumPy Arrays

 | Parameter |
 |---|
 | Comments |
 | Converters |
 | Delimiter |
 | Dtype |
 | Ndmin |
 | Skiprows |
 | Usecols |
 | Unpack |

### 10.3.1 Example: Reading and Writing Text Files to NumPy Arrays


```python
from pylab import *
def c0(x):
    return datestr2num(x.decode('utf-8'))

data = loadtxt('data/charts.xls', skiprows=2, converters={0:c0})
data
```


```python
savetxt('data/charts_mod.txt', data)
```

## 10.4 Object Serialization

### 10.4.1 The Pickle Module

* Example: Saving and Retrieving Python Session Variables


```python
import pickle
from numpy import *
fname = 'data/mysession.pickle'
a = 3
b = "A string"
c = {'dict': 10}
d = eye(3)
fout = open(fname, 'wb')
for var in [a, b, c, d]:
    pickle.dump(var, fout)
fout.close()
```


```python
import pickle
fname = 'data/mysession.pickle'
fin = open(fname, 'rb')
var_index = 0
while True:
    try:
        var_index += 1
        exec("v_%d = pickle.load(fin)" % var_index)
        exec("var_type = type(v_%d)" % var_index)
        print("Read v_%d, type is: %s" % (var_index, var_type))
    except EOFError:
            break
```

    Read v_1, type is: <class 'int'>
    Read v_2, type is: <class 'str'>
    Read v_3, type is: <class 'dict'>
    Read v_4, type is: <class 'numpy.ndarray'>



```python
v_4
```




    array([[ 1.,  0.,  0.],
           [ 0.,  1.,  0.],
           [ 0.,  0.,  1.]])




```python
from pylab import *
fname = 'data/session.npy'
save(fname, eye(3))
load(fname)
```




    array([[ 1.,  0.,  0.],
           [ 0.,  1.,  0.],
           [ 0.,  0.,  1.]])



## 10.5 Command-Line Parameters


```python
python tail.py -n 20 filename
```

### 10.5.1 argv


```python
import sys
for i, cmd in enumerate(sys.argv):
    print("argv[%d] = '%s'" % (i, cmd))
```

    argv[0] = 'C:\Anaconda36\lib\site-packages\ipykernel\__main__.py'
    argv[1] = '-f'
    argv[2] = 'C:\Users\AaronHsu\AppData\Roaming\jupyter\runtime\kernel-22a77c3f-dd01-40b6-8409-9abcb8f1f7ee.json'


### 10.5.2 Example: Creating a Fixed Size File (a Stand-Alone Script)


```python
# %load 0053-7-src-Ch10/src/empty_file.py
from sys import argv, exit

usage = "Usage: python empty_file.py nbytes filename"

# we expect three arguments: script name, size and file name
if len(argv) != 3:
    print("Improper number of arguments.")
    print(usage)
    exit()

# is size an integer?
try:
    nbytes = int(argv[1])
except ValueError:
    print("First argument is not an integer number.")
    print(usage)
    exit()

# retrieve the requested file name
filename = argv[2]

# can we create the file?
# here a failure could be due to a non-existing path
try:
    f = open(filename, 'wb')
except IOError:
    print("Unable to create file", filename)
    print(usage)
    exit()

# finally! create the file
f.seek(nbytes-1)
f.write(b'0')
f.close()
print("Successfully created file %s of size %d." % (filename, nbytes))

```

### 10.5.3 The optparse Module

* Tip the module getopt (http://docs.python.org/library/getopt.html) is an older module that also provides
functions to parse command-line options.

* Example: Processing Command-Line Parameters


```python
# %load 0053-7-src-Ch10/src/empty_opt.py
from optparse import OptionParser
from sys import exit

usage = "Usage: python empty_opt.py [options] filename"

# create an OptionParser instance
parser = OptionParser(usage)

# these are the options
parser.add_option("-n", "--numbytes", dest="nbytes",
    type = "int", default=1000, help="number of bytes in file")
parser.add_option("-x", "--ext", dest="ext",
    action="store_true", default=False,
    help="adds 'bin' extension to filename")
(opt, args) = parser.parse_args()

# must have a filename
if len(args) != 1:
    print("Improper number of arguments.")
    exit()

# append extension if switch is on
filename = args[0]+'.bin' if opt.ext else args[0]

# create the file
try:
    f = open(filename, 'wb')
except IOError:
    print("Unable to create file", filename)
    exit()

f.seek(opt.nbytes-1)
f.write(b'0')
f.close()

print("Successfully created file %s of size %d." % (filename, opt.nbytes))

```


```python
$ python empty_opt.py
$ python empty_opt.py -h
$ python empty_opt.py file1
$ python empty_opt.py -x file1
$ python empty_opt.py -n 2000 --ext file1
$ python empty_opt.py -n 2000 --ext file1 file2
$ python empty_opt.py -n 2a --ext file1
```

https://docs.python.org/3.3/library/optparse.html

https://docs.python.org/3.3/library/configparser.html

### 10.5.4 The FileInput Module

| Method                 | Description  |
|---|---|
| fileinput.close()      | Ends the processing, closing all opened files. |
| fileinput.filelineno() | Returns the line number in the current file. |
| fileinput.filename()   | Returns the name of the file currently being read. |
| fileinput.fileno()     | Returns the index of the current file. |
| fileinput.isfirstline()| Returns True if this is the first line in a file.  |
| fileinput.lineno()     | Returns the cumulative line number of all lines read from all the files. |
| fileinput.nextfile()   | Stops processing the current file and jumps to the next file.  |

* Example: Combining Data from Several Sources Based on the Epoch


```python
# %load 0053-7-src-Ch10/src/combine_epoch.py
import fileinput
from time import mktime, strptime
data = []
fmt = '%b %d %H:%M:%S %Y'
for line in fileinput.input():
    data.append([mktime(strptime(line[4:24], fmt)), line])
for line in sorted(data):
    print(line[1], end='')

```

* Example: Searching for Text in Multiple Files


```python
# %load 0053-7-src-Ch10/src/srchfiles.py
import fileinput, sys

# string to search is the first argument
for line in fileinput.input(sys.argv[2:]):
    if line.find(sys.argv[1]) != -1:
        print("File %s, #%d: %s" % (fileinput.filename(),
            fileinput.filelineno(), line.rstrip()))

```

https://docs.python.org/3.3/library/fileinput.html

## 10.6 File and Directory Manipulation

### 10.6.1 Module glob


```python
from glob import glob
glob('*.py')
```




    ['flood_fill.py', 'fractal.py', 'read_world_data.py', 'star_patch.py']




```python
glob('*[0-9]*py')
```




    []




```python
glob('[!c]*py')
```




    ['flood_fill.py', 'fractal.py', 'read_world_data.py', 'star_patch.py']



* Tip You should also see the module, fnmatch (https://docs.python.org/3.3/library/fnmatch.html).

### 10.6.2 Additional os Module Functionality

| Function |
|---|
| os.chmod(path, mode) |
| os.remove(pathname) , or os.unlink(pathname) |
| os.rmdir() |
| os.mkdir(path) |
| os.makedirs(path) |
| os.rename(old, new) |
| os.renames(old, new) |

### 10.6.3 Additional os.path Module Functionality

| Function |
|---|
| os.path.abspath(s) |
| os.path.basename(s) |
| os.path.dirname(s) |
| os.path.exists(s) |
| os.path.getatime(s) |
| os.path.getctime(s) |
| os.path.getmtime(s) |
| os.path.getsize(s) |
| os.path.isabs(s) |
| os.path.isdir(s) |
| os.path.isfile(s) |
| os.path.join(base, seq) |
| os.path.split(s) |
| os.path.splitext(s) |

### 10.6.4 Module shutil

https://docs.python.org/3.3/library/shutil.html


```python
import shutil
from os import makedirs
from glob import glob
makedirs('dir1/dir2/dir3/dir4')
shutil.copy('file1.txt', 'dir1/dir2/dir3/dir4')
```


```python
shutil.copy('file1.txt', 'dir1/dir2/dir3/dir4/file2.txt')
```


```python
glob('dir1/dir2/dir3/dir4/*')
```


```python
shutil.move('dir1/dir2/dir3/dir4/file2.txt', 'dir1/dir2')
```


```python
glob('dir1/dir2/*')
```


```python
glob('dir1/dir2/dir3/dir4/*')
```


```python
shutil.copytree('dir1', 'Dir_1')
```


```python
glob('Dir_1/dir2/dir3/dir4/*')
```


```python
shutil.rmtree('dir1')
shutil.rmtree('Dir_1')
glob('dir1')
```

## 10.7 File Compression

| Module name  | Functionality | Documentation link |
|---|---|---|
| bz2  | Nonlossy compression | https://docs.python.org/3.3/library/bz2.html |
| gzip  | Nonlossy compression | https://docs.python.org/3.3/library/gzip.html |
| zlib  | Nonlossy compression | https://docs.python.org/3.3/library/zlib.html; http://www.zlib.net/ |
| tarfile  | Archiving | https://docs.python.org/3.3/library/tarfile.html |
| zipfile  | Archiving and compression |https://docs.python.org/3.3/library/zipfile.html  |


### 10.7.1 Example: A Compressed tar File


```python
import tarfile, glob, os.path
# create some files
for i in range(5):
    f = open('data/file%d.txt' % i, 'w')
    # write some data
    for j in range(100):
        f.write('Some data: %d\n' % j)
    f.close()
# archive the files using bz2 compression
tf = tarfile.open('data/files.tar.bz2', 'w:bz2')

for filename in glob.glob('data/file*'):
    tf.add(filename, os.path.basename(filename))
tf.close()
```


```python
import tarfile, os
tf = tarfile.open('data/files.tar.bz2', 'r:bz2')
tf.extractall('data/new/')
tf.close()
```


```python
import tarfile, os
if not os.path.exists('data/new'):
    os.mkdir('data/new')

tf = tarfile.open('data/files.tar.bz2', 'r:bz2')
for member in tf.getmembers()[:3]:
    tf.extract(member, 'data/new')
tf.close()
```

## 10.8 Comparing Files


```python
data1 = open('data/file1.txt', 'rb').read()
data2 = open('data/file2.txt', 'rb').read()
data1 == data2
```




    True



### 10.8.1 Module filecmp

https://docs.python.org/3.3/library/os.html


```python
filenames = ['data/file1.bin', 'data/file2.bin']
for fn in filenames:
    f = open(fn, 'w')
    f.write('some data')
    f.close()
```


```python
import filecmp
filecmp.cmp(filenames[0], filenames[1])
```




    True




```python
import tarfile, os, filecmp

if not os.path.exists('new1'):
    os.mkdir('new1')
if not os.path.exists('new2/new3'):
    os.makedirs('new2/new3')

tf = tarfile.open('files.tar.bz2', 'r:bz2')
tf.extractall('new1')
tf.extractall('new2')
tf.extractall('new2/new3')
tf.close()
cmp = filecmp.dircmp('new1', 'new2')

cmp.report()
```

### 10.8.2 Module difflib


```python
import difflib
content = """A string
123, 456
789
some text\n"""
fname1 = 'data/file1.txt'
fname2 = 'data/file2.txt'
f1 = open(fname1, 'w')
f1.write('before\n')
f1.write(content)
f1.close()
f2 = open(fname2, 'w')
f2.write(content)
f2.write('after\n')
f2.close()
```


```python
import difflib
fname1 = 'data/file1.txt'
fname2 = 'data/file2.txt'
lines1 = open(fname1).readlines()
lines2 = open(fname2).readlines()
for line in difflib.context_diff(lines1, lines2, fname1, fname2):
    print(line, end='')
```

    *** data/file1.txt
    --- data/file2.txt
    ***************
    *** 1,5 ****
    - before
      A string
      123, 456
      789
      some text
    --- 1,5 ----
      A string
      123, 456
      789
      some text
    + after


* Additional difflib functionality can be found online at https://docs.python.org/3.3/library/difflib.html

## 10.9 Final Notes and References

* The Python Standard Library, https://docs.python.org/3.3/library/index.html
