
# sliding window + dp?



# start first buy, at all n (loop over and start on all)
# then recurse on all valid n+1 to len(prices) - 1 from that starting point
# update a max and memo for that buy/sell period, on (i, j) as key


# memo on (i, canBuy)



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        hm = {}

        def check(i, can_buy):

            if i >= len(prices):
                return 0

            if (i, can_buy) in hm:
                return hm[(i, can_buy)]


            if can_buy:
                # buy
                profit_buy = -prices[i] + check(i + 1, False)
                m_pro = max(profit_buy, check(i + 1, True))
                hm[(i, can_buy)] = m_pro
                return m_pro
                

            else:
                # sell
                profit_sell = prices[i] + check(i + 2, True)
                m_pro = max(profit_sell, check(i + 1, False))
                hm[(i, can_buy)] = m_pro
                return m_pro
        
        return check(0, True)
        




