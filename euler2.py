# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
# the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

import time
from datetime import timedelta

MAX = 4000000
fib = [1, 2]


def make_fib_range():
    while True:
        next_number = fib[-2] + fib[-1]
        if next_number < MAX:
            fib.append(next_number)
        else:
            break


def sum_even_numbers():
    total = sum(i for i in fib if i % 2 == 0)
    print(f"The result is {total}")


def fib_efficient():
    """
    Only evaluate the even numbers in the Fibonacci range.
    Every third number in a Fibonacci range is even.
    We can utilize this fact to only calculate the next even number.
    The next even number in the range equals 4 * the last even number + the last even number before that (because math)
    """

    fib3 = 2
    fib6 = 0
    summed = fib3
    total = 0

    while summed < MAX:
        total += summed

        summed = 4 * fib3 + fib6
        fib6 = fib3
        fib3 = summed

    print(f"The result is {total}")


start_time = time.monotonic()
make_fib_range()
sum_even_numbers()
end_time = time.monotonic()

print(f"Duration: {timedelta(seconds=end_time - start_time)}")

start_time = time.monotonic()
fib_efficient()
end_time = time.monotonic()

print(f"Duration: {timedelta(seconds=end_time - start_time)}")
