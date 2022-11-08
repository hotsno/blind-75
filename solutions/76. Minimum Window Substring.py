class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1
        window = {}
        l, r = 0, 0
        res_l, res_r = 0, len(s)
        filled = 0
        while r < len(s):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in t_dict and window[s[r]] == t_dict[s[r]]:
                filled += 1
            while filled == len(t_dict):
                if r - l + 1 < res_r - res_l + 1:
                    res_r = r
                    res_l = l
                window[s[l]] -= 1
                if s[l] in t_dict and window[s[l]] < t_dict[s[l]]:
                    filled -= 1
                l += 1
            r += 1
        return s[res_l:res_r+1] if res_r < len(s) else ""

