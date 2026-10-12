class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = 0
        for num in nums:
            if num == k:
                count += 1
        return [k, count]