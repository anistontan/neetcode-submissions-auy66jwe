class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets={}
        '''
        idea is to create 
        eg {1:2,2:1,3:0...}
        '''
        for num in nums: 
            buckets[num]=buckets.get(num,0)+1
        
        #now we find the k most frequent numbers 
        
        #make an array of lists where index=frequency 
        freqBuckets=[[] for i in range(len(nums)+1)]
        ''' so eg len(nums) is 6 
        freqBuckets= [
            [], index 0 : numbers that appear 0 times (unused)
            [].
            [],
            [],
            [],
            [],
            []  index 6: numbers that appear 6 times
        ]
        '''
        for num,freq in buckets.items():
            freqBuckets[freq].append(num)
        
        res=[]
        for freq in range(len(freqBuckets)-1,0,-1):
            for num in freqBuckets[freq]:
                res.append(num)
                if len(res)==k:
                    return res

            
