class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        
        while left <= right:
            mid = (left+right)//2
            val = mid * mid
            if val == x:
                return mid
            elif val > x:
                right = mid - 1
            elif val < x:
                left = mid + 1
        
        return right