class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        left = 0
        right = 0
        res = 99999999
        curr_sum = 0

        while right < len(nums):
            curr_sum += nums[right]

            while curr_sum >= target:
                res = min(res, right - left + 1)
                curr_sum -= nums[left]
                left += 1

            right += 1

        return res