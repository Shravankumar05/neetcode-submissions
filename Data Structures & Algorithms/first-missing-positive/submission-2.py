class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        setvals = set(i for i in range(1, len(nums)+2))
        setnums = set(nums)
        return min(setvals-setnums)