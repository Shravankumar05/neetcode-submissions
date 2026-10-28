class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1 for _ in range(len(arr))]

        i = len(arr)-1
        curr_max = -1
        while i > -1:
            res[i] = curr_max
            curr_max = max(arr[i], curr_max)
            i -= 1
        
        return res