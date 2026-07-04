class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pp = [1]*n
        fp = [1]*n
        for i in range(1,n):
            pp[i] = nums[i-1] * pp[i-1]
            fp[n-1-i] = nums[n-i] * fp[n-i]
        
        res = [1]*n
        for i in range(n):
            res[i] = pp[i] * fp[i]

        return res


            
            