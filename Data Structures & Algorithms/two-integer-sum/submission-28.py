class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in twoSumMap:
                return [twoSumMap[diff], i]
            twoSumMap[num] = i