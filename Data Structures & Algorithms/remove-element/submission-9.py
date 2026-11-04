class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums [3, 2, 2, 3]
        # val = 3
        # output = [2, 2]


        # initialize value to keep track of count and position
        k = 0
        # iterate through nums list
        for i in range(len(nums)):
            # check to see element doesn't equal val
            if nums[i] != val:
            # map i to k
                nums[k] = nums[i]
            # k increments by 1
                k += 1
        # return k
        return k
