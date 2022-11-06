class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in d:
                a = d.get(sorted_str)
                a.append(str)
            else:
                d[sorted_str] = [str]
        res = []
        for item in d:
            res.append(d[item])
        return res

