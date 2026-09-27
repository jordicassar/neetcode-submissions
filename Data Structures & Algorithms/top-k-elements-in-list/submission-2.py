class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        elements = list(count.keys())
        elements.sort(key=lambda num: count[num], reverse=True)

        return elements[:k]