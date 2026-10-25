class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        def canship(weight: int) -> bool:
            ships = 1
            currCap = weight
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = weight
                currCap -= w
            return True

        res = max(weights)
        while left < right:
            mid = (left+right)//2
            if canship(mid):
                res = min(res, mid)
                right = mid
            else:
                left = mid + 1
        
        return left