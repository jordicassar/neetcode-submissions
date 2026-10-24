from typing import List, Set # this adds type hints for List and Set

def list_to_set(nums: List[int]) -> Set[int]:
    # [1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5]
    # [1, 1, 2, 2, 3, 3] -> [1, 2, 3]
    # [1, 2, 3, 4, 5, 5, 5, 3, 4, 5] -> [1, 2, 3, 4, 5]

    # initialize a set
    seen = set()
    # iterate through nums list
    for num in nums:
        # add num into set
        seen.add(num)
    # return nums
    return seen

# do not modify below this line
print(list_to_set([1, 2, 3, 4, 5]))
print(list_to_set([1, 1, 2, 2, 3, 3]))
print(list_to_set([1, 2, 3, 4, 5, 5, 5, 3, 4, 5]))
