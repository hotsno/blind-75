class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for num in d:
            freq[d[num]].append(num)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) >= k:
                    return res
