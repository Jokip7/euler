# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

MAX = 20


def find_naive():
    i = 20

    while (
        i % 11 != 0
        or i % 12 != 0
        or i % 13 != 0
        or i % 14 != 0
        or i % 15 != 0
        or i % 16 != 0
        or i % 17 != 0
        or i % 18 != 0
        or i % 19 != 0
        or i % 20 != 0
    ):
        i += 20

    print(f"{i} is the smallest multiple")


def is_divisible(number: int) -> bool:
    for i in range(int(MAX / 2) + 1, MAX):
        if number % i != 0:
            return False
    return True


def find_smallest():
    number = MAX

    while not is_divisible(number):
        number += MAX

    print(f"{number} is the smallest multiple")


find_smallest()
find_naive()
