class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_arr = []
        for c in s:
            c = c.lower()
            if c.isalnum():
                cleaned_arr.append(c)
        cleaned_str = ''.join(cleaned_arr)

        l, r = 0, len(cleaned_str) - 1
        while l < r:
            if cleaned_str[l] != cleaned_str[r]:
                return False
            l += 1
            r -= 1
        return True
