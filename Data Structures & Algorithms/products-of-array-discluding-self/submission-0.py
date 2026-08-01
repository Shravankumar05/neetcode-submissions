class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = [0 for _ in range(len(nums))]
        R = [0 for _ in range(len(nums))]

        curr_l = 1
        curr_r = 1
        left = 0
        right = len(nums) - 1
        while left < len(nums):
            L[left] = curr_l
            curr_l *= nums[left]
            left += 1
            R[right] = curr_r
            curr_r *= nums[right]
            right -= 1
        
        i = 0
        res = []
        while i < len(nums):
            res.append(R[i]*L[i])
            i += 1
        
        return res