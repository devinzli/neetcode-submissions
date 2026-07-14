class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nms = sorted(nums)
        l = len(nms)
        i = 0
        while i < l:
            if nms[i] > 0:
                break
            if i > 0 and nms[i] == nms[i-1]:
                i += 1
            else:
                j = i+1
                k = l - 1
                while j < k:
                    if nms[i]+nms[j]+nms[k]<0:
                        j += 1
                    elif nms[i]+nms[j]+nms[k]>0:
                        k -= 1
                    elif nms[i]+nms[j]+nms[k] == 0:
                        res.append([nms[i],nms[j],nms[k]])
                        j += 1
                        k -= 1
                        while j < k and nms[j] == nms[j-1]:
                            j += 1
                i += 1
        return res
                    
            