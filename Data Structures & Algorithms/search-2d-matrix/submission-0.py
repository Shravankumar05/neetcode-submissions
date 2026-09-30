class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # just binary search over multiple matricies lol
        full = []
        for row in matrix:
            for val in row:
                full.append(val)
        
        left = 0
        right = len(full)-1

        while left <= right:
            mid = (left+right)//2
            if full[mid] == target:
                return True
            elif full[mid] > target:
                right = mid - 1
            elif full[mid] < target:
                left = mid + 1
        
        return False