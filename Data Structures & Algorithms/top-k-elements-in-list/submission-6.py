class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)
        top_k = sorted_items[:k]

        return [item[0] for item in top_k]