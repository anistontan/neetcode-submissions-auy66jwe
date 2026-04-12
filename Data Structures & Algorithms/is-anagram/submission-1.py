class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t): #if length not the same so automatically false
            return False
        s_char_counter={} #create a dictionary to store char:count
        for char in s:
            s_char_counter[char]=s_char_counter.get(char,0)+1
            '''s_char_counter.get(char,0) means : 
            - if char exists in the dictionary, give me its value 
            - if it doesnt exist yet, pretend its 0 
            -- then we add 1 and store it back
            -- we r building a freq table
            '''
        for char in t: #we loop through each char in t
        #the goal : "use up" the counts you stored from s
            if char not in s_char_counter:
            #if t contains a letter that never appeared in s, then it's not an anagram
                return False
            s_char_counter[char]-=1
            #we found a char in s, so we "consume -1" 1 copy
            if s_char_counter[char]<0:
            #if it goes below 0, that means t used that char more times than s had it
                return False
        return True # since we check lengths r equal 
