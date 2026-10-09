class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = {0: 0, 1: 0, 2: 0}
        for num in nums:
            colors[num] += 1
        
        i = 0
        for key, value in colors.items():
            j = 0
            while j < value:
                nums[i] = key
                j += 1
                i += 1
        
        return