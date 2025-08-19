# def fibo(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a+b

# for num in fibo(10):
#     print(num)

# Here this is a generator function that does lazy eval one at a time
# it doesn't load to memory?

def hello():
    pass

print(hello.__name__) # prints the name of the function (metadata of func)
