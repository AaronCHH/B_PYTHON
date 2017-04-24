
# Chapter 14: Testing and Debugging
<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [Chapter 14: Testing and Debugging](#chapter-14-testing-and-debugging)
  * [14-1. Timing a Section of Code](#14-1-timing-a-section-of-code)
  * [14-2. Profiling Code](#14-2-profiling-code)
  * [14-3. Tracing Subroutines](#14-3-tracing-subroutines)
  * [14-4. Tracing Memory Allocations](#14-4-tracing-memory-allocations)
  * [14-5. Performing Unit Tests](#14-5-performing-unit-tests)
  * [14-6. Debugging Code](#14-6-debugging-code)

<!-- tocstop -->


## 14-1. Timing a Section of Code
* Problem
* Solution
* How It Works


```python
python -m timeit 'print(42)'
```


```python
import timeit
timeit.timeit('42*42', number=1000)
```

## 14-2. Profiling Code
* Problem
* Solution
* How It Works


```python
def my_func():
    return 42

import profile
profile.run('my_func')
```


```python
python -m profile -o myscript.out myscript.py
```


```python
import pstats
p = pstats.Stats('myscript.out')
p.print_stats()
```

## 14-3. Tracing Subroutines
* Problem
* Solution
* How It Works


```python
python -m trace --trace myscript.py
```


```python
import trace
tracer = trace.Trace()
tracer.run('print("Hello World")')
```

     --- modulename: iostream, funcname: write
    iostream.py(362):         if self.pub_thread is None:
    iostream.py(366):             if not isinstance(string, unicode_type):
    iostream.py(369):             is_child = (not self._is_master_process())
     --- modulename: iostream, funcname: _is_master_process
    iostream.py(286):         return os.getpid() == self._master_pid
    iostream.py(371):             self.pub_thread.schedule(lambda : self._buffer.write(string))
     --- modulename: iostream, funcname: schedule
    iostream.py(185):         if self.thread.is_alive():
     --- modulename: threading, funcname: is_alive
    threading.py(1112):         assert self._initialized, "Thread.__init__() not called"
    threading.py(1113):         if self._is_stopped or not self._started.is_set():
     --- modulename: threading, funcname: is_set
    threading.py(508):         return self._flag
    threading.py(1115):         self._wait_for_tstate_lock(False)
     --- modulename: threading, funcname: _wait_for_tstate_lock
    threading.py(1069):         lock = self._tstate_lock
    threading.py(1070):         if lock is None:  # already determined that the C code is done
    threading.py(1072):         elif lock.acquire(block, timeout):
    threading.py(1116):         return not self._is_stopped
    iostream.py(186):             event_id = os.urandom(16)
    iostream.py(187):             while event_id in self._events:
    iostream.py(189):             self._events[event_id] = f
    iostream.py(190):             self._event_pipe.send(event_id)
     --- modulename: iostream, funcname: _event_pipe
    iostream.py(92):         try:
    iostream.py(93):             event_pipe = self._local.event_pipe
    iostream.py(101):         return event_pipe
    Hello Worldiostream.py(372):             if is_child:
    iostream.py(379):                 self._schedule_flush()
     --- modulename: iostream, funcname: _schedule_flush
    iostream.py(303):         if self._flush_pending:
    iostream.py(304):             return
     --- modulename: iostream, funcname: write
    iostream.py(362):         if self.pub_thread is None:
    iostream.py(366):             if not isinstance(string, unicode_type):
    iostream.py(369):             is_child = (not self._is_master_process())
     --- modulename: iostream, funcname: _is_master_process
    iostream.py(286):         return os.getpid() == self._master_pid
    iostream.py(371):             self.pub_thread.schedule(lambda : self._buffer.write(string))
     --- modulename: iostream, funcname: schedule
    iostream.py(185):         if self.thread.is_alive():
     --- modulename: threading, funcname: is_alive
    threading.py(1112):         assert self._initialized, "Thread.__init__() not called"
    threading.py(1113):         if self._is_stopped or not self._started.is_set():
     --- modulename: threading, funcname: is_set
    threading.py(508):         return self._flag
    threading.py(1115):         self._wait_for_tstate_lock(False)
     --- modulename: threading, funcname: _wait_for_tstate_lock
    threading.py(1069):         lock = self._tstate_lock
    threading.py(1070):         if lock is None:  # already determined that the C code is done
    threading.py(1072):         elif lock.acquire(block, timeout):
    threading.py(1116):         return not self._is_stopped
    iostream.py(186):             event_id = os.urandom(16)
    iostream.py(187):             while event_id in self._events:
    iostream.py(189):             self._events[event_id] = f
    iostream.py(190):             self._event_pipe.send(event_id)
     --- modulename: iostream, funcname: _event_pipe
    iostream.py(92):         try:
    iostream.py(93):             event_pipe = self._local.event_pipe
    iostream.py(101):         return event_pipe

    iostream.py(372):             if is_child:
    iostream.py(379):                 self._schedule_flush()
     --- modulename: iostream, funcname: _schedule_flush
    iostream.py(303):         if self._flush_pending:
    iostream.py(304):             return
     --- modulename: trace, funcname: _unsettrace
    trace.py(77):         sys.settrace(None)


## 14-4. Tracing Memory Allocations
* Problem
* Solution
* How It Works


```python
import tracemalloc
tracemalloc.start()
# Run you code here
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
for curr_stat in top_stats:
    print(curr_stat)
```


```python
import tracemalloc
tracemalloc.start()
snapshot1 = tracemalloc.take_snapshot()
# run your code
snapshot2 = tracemalloc.take_snapshot()
top_stats = snapshot2.compare_to(snapshot1, 'lineno')
```

## 14-5. Performing Unit Tests
* Problem
* Solution
* How It Works


```python
import unittest
class MyTestCase(unittest.TestCase):
    def test_the_answer(self):
        assertEqual(self.curr_val, 42)

if __name__ == '__main__':
    unittest.main()
```

## 14-6. Debugging Code
* Problem
* Solution
* How It Works


```python
import pdb
pdb.run('my_func()')
```


```python
python -m pdb myscript.py
```


```python
import pdb; pdb.set_trace()
```


```python
import pdb
def myfunc():
    print("Hello World")

pdb.run('myfunc()')
```


```python

```
