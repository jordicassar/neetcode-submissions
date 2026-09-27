class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize a map
        twoSumMap = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in twoSumMap:
                return [twoSumMap[difference],i]
            twoSumMap[num] = i