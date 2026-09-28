class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = 0
        k = 0
        i = 0
        seen = set()
        
        while i < len(nums):
            # if seen dont add and move next slot to add
            if nums[i] in seen:
                i += 1# increment i and move on
            # if not seen add to set and to nums increment k and i
            else:
                seen.add(nums[i])
                nums[k] = nums[i]
                k += 1
                i += 1

        return k