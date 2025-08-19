import math
from functools import reduce

numbers = [1, 5, 54, 12, 66]
evens = filter(lambda x: x%2 == 0, numbers)
squares = map(lambda x: math.pow(x,2), evens)
sum = reduce(lambda a, b: a+b, squares)

print(sum)