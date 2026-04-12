class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        from collections import deque

        # 1. Initialize an empty deque
        my_deque = deque()

        # 2. Initialize with an existing iterable (e.g., a list)
        numbers = deque([1, 2, 3, 4, 5])

        # 3. Initialize with a maximum length (maxlen)
        # When the deque is full, adding a new item will automatically remove an item from the opposite end.
        # Example: maxlen=3
        limited_deque = deque([1, 2, 3], maxlen=3)
        '''

        dq=deque() 
        l=0
        ans=[]

        for r in range(len(nums)):
            while dq and nums[dq[-1]]<=nums[r]:
                dq.pop() #pop from the back while the new number is bigger (those smalelr can never be max again)
            dq.append(r) #append r 

            #if leftmost index is out of the window, remove it 

            if dq[0]<l:
                dq.popleft()
            
            #once we have a full window, record max and slide l
            if r-l+1 == k:
                ans.append(nums[dq[0]])
                l+=1
            
        return ans


        ''' 
        how we keep the order : 
        think of dq as a "candidates list" for the max -- kept in decreasing order (big-->small)
        from front to back

        then rule that "orders" it 
        when a new number nums[r] comes in :
        pop from the back while it's smaller (or equal) than the new number 
        because any smaller number behind the new one cann never become max again 
        - it's smaller 
        - and it will also leave the window earlier or same time than the new one 
        so we keep only useful candidates 
        that's why deque ends up sorted (by value) automatically
        '''

        