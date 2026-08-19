
# Maximize a value by chosing the lowest day then sell AFTER on the highest, else 0 if it strictly decreases



# profit = sell price - buy price

# vibe is sliding window, with 2 pointers in  O(n) time, O(1) space



# 1. buy and sell pointers init to 0, 1
# 2. store max
# 3. buy must be strictly less than sell always


# Move sell forward until it stops increasing, then move buy forward until it reaches sell
# if sell is not at the end, move sell forward




class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 1

        max_profit = 0


        while sell < len(prices):
            
            if prices[sell] > prices[buy]:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            else:
                # Found a price lower or equal to current buying price
                # So prices[sell] is new best buying price
                buy = sell
            
            sell += 1

        
        return max_profit
            
        

        