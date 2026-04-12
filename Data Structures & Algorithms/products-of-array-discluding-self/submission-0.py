class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        output=[1]*n #we will multiply into it

        #2. build the LEFT products (prefix pass)
        prefix = 1 #make a running product 

        for i in range(n): #product of everything before i
            output[i]=prefix
            prefix*=nums[i]
        ''' what this does ( example nums=[1,2,4,6])
        - start : prefix=1 
        - i=0 : output[0]=1, prefix=1*1=1
        - i=1 : output[1]=1, prefix=1*2=2 
        - i=2 : output[2]=2, prefix=2*4=8
        - i=3 : output[3]=8, prefix=8*6=48 
        output becomes [1,1,2,8]
        '''

        #3 : Suffix past (right --> left)
        suffix=1 

        #Loop backwards
        for i in range(n-1,-1,-1):  #product of everything after i
            output[i]*=suffix
            suffix*=nums[i] 
            #final answer at i = left pile x right pile
        '''
        nums=[1,2,4,6]
        output = [1,1,2,8] (from just now)
        suffix=1
        i=3: output[3]=8*1=8, suffix=1*6=6
        i=2: output[2]=2*6=12, suffix=6*4=24
        ...
        final [48,24,12,8]
        '''
        return output



