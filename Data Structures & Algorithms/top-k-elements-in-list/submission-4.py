class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets={}

        for num in nums:
            buckets[num]=buckets.get(num,0)+1
            
            #mke an array of lists where index=frequency
            freqBuckets=[[] for i in range(len(nums)+1)]
            '''
            freqBuckets = [
                [],      # index 0: appears 0 times (unused)
                [3],     # index 1: numbers appearing 1 time
                [2],     # index 2: numbers appearing 2 times
                [1],     # index 3: numbers appearing 3 times
                [],      # index 4
                [],      # index 5
                []       # index 6
            ]
            '''

        for num,freq in buckets.items():
                freqBuckets[freq].append(num)

        res=[]
        '''
            You walk the buckets from highest frequency to lowest. That range(len(freqBuckets)-1, 0, -1) means: start at the last index, go down to 1 (the 0 is the stop point, so index 0 is never visited), stepping by -1.
            Because high-frequency buckets come first, the most frequent numbers get added to res first. As soon as res has k items, you return immediately.
        '''

        for freq in range(len(freqBuckets)-1,0,-1):
            for num in freqBuckets[freq]:
                res.append(num)
                if len(res)==k:
                    return res
