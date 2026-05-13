class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        l, r = 0, 1
        max_price =0

        while r < len(prices):
            if prices[l] < prices[r]:
                price_diff = prices[r] - prices[l]
                max_price = max(max_price, price_diff)
            else:
                l = r
            r += 1
        return max_price


