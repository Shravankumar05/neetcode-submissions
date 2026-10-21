class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        start = 0
        res = []

        while start < len(nums)-2:
            if start > 0 and nums[start] == nums[start-1]:
                start += 1
                continue
            left = start + 1
            right = len(nums)-1
            while left < right:
                val = nums[left] + nums[right] + nums[start]
                if val == 0:
                    res.append([nums[start], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1 
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif val > 0:
                    right -= 1
                elif val < 0:
                    left += 1
            start += 1
        return res