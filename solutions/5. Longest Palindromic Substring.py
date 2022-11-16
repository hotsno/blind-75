class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pal(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            return (l + 1, r - 1)

        i, res_l, res_r = 0, 0, 0
        while i < len(s):
            tmp1 = pal(i, i)
            tmp2 = pal(i - 1, i)
            if tmp1[1] - tmp1[0] > tmp2[1] - tmp2[0]:
                l, r = tmp1
            else:
                l, r = tmp2
            if r - l > res_r - res_l:
                res_l, res_r = l, r
            i += 1
        return s[res_l:res_r + 1]

