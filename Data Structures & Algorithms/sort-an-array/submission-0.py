class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        def mergeSort(L: List[int], R: list[int]) -> List[int]:
            if len(L) > 1:
                middle = len(L) // 2
                L = mergeSort(L[:middle], L[middle:])
            if len(R) > 1:
                middle = len(R) // 2
                R = mergeSort(R[:middle], R[middle:])
            
            merged = []
            i = 0
            j = 0

            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    merged.append(L[i])
                    i += 1
                else:
                    merged.append(R[j])
                    j += 1
            
            merged.extend(L[i:])
            merged.extend(R[j:])
            return merged
        
        if len(nums) == 1:
            return nums
        
        return mergeSort(left, right)