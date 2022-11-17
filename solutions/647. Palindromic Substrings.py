class Solution:
    def countSubstrings(self, s: str) -> int:
        def pal(l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res, l, r = res + 1, l - 1, r + 1
            return res
        res = 0
        for i in range(len(s)):
            res += pal(i - 1, i) + pal(i, i)
        return res
