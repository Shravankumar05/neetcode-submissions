class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 100001
        total = 0
        left = 0

        for right in range(len(nums)):
            total += nums[right]

            while target <= total:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
        
        if res == 100001:
            return 0
        else:
            return res