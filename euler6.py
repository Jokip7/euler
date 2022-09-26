import math

MAX = 100


def sum_square_difference():
    i = 0
    sum_square = 0
    square_sum = 0

    while i <= MAX:
        sum_square += math.pow(i, 2)
        square_sum += i
        i += 1

    square_sum = math.pow(square_sum, 2)

    difference = square_sum - sum_square
    print(difference)


sum_square_difference()
