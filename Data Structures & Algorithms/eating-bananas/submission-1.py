class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search speed, from 1 to max val
        left = 1
        right = max(piles)

        while left < right:
            mid = (left+right) // 2
            time = 0

            for i in range(len(piles)):
                duration_int = piles[i] // mid
                duration_raw = piles[i] / mid
                time += duration_int
                if duration_raw > duration_int:
                    time += 1
            
            if time <= h:
                right = mid
            else:
                left = mid + 1
        
        return right