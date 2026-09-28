class Solution:
    def trap(self, height: List[int]) -> int:
        max_right = [[] for _ in range(len(height))]
        curr_max = 0
        curr_idx = len(height)-1

        for i in range(len(height)-1, -1, -1):
            max_right[i] = [curr_max, curr_idx]
            if curr_max < height[i]:
                curr_max = height[i]
                curr_idx = i

        res = 0
        max_left = 0

        for i in range(len(height)):
            res += max(0, min(max_left, max_right[i][0]) - height[i])
            max_left = max(max_left, height[i])

        return res
