class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = []
        for row in matrix:
            for num in row:
                x.append(num)
        
        left = 0
        right = len(x)-1

        while left <= right:
            mid = (left+right)//2
            if x[mid] == target:
                return True
            elif x[mid] > target:
                right = mid - 1
            elif x[mid] < target:
                left = mid + 1
        
        return False