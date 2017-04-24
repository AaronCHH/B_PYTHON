
# Chapter 3: Iterators and Generators
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 3: Iterators and Generators](#chapter-3-iterators-and-generators)
  * [3-1. Iterating Over the Contents of a List](#3-1-iterating-over-the-contents-of-a-list)
  * [3-2. Extracting the Contents of an Iterator](#3-2-extracting-the-contents-of-an-iterator)
  * [3-3. Filtering an Iterator](#3-3-filtering-an-iterator)
  * [3-4. Iterating Over the Contents of a File](#3-4-iterating-over-the-contents-of-a-file)
  * [3-5. Iterating Over Data That Has no Iterator](#3-5-iterating-over-data-that-has-no-iterator)
  * [3-6. Creating Standard Classes of Iterators](#3-6-creating-standard-classes-of-iterators)

<!-- tocstop -->


## 3-1. Iterating Over the Contents of a List
* Problem
* Solution
* How It Works


```python
my_list = [1, 2, 3, 4]
new_iter = iter(my_list)
new_iter
```




    <list_iterator at 0xecd3c10898>




```python
next(new_iter)
```




    1




```python
next(new_iter)
```




    2




```python
next(new_iter)
```




    3




```python
next(new_iter)
```




    4




```python
next(new_iter)
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-11-ed6082c80a14> in <module>()
    ----> 1 next(new_iter)


    StopIteration:


## 3-2. Extracting the Contents of an Iterator
* Problem
* Solution
* How It Works


```python
>>> pets = ['dogs', 'cats', 'lizards', 'pythons']
>>> pet_enum = enumerate(pets)
>>> next(pet_enum)
(0, 'dogs')
>>> next(pet_enum)
(1, 'cats')
```


```python
>>> pet_enum2 = enumerate(pets, start=5)
>>> next(pet_enum2)
(5, 'dogs')
```


```python
>>> pet_list = list(enumerate(pets))
>>> pet_list
[(0, 'dogs'), (1, 'cats'), (2, 'lizards'), (3, 'pythons')]
```

## 3-3. Filtering an Iterator
* Problem
* Solution
* How It Works


```python
>>> odd_nums = filter(lambda x: x%2, range(10))
>>> next(odd_nums)
1
>>> next(odd_nums)
3
```


```python
>>> odd_list = list(filter(lambda x: x%2, range(10)))
>>> odd_list
[1, 3, 5, 7, 9]
```


```python
>>> import itertools
>>> even_list = list(itertools.filterfalse(lambda x: x%2, range(10)))
>>> even_list
[0, 2, 4, 6, 8]
```

## 3-4. Iterating Over the Contents of a File
* Problem
* Solution
* How It Works


```python
file1 = open('file.csv')
for line in file1:
    int(line)
```


```python
>>> file1 = open('file.csv')
>>> next(file1)
'1,one\n'
>>> next(file1)
'2,two\n'
```

## 3-5. Iterating Over Data That Has no Iterator
* Problem
* Solution
* How It Works


```python
def squares(value=0):
    while True:
        value = value + 1
        yield (value-1)*(value-1)
>>> generator = squares()
>>> next(generator)
0
>>> next(generator)
1
>>> next(generator)
4
>>> next(generator)
9
```


```python
def up_down(value=1):
    yield from range(1, value, 1)
    yield from range(value, 0, -1)
>>> list(up_down(3))
[1, 2, 3, 2, 1]
```

## 3-6. Creating Standard Classes of Iterators
* Problem
* Solution
* How It Works


```python
>>> import itertools
>>> accumulator = itertools.accumulate(range(10))
>>> next(accumulator)
0
>>> next(accumulator)
1
>>> next(accumulator)
3
>>> next(accumulator)
6
```


```python
>>> list(itertools.combinations(range(5), 2))
[(0,1),
(0, 2),
(0, 3),
(0, 4),
(1, 2),
(1, 3),
(1, 4),
(2, 3),
(2, 4),
(3, 4)]
```
