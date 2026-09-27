class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = 100001
        res = 0

        for price in prices:
            # if the price being seen is higher or equal than our buy we sell and rebase
            if price >= curr:
                res += (price-curr)
            # if the price being seen is lower than our buy we hold the new position
            curr = price

        return res    