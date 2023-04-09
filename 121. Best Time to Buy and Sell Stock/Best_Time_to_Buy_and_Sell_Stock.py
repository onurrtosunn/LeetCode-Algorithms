
class Solution(object):
    def maxProfit(self, prices):
        
        buy_price = prices[0] 
        profit = 0 
        
        for i in range(1,len(prices)):
            
            if prices[i] < buy_price:
                buy_price = prices[i]
            else:
                profit = max(profit, prices[i]-buy_price)
                
        return profit
		
