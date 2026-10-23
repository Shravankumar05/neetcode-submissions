class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        m = max(people)
        count = [0] * (m+1) # number of people at each weight
        
        for p in people:
            count[p] += 1
        
        idx = 0
        i = 1

        while idx < len(people):
            while count[i] == 0:
                i += 1
            people[idx] = i
            count[i] -= 1
            idx += 1
        
        res = 0
        left = 0
        right = len(people)-1

        while left <= right:
            remain = limit - people[right]
            right -= 1
            res += 1
            if left <= right and remain >= people[left]:
                left += 1
        
        return res