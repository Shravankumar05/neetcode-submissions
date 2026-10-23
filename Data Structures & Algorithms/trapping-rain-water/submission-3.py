class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        right = [0 for _ in range(len(height))]
        curr = 0
        i = len(height)-1
        curr = 0
        
        while i > - 1:
            right[i] = curr
            curr = max(curr, height[i])
            i -= 1
        
        res = 0
        curr = 0
        i = 0

        while i < len(height):
            left_max = curr
            res += max(0, min(left_max, right[i])-height[i])
            curr = max(curr, height[i])
            i += 1
        
        return res