class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left+right)//2
            t = 0
            for p in piles:
                t += (p//mid)
                if p % mid != 0:
                    t += 1
            if t > h:
                left = mid + 1
            else:
                right = mid - 1
        
        return left