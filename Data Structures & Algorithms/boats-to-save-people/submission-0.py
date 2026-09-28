class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        res = 0
        left = 0
        right = len(people)-1

        while left <= right:
            # big first on the right if space left, otherwise right
            # will drop to eventually cover them
            remainder = limit - people[right]
            right -= 1
            res += 1
            if left <= right and remainder >= people[left]:
                left += 1
        
        return res