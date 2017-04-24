
# Chapter 12: Concurrency
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 12: Concurrency](#chapter-12-concurrency)
  * [12-1. Creating a Thread](#12-1-creating-a-thread)
  * [12-2. Using Locks](#12-2-using-locks)
  * [12-3. Setting a Barrier](#12-3-setting-a-barrier)
  * [12-4. Creating a Process](#12-4-creating-a-process)
  * [12-5. Communicating Between Processes](#12-5-communicating-between-processes)
  * [12-6. Creating a Pool of Workers](#12-6-creating-a-pool-of-workers)
  * [12-7. Creating a Subprocess](#12-7-creating-a-subprocess)
  * [12-8. Scheduling Events](#12-8-scheduling-events)

<!-- tocstop -->


## 12-1. Creating a Thread
* Problem
* Solution
* How It Works


```python
import threading
def print_sum():
    print('The sum of 1 and 2 is 3')
my_thread = threading.Thread(target=print_sum)
my_thread.start()
```

    The sum of 1 and 2 is 3


## 12-2. Using Locks
* Problem
* Solution
* How It Works


```python
import threading
sum = 0
my_lock = threading.Lock()
def adder():
    global sum, my_lock
    my_lock.acquire()
    sum = sum + 1
    my_lock.release()
my_thread = threading.Thread(target=adder)
my_thread.start()
```

## 12-3. Setting a Barrier
* Problem
* Solution
* How It Works


```python
import threading
b = threading.Barrier(5, timeout=10)
```

## 12-4. Creating a Process
* Problem
* Solution
* How It Works


```python
import multiprocessing
def adder(a, b):
    return a+b
proc1 = multiprocessing.Process(target=adder, args=(2,2))
proc1.start()
proc1.join()
```

## 12-5. Communicating Between Processes
* Problem
* Solution
* How It Works


```python
import multiprocessing
def func(pipe_end):
    pipe_end.send(['hello', 'world'])
    pipe_end.close()
parent_end, child_end = multiprocessing.Pipe()
proc1 = multiprocessing.Process(target=func, args=(child_end,))
proc1.start()
print(parent_end.recv())
proc1.join()
```


```python
import multiprocessing

def func(queue1):
    queue1.put(['hello', 'world'])

my_queue = multiprocessing.Queue()
proc1 = multiprocessing.Process(target=func, args=(my_queue,))
proc1.start()
print(my_queue.get())
proc1.join()
```

## 12-6. Creating a Pool of Workers
* Problem
* Solution
* How It Works


```python
import multiprocessing
def adder(a):
    return a+a
pool1 = multiprocessing.Pool(processes=4)
```


```python
# This method blocks untill all processes return
pool1.map(adder, range(10))
# This method returns a result object
results = pool1.map_async(adder, range(10))
results.wait()
```

## 12-7. Creating a Subprocess
* Problem
* Solution
* How It Works


```python
import subprocess
results = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
print(results.stdout)
```

## 12-8. Scheduling Events
* Problem
* Solution
* How It Works


```python
import sched, time
def print_time():
    print(time.time())
my_sched = sched.scheduler()
my_sched.enter(10, 1, print_time)
```
