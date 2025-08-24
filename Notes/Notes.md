Some modules:
Functional style (map, filter, reduce)

Collections (Counter, deque, defaultdict)

Utility modules (itertools, datetime, json)

This is a context check This is a context check 

- decorators are just wrapper functions that can help in doing some tasks before starting the required funcion kinda like constructors?

- hello.__meta__, here the things under__*__ are just metadata
- @timer it just means `function = timer(function)`
- yield pauses the function and remembers its state. Next time you call next() on it, it resumes from where it left off.
- ClassName() runs __init__ and gives you an object.


generators = memory-efficient, great for streams of data.
so nums = [x**2 for x in range(10**6)]  is better than nums = x**2 for x in range(10**6)

