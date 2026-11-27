class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        


        # sliding window

        # while it's a higher price to the left, move l left
        # if this newer l is lower than r, move r to l, since it if ever goes higher than the max found before
        # by this i mean a new higher found to the right, it would always be better to have bought on that min day


        buy, sell = 0, 0

        max_profit = 0

        while sell < len(prices):

            max_profit = max(max_profit, prices[sell] - prices[buy])

            if prices[sell] < prices[buy]:
                buy = sell
            
            sell += 1
        
        return max_profit
        

