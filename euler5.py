# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math
from typing import List

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


# In the solution to problem 3 we discussed prime factorization.
# From this we can deduct two important properties which we use for this problem:
# 1. All numbers have a unique prime factorization
# 2. All non-prime factors of a number can be generated from the prime factors
#
# This enables us to restate the problem as:
# Find the smallest set of primes, such that all numbers (1-20) can be constructed.
# This set will be the prime factorization of the smallest number to which 1-20 are all evenly divisible.


def generate_primes(upperLimit: int) -> List[int]:
    """Generate a list of primes

    Args:
        upperLimit (int): Will try to find primes for every number up until this point

    Returns:
        List[int]: List of primes
    """
    primes = [2]
    isPrime = False

    i = 3
    j = 0

    while i <= upperLimit:
        j = 0
        isPrime = True
        while primes[j] * primes[j] <= i:
            if i % primes[j] == 0:
                isPrime = False
                break
            j += 1
        if isPrime:
            primes.append(i)
        i += 2

    return primes


# Now that we have our primes, we can find the divisible
def find_divisible():
    p = generate_primes(MAX)
    result = 1

    for i in range(len(p)):
        a = int(math.floor(math.log(MAX) / math.log(p[i])))
        result = result * int(math.pow(p[i], a))

    print(f"{result} is the smallest divisible")


# find_smallest()
# find_naive()
find_divisible()
