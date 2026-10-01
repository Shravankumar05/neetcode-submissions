class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x = {}

        for num in nums:
            if num in x:
                return num
            else:
                x[num] = 1
        
        return