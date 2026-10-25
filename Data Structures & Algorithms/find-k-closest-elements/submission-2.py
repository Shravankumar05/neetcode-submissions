class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid

        l, r = left - 1, left
        res_left = []
        res_right = []

        while l >= 0 and len(res_left) + len(res_right) < k:
            if r >= len(arr) or abs(arr[l] - x) <= abs(arr[r] - x):
                res_left.append(arr[l])
                l -= 1
            else:
                res_right.append(arr[r])
                r += 1

        while r < len(arr) and len(res_left) + len(res_right) < k:
            res_right.append(arr[r])
            r += 1

        res_left.reverse()
        return res_left + res_right