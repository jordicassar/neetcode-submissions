class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Initialize map 
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False