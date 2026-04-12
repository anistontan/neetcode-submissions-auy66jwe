from typing import List
#lets you write that a function expects a list of strings and returns a string of listds 
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=defaultdict(list)
        #creates a dictionary where each value is automatically an empty list [] the first time you use a new key
        '''
        defaultdict is like a normal python dictionary, it automatically creates a default
        value when you access a key that doesnt exist yet
        
        when grouping anagrams, we want to do : 
        - if this key doesn't exist, start an empty list
        - append the word
        '''
        for s in strs: 
            key=''.join(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())
