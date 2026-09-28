class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        if n < 3:
            return 0

        left = 0
        res = 0

        while left < n - 1:
            right = left + 1

            while right < n and height[right] < height[left]:
                right += 1

            if right == n:
                right = left + 1

                for i in range(left + 1, n):
                    if height[i] > height[right]:
                        right = i

            water_level = min(height[left], height[right])

            for i in range(left + 1, right):
                res += water_level - height[i]

            left = right

        return res