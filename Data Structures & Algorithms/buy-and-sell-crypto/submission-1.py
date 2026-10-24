
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best=0
        minn=prices[0]
        for x in range(len(prices)):
           minn=min(minn,prices[x])
           best=max(best,prices[x]-minn)
        return best


