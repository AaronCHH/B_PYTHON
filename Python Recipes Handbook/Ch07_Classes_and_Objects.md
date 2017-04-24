
# Chapter 7: Classes and Objects
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 7: Classes and Objects](#chapter-7-classes-and-objects)
  * [7-1. Discovering the Type of an Object (Everything Is an Object)](#7-1-discovering-the-type-of-an-object-everything-is-an-object)
  * [7-2. Creating Classes](#7-2-creating-classes)
  * [7-3. Adding Private Fields](#7-3-adding-private-fields)
  * [7-4. Subclassing](#7-4-subclassing)
  * [7-5. Initializing Objects](#7-5-initializing-objects)
  * [7-6. Comparing Objects](#7-6-comparing-objects)
  * [7-7. Changing an Object After Creation](#7-7-changing-an-object-after-creation)
  * [7-8. Implementing Polymorphic Behavior](#7-8-implementing-polymorphic-behavior)

<!-- tocstop -->



## 7-1. Discovering the Type of an Object (Everything Is an Object)
* Problem
* Solution
* How It Works


```python
>>> a = 1
>>> type(a)
<class 'int'>
>>> b = "Hello World"
>>> type(b)
<class 'str'>
```


```python
>>> a = 1
>>> isinstance(a, int)
TRUE
```

## 7-2. Creating Classes
* Problem
* Solution
* How It Works


```python
class my_simple_class:
    a = 3
    b = "Hello World"
```


```python
class my_complex_class:
    a = 42
    def method1():
        print("The value of a is " + str(a))
    b = "Hello World"
```

## 7-3. Adding Private Fields
* Problem
* Solution
* How It Works


```python
class priv_vars:
    __a__ = "This is a private variable"
```


```python
class my_class1:
    __a_ = 1
```

## 7-4. Subclassing
* Problem
* Solution
* How It Works


```python
class animal:
    type = "mammal"
class dog(animal):
    breed = "labrador"
```


```python
my_dog = dog()
my_dog.breed
```




    'labrador'




```python
my_dog.type
```




    'mammal'



---


```python
class bird(animal):
    type = "bird"
```


```python
my_bird = bird()
```


```python
my_bird.type
```




    'bird'



---


```python
class eagle(animal, bird):
    species = "eagle"
```


```python
my_eagle = eagle()
```


```python
my_eagle.type
```

## 7-5. Initializing Objects
* Problem
* Solution
* How It Works


```python
class my_complex:
    def __init__(self, real_part, imaginary_part):
        self.r = real_part
        self.i = imaginary_part
```


```python
complex_num = my_complex(2, 3)
```


```python
complex_num.r
```




    2



## 7-6. Comparing Objects
* Problem
* Solution
* How It Works


```python
a = "string1"
b = a
a is b
```




    True




```python
class book:
    def __init__(self, pages):
        self.pages = pages
    def __lt__(self, other):
        return self.pages < other
    def __gt__(self, other):
        return self.pages > other
....
```

## 7-7. Changing an Object After Creation
* Problem
* Solution
* How It Works


```python
book1 = book(42)
book1.title = "My Book"
book1.title
```


```python
class my_container:
    pass
```


```python
container1 = my_container()
container1.label = "The first container"
container1.phone = "555-5555"
container1.name = "John Doe"
```

## 7-8. Implementing Polymorphic Behavior
* Problem
* Solution
* How It Works


```python
class dog:
    def talk(self):
        print("bark")
class cat:
    def talk(self):
        print("meow")

def speak(animal):
    animal.talk()
```


```python
my_dog = dog()
my_cat = cat()
speak(my_dog)
```

    bark



```python
speak(my_cat)
```

    meow
