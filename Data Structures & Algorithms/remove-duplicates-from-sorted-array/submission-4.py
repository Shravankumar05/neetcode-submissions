class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = 0
        k = 0
        i = 0
        seen = set()
        
        while i < len(nums):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[k] = nums[i]
                k += 1
            i += 1

        return k