from typing import TypeVar

T = TypeVar('T')


def add_elem_at(ls: [T], element: T, index: int) -> [T]:
    left_side = ls[:index]
    right_side = ls[index:]
    return left_side + [element] + right_side


myList = [1, 2, 4, 5, 6]
complete_list = add_elem_at(myList, 3, 2)
print(complete_list)

list_of_strings = ["Amin", "Ali"]
complete_string_list = add_elem_at(list_of_strings, "Ard", 1)
print(complete_string_list)
