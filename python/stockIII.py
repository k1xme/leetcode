# 3 passes. First pass starts from left to right, fills in `firstTrans` with the
# max profit made by buying and selling once from day 0 to day i.
# Second pass starts from right to left, fills in `secondTrans` with the
# max profit made from day i to day n-1.
# Third pass chooses the max profit in the array of sums of firstTrans and secondTrans.
# O(n)

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if not prices: return 0
        
        opt = [0]*len(prices)
        
        
        # fill in the firstTrans
        minPrice = prices[0]
        for i in range(len(prices)):
            if prices[i] < minPrice:
                opt[i] = prices[i-1]
                minPrice = prices[i]
            
            opt[i] = max(opt[i-1], prices[i]-minPrice)
        
        # fill in the secondTrans
        maxPrice = prices[len(prices)-1]
        opt[len(prices)-1] += 0

        for i in range(len(prices)-2, -1, -1):
            if prices[i] > maxPrice:
                maxPrice = prices[i]
            
            opt[i] = max(opt[i+1], opt[i]+ maxPrice-prices[i])
            
        return max(opt)
s = Solution()
print s.maxProfit([1,4,2])