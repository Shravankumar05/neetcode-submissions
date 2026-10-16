class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        target = len(nums) // 3
        res = set()
        result = []

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            
            if counts[num] > target and num not in res:
                result.append(num)
                res.add(num)
        
        return result