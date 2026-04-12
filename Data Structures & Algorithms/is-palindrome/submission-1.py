class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=[]
        for ch in s:
            if ch.isalnum():
                cleaned.append(ch.lower())
        cleaned="".join(cleaned)
        # "" is a separator, so it joins with nothing in between 
        # cleaned will still be a list, but we can't do string stuff like [::-1]
        return cleaned==cleaned[::-1]