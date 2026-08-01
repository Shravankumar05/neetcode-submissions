class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        availables = {}

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if diff in availables:
                return [availables[diff], i]
            else:
                availables[num] = i
        
        return -1