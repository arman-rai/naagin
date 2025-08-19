import math

# V1 
# def sum_of_squares(numbers):
#     sum = 0
#     for i in range(0, len(numbers)):
#         sum +=(numbers[i] ** 2)
#     return sum

# V2 
# def sum_of_squares(numbers):
#     return sum(i**2 for i in numbers)

# V3
# def sum_of_squares(numbers):
#     return int(sum(math.pow(i,2) for i in numbers))


numbers = [1, 2, 4, 46]

print(sum_of_squares(numbers))