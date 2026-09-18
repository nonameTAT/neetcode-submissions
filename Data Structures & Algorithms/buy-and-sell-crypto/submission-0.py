class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=101
        mx_profit=0
        for price in prices:
            minp=min(price,minp)
            mx_profit=max(mx_profit,price-minp)
        return mx_profit