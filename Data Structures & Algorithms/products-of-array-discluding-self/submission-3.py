class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = []
        right_product = []

        i = 0
        curr = 1
        while i < len(nums):
            left_product.append(curr)
            curr = curr * nums[i]
            i += 1
        
        i -= 1
        curr = 1
        while i > -1:
            right_product.append(curr)
            curr = curr * nums[i]
            i -= 1
        
        i += 1
        res = []
        while i < len(nums):
            res.append(left_product[i] * right_product[len(nums)-1-i])
            i += 1
        
        return res