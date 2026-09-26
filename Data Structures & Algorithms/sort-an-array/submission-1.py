class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def sorter(numbers: List[int]) -> List[int]:
            mid = len(numbers) // 2
            L = numbers[:mid]
            R = numbers[mid:]

            if len(L) > 1:
                L = sorter(L)
            if len(R) > 1:
                R = sorter(R)
            
            left_pointer = 0
            right_pointer = 0
            res = []

            while left_pointer < len(L) and right_pointer < len(R):
                if L[left_pointer] >= R[right_pointer]:
                    res.append(R[right_pointer])
                    right_pointer += 1
                else:
                    res.append(L[left_pointer])
                    left_pointer += 1
            
            while left_pointer < len(L):
                res.append(L[left_pointer])
                left_pointer += 1
            
            while right_pointer < len(R):
                res.append(R[right_pointer])
                right_pointer += 1
            
            return res
        
        return sorter(nums)