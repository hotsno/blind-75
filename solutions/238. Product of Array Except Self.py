class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cur = 1
        res = [1] * len(nums)
        for i in range(len(nums) - 1):
            cur *= nums[i]
            res[i + 1] = cur
        cur = 1
        for i in range(len(nums) - 1, 0, -1):
            cur *= nums[i]
            res[i - 1] = res[i - 1] * cur
        return res
