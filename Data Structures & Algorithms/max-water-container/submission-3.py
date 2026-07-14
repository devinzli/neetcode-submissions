class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mj,mk = 0, len(heights)-1
        j, k = 0, len(heights)-1
        max_area = (mk-mj)*min(heights[mj],heights[mk])

        while j < k:
            area = (k-j)*min(heights[j],heights[k])
            if area > max_area:
                mj = j
                mk = k
                max_area = area
            if heights[k] < heights[j]:
                k -= 1
            else:
                j += 1
        
        
        return max_area
