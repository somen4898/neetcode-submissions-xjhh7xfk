class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        str = []
        for i, num in enumerate(nums):
            for j , n in enumerate(nums):
                if j == i :
                    continue
                prod = prod * n
            str.append(prod) 
            prod = 1
        return str
            

            
            