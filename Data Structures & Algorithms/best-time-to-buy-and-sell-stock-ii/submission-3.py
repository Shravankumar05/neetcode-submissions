class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy_price = prices[0]

        i = 0
        while i < len(prices):
            # current price is higher than the buy
            # sell for profit
            if prices[i] > buy_price:
                res += (prices[i]-buy_price)
            # lower price available rebase
            buy_price = prices[i]
            i += 1



        return res