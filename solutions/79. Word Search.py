class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.visited = set()
        def dfs(x, y, length):
            if (x, y) in self.visited or x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return False
            length += 1
            if length > len(word) or word[length - 1] != board[x][y]:
                return False
            if length == len(word):
                return True
            self.visited.add((x, y))
            res = (dfs(x - 1, y, length) or
                   dfs(x + 1, y, length) or
                   dfs(x, y - 1, length) or
                   dfs(x, y + 1, length))
            self.visited.remove((x, y))
            return res

        # If last letter repeats more often than first letter, reverse word
        # to prevent TLE
        l, r = 0, len(word) - 1
        prev_l, prev_r = word[l], word[r]
        while l <= r:
            if prev_r != word[r]:
                word = word[::-1]
            if prev_l != word[l]:
                break
            l += 1
            r -= 1

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
