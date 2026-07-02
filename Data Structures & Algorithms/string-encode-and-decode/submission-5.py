class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "" 
        res = ""
        for s in strs:
            l = len(s)
            res += str(l) + "#" + s
        return res
        
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        res = []
        j = k = 0
        while k < len(s):
            if s[k] == "#":
                l = int(s[j:k])
                res.append(s[k+1:k+1+l])
                k += l + 1
                j = k
                continue
            k += 1
        return res




        
