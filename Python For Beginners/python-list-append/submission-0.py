from typing import List # this is used to add type hints for List type

def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:
    # [1, 2, 3] are the elements in the current list (my_list), 
    # we must append elements 4 and 5 to my_list and return it 
    # as a list of integers e.g. (1, 2, 3, 4, 5)

    # enter the elements list
    for element in elements:
    # append elements to my_list
        my_list.append(element)
    # return my_list with newly appended elements
    return my_list




# do not modify below this line
print(append_to_list([1, 2, 3], [4, 5]))
print(append_to_list([], [1, 2, 3, 4]))
