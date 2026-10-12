class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        buy = 0
        sell = 0

        mp = 0

        # sliding window
        while sell < len(prices):

            if prices[sell] > prices[buy]:
                mp = max(mp, prices[sell] - prices[buy])
            else:
                # this element is less than or equal to the buy price
                # which means regardless of what values come after,
                # any larger profit found after will have this buy price
                buy = sell
            
            sell += 1
        
        return mp
                
            