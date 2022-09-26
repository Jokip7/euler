# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math
import time
from datetime import timedelta

TARGET = 600851475143


def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def find_largest_prime_factor():
    print(f"Finding largest prime factor for {TARGET}...")

    for num in reversed(range(2, int(math.sqrt(TARGET)))):
        if TARGET % num == 0:
            if is_prime(num):
                print(f"{num} is the largest prime factor!")
                return


start_time = time.monotonic()
find_largest_prime_factor()
end_time = time.monotonic()

print(f"Duration: {timedelta(seconds=end_time - start_time)}")
