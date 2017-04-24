
# Chapter 4: Files and I/O
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 4: Files and I/O](#chapter-4-files-and-io)
  * [4-1. Copying Files](#4-1-copying-files)
  * [4-2. Moving Files](#4-2-moving-files)
  * [4-3. Reading and Writing Text Files](#4-3-reading-and-writing-text-files)
  * [4-4. Reading and Writing XML Files](#4-4-reading-and-writing-xml-files)
  * [4-5. Creating a Directory](#4-5-creating-a-directory)
  * [4-6. Monitoring a Directory for Changes](#4-6-monitoring-a-directory-for-changes)
  * [4-7. Iterating Over the Files in a Directory](#4-7-iterating-over-the-files-in-a-directory)
  * [4-8. Saving Data Objects](#4-8-saving-data-objects)
  * [4-9. Compressing Files](#4-9-compressing-files)

<!-- tocstop -->


## 4-1. Copying Files
* Problem
* Solution
* How It Works


```python
import shutil
new_file_path = shutil.copy('file1.txt', 'file2.txt')
```


```python
shutil.copy('file1.txt', 'file2.txt', follow_symlinks=False)
```


```python
shutil.copy2('file1.txt', 'file2.txt')
```

## 4-2. Moving Files
* Problem
* Solution
* How It Works


```python
import shutil
shutil.move('file1.txt', 'dir2', copy_function=copy)
```


```python
import os
os.rename('file1.txt', 'dir2')
```

## 4-3. Reading and Writing Text Files
* Problem
* Solution
* How It Works


```python
>>> fd1 = open('file1.txt')
>>> entire_file = fd1.read()
```


```python
>>> chunk1 = fd1.read(100)
```


```python
>>> line1 = fd1.readline()
OR
>>> for line in fd1:
>>> do_my_process(line)
```


```python
>>> file_list = fd1.readlines()
>>> first_line = file_list[0]
```

## 4-4. Reading and Writing XML Files
* Problem
* Solution
* How It Works


```python
import xml.etree.ElementTree as ET
my_tree = ET.parse(‘my_data.xml’)
root = my_tree.getroot()
```


```python
>>> root.tag
'tag value'
>>> root.attrib
{ }
```


```python
for child in root:
    # look at the tag
    print(child.tag)
```


```python
>>> child1 = root[0]
```


```python
>>> a = ET.Element(‘a’)
>>> b = ET.SubElement(a, ‘b’)
>>> c = ET.SubElement(a, ‘c’)
>>> a.write(‘new_file.xml’)
```

## 4-5. Creating a Directory
* Problem
* Solution
* How It Works


```python
from pathlib import Path
p = Path('.')
p.joinpath('subdir1')
```




    WindowsPath('I:/BOOKS/PYTHON/_P_APRESS/Python Recipes Handbook/SF_PRH/subdir1')




```python
p.mkdir()
```

## 4-6. Monitoring a Directory for Changes
* Problem
* Solution
* How It Works


```python
import pathlib
p = pathlib.Path('.')
modified_time = p.stat().st_mtime
```


```python
import pathlib
dir_list = sorted(pathlib.Path('.').glob('*'))
```

## 4-7. Iterating Over the Files in a Directory
* Problem
* Solution
* How It Works


```python
import pathlib
p = pathlib.Path('.')
for child in p.iterdir():
    # Do something with the child object
    my_func(child)
```


```python
import pathlib
for child in pathlib.Path('.').iterdir():
    if child.is_file():
        my_func(child)
```

## 4-8. Saving Data Objects
* Problem
* Solution
* How It Works


```python
import pickle
file1 = open('data1.pickle', 'wb')
pickle.dump(data_obj1, file1)
```


```python
>>> file2 = open('data1.pickle', 'rb')
>>> data_reload = pickle.load(file2)
```

## 4-9. Compressing Files
* Problem
* Solution
* How It Works


```python
>>> import zipfile
>>> my_zip = zipfile.ZipFile('my_file.zip', mode='r')
```


```python
>>> import zipfile
>>> my_zip = zipfile.ZipFile(‘archive1.zip’, mode=’w’)
>>> my_zip.write(‘file1.txt’)
>>> my_zip.close()
```


```python
>>> import zipfile
>>> my_zip = zipfile.ZipFile(‘archive1.zip’, mode=’r’)
>>> my_zip.extract(‘file1.txt’)
>>> my_zip.close()
```


```python
>>> import zipfile
>>> my_zip = zipfile.ZipFile(‘file1.zip’, ‘a’)
>>> data_in = my_zip.read(‘data1.txt’)
>>> my_zip.write(‘data2.txt’, data_out)
>>> my_zip.close()
```


```python
>>> import gzip
>>> my_gzip = gzip.GzipFile(‘data1.txt.gz’)
>>> import bz2
>>> my_bzip = bz2.BZ2File(‘data2.txt.bz’)
```
