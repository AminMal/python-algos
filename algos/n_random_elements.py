import random


def random_elements(n: int, cap: int) -> [int]:

    def iterate(numbers_to_go: int = n, acc: [int] = None):
        if acc is None:
            acc = []
        if numbers_to_go == 0:
            return acc + [random.randint(0, cap)]
        else:
            return iterate(numbers_to_go - 1, acc + [random.randint(0, cap)])

    return iterate()


print(random_elements(6, 49))