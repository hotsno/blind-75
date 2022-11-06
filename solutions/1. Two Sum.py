class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in d:
                return [d[remainder], i]
            d[nums[i]] = i
        return None
