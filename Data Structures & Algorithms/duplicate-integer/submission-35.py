class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Declare a set() named numSeen
        numSeen = set()

        # Initialize for loop to iterate through nums array
        for num in nums:
            # Check if num in seen
            if num in numSeen:
                return True
            # Add num into numSeen if not True
            numSeen.add(num)
        return False