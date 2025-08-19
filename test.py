import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start : }sec")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("done~")


slow_function()

# decorators
# what does the func.__name__ do?
# why did the wrapper function return itself?
# and also what is the @timer what does it mean, the timer was not even called 