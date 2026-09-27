class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # intialize map
        mapTwoSum = {}

        # Iterate through nums array 
        for i, num in enumerate(nums):
            diff = target - num
            if diff in mapTwoSum:
                    return [mapTwoSum[diff], i]
            mapTwoSum[num] = i