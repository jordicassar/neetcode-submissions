class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # 1. count frequency of each number
        for num in nums:
            count[num] = count.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        # 2. put each number into bucket[its frequency]
        for num, freq in count.items():
            buckets[freq].append(num)
        # 3. walk buckets from high to low, collect until we have k
        res = []
        for freq in range(len(buckets) -1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res