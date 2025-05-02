import math

import random


def random_number():
    return random.randint(1, 20)


def random_operador():
    return random.choice(['+', '-', '*'])


def mcd(a, b):
    return math.gcd(a, b)


def generar_progression(length=10, start=None, step=None):
    if start is None:
        start = random.randint(1, 20)
    if step is None:
        step = random.randint(1, 10)
    return [start + step * i for i in range(length)]


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True