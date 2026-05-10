class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)-1, 1, -1):
            if i < len(nums)-1 and nums[i] == nums[i+1]:
                continue
            l, r = 0, i-1
            while l < r:
                total = nums[l] + nums[r] + nums[i]
                if total == 0:
                    res.append([nums[l], nums[r], nums[i]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        
        return res