class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        res = []
        target = len(nums)//3

        for num in nums:
            if num in res:
                continue
            elif num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            if counts[num] > target:
                res.append(num)


        return res