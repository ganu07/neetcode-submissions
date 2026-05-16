class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        total = 0

        while r < len(prices):
            et = prices[r] - prices[l]
            total = max(total, et)

            if prices[r] < prices[l]:
                l = r
            
            r += 1
        
        return total