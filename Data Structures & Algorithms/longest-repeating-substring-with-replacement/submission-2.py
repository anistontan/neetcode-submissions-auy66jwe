class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        for any window [l...r], if you want to make the whole window become one repeated character,
        keep the MOST frequent character in the window and "replace" the rest
        so: 
        - window_len = r-l+1
        - maxFreq = highest frequency of any single letter inside the window 
        - replacements needed = window_len - maxFreq
        - window is valid if window_len - maxFreq <k 
        '''
        
        count=[0]*26
        l=0
        best=0 
        maxFreq=0 #max frequency of single char in current window 

        for r in range(len(s)):
            leftIdx=ord(s[r])-ord('A')
            count[leftIdx]+=1
            maxFreq=max(maxFreq,count[leftIdx])
            '''
            shrinking means u r moving l forward, so you remove s[l] (the char leaving the window)
            not s[r]
            - compute the index of s[l]
            - decrement it
            - then l+=1
            '''
            while ((r-l+1)-maxFreq) >k:
                rightIdx=ord(s[l])-ord('A')
                count[rightIdx]-=1
                l+=1
            
            best=max(best, r-l+1)

        return best








