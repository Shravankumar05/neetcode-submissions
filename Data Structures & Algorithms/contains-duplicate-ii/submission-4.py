class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        contains = {}

        i = 0
        while i < len(nums):
            num = nums[i]
            if num in contains:
                if i - contains[nums[i]] <= k:
                    return True
                else:
                    contains[nums[i]] = i
            else:
                contains[nums[i]] = i
            
            i += 1
        
        return False