# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

MAX = 20


def is_divisible(number: int) -> bool:
    for i in range(int(MAX / 2) + 1, MAX):
        if number % i != 0:
            return False
    return True


def find_smallest():
    number = MAX
    for i in range(int(MAX / 2) + 1, MAX):
        number = number * i

    smallest = 0

    while number > MAX:
        if is_divisible(number):
            smallest = number
            number = int(number / 2)
        else:
            number -= MAX

    print(f"Smallest multiple is {smallest}")


find_smallest()
