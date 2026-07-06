class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.lower()
        l = 0
        r = len(st)-1
        while l < r:
            while l < len(st) and not st[l].isalnum():
                l += 1
            while r >= 0 and not st[r].isalnum():
                r -= 1
            if l < r:
                print(st[l], st[r])
                if st[l] != st[r]:
                    return False
                l += 1
                r -= 1
                
        
        return True

            