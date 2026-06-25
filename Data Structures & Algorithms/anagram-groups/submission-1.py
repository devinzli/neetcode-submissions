from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            ctn = tuple(sorted(Counter(s).items()))
            if ctn in res:
                res[ctn].append(s)
            else:
                res[ctn] = [s]
        return list(res.values())