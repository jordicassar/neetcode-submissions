class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initialize a set 
        seen = set()

        # iterate through nums array
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False