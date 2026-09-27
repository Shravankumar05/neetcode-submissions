class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr = 1
        left = [0 for _ in range(len(nums))]
        right = [0 for _ in range(len(nums))]
        i = 0

        while i < len(nums):
            left[i] = curr
            curr *= nums[i]
            i += 1
        
        curr = 1
        i = len(nums)-1
        while i >= 0:
            right[i] = curr
            curr *= nums[i]
            i -= 1
        
        res = []
        i += 1
        while i < len(nums):
            res.append(left[i] * right[i])
            i += 1
        
        return res