class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        x = []

        for event in asteroids:
            while x and event < 0 and x[-1] > 0:
                diff = event + x[-1]
                if diff < 0:
                    x.pop()
                elif diff > 0:
                    event = 0
                else:
                    event = 0
                    x.pop()
            if event:
                x.append(event)
        
        return x