class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr = prices[0]
        for num in prices:
            if num >= curr:
                res += (num-curr)
            curr = num
        
        return res