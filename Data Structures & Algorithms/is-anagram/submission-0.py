class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t): #if length not the same so automatically false
            return False
        s_char_counter={} #create a dictionary to store char:count
        for char in s:
            s_char_counter[char]=s_char_counter.get(char,0)+1
            # we use .get
        for char in t: 
            if char not in s_char_counter:
                return False
            s_char_counter[char]-=1
            if s_char_counter[char]<0:
                return False
        return True
