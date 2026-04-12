class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        1. keep min_price = cheapest price we've seen so far ( best day to buy )
        2. best= maximum profit we get so far 
        3. for each day's price p: 
        - if we sold today, profit would be p-min_price 
        - update best=max(best,p-min_price)
        - update min_price=min(min_price,p) (maybe today is a better day to buy)
        '''
        min_price=prices[0]
        best=0

        for p in range(len(prices)):
            cur=prices[p]-min_price 
            best=max(best,cur)
            min_price=min(min_price,prices[p])

        return best