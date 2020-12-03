from typing import TypeVar
import random

T = TypeVar('T')


def take_n_random(n: int, source: [T]) -> [T]:

    def except_index(index: int, src: [T]) -> [T]:
        left_side = src[:index]
        right_side = src[index + 1:]
        return left_side + right_side

    def iterate(numbers_to_go: int = n, src: [T] = source, acc: [T] = []) -> [T]:
        if numbers_to_go == 1:
            return acc + [src[random.randint(0, len(src) - 1)]]
        else:
            random_index = random.randint(0, len(src) - 1)
            rest = except_index(random_index, src)
            return iterate(numbers_to_go - 1, rest, acc + [src[random_index]])

    if n > len(source) or n < 0:
        raise Exception("n is not valid \n1 <= n <= len(source)")
    elif n == 0:
        return None
    else:
        return iterate()


ls = [1, 2, 3, 4, 5, 6, 7]
stringList = ["Amin", "Ali", "Whatever", "Hello"]

print(take_n_random(4, ls))
print(take_n_random(4, stringList))

try:
    print(take_n_random(9, ls))
except Exception:
    print("that caused exception, because number was out of bounds")

