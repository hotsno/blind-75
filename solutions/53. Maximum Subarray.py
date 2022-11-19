class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = cur = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            cur += num
            if num > cur:
                cur = num
            res = max(res, cur)
        return res
