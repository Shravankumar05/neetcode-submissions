class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target_freq = len(nums) // 3
        count = {}
        res = []

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

            if count[num] > target_freq and num not in res:
                res.append(num)
        
        return res