class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars=set() # a set to store the characters currently inside our window
        l=0 #left pointer of the window 
        best=0 #stores the max length we have seen so far 

        for r in range(len(s)): # r is the right pointer 
        # we move r from left to right across the string
            while s[r]in chars: # if it is alreaedy in the window, means we now have a duplicate 
            # we must shrink the window from left until the duplicate is gone 
                chars.remove(s[l])
                l+=1 #move the pointer right by 1(shrinks the window)
            
            chars.add(s[r]) #now it is safe to include s[r] in the window 
            best=max(best,r-l+1) #the current window length r-l+1
        
        return best