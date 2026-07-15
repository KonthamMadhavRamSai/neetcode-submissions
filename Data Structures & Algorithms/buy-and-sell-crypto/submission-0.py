class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprice=0
        minprice=float('inf')
        for i in range(len(prices)):
            minprice=min(minprice,prices[i])
            maxprice=max(maxprice,prices[i]-minprice)
        return maxprice