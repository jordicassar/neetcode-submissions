class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in twoSumMap:
                return complement, i
            twoSumMap[num] = i