class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            j = i
            while j < len(nums)-1 and nums[j] == nums[j+1]:
                nums.pop(j+1)
            i += 1
        return len(nums)