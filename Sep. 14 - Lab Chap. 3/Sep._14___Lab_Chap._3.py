"""
Why do java programmers wear glasses?
"""

import math


def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    r = int(math.sqrt(x))
    for i in range(3, r + 1, 2):
        if x % i == 0:
            return False
    return True
"""
This function checks for prime numbers
between 2 and 100. It returns True if the number is prime, and False otherwise.
"""

def main():
    try:
        n = int(input("Enter a number (0-100): "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if n < 0 or n > 100:
        print("Please enter a number between 0 and 100.")
        return

    if is_prime(n):
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")
#Because they don't C# (see sharp)

if __name__ == "__main__":
    main()


