from math import sqrt


def is_prime(number):
    for i in range(2,  int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def find_prime_numbers(target: int) -> list[int]:
    if target < 0:
        raise ValueError
    if target < 2:
        return []
    primes = [num for num in range(2, target + 1) if is_prime(num)]
    return primes
