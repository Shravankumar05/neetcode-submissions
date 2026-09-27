class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        i = 0

        for oof in range(3):
            if oof in counts:
                j = 0
                while j < counts[oof]:
                    nums[i] = oof
                    i += 1
                    j += 1
                
        return