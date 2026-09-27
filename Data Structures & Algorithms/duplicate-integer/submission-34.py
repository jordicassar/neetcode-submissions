class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_tracker = set()

        for num in nums:
            if num in seen_tracker:
                return True
            seen_tracker.add(num)
        return False