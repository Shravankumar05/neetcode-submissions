class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counters = {}

        for num in nums:
            if num in counters:
                counters[num] += 1
                if counters[num] >= len(nums) / 2:
                    return num
            else:
                counters[num] = 1
        return nums[0]