# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math

TARGET = 10001


def find_prime():
    prime_count = 1
    i = 1

    while prime_count < TARGET:
        i += 2
        if is_prime(i):
            prime_count += 1

    print(f"{i} is the {TARGET}st prime")


def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


find_prime()
