class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left+right) // 2
            time = 1
            curr_sum = 0

            for i in range(len(weights)):
                if curr_sum + weights[i] > mid:
                    time += 1
                    curr_sum = weights[i]
                else:
                    curr_sum += weights[i]

            if time <= days:
                right = mid - 1
            else:
                left = mid + 1
        
        return left