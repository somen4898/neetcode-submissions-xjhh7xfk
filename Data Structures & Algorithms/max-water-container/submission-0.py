class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxh=0
        l,r = 0, len(heights)-1
        while l<r:
            br = r-l
            h = min(heights[r],heights[l])
            carea = br*h
            maxh = max(carea,maxh)
            if heights[r]>heights[l]:
                l+=1
            else:
                r-=1
        return maxh
        


