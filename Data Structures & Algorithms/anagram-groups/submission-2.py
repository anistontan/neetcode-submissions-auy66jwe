class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        In Python, a defaultdict is a container subclass found in the built-in collections module. It works exactly like a standard dictionary (dict) but solves one major issue: it prevents KeyError exceptions when you try to access or modify a key that does not exist yet.
        '''
        groups=defaultdict(list)

        for s in strs:
            count=[0]*26
            for char in s:
                index=ord(char)-ord('a')
                count[index]+=1
            key=tuple(count)

            groups[key].append(s)
        '''
        You don't care about the fingerprints themselves — just the groups. .values() gives you all the buckets (lists of words), and list(...) wraps them up.
        '''
        return list(groups.values())