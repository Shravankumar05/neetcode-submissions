class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        res = [0 for _ in range(len(nums))]

        while i < len(nums):
            res[(i+k)%(len(nums))] = nums[i]
            i += 1
        
        nums[:] = res
        return