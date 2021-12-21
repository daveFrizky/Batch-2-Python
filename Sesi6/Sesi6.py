#list using for
num=[y*y for y in [1,2,3]]
#num=[y+1 for y in range(3)]
print(num)

#generator
def my_generator():
    print("Inside my generator")
    yield 'a'
    yield 'b'
    yield 'c'

# for char in my_generator():
#   print(char)
print(*my_generator(),sep="\n" )

def counter_generator(low, high):
    while low <= high:
       yield low
       low += 1

for i in counter_generator(5,10):
  print(i, end=' ')

# decorator

def coba(a):
    def inside():
        a()
    return inside

print("\n")

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.\n")
    return wrapper

@coba
def say_whee():
    print("Whee!")

say_whee()

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(5)