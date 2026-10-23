class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right = [0 for _ in range(len(prices))]
        curr = 0
        res = 0

        for i in range(len(prices)-1, -1, -1):
            right[i] = curr
            curr = max(curr, prices[i])
        
        for i in range(len(prices)):
            res = max(res, right[i]-prices[i])
        
        return res