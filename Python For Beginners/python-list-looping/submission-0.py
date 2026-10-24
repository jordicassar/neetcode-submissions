from typing import List # used to add type hint for List

def count_x(nums: List[int], x: int) -> int:
    # [ 1, 2, 3, 4, 5 ] x is 5 output should be 1 since 5 is seen in nums list once
    # make a count variable
    count = 0
    # enter the loop
    for num in nums:
        # check to see if x is in list nums
        if num == x:
        # return value of count variable
            count += 1
    return count
    # if x is not in nums list return empty string or zero


# do not modify below this line
print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))
