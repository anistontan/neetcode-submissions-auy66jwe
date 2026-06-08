class Solution:

    def encode(self, strs: List[str]) -> str:
        out=[]
        for s in strs:
            out.append(str(len(s)))
            out.append("#")
            out.append(s)
        return ''.join(out)

    def decode(self, s: str) -> List[str]:
        decodedStr=[]
        i=0

        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            j+=1 #move past '#'
            decodedStr.append(s[j:j+length])
            i=j+length 
        return decodedStr
