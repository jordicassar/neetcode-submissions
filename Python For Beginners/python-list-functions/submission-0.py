from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    return sum(nums)

def get_min(nums: List[int]) -> int:
    return min(nums)

def get_max(nums: List[int]) -> int:
    return max(nums)

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
