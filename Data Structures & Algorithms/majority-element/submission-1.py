class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        target = len(nums) // 2
        
        for num in nums:
            if num in counts:
                counts[num] += 1
                if counts[num] > target:
                    return num
            else:
                counts[num] = 1
        
        return nums[0]