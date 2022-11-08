class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= nums[r]:
                if m == 0 or nums[m - 1] > nums[m]:
                    return nums[m]
                else:
                    r = m - 1
            else:
                l = m + 1
