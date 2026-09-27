class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize map
        map = {}

        # Traverse through nums array
        for i, num in enumerate(nums):
            # Initilize complement
            complement = target - num

            if complement in map:
                return [map[complement], i]
            
            map[num] = i