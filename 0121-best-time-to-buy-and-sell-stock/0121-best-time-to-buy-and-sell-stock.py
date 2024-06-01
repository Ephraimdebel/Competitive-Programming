class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        minimum = prices[0]
        maximum = 0

        for price in prices:
            if price < minimum:
                minimum = price
            elif price - minimum > maximum:
                maximum = price - minimum

        return maximum
