class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set(nums)

        for num in nums:
            if num-1 in numset:
                continue
            else:
                val = num
                while (val+1) in numset:
                    val += 1
                res = max(res, val-num+1)
        
        return res