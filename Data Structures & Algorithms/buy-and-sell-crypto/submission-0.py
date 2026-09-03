class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_p=0

        for i in range(len(prices)-1):
            buy=prices[i]
            sell=max(prices[i+1:])

            if sell>buy:
                temp_p=sell-buy
                if temp_p> max_p:
                    max_p=temp_p
        return max_p



        