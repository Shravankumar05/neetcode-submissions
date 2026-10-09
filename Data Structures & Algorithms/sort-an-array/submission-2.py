class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def spliter(values: List[int]) -> List[int]:
            mid = len(values)//2
            L = values[:mid]
            R = values[mid:]

            if len(L) > 1:
                L = spliter(L)
            
            if len(R) > 1:
                R = spliter(R)
            
            i = 0
            j = 0
            res = []

            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    res.append(L[i])
                    i += 1
                else:
                    res.append(R[j])
                    j += 1
            
            while i < len(L):
                res.append(L[i])
                i += 1

            while j < len(R):
                res.append(R[j])
                j += 1
            return res
        
        return spliter(nums)