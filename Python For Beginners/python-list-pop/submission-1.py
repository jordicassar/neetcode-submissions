from typing import List # this is used to add type hints for List type

def remove_from_list(my_list: List[int], index: int) -> List[int]:
    # pop given index from my_list
    my_list.pop(index)
    # return my_list
    return my_list


def pop_n_from_list(my_list: List[int], n: int) -> List[int]:
    # n = 2: [1, 2, 3, 4, 5] -> [1, 2, 3]
    # n = 0: [1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5]
    # n = 5: [1, 2, 3, 4, 5] -> []
    # return a list of int most likely my_list since elements will be
    # popped from the list

    # enter the n elements
    for _ in range(n):
        # pop n elements from my_list
        my_list.pop()
    # return my_list with n popped elements
    return my_list


# don't modify below this line
print(remove_from_list([1, 2, 3, 4, 5], 2))
print(remove_from_list([1, 2, 3, 4, 5], 0))
print(remove_from_list([1, 2, 3, 4, 5], 4))

print(pop_n_from_list([1, 2, 3, 4, 5], 2))
print(pop_n_from_list([1, 2, 3, 4, 5], 0))
print(pop_n_from_list([1, 2, 3, 4, 5], 5))
