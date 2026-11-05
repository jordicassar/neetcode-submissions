class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initialize a set
        seen = set()

        # iterate through nums
        for num in nums:
            # check to see if a number is in the set
            if num in seen:
                # return true
                return True
            # add it 
            seen.add(num)
        # return false
        return False