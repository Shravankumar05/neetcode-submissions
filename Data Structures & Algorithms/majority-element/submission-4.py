class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = {}
        target = len(nums) // 2

        for num in nums:
            if num in x:
                x[num] += 1
            else:
                x[num] = 1
            
            if x[num] > target:
                return num
        
        return -1