class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            nums_set.add(num)
        seen = set()
        res = 0
        for num in nums_set:
            if num in seen:
                continue
            cur = 0
            while num in nums_set:
                seen.add(num)
                cur += 1
                num += 1
            res = max(res, cur)
        return res
