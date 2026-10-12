class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # intialize map
        map = {}

        # Iterate through nums array
        for i, num in enumerate(nums):
            diff = target - num
            if diff in map:
                return diff, i
            map[num] = i