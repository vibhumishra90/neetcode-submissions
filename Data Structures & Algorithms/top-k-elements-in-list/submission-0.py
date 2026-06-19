class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1) frequency map banalo
        freq = {}  # num -> count
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        # 2) buckets: index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in freq:
            f = freq[num]
            buckets[f].append(num)

        # 3) highest frequency se k elements collect
        res = []
        for f in range(len(nums), 0, -1):
            for num in buckets[f]:
                res.append(num)
                if len(res) == k:
                    return res
        return res