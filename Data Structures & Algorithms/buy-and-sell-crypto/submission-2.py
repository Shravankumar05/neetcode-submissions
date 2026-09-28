class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_right = [0 for _ in range(len(prices))]
        res = 0
        curr_max = 0

        for i in range(len(prices)-1, -1, -1):
            max_right[i] = curr_max
            curr_max = max(curr_max, prices[i])
        
        for i in range(len(prices)):
            res = max(res, (max_right[i]-prices[i]))
        return res