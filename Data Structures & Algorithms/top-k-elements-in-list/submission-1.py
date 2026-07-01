class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = 1 + d.get(n,0)
        
        freq = []
        res = []
        for _ in range(len(nums)):
            freq.append([])
        
        for n, c in d.items():
            freq[c-1].append(n)
        
        for i in range(len(nums)-1,-1, -1):
            while((len(freq[i])!=0)):
                res.append(freq[i].pop())
                if len(res) == k:
                    return res

            
            