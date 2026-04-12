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
        l=0 #left pointer
        best=0 #stores the best valid window length we have seen so far 
        maxFreq=0 #max frequency of single char in current window 

        for r in range(len(s)):
            idxR=ord(s[r])-ord('A')
            count[idxR]+=1 
            maxFreq=max(maxFreq,count[idxR])
            '''
            shrinking means u r moving l forward, so you remove s[l] (the char leaving the window)
            not s[r]
            - compute the index of s[l]
            - decrement it
            - then l+=1
            '''
            while ((r-l+1)-maxFreq) >k: 
                #r-l+1is the current window length
                #maxFreq = number of chars we can keep most (most frequent char)
                #so window_len - maxFreq = how many chars are NOT that most frequent char (these r the ones we need to replace)
                #if replacements needed is > k, the window is invalid --> shrink it from the left
                idxL=ord(s[l])-ord('A')
                count[idxL]-=1
                l+=1 #shrink the window, so we move pointer left
            
            best=max(best, r-l+1)

        return best








