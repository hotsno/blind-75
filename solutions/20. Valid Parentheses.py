class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in "([{":
                stack.append(c)
            if c in ")]}":
                if len(stack) == 0:
                    return False
                if d[c] != stack.pop():
                    return False
        return len(stack) == 0
