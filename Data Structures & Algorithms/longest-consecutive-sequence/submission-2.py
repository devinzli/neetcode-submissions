from collections import defaultdict
class Solution:
    # union find
    def longestConsecutive2(self, nums: List[int]) -> int:
        res = 0
        mp = defaultdict(int)
        for n in nums:
            if not mp[n]:
                mp[n] = mp[n-1] + mp[n+1] + 1
                mp[n - mp[n-1]] = mp[n]
                mp[n + mp[n+1]] = mp[n]
                res = max(mp[n],res)
        return res 
    
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)
        for n in s:
            length = 0
            if n-1 not in s:
                length = 1
                while n + length in s:
                    length += 1
                res = max(length, res)
        
        return res

