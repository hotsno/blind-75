class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.helper(0, target, [], candidates)
        
    def helper(self, cur, target, arr, nums):
        if target - cur == 0:
            return [arr]
        if target - cur < 0:
            return []
        res = []
        for i in range(len(nums)):
            for j in self.helper(cur + nums[i], target, arr + [nums[i]], nums[i:]):
                res.append(j)
        return res
