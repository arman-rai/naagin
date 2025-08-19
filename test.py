# V1 
def sum_of_squares(numbers):
    sum = 0
    for i in range(0, len(numbers)):
        sum +=(numbers[i] ** 2)
    return sum

numbers = [1, 2, 4, 46]

print(sum_of_squares(numbers))

# V2 
# def sum_of_squares(numbers):
#     return()