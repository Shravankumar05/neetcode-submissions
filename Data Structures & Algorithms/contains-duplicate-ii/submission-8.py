class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = set()
        
        for i, num in enumerate(nums):
            if num in check:
                return True
            check.add(num)
            if len(check) > k:
                check.remove(nums[i-k])
        
        return False