class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        core idea : 
        1) count what we need 
        - make a dictionary need for characters in t : 
            need[c]=how many of c we must have 
            eg t="AABC"
            need={A:2,B:1,C:1}
        - also keep required=number of distinct characters in need (here 3)
        2) expand right pointer r 
        - maintain another dict have for the current window counts 
        when u add s[r] into the window : 
            - increment have[s[r]]
            - if s[r] is a needed char and have[s[r]]==need[s[r]]
            then that character is now satisfied--> formed+=1 
        so
        formed= how many distinct needed chars currently meet their required counts 
        3) when window is valid (formed==required )--> shrink from left 
        when valid : 
        - update best answer (smallest window)
        - try removing s[l] (decrement have[s[l]])
        - if s[l] is needed and now have[s[l]] < need[s[l]], the window becomes invalid --> forme-=1
        - move l forward
        then continue expanding r again
        '''
        need={}
        required=0 

        for c in t:
            if c not in need:
                required+=1
            need[c]=need.get(c,0)+1

        
        #sliding window
        window={}
        formed=0
        l=0

        bestLen=float("inf")
        #my best length is infinite at the start so any real window length (Eg 5,10 etc) will be smaller and replace it
        bestL=0
        bestR=0

        #expand window with r 
        for r in range(len(s)):
            ch=s[r]
            window[ch]=window.get(ch,0)+1

            #if this char is needed AND we now have enough of it, we satisfied 1 requirement
            if ch in need and window[ch]==need[ch]:
                formed+=1
            
            #when window is valid, shrink from left
            while formed==required:
                #update best answer
                if (r-l+1) < bestLen : 
                    bestLen=r-l+1
                    bestL=l
                    bestR=r

                #remove left char and move l
                leftChar=s[l]
                window[leftChar]-=1

                #if we broke a needed requirement, window become invalid
                if leftChar in need and window[leftChar] < need[leftChar]:
                    formed-=1
                
                l+=1
            
        if bestLen == float("inf"):
                return ""

            
        return s[bestL:bestR+1]

        
        








