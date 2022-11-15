class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        n1, n2 = 1, 2
        for i in range(n - 3, -1, -1):
            temp = n1
            n1 = n2
            n2 = n2 + temp
        return n2
