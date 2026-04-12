class Solution:

    def encode(self, strs: List[str]) -> str:
        ''' we take the separated strings 
        and encode them into a single string'''
        out = []
        for s in strs:
            out.append(str(len(s)))
            out.append('#')
            out.append(s)
        return ''.join(out)

    ''' 
    example : strs = ["Hello", "World"]
    out = [] (during the loop)
    after the loop : 
    out = ["5","#","Hello","5","#", "World"]
    
    then ''.join(out) --> "5#Hello5#World"
    '''

            
    def decode(self, s: str) -> List[str]:
        ''' we take the single string and decode
        them to their singular strings'''
        decodedStr=[]
        i=0

        '''
        1. start at i 
        2. move j forward until we hit '#'
        3. convert that into an int L
        4. the next L characters are the actual word:
            - word = s[j+1 : j+1+L]
        5. jump i forward and repeat
        '''
        
        while i<len(s):
            j=i 
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            j+=1 # move past '#'
            decodedStr.append(s[j:j + length])
            i=j+length
        
        return decodedStr
