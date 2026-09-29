class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for val in asteroids:
            while res and res[-1] > 0 and val < 0:
                if res[-1] < -val:
                    res.pop()
                    continue
                if res[-1] == -val:
                    res.pop()
                    break
                if res[-1] > -val:
                    break

            else:
                res.append(val)
                        
        return res