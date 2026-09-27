class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0

        for num in nums:
            if num-1 in numset:
                continue
            else:
                curr = 1
                while num+curr in numset:
                    curr += 1
                res = max(curr, res)
        
        return res