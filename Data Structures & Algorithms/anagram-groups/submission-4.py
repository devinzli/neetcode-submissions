class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def count(s: str) -> tuple:
            l = [0]*26
            for c in s:
                l[ord(c)-ord('a')] += 1
            return tuple(l)
        res = {}
        for s in strs:
            ctn = count(s)
            if ctn in res:
                res[ctn].append(s)
            else:
                res[ctn] = [s]
        return list(res.values())