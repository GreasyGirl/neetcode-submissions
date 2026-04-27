class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        maxP = 0
        while r <= (len(prices) - 1):
            if prices[l] < prices[r]: # profitable 
                maxP = max(prices[r] - prices[l], maxP)
                r += 1
            else: # non -profit
                l = r
                r = l + 1
        return maxP
                

        