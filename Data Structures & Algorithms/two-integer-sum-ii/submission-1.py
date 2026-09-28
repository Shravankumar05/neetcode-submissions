class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {} # number: idx

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in seen:
                return [seen[diff], i+1]
            else:
                seen[numbers[i]] = i+1
        
        return [67]