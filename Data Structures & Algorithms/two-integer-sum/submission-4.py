class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        # Traverse through the array nums
        for i, nums in enumerate(num):
            complement = target - num

            if complement in map:
                return [map[complement], i]
            
            map[num] = i
