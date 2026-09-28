class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        
        for idx, value in enumerate(nums):
            if idx > 0 and value == nums[idx-1]:
                continue
            else:
                # sorted two sum
                left = idx + 1
                right = len(nums) - 1
                while left < right:
                    sonion_ring = nums[left] + nums[right] + value
                    if sonion_ring == 0:
                        res.append([value, nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif sonion_ring > 0:
                        right -= 1 # too high
                    else:
                        left += 1 # too low
        
        return res