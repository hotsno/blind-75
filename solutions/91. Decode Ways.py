class Solution:
    def numDecodings(self, s: str) -> int:
        cur, prev, prev2 = len(s) - 1, 1, 1
        while cur >= 0:
            if s[cur] == '0':
                temp = 0
            else:
                temp = prev
                if cur < len(s) - 1 and int(s[cur:cur + 2]) <= 26:
                    temp += prev2
            prev2 = prev
            prev = temp
            cur -= 1
        return prev
