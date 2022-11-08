class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        d = {}
        most_freq = 0
        res = 0
        while r < len(s):
            d[s[r]] = d.get(s[r], 0) + 1
            most_freq = max(most_freq, d[s[r]])
            if (r - l + 1) - most_freq > k:
                d[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
    # yikes
