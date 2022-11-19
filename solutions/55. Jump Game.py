class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] >= count:
                count = 0
            count += 1
        return count == 1
