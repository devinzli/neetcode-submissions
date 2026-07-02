class Solution:
    # Attaching length of each str follow by #, so that I know exactly how much 
    # to parse during decode
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
                j = k + 1
                k = j + l
                res.append(s[j:k])
                j = k
                continue
            k += 1
        return res




        
