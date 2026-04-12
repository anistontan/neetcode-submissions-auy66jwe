class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        order doesnt matter
        as long as ALL the letters in s1 are seen in s2 consecutively but any permuation is fine
        return true 
        '''
        '''
        we r looking for a substring in s2 of exactly length len(s1) whose letter count matches s1
        so instead of a "growing window until you found all letters" do a : 
        - fixed length sliding window of size len(s1) over s2 
        at each position, compare : 
        - counts of letters in s1
        - counts of letters in the current window of s2 
        --if they match --> found a permutation --> return True
        '''

        if len(s1) > len(s2):
            return False 
        
        need=[0]*26
        window=[0]*26
        m=len(s1)
        for ch in s1: 
            need[ord(ch)-ord('a')]+=1

        for i in range(m): #build first window (size m)
            window[ord(s2[i])-ord('a')]+=1

        if window == need:
                return True 

        #slide the window across 2 
        for r in range(m,len(s2)):
            #add new right char
            window[ord(s2[r])-ord('a')]+=1
            #remove left char (the one that just moved out)
            l=r-m
            window[ord(s2[l])-ord('a')]-=1

            if window==need:
                return True
            
        return False



    