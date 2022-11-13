class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.seen = set()
        def dfs(x, y):
            if (x, y) in self.seen or min(x, y) < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != "1":
                return
            self.seen.add((x, y))
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in self.seen:
                    dfs(i, j)
                    res += 1
        return res
