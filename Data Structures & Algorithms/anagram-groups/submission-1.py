class Solution:
    '''
    ord() gives the Unicode number for a character 
    for lowercase letters : 
        - ord('a')=97
        - ord('b')=98
    so we minus so that it fits neaetly in a 26-length array
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=defaultdict(list)
        for s in strs: 
            count=[0]*26
            for char in s: 
                index=ord(char) - ord('a')
                count[index]+=1
            key=tuple(count) #converts list into a tuple (unchangeable list)
            #this is so that key becomes stable fingerprint we can use as dictionary key

            groups[key].append(s)
            '''
            groups is a dictionary like:
            - key (fingerprint) --> value (list of words that match)
            so this line means : 
            - go to the bucket for the fingerprint
            - put the word s inside that bucket
            '''
        return list(groups.values())
