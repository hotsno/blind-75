from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Make adjacency list
        # Check for no cycles
        d = defaultdict(list)
        for p in prerequisites:
            # in order to take p[1], you need to have
            # taken p[0]
            d[p[1]].append(p[0])
        def dfs(i, seen):
            if i in seen:
                return False
            seen.add(i)
            for n in d[i]:
                if not dfs(n, seen):
                    return False
            seen.remove(i)
            d[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        return True

