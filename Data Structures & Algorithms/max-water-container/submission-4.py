class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j, k = 0, len(heights)-1
        res = 0

        while j < k:
            res = max(res, (k-j)*min(heights[j],heights[k]))
            if heights[k] < heights[j]:
                k -= 1
            else:
                j += 1 
        return res
