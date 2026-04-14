class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        1 --> 1h
        4 --> 2h
        3 --> 2h 
        2 --> 1h

        key idea:
        the faster she eats, the fewer hours she needs
        so :
        if speed k works, then any speed bigger than k also works 
        if speed k does not work, then any speed smaller than k also does not work

        minimum : 1
        maximum : max(piles) --> if she eats the biggest pile, she can finish any pile in at most 1 hour
        so we binary search from :
        left=1
        right=max(piles)
        for each pile, the hours needed is 
        (pile+k-1)//k
        total hours is: 
        sum(ceil(pile/k) for pile in piles)
        '''
        left=1
        right=max(piles)

        while left<right: 
            mid=(left+right)//2

            hours=0
            for pile in piles:
                hours+=(pile+mid-1)//mid

            if hours <= h:
                right=mid 
            else: 
                left=mid+1
        
        return left

