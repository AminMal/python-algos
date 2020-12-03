

def bst(source: [int], target):
    length = len(source)
    current_search_index = int(length / 2)
    current_value_at_index = source[current_search_index]

    if length == 1:
        if source[0] == target:
            return True
        else:
            return False

    if current_value_at_index == target:
        return True
    else:
        if target > current_value_at_index:
            return bst(source[current_search_index + 1:], target)
        else:
            return bst(source[:current_search_index], target)


aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(bst(aList, 7))

