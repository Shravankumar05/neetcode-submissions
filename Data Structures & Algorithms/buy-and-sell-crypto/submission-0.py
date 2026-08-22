class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = len(prices) - 1
        right_max = [-1 for _ in range(len(prices))]
        curr = -1
        while i > -1:
            curr = max(curr, prices[i])
            right_max[i] = curr
            i -= 1
        
        profit = 0
        res = 0
        for i in range(len(prices)):
            res = max(res, right_max[i] - prices[i])
        
        return res