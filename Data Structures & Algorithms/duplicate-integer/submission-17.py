class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Initialize seen list
        seen = set()

        # Traverse through nums array
        for num in nums:
            # If num is in seen return True
            if num in seen:
                return True
            # Add num into seen if not in seen
            seen.add(num)
        # Return false it not seen
        return False