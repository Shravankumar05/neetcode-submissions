class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        available = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in available:
                return [available[diff], i]
            else:
                available[nums[i]] = i
        
        return []