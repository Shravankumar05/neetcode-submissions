class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        i = 0

        if 0 in counts:
            j = 0
            while j < counts[0]:
                nums[i] = 0
                i += 1
                j += 1
        
        if 1 in counts:
            j = 0
            while j < counts[1]:
                nums[i] = 1
                i += 1
                j += 1
        
        if 2 in counts:
            j = 0
            while j < counts[2]:
                nums[i] = 2
                i += 1
                j += 1
        
        return