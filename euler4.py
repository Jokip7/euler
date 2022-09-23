# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(input) -> bool:
    """Checks whether a string is a palindrome

    Args:
        input: The evaluated input

    Returns:
        bool: Whether the number is a palindrome
    """

    input = str(input).lower()
    half_length = int(len(input) / 2)

    for i in range(half_length):

        if input[i] != input[-i - 1]:
            return False

    return True


def make_palindrome():
    biggest = 0
    num1 = 999
    num2 = 999

    while num1 > 100:
        while num2 > 100:
            result = num1 * num2
            if is_palindrome(result):
                if result > biggest:
                    biggest = result
            num2 -= 1
        num1 -= 1
        num2 = 999

    print(f"Largest palindrome is {biggest}")


make_palindrome()
