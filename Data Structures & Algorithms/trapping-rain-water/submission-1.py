class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        maxl,maxr = height[l],height[r]
        tsum = 0
        while l<r:
            if maxl<maxr:
                l = l+1
                maxl = max(height[l],maxl)
                tsum += maxl-height[l]
            else:
                r = r-1
                maxr = max(height[r],maxr)
                tsum += maxr-height[r]
        return tsum

